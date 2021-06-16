import os
import pydicom
from typing import List

from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication

from src.label_set import LabelSet


class Utils:
    @staticmethod
    def change_cursor(cursorShape):
        QApplication.setOverrideCursor(QCursor(cursorShape))

    @staticmethod
    def isDicomFile(path: str) -> bool:
        if not os.path.isfile(path):
            return False
        try:
            with open(path, "rb") as f:
                return f.read(132).decode("ASCII")[-4:] == "DICM"
        except:
            return False

    @staticmethod
    def dicomFilesInDir(directory: str = ".") -> List[str]:
        directory = os.path.expanduser(directory)
        candidates = [os.path.join(directory, f) for f in sorted(os.listdir(directory))]
        return [f for f in candidates if Utils.isDicomFile(f)]

    @staticmethod
    def build_COCO_annotation(img, body, tag_grop, label, img_id, ann_id):
        try:
            segmentation = img.overlay_array(tag_grop)
            bbox = img[tag_grop, 0x0022].value
            ann_id += 1
            cat_id = LabelSet.get_label_id(label)
            body.write('\t' + '{' + '\n')
            body.write('\t' + '\t' + '"image_id": ' + str(img_id) + ',' + '\n')
            body.write('\t' + '\t' + '"id": ' + str(ann_id) + ',' + '\n')
            body.write('\t' + '\t' + '"category_id": ' + str(cat_id) + ',' + '\n')
            body.write('\t' + '\t' + '"segmentation": ' + str(segmentation) + ',' + '\n')
            body.write('\t' + '\t' + '"bbox": ' + str(bbox) + ',' + '\n')
            body.write('\t' + '}' + '\n')
        except BaseException:
            pass

    @staticmethod
    def build_COCO_category(body, label):
        try:
            body.write('\t' + '{' + '\n')
            body.write('\t' + '\t' + '"id": ' + str(LabelSet.get_label_id(label)) + ',' + '\n')
            body.write('\t' + '\t' + '"name": ' + str(label) + ',' + '\n')
            body.write('\t' + '}' + '\n')
        except BaseException:
            pass

    @staticmethod
    def export_to_COCO(input_path, save_sath):
        img_list = [pydicom.read_file(input_path + '/' + i) for i in os.listdir(input_path)]
        body = open('.temp/coco.json', 'w')
        body.write('annotation [' + '\n')
        img_id = 0

        for img in img_list:
            img_id += 1
            ann_id = 0

            for label in LabelSet.get_label_list():
                if LabelSet.get_label_id(label) == 1:
                    Utils.build_COCO_annotation(body, 0x6000, label, img_id, ann_id)
                elif LabelSet.get_label_id(label) == 2:
                    Utils.build_COCO_annotation(body, 0x6002, label, img_id, ann_id)
                elif LabelSet.get_label_id(label) == 3:
                    Utils.build_COCO_annotation(body, 0x6004, label, img_id, ann_id)
                elif LabelSet.get_label_id(label) == 4:
                    Utils.build_COCO_annotation(body, 0x6006, label, img_id, ann_id)
                elif LabelSet.get_label_id(label) == 5:
                    Utils.build_COCO_annotation(body, 0x6008, label, img_id, ann_id)
                elif LabelSet.get_label_id(label) == 6:
                    Utils.build_COCO_annotation(body, 0x6010, label, img_id, ann_id)
                elif LabelSet.get_label_id(label) == 7:
                    Utils.build_COCO_annotation(body, 0x6012, label, img_id, ann_id)
                elif LabelSet.get_label_id(label) == 8:
                    Utils.build_COCO_annotation(body, 0x6014, label, img_id, ann_id)
                elif LabelSet.get_label_id(label) == 9:
                    Utils.build_COCO_annotation(body, 0x6016, label, img_id, ann_id)
                elif LabelSet.get_label_id(label) == 10:
                    Utils.build_COCO_annotation(body, 0x6018, label, img_id, ann_id)
                elif LabelSet.get_label_id(label) == 11:
                    Utils.build_COCO_annotation(body, 0x6020, label, img_id, ann_id)
                elif LabelSet.get_label_id(label) == 12:
                    Utils.build_COCO_annotation(body, 0x6022, label, img_id, ann_id)
                elif LabelSet.get_label_id(label) == 13:
                    Utils.build_COCO_annotation(body, 0x6024, label, img_id, ann_id)
                elif LabelSet.get_label_id(label) == 14:
                    Utils.build_COCO_annotation(body, 0x6026, label, img_id, ann_id)
                elif LabelSet.get_label_id(label) == 15:
                    Utils.build_COCO_annotation(body, 0x6028, label, img_id, ann_id)
                elif LabelSet.get_label_id(label) == 16:
                    Utils.build_COCO_annotation(body, 0x6030, label, img_id, ann_id)
            
        body.write(']' + '\n' + '\n')
        body.write('category [' + '\n')

        for label in LabelSet.get_label_list():
            Utils.build_COCO_category(body, label)
            
        body.write(']')
        body.close()

    @staticmethod
    def build_Pascal_VOC_object(body, img, tag_grop, label):
        bbox = img[tag_grop, 0x0022].value
        x_min = bbox[0]
        y_min = bbox[1]
        x_max = x_min + bbox[2]
        y_max = y_min + bbox[3]
        body.write('\t' + '<object>' + '\n')
        body.write('\t' + '\t' + '<name>' + str(label) + '</name>' + '\n')
        body.write('\t' + '\t' + '<bbox>' + '\n')
        body.write('\t' + '\t' + '\t' + '<xmin>' + str(x_min) + '</xmin>' + '\n')
        body.write('\t' + '\t' + '\t' + '<ymin>' + str(y_min) + '</xmin>' + '\n')
        body.write('\t' + '\t' + '\t' + '<xmax>' + str(x_max) + '</xmin>' + '\n')
        body.write('\t' + '\t' + '\t' + '<ymax>' + str(y_max) + '</xmin>' + '\n')
        body.write('\t' + '\t' + '</bbox>' + '\n')
        body.write('\t' + '</object>' + '\n')

    @staticmethod
    def export_to_Pascal_VOC(input_path, save_path):
        file_name_list = [i for i in os.listdir(input_path)]
        body = open('.temp/text.xml', 'w')
        body.write('<annotation>' + '\n')
        body.write('\t' + '<folder>' + input_path + '</folder>' + '\n')

        for file in file_name_list:
            body.write('\t' + '<filename>' + file + '</filename>' + '\n')
            body.write('\t' + '<path>' + input_path + '/' + file + '</path>' + '\n')
            body.write('\t' + '<size>' + '\n')
            img = pydicom.read_file(input_path + '/' + file)
            width = img.pixel_array.shape[0]
            height = img.pixel_array.shape[1]
            body.write('\t' + '\t' + '<width>' + str(width) + '</width>' + '\n')
            body.write('\t' + '\t' + '<height>' + str(height) + '</height>' + '\n')
            body.write('\t' + '</size>' + '\n')

            for label in LabelSet.get_label_list():
                if LabelSet.get_label_id(label) == 1:
                    Utils.build_Pascal_VOC_object(body, img, 0x6000, label)
                elif LabelSet.get_label_id(label) == 2:
                    Utils.build_Pascal_VOC_object(body, img, 0x6002, label)
                elif LabelSet.get_label_id(label) == 3:
                    Utils.build_Pascal_VOC_object(body, img, 0x6004, label)
                elif LabelSet.get_label_id(label) == 4:
                    Utils.build_Pascal_VOC_object(body, img, 0x6006, label)
                elif LabelSet.get_label_id(label) == 5:
                    Utils.build_Pascal_VOC_object(body, img, 0x6008, label)
                elif LabelSet.get_label_id(label) == 6:
                    Utils.build_Pascal_VOC_object(body, img, 0x6010, label)
                elif LabelSet.get_label_id(label) == 7:
                    Utils.build_Pascal_VOC_object(body, img, 0x6012, label)
                elif LabelSet.get_label_id(label) == 8:
                    Utils.build_Pascal_VOC_object(body, img, 0x6014, label)
                elif LabelSet.get_label_id(label) == 9:
                    Utils.build_Pascal_VOC_object(body, img, 0x6016, label)
                elif LabelSet.get_label_id(label) == 10:
                    Utils.build_Pascal_VOC_object(body, img, 0x6018, label)
                elif LabelSet.get_label_id(label) == 11:
                    Utils.build_Pascal_VOC_object(body, img, 0x6020, label)
                elif LabelSet.get_label_id(label) == 12:
                    Utils.build_Pascal_VOC_object(body, img, 0x6022, label)
                elif LabelSet.get_label_id(label) == 13:
                    Utils.build_Pascal_VOC_object(body, img, 0x6024, label)
                elif LabelSet.get_label_id(label) == 14:
                    Utils.build_Pascal_VOC_object(body, img, 0x6026, label)
                elif LabelSet.get_label_id(label) == 15:
                    Utils.build_Pascal_VOC_object(body, img, 0x6028, label)
                elif LabelSet.get_label_id(label) == 16:
                    Utils.build_Pascal_VOC_object(body, img, 0x6030, label)

        body.write('</annotation>')
        body.close()

    @staticmethod
    def build_YOLO_annotation(body, img, tag_grop, label):
        bbox = img[tag_grop, 0x0022].value
        body.write(label + ' ' + bbox[0] + ' ' + bbox[1] + ' ' + bbox[2] + ' ' + bbox[3] + '\n')

    @staticmethod
    def export_to_YOLO(input_path, save_path):
        file_name_list = [i for i in os.listdir(input_path)]
        for file in file_name_list:
            img = pydicom.read_file(input_path + '/' + file)
            body = open(save_path + file[:-4] + '.xml', 'w')
            
            for label in LabelSet.get_label_list():
                if LabelSet.get_label_id(label) == 1:
                    Utils.build_YOLO_annotation(body, img, 0x6000, label)
                elif LabelSet.get_label_id(label) == 2:
                    Utils.build_YOLO_annotation(body, img, 0x6002, label)
                elif LabelSet.get_label_id(label) == 3:
                    Utils.build_YOLO_annotation(body, img, 0x6004, label)
                elif LabelSet.get_label_id(label) == 4:
                    Utils.build_YOLO_annotation(body, img, 0x6006, label)
                elif LabelSet.get_label_id(label) == 5:
                    Utils.build_YOLO_annotation(body, img, 0x6008, label)
                elif LabelSet.get_label_id(label) == 6:
                    Utils.build_YOLO_annotation(body, img, 0x6010, label)
                elif LabelSet.get_label_id(label) == 7:
                    Utils.build_YOLO_annotation(body, img, 0x6012, label)
                elif LabelSet.get_label_id(label) == 8:
                    Utils.build_YOLO_annotation(body, img, 0x6014, label)
                elif LabelSet.get_label_id(label) == 9:
                    Utils.build_YOLO_annotation(body, img, 0x6016, label)
                elif LabelSet.get_label_id(label) == 10:
                    Utils.build_YOLO_annotation(body, img, 0x6018, label)
                elif LabelSet.get_label_id(label) == 11:
                    Utils.build_YOLO_annotation(body, img, 0x6020, label)
                elif LabelSet.get_label_id(label) == 12:
                    Utils.build_YOLO_annotation(body, img, 0x6022, label)
                elif LabelSet.get_label_id(label) == 13:
                    Utils.build_YOLO_annotation(body, img, 0x6024, label)
                elif LabelSet.get_label_id(label) == 14:
                    Utils.build_YOLO_annotation(body, img, 0x6026, label)
                elif LabelSet.get_label_id(label) == 15:
                    Utils.build_YOLO_annotation(body, img, 0x6028, label)
                elif LabelSet.get_label_id(label) == 16:
                    Utils.build_YOLO_annotation(body, img, 0x6030, label)
        
            body.close()
            
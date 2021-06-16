from cv2 import cv
import numpy as np
from skimage import measure, morphology


class MaskGenerator:
    @staticmethod
    def create_mask(image_path):
        img = cv.imread(image_path)
        img_reshaped = img.reshape((-1, 3))
        img_reshaped = np.float32(img_reshaped)
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1)
        claster_num = 2
        ret, label, center = cv.kmeans(img_reshaped, claster_num, None,
        criteria, 1, cv.KMEANS_RANDOM_CENTERS)
        center = np.uint8(center)
        result = center[label.flatten()]
        result_reshaped = result.reshape((img.shape))
        return result_reshaped
    
    @staticmethod
    def edit_mask(mask, erosion_kernel_val=None, dilation_kernel_val=None):
        if dilation_kernel_val == None:
            erosion = morphology.erosion(mask, np.ones([erosion_kernel_val], [erosion_kernel_val]))
            return measure.label(erosion)
        elif erosion_kernel_val == None:
            dilation = morphology.dilation(mask, np.ones([dilation_kernel_val], [dilation_kernel_val]))
            return measure.label(dilation)
        else:
            erosion = morphology.erosion(mask, np.ones([erosion_kernel_val], [erosion_kernel_val]))
            dilation = morphology.dilation(erosion, np.ones([dilation_kernel_val], [dilation_kernel_val]))
            return measure.label(dilation)
            
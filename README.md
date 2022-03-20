# MILT - Medical Images Labeling Tool

Application for labeling medical images in DICOM format and saving annotations inside the metadata of labeled files.

### Creating and installing a virtual environment
1. Я предлагаю создать окружение из файла `environment.yml` (**Необходимо изменить `prefix` в файле**):
```sh
conda env create -f environment.yml
```

Первая строка файла `yml` устанавливает новое имя окружения.

2. Активируйте новое окружение: 
```sh
conda activate DICOMLabeling
```

3. Проверьте, что окружение было корректно установлено:
```sh
conda env list
```

### Правила работы с приложением

1. Работать можно как и с единичным изображением формата **DICOM**, так и с сериями снимков **DICOM**.


2. После того как открыто изображение или выбрано изображение из серии, нужно ввеси имя класса объекта поиска, выбрать его и выделить его на изображении.


3. Далее нужно нажать кнопку **"Наложить маску"**, после этого автоматически будет сгенерирована маска для выделенного объекта на изображении. Для уточнения полученной маски нужно нажать **"Редактировать маску"**:

![mask](https://github.com/AlexeyPopov1997/DICOMLabeling/blob/master/pictures/1.png?raw=true)

Маска редактируется изменением ее темных и светлых областей:

![editMask](https://github.com/AlexeyPopov1997/DICOMLabeling/blob/master/pictures/2.png?raw=true)


4. Далее нужно сохранить обработанное изображение и перейти к следующему изображению, если необходимо.


5. Также, можно экспортировать аннотированные сериализованные данные в форматах **COCO**, **Pascal VOC** и **YOLO**:

![export1](https://github.com/AlexeyPopov1997/DICOMLabeling/blob/master/pictures/3.png?raw=true)


6. После этого открывается окно экпорта, в котором можно выбрать необходимые параметры и экспортировать данные:

![export2](https://github.com/AlexeyPopov1997/DICOMLabeling/blob/master/pictures/4.png?raw=true)
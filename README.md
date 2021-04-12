# MILT - Medical Images Labeling Tool

Приложение для разметки медицинских изображений формата DICOM и сохранения данных, сгенерированных при разметке внутри метаданных DICOM.
![MILT](https://github.com/AlexeyPopov1997/DICOMLabeling/blob/master/icons/title.png?raw=true)

### Создание и установка виртуального окружения
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

1. Работать можно как и с единичным изображением формата DICOM, так и с сериями снимков DICOM.

2. После того как открыто изображение или выбрано изображение из серии, нужно ввеси имя класса объекта поиска, выбрать его и выделить его на изображении:
![labels](https://github.com/AlexeyPopov1997/DICOMLabeling/blob/master/icons/labels.png?raw=true)

3. Далее нужно нажать кнопку "Наложить маску". Уточнить маску, изменяя значения эрозии и дилатации. В итоге нажать "Наложить маску":
![mask](https://github.com/AlexeyPopov1997/DICOMLabeling/blob/master/icons/mask.png?raw=true)

4. Далее нужно сохранить обработанное изображение и перейтик следующему изображению, если необходимо.

5. Также, можно экспортировать сериализованные данные для решения задач **классификации**, **сегментации** и **обнаружения объектов**:
![exports1](https://github.com/AlexeyPopov1997/DICOMLabeling/blob/master/icons/export1.png?raw=true)

6. После этого открывается окно экпорта, в котором можно выбрать необходимые параметры и экспортировать данные в .pickle-файл:
![exports2](https://github.com/AlexeyPopov1997/DICOMLabeling/blob/master/icons/export2.png?raw=true)
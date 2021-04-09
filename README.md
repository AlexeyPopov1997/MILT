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

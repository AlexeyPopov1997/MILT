# MILT - Medical Images Labeling Tool

Application for labeling medical images in DICOM format and saving annotations inside the metadata of labeled files.

### Creating and installing a virtual environment
1. I suggest creating an environment from the `environment.yml` file (**You need to change the `prefix` in the file**):
```sh
conda env create -f environment.yml
```

The first line of the `yml` file sets the new environment name.

2. Activate the new environment:
```sh
conda activate MILT
```

3. Check that the environment has been correctly set:
```sh
conda env list
```
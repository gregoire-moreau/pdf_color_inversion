# How to use : 
```console
python3 src/main.py PATH_TO_PDF
```
By default the output will be saved in the output/ directory with the filename {title of the input pdf}.pdf .

```console
python3 src/main.py PATH_TO_PDF -n NAME_OF_OUTPUT_FILE
python3 src/main.py PATH_TO_PDF --name NAME_OF_OUTPUT_FILE
```
The output will be saved in the output/ directory with the filename {NAME_OF_THE_OUTPUT_FILE}.pdf

```console
python3 src/main.py PATH_TO_PDF -o OUTPUT_PATH
python3 src/main.py PATH_TO_PDF --output OUTPUT_PATH
```

The output will be saved at OUTPUT_PATH.

The script uses [PyMuPDF](https://pymupdf.readthedocs.io) to read PDF files and [Pillow](https://pillow.readthedocs.io) to save them.
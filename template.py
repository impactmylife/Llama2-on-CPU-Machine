import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') # it will give the log message and current execution time

# creating folder( e.g src) and files 
list_of_files = [
    "src/__init__.py",
    "src/run_local.py",
    "src/helper.py",
    "model/instruction.txt",
    "requirements.txt",
    "setup.py",
    "main.py",
    "research/trials.ipynb"

]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) # spliting the folder and files

# create directory
    if filedir !="":
        os.makedirs(filedir, exist_ok=True) # creating the folder
        logging.info(f"Creating directory; {filedir} for the file: {filename}") # it show the log messages
# creating the file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")
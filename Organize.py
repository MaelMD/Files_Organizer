## !! Note !!
## You must have this file in the same folders with files you want to organize

## importing libraries

import os
from pathlib import Path

## I created at first a dictionnary where I add the suffixes of files of types I want to organize

SUBDIRS = {
    "DOCUMENTS": ['.pdf','.rtf','.txt','.docx','.xlsx','.pptx','.odt'],
    "AUDIO": ['.m4a','.m4b','.wav','.mp3','.flac','.wma','.aac'],
    "VIDEOS": ['.mov','.avi','.mp4','.m4v','.ogv','.webm','.wmv'],
    "IMAGES": ['.jpg','.jpeg','.png','.webp','.bmp','.gif','.apng']
}

## Here I created a function that returns the type of the file entered as a parameter

def pickDir(value):
    for category, suffixes in SUBDIRS.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'  ## The function returns 'MISC' for the suffixes that weren't defined in the dictionary

## This function does the work of organizing files into seperate folders based on their type

def organizeDir():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDir(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

## Calling the function

organizeDir()

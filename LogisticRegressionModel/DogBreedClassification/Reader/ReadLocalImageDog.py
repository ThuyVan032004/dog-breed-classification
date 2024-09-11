import sys 

paths = ['../Shared/Shared.ReadData/Abstraction']
for path in paths:
    sys.path.append(path)

from AReadLocalImage import AReadLocalImage 
from abc import ABC 

class ReadLocalImage(AReadLocalImage):
    def __init__(self, directory, file, format):
        super().__init__(directory, file, format)
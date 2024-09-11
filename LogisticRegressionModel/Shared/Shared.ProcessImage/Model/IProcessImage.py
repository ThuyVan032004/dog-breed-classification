import zope.interface as zi 

class IProcessImage(zi.Interface):
    def flattenImage(self):
        pass
    def resize(self, sizeX, sizeY):
        pass 
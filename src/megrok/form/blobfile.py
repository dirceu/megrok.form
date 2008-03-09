from zope.interface import implements
from z3c.blobfile.file import File
from collective.namedfile.interfaces import INamedFile, INamedImage

class NamedBlobFile(File):
    implements(INamedFile)

    def __init__(self, data='', contentType='', filename=None):
        File.__init__(self, data, contentType)
        self.filename=filename

class NamedBlobImage(NamedBlobFile):
    implements(INamedImage)

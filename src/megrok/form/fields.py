from zope import interface, schema
from collective.namedfile.interfaces import INamedFile, INamedImage
from collective.namedfile.field import NamedImage as Image
from collective.namedfile.field import NamedFile as File
from blobfile import NamedBlobFile as BlobFileValueType
from blobfile import NamedBlobImage as BlobImageValueType
import constraints
import interfaces

class Email(schema.TextLine):
    def __init__(self, **kw):
        kw['constraint'] = constraints.isEmail
        super(Email, self).__init__(**kw)

class HTML(schema.Text):
    interface.implements(interfaces.IHTML)

class NamedBlobFile(schema.Field):
    interface.implements(INamedFile, interfaces.INamedBlobFile)

class NamedBlobImage(NamedBlobFile):
    interface.implements(INamedImage, interfaces.INamedBlobImage)
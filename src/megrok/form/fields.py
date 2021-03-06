from zope import interface, schema
from collective.namedfile.field import NamedImage as Image
from collective.namedfile.field import NamedFile as File
from collective.namedblobfile.field import NamedBlobImage as BlobImage
from collective.namedblobfile.field import NamedBlobFile as BlobFile
import constraints
import interfaces

class Email(schema.TextLine):
    def __init__(self, **kw):
        kw['constraint'] = constraints.isEmail
        super(Email, self).__init__(**kw)

class HTML(schema.Text):
    interface.implements(interfaces.IHTML)
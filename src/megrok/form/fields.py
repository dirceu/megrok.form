from zope import interface, schema
from collective.namedfile.field import NamedImage as Image
from collective.namedfile.field import NamedFile as File
import validators
import interfaces

class Email(schema.TextLine):
    def __init__(self, **kw):
        kw['constraint'] = validators.isEmail
        super(Email, self).__init__(**kw)

class HTML(schema.Text):
    interface.implements(interfaces.IHTML)
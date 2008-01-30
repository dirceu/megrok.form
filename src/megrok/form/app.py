import grok
from zope import interface, schema
from megrok.form.fields import Email, Image, HTML, File

class megrokform_test(grok.Application, grok.Container):
    pass

class IPerson(interface.Interface):
    """ A simple class used to show how to use widgets and fields from megrok.form
    """
    name = schema.TextLine(title=u"Name")
    email = Email(title=u"Email")
    picture = Image(title=u"Picture")
    description = HTML(title=u"Description")
    birthday = schema.Date(title=u"Birthday")
    resume = File(title=u"Resume")

class Person(grok.Model):
    interface.implements(IPerson)

    def __init__(self, name, email, picture, description, birthday, resume):
        self.name = name
        self.email = email
        self.picture = picture
        self.description = description
        self.birthday = birthday
        self.resume = resume

class AddPerson(grok.AddForm):
    grok.context(megrokform_test)
    form_fields = grok.AutoFields(Person)

    @grok.action('Add person')
    def add(self, **data):
        obj = Person(**data)
        name = data['name'].lower().replace(' ', '_')
        self.context[name] = obj

class Edit(grok.EditForm):
    grok.context(Person)
    form_fields = grok.AutoFields(Person)

class Index(grok.DisplayForm):
    grok.context(Person)

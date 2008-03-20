import grok
from zope import component, interface, schema
from zope.publisher.browser import TestRequest
from zope.schema.interfaces import ConstraintNotSatisfied
from megrok.form.fields import Email, Image, HTML, File, BlobFile, BlobImage
import unittest

class MeGrokFormTest(grok.Application, grok.Container):
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
    video = BlobFile(title=u"Favorite Video")
    wallpaper = BlobImage(title=u"Favorite Wallpaper")

class Person(grok.Model):
    interface.implements(IPerson)

    def __init__(self, name, email, picture, description, birthday, resume, video, wallpaper):
        self.name = name
        self.email = email
        self.picture = picture
        self.description = description
        self.birthday = birthday
        self.resume = resume
        self.video = video
        self.wallpaper = wallpaper

class AddPerson(grok.AddForm):
    grok.context(MeGrokFormTest)
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

class MeGrokFormTests(unittest.TestCase):
    def test_widgets(self):
        """
        Assures that all widgets are being rendered correctly.
        """
        grok.grok('megrok.form.tests')
        view = component.getMultiAdapter((MeGrokFormTest(), TestRequest()), name='addperson')
        rendered_form = view.render()

        # test rendered email widget
        s = """<div class="widget"><input class="textType" id="form.email" name="form.email" size="20" type="text" value=""  /></div>"""
        assert(s in rendered_form)

        # test rendered image widget
        s = """<div class="widget">\n\t<input type="hidden" value="" name="form.picture.used"\n        id="form.picture.used" />\n\t\n\t\n\t<div>\n\t\t<input type="file" maxlength="True" class="" size="30"\n         name="form.picture" id="form.picture" />\n\t\t\n\t</div>\n</div>"""
        assert(s in rendered_form)
        
        # test rendered html widget
        s = """<div class="widget"><textarea cols="60" id="form.description" name="form.description" rows="15" ></textarea><script type="text/javascript">\ntinyMCE.init({ \nmode : "exact", \nelements : "form.description"\n}\n);\n</script>\n</div>"""
        assert(s in rendered_form)
        
        # test rendered datetime widget
        s = """<div class="widget">\n<input class="textType" id="form.birthday" name="form.birthday" size="10" type="text" value=""  />\n<input type="button" value="..." id="form.birthday_trigger">\n<script type="text/javascript">\n  \n  \n  Calendar.setup({\n  inputField: \'form.birthday\',\n  button: \'form.birthday_trigger\',\n  ifFormat: \'%Y-%m-%d\'\n});\n\n</script>\n</div>"""
        assert(s in rendered_form)
        
        # test rendered file widget
        s = """<div class="widget">\n\t<input type="hidden" value="" name="form.resume.used"\n        id="form.resume.used" />\n\t\n\t\n\t<div>\n\t\t<input type="file" maxlength="True" class="" size="30"\n         name="form.resume" id="form.resume" />\n\t\t\n\t</div>\n</div>"""
        assert(s in rendered_form)

        # test rendered blobfile widget
        s = """<div class="widget">\n\t<input type="hidden" value="" name="form.video.used"\n        id="form.video.used" />\n\t\n\t\n\t<div>\n\t\t<input type="file" maxlength="True" class="" size="30"\n         name="form.video" id="form.video" />\n\t\t\n\t</div>\n</div>"""
        assert(s in rendered_form)

        # test rendered blobimage widget
        s = """<div class="widget">\n\t<input type="hidden" value="" name="form.wallpaper.used"\n        id="form.wallpaper.used" />\n\t\n\t\n\t<div>\n\t\t<input type="file" maxlength="True" class="" size="30"\n         name="form.wallpaper" id="form.wallpaper" />\n\t\t\n\t</div>\n</div>"""
        assert(s in rendered_form)
        
    def test_email_default_constraint(self):
        """
        Assures that the default constraint for the Email field is working
        """
        from megrok.form.fields import Email
        email = Email(title=u'Email')
        self.assertRaises(ConstraintNotSatisfied, email.validate, u'thisisnotanemailaddress')
        email.validate(u'thisisanemailaddress@email.com')        

def test_suite():
    from megrok.form.tests import FunctionalLayer
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MeGrokFormTests))
    suite.layer = FunctionalLayer
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')

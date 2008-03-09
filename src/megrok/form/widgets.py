from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from collective.namedfile.widget import NamedFileWidget
from fields import NamedBlobFile

class NamedBlobFileWidget(NamedFileWidget):
    """A correctly working Blob File widget.

    The standard FileWidget returns a string instead of an IFile inst,
    which means it will always fail schema validation in formlib.

    In addition this widget will also extract the filename and Content-Type
    from the request.
    """
    def _toFieldValue(self, input):
        value=super(NamedFileWidget, self)._toFieldValue(input)
        if value is not self.context.missing_value:
            filename=getattr(input, "filename", None)
            contenttype=input.headers.get("content-type",
                                          "application/octet-stream")
            value=NamedBlobFile(value, contenttype, filename)

        return value

class NamedBlobImageWidget(NamedBlobFileWidget):
    """A image widget simply uses a different template to display the image"""
    template = ViewPageTemplateFile('imageinputwidget.pt')
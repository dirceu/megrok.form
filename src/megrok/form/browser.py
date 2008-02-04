from zope.publisher.interfaces import NotFound
import mimetypes
import os.path
from collective.namedfile.browser import UrlDispatcher
from zope import interface, component
from zope.interface.common.idatetime import ITZInfo
from zope.publisher.interfaces.browser import IBrowserRequest
import pytz

class FileViewDispatcher(UrlDispatcher):
    """
    This overrides collective.namedfile.browser.FileViewDispatcher. The former is
    almost equal, but uses restrictedTraverse (which is specific to Zope 2 / Plone),
    I think.
    """
    
    def __call__(self):    
        if not self.traverse_subpath:
            raise NotFound(self, '', self.request)
        field_name = self.traverse_subpath[0]
        form_field = self.context.form_fields.get(field_name, None)
        if form_field is None:
            raise NotFound(self, field_name, self.request)
        field = form_field.field.bind(self.context.context)
        file = field.get(self.context.context)
        if getattr(file, 'filename', None):
            extension = os.path.splitext(file.filename)[1].lower()
            contenttype = mimetypes.types_map.get(extension,
                                                  "application/octet-stream")
        elif file.contentType:
            contenttype = file.contentType
        else:
            contenttype = "application/octet-stream"
        self.request.response.setHeader("Content-Type", contenttype)
        self.request.response.setHeader("Content-Length", file.getSize())
        return file.data


@interface.implementer(ITZInfo)
@component.adapter(IBrowserRequest)
def tzinfo(request):
    """
    FIXME: zc.datetimewidget.datetimewidget.DatetimeDisplayWidget needs an adapter
    for zope.interface.common.idatetime.ITZInfo. This should be set automatically.
    """
    return pytz.timezone('Europe/Vienna')

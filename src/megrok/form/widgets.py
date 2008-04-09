from zope.app.form.browser.widget import DisplayWidget
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

class TinyDisplayWidget(DisplayWidget):
    template = ViewPageTemplateFile('tinydisplaywidget.pt')

    def __call__(self):
        if self._renderedValueSet():
            value = self._data
        else:
            value = ""
        return self.template(name=self.context.__name__, value=value)
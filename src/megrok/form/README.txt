===========
megrok.form
===========

megrok.form is a helper package that provides some useful fields, widgets and constraints for Grok.

Fields
------

- Email, a TextLine field with a default contraint
- HTML, a Text field that uses z3c.widget.tiny
- File, from collective.namedfile
- Image, from collective.namedfile

Widgets
-------

megrok.form overrides the default widgets for:

- zope.interface.schema.Date (using zc.datetimewidget.widget.DateWidget)
- zope.interface.schema.Datetime (using zc.datetimewidget.widget.DatetimeWidget)

And add new widgets for Image and File (from collective.namedfile).

Validators / Constraints
------------------------

megrok.form add constraints for:

- SSN
- US Phone Numbers
- International Phone Numbers
- Zip Code
- URL
- Email

Installation
------------

To use megrok.form under Grok all you need is to install megrok.form as an egg 
and include it's zcml. The best place to do this is to make megrok.form
a dependency of your application by adding it to your install_requires
list in setup.cfg. If you used grokprojet to create your application setup.cfg
is located in the project root. It should look something like this::

   install_requires=['setuptools',
                     'grok',
                     'megrok.form',
                     # Add extra requirements here
                     ],

Then include megrok.form in your configure.zcml. If you used grokproject to
create your application it's at src/<projectname>/configure.zcml. Add the
include line after the include line for grok, but before the grokking of the
current package. It should look something like this::

      <include package="grok" />
      <include package="megrok.form" />  
      <grok:grok package="." />
  
Then run bin/buildout again. You should now see buildout saying something like::

   Getting distribution for 'megrok.form'.
   Got megrok.form 0.1.

That's all.

Authors
-------

- Dirceu Pereira Tiegs (dirceutiegs at gmail dot com)
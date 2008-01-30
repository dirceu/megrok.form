===========
megrok.form
===========

:Author: Dirceu Pereira Tiegs

megrok.form is a helper package that provides some very useful fields, widgets and validation methods for Grok.

Fields
------

- Email, a TextLine field with a default validator (contraint);
- HTML, a Text field that uses z3c.widget.tiny;
- File, from collective.namedfile;
- Image, from collective.namedfile;

Widgets
-------

megrok.form overrides the default widgets for:

- zope.interface.schema.Date (using zc.datetimewidget.widget.DateWidget);
- zope.interface.schema.Datetime (using zc.datetimewidget.widget.DatetimeWidget);

Validators / Constraints
------------------------

megrok.form add validators for:

- SSN
- US Phone Numbers;
- International Phone Numbers;
- Zip Code
- URL
- Email

TODO
----

- Remove "app.py" and add some automated tests;
- Release the egg on cheeseshop.
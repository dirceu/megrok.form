from zope import interface, schema

class IHTML(schema.interfaces.ITextLine):
    u"""Field containing a HTML unicode string."""

class INamedBlobFile(interface.Interface):
	u"""Marker interface for blob files."""

class INamedBlobImage(interface.Interface):
	u"""Marker interface for blob images."""
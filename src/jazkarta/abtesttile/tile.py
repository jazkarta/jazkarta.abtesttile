from plone.app.textfield import RichText
from plone.tiles import PersistentTile
from plone.supermodel import model
from zope import schema
from . import _


class IABTestTile(model.Schema):

    text_a = RichText(
        title=_(u'Text A'),
        required=False,
        allowed_mime_types=('text/html',),
        default_mime_type='text/html',
        output_mime_type='text/x-html-safe',
        default=u'')

    text_b = RichText(
        title=_(u'Text B'),
        required=False,
        allowed_mime_types=('text/html',),
        default_mime_type='text/html',
        output_mime_type='text/x-html-safe',
        default=u'')

    ratio = schema.Int(
        title=_(u'Percentage of time that tile A will be shown'),
        min=0,
        max=100,
        default=50,
        required=True)


class ABTestTile(PersistentTile):
    """Existing content tile
    """

    pass
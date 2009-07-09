import datetime
from StringIO import StringIO

from django.core.files.base import ContentFile
import django.db.models as m

# import PIL.PngImagePlugin

from turtlecanvas.canvas import Renderer


class Canvas(m.Model):
    """A canvas for turtle(s) to draw on.

    - The origin of a canvas is the bottom left of the plane.
    - A heading of 0 degrees points upward.
    - The turtle state is kept with the canvas as this implementation supports
      only one turtle.
    """

    title = m.CharField(max_length=100)
    width = m.IntegerField()
    height = m.IntegerField()
    turtle_x = m.FloatField(default=-1)
    turtle_y = m.FloatField(default=-1)
    turtle_heading = m.FloatField(default=-1)
    rendering = m.ImageField(upload_to='renderings', blank=True)

    class Meta:
        verbose_name_plural = 'canvases'

    def __unicode__(self):
        return u'%s (%i)' % (self.title, self.id)

    def save(self, *args, **kw):
        new_canvas = self.pk is None
        # XXX: I'd like to keep this in the model but Django appears
        # to lack hooks needed.
#         # Prevent alteration after creation.
#         if not new_canvas:
#             raise ValueError('Canvases cannot be altered.')
        # /XXX
        # Set x, y, and heading if not specified.
        if self.turtle_x == -1:
            self.turtle_x = self.width / 2
        if self.turtle_y == -1:
            self.turtle_y = self.height / 2
        if self.turtle_heading == -1:
            self.turtle_heading = 0
        m.Model.save(self)
        # Render the image and save the file now that we have the id.
        # XXX: Is there a more direct way to do this?
        renderer = Renderer(self.width, self.height)
        file = StringIO()
        renderer.image.save(file, 'PNG')
        cfile = ContentFile(file.getvalue())
        self.rendering.save('%i.png' % self.pk, cfile, save=False)
        m.Model.save(self)

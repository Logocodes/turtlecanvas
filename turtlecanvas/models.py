import datetime

import django.db.models as m


class Canvas(m.Model):
    """A canvas for turtle(s) to draw on.

    The origin of a canvas is the bottom left of the plane.

    A heading of 0 degrees points upward.
    """

    title = m.CharField(max_length=100)
    width = m.IntegerField('width (pixels)')
    height = m.IntegerField('height (pixels)')

    class Meta:
        verbose_name_plural = 'canvases'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kw):
        m.Model.save(self)
        # Store initial canvas state with centered turtle.
        initial_state = CanvasState(
            canvas=self,
            previous_state=None,
            turtle_x=float(self.width) / 2,
            turtle_y=float(self.height) / 2,
            turtle_heading=0.0,
        )
        initial_state.save()


class CanvasState(m.Model):
    """The current state of a canvas."""

    canvas = m.ForeignKey('Canvas')
    previous_state = m.ForeignKey('CanvasState', blank=True, null=True)
    timestamp = m.DateTimeField(default=datetime.datetime.now)
    # Only supporting one turtle, so keep the turtle state here too.
    # Use float fields for turtle position for finer accuracy.
    turtle_x = m.FloatField()
    turtle_y = m.FloatField()
    turtle_heading = m.FloatField('turtle heading (degrees)')

    def __unicode__(self):
        return '%s @ %s' % (self.canvas, self.timestamp)

import datetime

import django.db.models as m


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

    class Meta:
        verbose_name_plural = 'canvases'

    def __unicode__(self):
        return u'%s (%i)' % (self.title, self.id)

    def save(self, *args, **kw):
        new_canvas = self.pk is None
        # Prevent alteration after creation.
        if not new_canvas:
            raise ValueError('Canvases cannot be altered.')
        # Set x, y, and heading if not specified.
        if self.turtle_x == -1:
            self.turtle_x = self.width / 2
        if self.turtle_y == -1:
            self.turtle_y = self.height / 2
        if self.turtle_heading == -1:
            self.turtle_heading = 0
        m.Model.save(self)

from django.test import TestCase

import turtlecanvas.models as m


class TurtleCanvasTests(TestCase):

    def test_starts_empty(self):
        assert len(m.Canvas.objects.all()) == 0
        assert len(m.CanvasState.objects.all()) == 0

    def test_canvas_creates_initial_state(self):
        canvas = m.Canvas(
            title='My fancy art',
            width=400,
            height=300,
        )
        canvas.save()
        assert len(m.Canvas.objects.all()) == 1
        assert len(m.CanvasState.objects.filter(canvas=canvas)) == 1

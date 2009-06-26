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
        state = canvas.initial_state()
        assert state.canvas == canvas
        assert state.previous_state == None
        assert state.turtle_x == 200.0
        assert state.turtle_y == 150.0
        assert state.turtle_heading == 0.0

    def test_canvas_can_change_title(self):
        canvas = m.Canvas(
            title='My fancy art',
            width=400,
            height=300,
        )
        canvas.save()
        assert canvas.title == 'My fancy art'
        canvas.title = 'Go turtle go'
        canvas.save()
        assert canvas.title == 'Go turtle go'

    def test_canvas_cannot_change_dimensions(self):
        canvas = m.Canvas(
            title='My fancy art',
            width=400,
            height=300,
        )
        canvas.save()
        canvas.width = 200
        canvas.height = 100
        self.assertRaises(ValueError, canvas.save)

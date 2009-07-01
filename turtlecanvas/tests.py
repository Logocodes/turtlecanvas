from django.test import TestCase

import turtlecanvas.models as m


class BasicCanvasTests(TestCase):

    def test_starts_empty(self):
        assert len(m.Canvas.objects.all()) == 0

    def test_canvas_creates_initial_state(self):
        canvas = m.Canvas(
            title='My fancy art',
            width=400,
            height=300,
        )
        canvas.save()
        assert len(m.Canvas.objects.all()) == 1
        assert canvas.turtle_x == 200.0
        assert canvas.turtle_y == 150.0
        assert canvas.turtle_heading == 0.0

    def test_canvas_cannot_change(self):
        canvas = m.Canvas(
            title='My fancy art',
            width=400,
            height=300,
        )
        canvas.save()
        canvas.width = 200
        canvas.height = 100
        self.assertRaises(ValueError, canvas.save)


##class TransformationTests(TestCase):

    ##def test_forward_100(self):
        ##canvas = m.Canvas(
            ##title='My fancy art',
            ##width=400,
            ##height=300,
        ##)
        ##canvas.save()
        ##transformation = m.Transformation(
            ##before=canvas,
            ##command='forward',
            ##param_float=100.0,
        ##)
        ##transformation.save()
        ##assert len(m.Transformation.objects.all()) == 1
        ##assert len(m.Canvas.objects.all()) == 2
        ##canvas2 = transformation.after
        ##assert canvas2.title == canvas.title
        ##assert canvas2.width == canvas.width
        ##assert canvas2.height == canvas.height
        ##assert canvas2.turtle_x == 200.0
        ##assert canvas2.turtle_y == 250.0
        ##assert canvas2.turtle_heading == 0.0

    ##def test_right_90(self):
        ##canvas = m.Canvas(
            ##title='My fancy art',
            ##width=400,
            ##height=300,
        ##)
        ##canvas.save()
        ##transformation = m.Transformation(
            ##before=canvas,
            ##command='right',
            ##param_float=90.0,
        ##)
        ##transformation.save()
        ##assert len(m.Transformation.objects.all()) == 1
        ##assert len(m.Canvas.objects.all()) == 2
        ##canvas2 = transformation.after
        ##assert canvas2.title == canvas.title
        ##assert canvas2.width == canvas.width
        ##assert canvas2.height == canvas.height
        ##assert canvas2.turtle_x == 200.0
        ##assert canvas2.turtle_y == 150.0
        ##assert canvas2.turtle_heading == 90.0

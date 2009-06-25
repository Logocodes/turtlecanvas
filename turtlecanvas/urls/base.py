from django.conf.urls.defaults import *

urlpatterns = patterns(
    'turtlecanvas.views',
    (r'^$', 'index'),
)

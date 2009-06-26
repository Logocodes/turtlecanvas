import turtlecanvas.models as m
from django.contrib import admin
from django import forms

from turtlecanvas.adminext import ReadOnlyAdminFields


class CanvasAdmin(ReadOnlyAdminFields, admin.ModelAdmin):

    readonly_update = ['width', 'height']


admin.site.register(m.Canvas, CanvasAdmin)
admin.site.register(m.CanvasState)

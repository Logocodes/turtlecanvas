"""Support for readonly admin fields."""

# Based on http://www.djangosnippets.org/snippets/937/


from django import forms


class ReadOnlyWidget(forms.Widget):

    def __init__(self, original_value, display_value):
        self.original_value = original_value
        self.display_value = display_value
        super(ReadOnlyWidget, self).__init__()

    def render(self, name, value, attrs=None):
        if self.display_value is not None:
            return unicode(self.display_value)
        return unicode(self.original_value)

    def value_from_datadict(self, data, files, name):
        return self.original_value


class ReadOnlyAdminFields(object):

    def get_form(self, request, obj=None):
        form = super(ReadOnlyAdminFields, self).get_form(request, obj)
        readonly = set()
        if (hasattr(self, 'readonly_update')
            and getattr(obj, 'pk', None) is not None
            ):
            readonly.update(self.readonly_update)
        if hasattr(self, 'readonly'):
            readonly.update(self.readonly)
        for field_name in readonly:
            if field_name in form.base_fields:
                if hasattr(obj, 'get_%s_display' % field_name):
                    display_value = getattr(
                        obj, 'get_%s_display' % field_name)()
                else:
                    display_value = None
                form.base_fields[field_name].widget = ReadOnlyWidget(
                    getattr(obj, field_name, ''), display_value)
                form.base_fields[field_name].required = False
        return form

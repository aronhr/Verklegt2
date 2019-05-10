from django.forms import CheckboxInput
from django.template.defaultfilters import register


@register.filter(name='is_checkbox')
def is_checkbox(field):
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__

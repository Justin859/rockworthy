from django import template
from django.utils.safestring import mark_safe
from datetime import datetime

import markdown2

register = template.Library()

@register.filter(name='fix_date')
def fix_date(value):
    value = value.split("+")[0]
    format = "%Y-%m-%dT%H:%M:%S"
    value = datetime.strptime(value, format)
    return value

@register.filter(name='get_weekday')
def fix_date(value):
    value = value.split("+")[0]
    format = "%Y-%m-%dT%H:%M:%S"
    value = datetime.strptime(value, format)
    week_day = (value.strftime('%A'))
    return week_day

@register.filter(name='trim_time')
def trim_time(value):
    value = value.split("+")[0]
    format = "%Y-%m-%dT%H:%M:%S"
    value = datetime.strptime(value, format)
    return value.date()

@register.filter(name='markdown_to_html')
def markdown_to_html(markdown_text):
    '''Converts markdown text to HTML '''   
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)

@register.filter(name='sort_pop')
def sort_pop(events):
    return sorted(events,key=lambda k: k['attending_count'],reverse=True)


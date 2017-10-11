from django import template
from django.utils.safestring import mark_safe
from datetime import datetime

import markdown2

register = template.Library()

@register.filter(name='fix_date')
def fix_date(value):
    try:
        value = value.split("+")[0]
        format = "%Y-%m-%dT%H:%M:%S"
        value = datetime.strptime(value, format)
    except ValueError:
        value = 'N/A'
    return value

@register.filter(name='get_weekday')
def fix_date(value):
    value = value.split("+")[0]
    format = "%Y-%m-%dT%H:%M:%S"
    try:  
        value = datetime.strptime(value, format)
        week_day = (value.strftime('%A'))
    except ValueError:
        week_day = 'N/A'
    return week_day

@register.filter(name='trim_time')
def trim_time(value):
    try: 
        value = value.split("+")[0]
        format = "%Y-%m-%dT%H:%M:%S"
        value = datetime.strptime(value, format).date()
    except ValueError:
        value = 'N/A'
        
    return value

@register.filter(name='markdown_to_html')
def markdown_to_html(markdown_text):
    '''Converts markdown text to HTML '''   
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)

@register.filter(name='sort_pop')
def sort_pop(events):
    return sorted(events,key=lambda k: k['attending_count'],reverse=True)

@register.filter(name='length_fix')
def length_fix(string):
    str_arr = string.split(" ");
    has_bad_length = False
    for item in str_arr:
        if (len(item) > 25):
            has_bad_length = True
    if has_bad_length == True:
        return string[:25]
    else:
        return string


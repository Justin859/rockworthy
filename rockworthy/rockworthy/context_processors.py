import datetime

def add_variable_to_context(request):
    
    date_today = datetime.date.today()
    week_day = date_today.weekday()

    if (week_day == 0 or week_day == 1 or week_day == 2 or week_day == 3 or week_day == 4):
        weekend_start = date_today + datetime.timedelta(days=4-week_day)
        weekend_stop = weekend_start + datetime.timedelta(days=2)
        mid_weekend = weekend_start + datetime.timedelta(days=1)
    else:
        weekend_start = date_today
        weekend_stop = weekend_start + datetime.timedelta(days=6-week_day)
        mid_weekend = weekend_start

    return {
        "weekend_start": weekend_start,
        "weekend_stop": weekend_stop,
        "mid_weekend": mid_weekend,
        "date_today": date_today,
        "date": datetime.datetime.now().strftime('%Y-%m-%dT00:00:00+0200')
    }
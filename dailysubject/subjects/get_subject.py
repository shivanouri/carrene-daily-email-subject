import calendar

import pyperclip
from khayyam import *
from datetime import date


def get_daily_subject(team: str):
    my_date = date.today()
    week_day = calendar.day_name[my_date.weekday()]
    jalali_date = str(JalaliDate.today()).replace('-', '/')
    subject = 'Daily Report %s %s' % (week_day, jalali_date)
    if len(team) > 0:
        subject = subject + ' (%s)' % team
    pyperclip.copy(subject)
    return subject

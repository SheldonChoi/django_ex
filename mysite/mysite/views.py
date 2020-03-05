from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(httpRequest):
    home = "<html><body>welcome My New Home, powered by Django</body></html>"
    return HttpResponse(home)


def hello(httpRequest):
    current_time = datetime.datetime.now()
    return HttpResponse(f"Hello, Now is {current_time}")

def current_time(httpRequest):
    current_time = datetime.datetime.now()
    return render(httpRequest, 'test.html', {'current_time': current_time, 'is_first': True})

def template_test(httpRequest):
    current_time = datetime.datetime.now()
    return render(httpRequest, 'content.html', {'current_time': current_time, 'name': 'UnyongChoi'})

def cal_extra_work_time(httpRequest) :
    worktimes = """  
        9:00, 8:30, 8:20, 6:00, 0:00,
        8:50, 11:00, 7:30, 8:00, 8:00,
        8:00, 6:50, 9:20, 8:00, 8:10,
        8:00, 8:00, 8:00, 8:00, 8:00
    """
    days, calculated_time, expected_time = parsing_and_calculate_extra_or_overtime(worktimes)

    return render(httpRequest, 'extra_time_calculator.html', {'worktimes': worktimes, 'work_days': days, "calculated_time": calculated_time, "expected_time":expected_time})

def parsing_and_calculate_extra_or_overtime(worktimes):
    times = [x.strip() for x in worktimes.split(',')]
    workdays = len(times)

    totalMyTime = MyTimeClass("0:0")
    for time in times:
        totalMyTime = totalMyTime + MyTimeClass(time)

    expected_hour = 8 * workdays
    expected_work_time = MyTimeClass(f"{expected_hour}:0")

    return workdays, totalMyTime, expected_work_time

class MyTimeClass:
    def __str__(self):
        return f"{self.hour}:{self.minutes}"

    def __init__(self, timestring):
        self.hour = int(timestring.split(':')[0])
        self.minutes = int(timestring.split(':')[1])
    
    def __add__ (self, other):
        sumTime = MyTimeClass('0:0')

        sumTime.hour = self.hour + other.hour
        sumTime.minutes = self.minutes + other.minutes

        offset_hour, remainder_minute = divmod(sumTime.minutes, 60)
        sumTime.hour = sumTime.hour + offset_hour

        if offset_hour > 0:
            sumTime.minutes = remainder_minute

        return sumTime

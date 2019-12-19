from django.shortcuts import render 
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    return render(request,'time_teller_app/index.html')

def today(request):
    todays_date = datetime.datetime.today()
    todays_date = {
        'todaysdate' = 'todays_date'
        }
    return render(request,'time_teller_app/today.html',todays_date)    

def timestamp(request):
    now = time.time()
    ts = {
          'tstmp' = 'now'
        }
    return render(request,'time_teller_app/timestamp.html',ts)    
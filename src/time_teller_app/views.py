from django.shortcuts import render 
from django.http import HttpResponse
from datetime import datetime
import time 

# Create your views here.

def index(request):
    return render(request,'time_teller_app\index.html')

def today(request):
    todaysdate = datetime.today()
    td = {
        'todays_date' : todaysdate
        }
    return render(request,'time_teller_app/today.html',td)    

def timestamp(request):
    now = time.time()
    ts = {
          'tstmp' : now
        }
    return render(request,'time_teller_app/timestamp.html',ts)    
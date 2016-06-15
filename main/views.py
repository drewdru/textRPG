from django.shortcuts import render_to_response
import datetime
   
def home(request):
    now = datetime.datetime.now()
    return render_to_response('home.html', {
        'current_date': now,
    })
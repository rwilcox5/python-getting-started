from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import selenium
from selenium import webdriver
driver = webdriver.PhantomJS()
b_url = "http://projects.fivethirtyeight.com/2016-mlb-predictions/cubs"
driver.get(b_url)
allprobs = driver.find_elements_by_class_name("prob")
p538prob0 = 100./int(allprobs[0].text[0:2])
driver.close()
# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!')
    #return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import math
import selenium
import csv
from selenium import webdriver
def writecsv(parr, filen):
        print "hiii"
        with open(filen, 'wb') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                spamwriter.writerow(parr[i])
                        except:
                                print parr[i], i
        print "hhh"
writecsv([['a','b'],['c','d'],['a','c']],'testcsv.csv')

def getplayerlist(driver,pagen):
    plist = []
    aaa= []
    ap = []
    pvsa = []
    allteams = ['cardinals','Astros','Athletics','Blue-Jays','Braves','Brewers','Cardinals','Cubs','Diamondbacks','Dodgers','Giants','Indians','Mariners','Marlins','Mets','Nationals','Orioles','Padres','Phillies','Pirates','Rangers','Rays','Red-Sox','Reds','Rockies','Royals','Tigers','Twins','White-Sox','Yankees']
    all538 = []
    for nstars in range(0,1):
            allprobsa = []
            allres = []
            alldays = []
            b_url = "http://projects.fivethirtyeight.com/2016-mlb-predictions/"+allteams[nstars].lower()
            driver.get(b_url)
            allprobs = driver.find_elements_by_class_name('prob')
            for i in allprobs:
                aaa.append(i.get_attribute("outerHTML"))

    return aaa


#firefox_profile = webdriver.FirefoxProfile()
#firefox_profile.set_preference("browser.download.folderList",2)
#firefox_profile.set_preference("permissions.default.stylesheet",2)
#firefox_profile.set_preference("permissions.default.image",2)
#firefox_profile.set_preference("javascript.enabled", False)
print "hii"
driver = webdriver.PhantomJS()


allbets = getplayerlist(driver,0)




# Create your views here.
def index(request):
    return HttpResponse(allbets)
    #return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})


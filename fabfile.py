from fabric.api import task

from ftplib import FTP
import csv
import math
import time
from selenium import webdriver





def writecsv(parr, filen):

        with open(filen, 'a') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                spamwriter.writerow(parr[i])
                        except:
                                print parr[i], i





def getplayerlist(driver,pagen):
    plist = []
    ap = []
    aparr = []
    pvsa = []
    xtime = time.time()
    allteams = ['angels','Astros','Athletics','Blue-Jays','Braves','Brewers','Cardinals','Cubs','Diamondbacks','Dodgers','Giants','Indians','Mariners','Marlins','Mets','Nationals','Orioles','Padres','Phillies','Pirates','Rangers','Rays','Red-Sox','Reds','Rockies','Royals','Tigers','Twins','White-Sox','Yankees']
    all538 = []
    for nstars in range(0,30):
            allprobsa = []
            allres = []
            alldays = []
            b_url = "http://projects.fivethirtyeight.com/2016-mlb-predictions/"+allteams[nstars].lower()
            driver.get(b_url)
            allprobs = driver.find_elements_by_class_name("prob")
            proarr = []
            for i in allprobs:
                proarr.append(str(i.get_attribute('innerHTML')))
            p538prob0 = 100./int(proarr[0][0:2])
            p538prob1 = 100./int(proarr[2][0:2])
            #print p538prob0
            allpitchers = driver.find_elements_by_class_name("pitcher")
            
            all538.append([allteams[nstars], p538prob0, str(allpitchers[0].get_attribute('innerHTML')), p538prob1, str(allpitchers[2].get_attribute('innerHTML'))])

    teamslist = ['angels','Astros','Athletics','Jays','Braves','Brewers','Cardinals','Cubs','Diamondbacks','Dodgers','Giants','Indians','Mariners','Marlins','Mets','Nationals','Orioles','Padres','Phillies','Pirates','Rangers','Rays','Red Sox','Reds','Rockies','Royals','Tigers','Twins','White Sox','Yankees']
    
    b_url = "https://www.5dimes.eu"
    driver.get(b_url)
    cidbox = driver.find_element_by_id("customerID")
    cidbox.send_keys('5D1998716')
    passbox = driver.find_element_by_name("password")
    passbox.send_keys('5DimeS')
    cidbox = driver.find_element_by_id("submit1")
    cidbox.click()
    cidbox = driver.find_element_by_id("Baseball_MLB")
    cidbox.click()
    cidbox = driver.find_element_by_id("btnContinue")
    cidbox.click()
    allrowst = driver.find_elements_by_class_name('linesRow')
    allrowsb = driver.find_elements_by_class_name('linesRowBot')
    allrows = []
    for i in allrowst:
            allrows.append(i)
    for i in allrowsb:
            allrows.append(i)
    allgames = []
    allgamesodds = []
    for nstars in range(0,30):
            nlines = []
            nnlines = []
            irow = 0
            for eachrow in allrowst:
                    rowstr = eachrow.text
                    rstr = rowstr.lower()
                    #print nstars, teamslist[nstars]
                    rstri = rstr.find(teamslist[nstars].lower())
                    if rstri>-1:
                            inputb = eachrow.find_elements_by_id('editx')
                            mybox='M'
                            for eachinput in inputb:
                                    try:
                                            if str(eachinput.get_attribute('name'))[0]=='M':
                                                    mybox = str(eachinput.get_attribute('name'))
                                    except:
                                            pass
                            pname = rstr[rstri+len(teamslist[nstars])+3:]
                            pni = pname.find(' ')
                            pname = pname[0:pni]
                            nlines = [teamslist[nstars],str(pname)]
                            if rstr.find('\n')>-1:
                                    while rstr.find('\n')>-1:
                                            rindex = rstr.find('\n')
                                            try:
                                                    listedind = str(rstr[0:rindex]).find('listed')
                                                    #print listedind, str(rstr[0:rindex])[0:listedind]
                                                    if listedind >-1:
                                                            nlines.append(float(str(rstr[0:rindex])[0:listedind]))
                                            except:
                                                    pass
                                            rstr = rstr[rindex+1:len(rstr)]
                            else:
                                    rindex = rstr.find('listed')
                                    if rindex>-1:
                                            nl = float(rstr[rindex-7:rindex])
                                            nlines.append(nl)
                            if nlines[0:1] not in allgames:
                                    #print 'hj', nlines
                                    allgames.append(nlines[0:1])
                                    nlines.append(0)
                                    nlines.append(mybox)
                                    allgamesodds.append(nlines)
                                    nnlines = nlines
                                    #print 'hjj', nlines
                    irow=irow+1

            irow = 0
            for eachrow in allrowsb:
                    rowstr = eachrow.text
                    rstr = rowstr.lower()
                    #print nstars, teamslist[nstars]
                    rstri = rstr.find(teamslist[nstars].lower())
                    if rstri>-1:
                            inputb = eachrow.find_elements_by_id('editx')
                            mybox='M'
                            for eachinput in inputb:
                                    try:
                                            if str(eachinput.get_attribute('name'))[0]=='M':
                                                    mybox = str(eachinput.get_attribute('name'))
                                    except:
                                            pass
                            pname = rstr[rstri+len(teamslist[nstars])+3:]
                            pni = pname.find(' ')
                            pname = pname[0:pni]
                            nlines = [teamslist[nstars],str(pname)]
                            if rstr.find('\n')>-1:
                                    while rstr.find('\n')>-1:
                                            rindex = rstr.find('\n')
                                            try:
                                                    listedind = str(rstr[0:rindex]).find('listed')
                                                    #print listedind, str(rstr[0:rindex])[0:listedind]
                                                    if listedind >-1:
                                                            nlines.append(float(str(rstr[0:rindex])[0:listedind]))
                                            except:
                                                    pass
                                            rstr = rstr[rindex+1:len(rstr)]
                            else:
                                    rindex = rstr.find('listed')
                                    if rindex>-1:
                                            nl = float(rstr[rindex-7:rindex])
                                            nlines.append(nl)
                            if nlines[0:1] not in allgames:
                                    #print 'hjh', nlines
                                    allgames.append(nlines[0:1])
                                    nlines.append(0)
                                    nlines.append(mybox)
                                    allgamesodds.append(nlines)
                                    nnlines = nlines
                                    #print 'hjjh', nlines
                    irow=irow+1
                                    
            #print "hh", nlines
            nlines = nnlines
            if len(nlines)>4:
                    
                    print 'a',nlines
                    p1 = str(all538[nstars][2])
                    p2 = str(all538[nstars][4])
                    p1i = p1.find(' ')
                    p2i = p2.find(' ')
                    print p1, p2
                    if p1i > -1:
                            
                            if p1[:p1i].lower()==nlines[1].lower():
                                    #nlines.append(all538[nstars][0])
                                    nlines.append(all538[nstars][1])
                                    nlines.append(nlines[2]/nlines[5])
                                    if 1./nlines[5]>1./nlines[2]+.01:
                                            nlines.append(min((100*nlines[2]/nlines[5]-100)/nlines[2],10/nlines[2]))
                                    #nlines.append(all538[nstars][2])
                                    #print nlines
                            if p2[:p2i].lower()==nlines[1].lower():
                                    #nlines.append(all538[nstars][0])
                                    nlines.append(all538[nstars][3])
                                    nlines.append(nlines[2]/nlines[5])
                                    if 1./nlines[5]>1./nlines[2]+.01:
                                            nlines.append(min((100*nlines[2]/nlines[5]-100)/nlines[2],10/nlines[2]))
                                    #nlines.append(all538[nstars][4])
                                    #print nlines
                    else:
                            if p1.lower()==nlines[1].lower():
                                    #nlines.append(all538[nstars][0])
                                    nlines.append(all538[nstars][1])
                                    nlines.append(nlines[2]/nlines[5])
                                    if 1./nlines[5]>1./nlines[2]+.01:
                                            nlines.append(min((100*nlines[2]/nlines[5]-100)/nlines[2],10/nlines[2]))
                                    #nlines.append(all538[nstars][2])
                                    #print nlines
                            if p2.lower()==nlines[1].lower():
                                    #nlines.append(all538[nstars][0])
                                    nlines.append(all538[nstars][3])
                                    nlines.append(nlines[2]/nlines[5])
                                    if 1./nlines[5]>1./nlines[2]+.01:
                                            nlines.append(min((100*nlines[2]/nlines[5]-100)/nlines[2],10/nlines[2]))
                                    #nlines.append(all538[nstars][4])
                                    #print nlines
                    #print nlines
                    nlines0 = [xtime]
                    for iin in nlines:
                            nlines0.append(iin)
                    aparr.append(nlines0)
                    print nlines0
                    if len(nlines)>7:
                            #aparr.append(nlines)
                            #print 'a', nlines
                            namestr = str(nlines0[4])
                            thebet = int(nlines0[7]*100)*1./100
                            try:
                                    bidbox = driver.find_element_by_name(namestr)
                                    bidbox.send_keys(str(thebet))
                            except:
                                    pass
                    #print nlines,all538[nstars]

    #print allgamesodds


    #writecsv(pvsa,'allprobs1.csv')
    return aparr


@task
def run_bets():
    #driver = webdriver.Firefox()
    driver=webdriver.PhantomJS()
    allplayers = getplayerlist(driver,0)
    ftp = FTP('xo6.x10hosting.com')
    ftp.login(user='shiohx10', passwd = 'X10password')
    ftp.cwd('/public_html/')
    ftp.retrlines('LIST')
    print 'done in one.'

    writecsv(allplayers,'allp'+'.csv')
    filename = 'allp'+'.csv'
    ftp.storbinary('STOR '+filename, open(filename, 'wb'))
    ftp.quit()
    driver.close()
    print 'done in tow.'

#run_bets()

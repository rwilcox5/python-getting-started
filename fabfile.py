from fabric.api import task

from ftplib import FTP
import csv
import math

from selenium import webdriver
#domain name or server ip:




def writecsv(parr, filen):
        with open(filen, 'wb') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for i in range(0,len(parr)):
                        try:
                                spamwriter.writerow(parr[i])
                        except:
                                print parr[i], i





##This gets all the owners from the conferences to check if sims or not.

def getplayerlist(driver,pagen):
    plist = []
    ap = []
    aparr = []
    pvsa = []
    allteams = ['Angels','Astros','Athletics','Blue-Jays','Braves','Brewers','Cardinals','Cubs','Diamondbacks','Dodgers','Giants','Indians','Mariners','Marlins','Mets','Nationals','Orioles','Padres','Phillies','Pirates','Rangers','Rays','Red-Sox','Reds','Rockies','Royals','Tigers','Twins','White-Sox','Yankees']
    all538 = []
    for nstars in range(0,10):
            allprobsa = []
            allres = []
            alldays = []
            b_url = "http://projects.fivethirtyeight.com/2016-mlb-predictions/"+allteams[nstars].lower()
            driver.get(b_url)
            allprobs = driver.find_elements_by_class_name("prob")
            proarr = []
            for i in allprobs:
                    proo = str(i.get_attribute('innerHTML'))
                    proarr.append(proo)
            p538prob0 = 100./int(proarr[0][0:2])
            p538prob1 = 100./int(proarr[2][0:2])
            allpitchers = driver.find_elements_by_class_name("pitcher")
            
            all538.append([allteams[nstars], p538prob0, allpitchers[0].text, p538prob1, allpitchers[2].text])

    teamslist = ['Angels','Astros','Athletics','Jays','Braves','Brewers','Cardinals','Cubs','Diamondbacks','Dodgers','Giants','Indians','Mariners','Marlins','Mets','Nationals','Orioles','Padres','Phillies','Pirates','Rangers','Rays','Red Sox','Reds','Rockies','Royals','Tigers','Twins','White Sox','Yankees']
    
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
    for nstars in range(0,10):
            nlines = []
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
                                    allgames.append(nlines[0:1])
                                    nlines.append(irow)
                                    nlines.append(mybox)
                                    allgamesodds.append(nlines)
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
                                    allgames.append(nlines[0:1])
                                    nlines.append(irow)
                                    nlines.append(mybox)
                                    allgamesodds.append(nlines)
                    irow=irow+1
                                    
                            
            if len(nlines)>4:
                    aparr.append(nlines)
                    p1 = str(all538[nstars][2])
                    p2 = str(all538[nstars][4])
                    p1i = p1.find(' ')
                    p2i = p2.find(' ')
                    if p1i > -1:
                            
                            if p1[:p1i].lower()==nlines[1].lower():
                                    #nlines.append(all538[nstars][0])
                                    nlines.append(all538[nstars][1])
                                    nlines.append(nlines[2]/nlines[5])
                                    if 1./nlines[5]>1./nlines[2]+.01:
                                            nlines.append((1000*nlines[2]/nlines[5]-1000)/nlines[2])
                                    #nlines.append(all538[nstars][2])
                                    #print nlines
                            if p2[:p2i].lower()==nlines[1].lower():
                                    #nlines.append(all538[nstars][0])
                                    nlines.append(all538[nstars][3])
                                    nlines.append(nlines[2]/nlines[5])
                                    if 1./nlines[5]>1./nlines[2]+.01:
                                            nlines.append((1000*nlines[2]/nlines[5]-1000)/nlines[2])
                                    #nlines.append(all538[nstars][4])
                                    #print nlines
                    else:
                            if p1.lower()==nlines[1].lower():
                                    #nlines.append(all538[nstars][0])
                                    nlines.append(all538[nstars][1])
                                    nlines.append(nlines[2]/nlines[5])
                                    if 1./nlines[5]>1./nlines[2]+.01:
                                            nlines.append((1000*nlines[2]/nlines[5]-1000)/nlines[2])
                                    #nlines.append(all538[nstars][2])
                                    #print nlines
                            if p2.lower()==nlines[1].lower():
                                    #nlines.append(all538[nstars][0])
                                    nlines.append(all538[nstars][3])
                                    nlines.append(nlines[2]/nlines[5])
                                    if 1./nlines[5]>1./nlines[2]+.01:
                                            nlines.append((1000*nlines[2]/nlines[5]-1000)/nlines[2])
                                    #nlines.append(all538[nstars][4])
                                    #print nlines
                    if len(nlines)>7:
                            aparr.append(nlines)
                            namestr = str(nlines[4])
                            thebet = float(nlines[7]/10)
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
    driver = webdriver.PhantomJS()
    allplayers = getplayerlist(driver,0)
    ftp = FTP('ftp.byethost24.com')
    ftp.login(user='b24_18788153', passwd = 'ByeTpi3.14')
    ftp.cwd('/htdocs/')
    ftp.retrlines('LIST')
    print 'done in one.'
    writecsv(allplayers,'allp.csv')
    filename = "allp.csv"
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()
    print 'done in tow.'

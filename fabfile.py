from fabric.api import task

from ftplib import FTP

#domain name or server ip:


@task
def run_bets():
    ftp = FTP('ftp.byethost24.com')
    ftp.login(user='b24_18788153', passwd = 'ByeTpi3.14')
    ftp.cwd('/htdocs/')
    ftp.retrlines('LIST')
    print 'done in one.'
    filen = open("newfile.txt", "w")
    filen.write("hello world in the new filedd")
    filen.close()
    filename = "newfile.txt"
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()
    print 'done in tow.'

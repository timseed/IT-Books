#http://it-ebooks-api.info/v1/
#The API is   http://it-ebooks-api.info/v1/search/php {Subject}

import pycurl
import re
from StringIO import StringIO
import json
import yaml
import pprint
import sqlite3 as lite
import sys

URLMAIN="http://it-ebooks-api.info/v1/search/"
LIBRARY=[]

def GetSubject(sub):
  URL=URLMAIN+sub
  response=StringIO()
  c=pycurl.Curl()
  c.setopt(c.URL,URL)
  c.setopt(c.WRITEDATA,response)
  c.perform()
  c.close()
  jd=json.loads(response.getvalue())
  total_hits=int(jd[u'Total'])
  #print ("%s has %d hits "%(sub,total_hits))
  #pprint.pprint(jd)
  exit
  return total_hits,jd

def BookInfo(search):
  hits,data=GetSubject(search)
  for page in range (1,hits/10+1):
  #for page in range (1,2):
    #pprint.pprint(data)
    hits,data=GetSubject(search+"/page/"+str(page))
    for b in data[u'Books']:
       title= re.sub('[^0-9a-zA-Z ]+', ' ', b[u'Title'])
       LIBRARY.append((b[u'isbn'],b[u'ID'],title))

def LibList():
    ofp=open("library.txt","w+")
    for book in LIBRARY:
       ofp.write(str.format("%-15s\t%-15s\t%s\n")%(book[0],book[1],book[2]))
    ofp.close() 

def LIBAdd():
  con = None
  try:
    con = lite.connect('books.db')
    with con:
      cur = con.cursor()    
      for book in LIBRARY:
        cmd=str.format("INSERT into ebooks(isbn,id,title) values(%d,%d,'%s')"%(int(book[0]),int(book[1]),str(book[2])))
        #print " "+cmd
        try:
           cur.execute(cmd)
        except lite.IntegrityError:
              print ("Book %s - already there "%str(book[2]))
              pass
        except lite.Error, e:
              print "Error %s:" % e.args[0]
              pass 
              #sys.exit(1)
 
  except lite.Error, e:  
    print "Error %s:" % e.args[0]
    sys.exit(1)

  finally:  
    if con:
        con.close()

def GetBooks():
  f=open("books.yaml")
  data=yaml.safe_load(f)
  f.close()
  for title in data['books']:
      BookInfo(title)
  LibList()
  LIBAdd()

if __name__ == "__main__":
    GetBooks()
    print("Database updated")
    print("library.txt created")
    

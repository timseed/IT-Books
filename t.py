#http://it-ebooks-api.info/v1/
#The API is   http://it-ebooks-api.info/v1/search/php {Subject}

import pycurl
from StringIO import StringIO
import json
import pprint

URLMAIN="http://it-ebooks-api.info/v1/search/"

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
  return total_hits,jd

def BookInfo(search):
  hits,data=GetSubject(search)
  for page in range (1,hits/10+1):
    hits,data=GetSubject(search+"/page/"+str(page))
    for b in data[u'Books']:
       print ("%-15s %s")%(b[u'isbn'],b[u'Title'])


BookInfo("Python")

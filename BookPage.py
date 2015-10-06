import sys
import pycurl
import pprint
from StringIO import StringIO
import json

URLMAIN="http://it-ebooks-api.info/v1/book/"

def GetPage(book):
  URL=URLMAIN+book
  response=StringIO()
  c=pycurl.Curl()
  c.setopt(c.URL,URL)
  c.setopt(c.WRITEDATA,response)
  c.perform()
  c.close()
  jd=json.loads(response.getvalue())
  #pprint.pprint(jd)
  print("%s"%(str(jd['Download'])))



#expecting the ID as an argument
book=sys.argv[1]
#curl -X GET  "http://it-ebooks-api.info/v1/book/3692117413
GetPage(book)

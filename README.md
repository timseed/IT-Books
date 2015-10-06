# IT-Books
Small Code - allows you to follow a nice IT Book Web Site


#Requirements
From the OS Level you will need SQLite3.

There are a few python (2.7) requirements 
    - pycurl
    - yaml
    - sqlite3

I think are the main items - you may need to install ncurses in your l#nx OS as well.


#Before you Start

You need a SQLite databash so create one - no wait... there is a script.

  bash setupDb.sh

And you should be sorted


#Check what subjects you want to follow....

Edit the file called *books.yaml* 

Pleace the search books in the list

#Run the Query Agent

You now will query the API - and with the results 
   - update the database
   - produce a Text file (library.txt)
   - produce an XML page (latest.html)


python update.py  

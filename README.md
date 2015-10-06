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


#To View the html

firefox latest.html&

# To generate a Download request

Look at either library.txt or latest.html - and see a Manual that you are interested in.

It will have a name, index number and a ISBN Number.  You want the Index Number.

Then run the following command

   python  BookPage.py <Index>


ie 
   python BookPage.py 2235454092
   http://filepi.com/i/IrlAtdd

To Download lots automatically.... 

   cat library.txt | cut -f 2 | xargs -i -t python BookPage.py  {}



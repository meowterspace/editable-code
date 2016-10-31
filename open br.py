import webbrowser
import selenium
#selenium is also good resource, try that
import time
from mechanize import Browser
br=Browser()
br.open("www.google.com")
time.sleep(0)
webbrowser.open("www.facebook.com")
//doesn't work

import os, random, requests, sys, time, webbrowser
from bs4 import BeautifulSoup
from tkinter import *
from tkinter.ttk import *


#initializations
sample_size = 5
page_lists = {} #dictionary of lists of movie posters/entries associated with each (required) page of the watchlist
gui_mode = False #flag for whether to run in GUI mode or run headless ; default = headless mode
url_prefix = 'https://letterboxd.com'
list_name = "watchlist" # name of the list being searched ; default value is 'watchlist'
list_name_base = ""

#flag/argument checking
for i in range(len(sys.argv)):
    if sys.argv[i] == "-n": #flag for custom sample size, default = 5
        try:
            if sys.argv[i+1].isdigit() and int(sys.argv[i+1]) > 0:
                sample_size = int(sys.argv[i+1])
                i += 1
            else:
                print("ERROR: Invalid sample size input. '-s' flag must be followed by a positive integer.")
                sys.exit() # dont use quit() or exit(): both rely on the interpreter 'site' module, which is not always present
        except IndexError:
            print("ERROR: Invalid sample size input. '-s' flag must be followed by a positive integer.")
            sys.exit()
    elif sys.argv[i] == "-g": #flag for using gui mode
        try: 
            if sys.argv[i+1] == "0":
                gui_mode = False #running in headless 
            elif sys.argv[i+1] == "1": 
                gui_mode = True #running in GUI mode
            else:
                print("ERROR: Invalid input for GUI mode. '-g' flag must be followed by a '0' or '1' to indicate headless or GUI mode, respectively.")
        except IndexError:
            print("ERROR: Invalid input for GUI mode. '-g' flag must be followed by a '0' or '1' to indicate headless or GUI mode, respectively.")
            sys.exit()
    elif sys.argv[i] == "-l": #flag for a custom list name 
        try: 
            list_name = "list/" + sys.argv[i+1].replace(" ", "-")
        except IndexError:
            print("ERROR: custom list name was not provided following the '-l' flag")
            
#username for the target profile
##username = input('Input username for account: ')            
username = "naomi_lover"           
            
#getting HTML of the user's watchlist page
#using user-agent request header associated with Firefox for image loading (posters)
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0"}
r = requests.get('https://letterboxd.com/%s/%s' %(username, list_name), headers=headers)
##print(r.content)
with open('temp.txt', 'w') as f:
    f.write(r.text)
    f.close    

#parse the HTML for watchlist length, this will be the randomizer range
soup = BeautifulSoup(r.text, features="html.parser")
spans = soup.find_all('span', {"class": "watchlist-count"})
##print("length of spans: ", len(spans))
watch_count = [int(watchcount) for watchcount in str.split(spans[0].text) if watchcount.isdigit()]
watch_count = watch_count[0]    #type conversion from list --> int


if sample_size > watch_count:
    sample_size = watch_count
random_values = random.sample(range(watch_count), k=sample_size)
random_values.sort()
##print(random_values)


selections = {}
#original BeautifulSoup object is for the 0th page (21 results per page)
increment = 1
for random_val in random_values:
    entry_number = random_val % 28
    page_number = int(((random_val) / 28)+1)
    if page_number not in page_lists:
        if page_number == 1:
            posters = soup.find_all('li', {"class": "poster-container"})
            page_lists[page_number] = posters
            ##print("le size: ", len(page_lists[page_number]))
        else:
            r = requests.get('https://letterboxd.com/%s/%s/page/%s' %(username, list_name, page_number))
            ##print(r.url)
            ##print(r.text)
            soup = BeautifulSoup(r.text, features="html.parser")
            posters = soup.find_all('li', {"class": "poster-container"})
            page_lists[page_number] = posters
            ##print("le size: ", len(page_lists[page_number]))
        time.sleep(1)   
    
    #storing the random selection to a dictionary using (title, url) pairing 
    div_object = page_lists[page_number][entry_number].findChild('div')
    img_object = page_lists[page_number][entry_number].findChild('img')
    selections[increment-1] =  (img_object['alt'], div_object['data-target-link'])
    if not gui_mode:
        print(str(increment), '. ', img_object['alt'],  '\n       ',  url_prefix, div_object['data-target-link'])
    increment += 1
    
if not gui_mode: #headless mode ; terminal output 
    entry_choice = input('Enter entries to open in your default browser?(1 - %d)\n' % (sample_size))
    entries = entry_choice.split(',')
    already_loaded = []
    for entry in entries: 
        entry = entry.replace(" ", "")
        if entry.isdigit() and int(entry) > 0 and int(entry) <= sample_size and int(entry)-1 not in already_loaded: 
            entry = int(entry) - 1
            already_loaded.append(entry)
            url = url_prefix + selections[entry][1]
            webbrowser.open(url)
            time.sleep(.1)
    sys.exit()
else: #gui mode using the tkinter module for display
    root = Tk()
    list_name_base = 
    root.title('Letterboxd Results for: %s' % (list_name)) 
    
    
    
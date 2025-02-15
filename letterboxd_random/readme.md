### letterboxd_random
***Language: Python***

I wanted a script that returns a randomized set of movies from a user's watchlist on letterboxd.com. This implementation is a single Python script with dependencies on **BeautifulSoup** and **requests** for webscraping the information. It's highly reliant on the formatting of the returned HTML for parsing information. This methodology is necessary because the only other method is using the Letterboxd API, which requires unique registration and authentication from each user. 

Default mode is headless, so results are displayed to the command line / terminal. The user supplies a username argument, an optional argument for a GUI mode that utilizes the **tkinter** module, and some other optional arguments that are detailed below. Simply execute the **letterboxd_random.py** script for functionality. 

#### Options:

python ***letterboxd_random.py*** [-***l*** list_name] [-***n*** number_of_results] [-***g*** option] [***-help***]
  

***-l*** : 
	Insert the name of a different list (under the username supplied) to search from. Default list is the watchlist. If you use this, ensure the list name you supply is character accurate, otherwise it won't work.

***-n*** : 
	Specify a number of results to return. Supplied value must be greater than 0. Default value is 5.

***-g*** : 
	Argument for GUI mode. Accepts '0' for headless or '1' for GUI mode. Default is headless.
	
***-help*** : 
	Prints all arguments the script takes with minimal descriptions

#### Planned updates:
- Finish implementing GUI mode, with a scrollable window displaying movie posters and interactive links for each randomly selected entry. Will utilize the **tkinter** module for Python.
- Implement an option to save a username and other potential arguments, using metadata or some simple txt file structure. This should save you repeating the same username over and over per use
- Android app version
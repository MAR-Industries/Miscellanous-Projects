# README 

This repo is for smaller scripts and projects of mine. They were mostly designed for personal use, with some small optimizations for a more general accessibility. Each folder contains the necessary files for each project, including additional setup files or READMEs describing further dependencies the user might need to install. 

## Projects

### letterboxd_random
***Language: Python***
This script returns a randomized set of movies from a user's watchlist on letterboxd.com. Default mode is headless, so results are displayed to the command line / terminal. The user supplies a username argument, an argument for a GUI mode, and some other arguments that are detailed below. Simply execute the **letterboxd_random.py** script for functionality. 
> -l : Insert the name of a custom list to search from. Default list is the watchlist. If you use this, ensure the list name you supply is character accurate, otherwise it won't work.

> -n : Specify a number of results to return. Supplied value must be greater than 0. 

> -g : Argument for GUI mode. Accepts '0' for headless or '1' for GUI mode. Default is headless.

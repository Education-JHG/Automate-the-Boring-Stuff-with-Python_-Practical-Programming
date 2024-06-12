#! python3
# ytSearcher.py - Search for youtube videos directly from the command line by including the name of the video as an argument or from the clipboard.
# Usage: python ytSearcher.py <name of video>

import webbrowser, sys, pyperclip

# Get video name

if len(sys.argv) > 1:
    # If value of sys.argv string > 1, it means user provided a search query
    videoName = ' '.join(sys.argv[1:]) # Joins seach query (before a list) but excludes the calling of the program in CLI.
else:
    videoName = pyperclip.paste()


webbrowser.open('https://www.youtube.com/results?search_query=' + videoName)

#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

# Provide source url where data is going to be extracted from.
url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True) # stores comics in ./xkcd
while not url.endswith('#'): # The first comic’s Prev button links to the https://xkcd.com/# URL, indicating that there are no more previous pages.
    # TODO: Download the page

    # TODO: Find the URK of the comic image.
    # TODO: Download the image.
    # TODO: Save the image to ./xkcd
    # TODO: Get the prev button's URL

print('Done.')
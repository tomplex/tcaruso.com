tcaruso.com
---

My website. Still in development.

## Installation

First, make sure you have bower installed. If you have npm...

    sudo npm install -g bower

then cd into the directory where you cloned this repo and type `bower install`  to install all frontend package dependencies.
 
Then create a python3.6 virtualenv and run 

    pip install -r requirements.txt
    
You're almost there. Run 

    python3.6 app/main.py
    
and the site will be running on localhost on port 8000.
## Welcome to the repo for oxyos.github.io, the website for Oxy Open Source!

## Git workflow

# Requirements
1. The `python` programming language, which can be downloaded from [python.org](https://python.org)
1. The python packages `Flask` and `Frozen_Flask`
    1. These can be installed by running `python3 -m pip install -r src/requirements.txt` within the same folder that the code is in

### Once you have all the requirements, continue to Environment Setup

# Environment Setup
1. On Github, **fork** oxyos/oxyos.github.io
1. Either using GitKraken (highly recommended), any other git GUI, or the command line, **clone** the repo
    1. For GitKraken: In the Remote section of the left panel in GitKraken, click the "+" button and add the forked repo as a remote

### Once you have the files, continue to Running the Site for Development

# Running the Site For Development
1. To develop, run the following command to start the built-in flask web server:
    1. MacOS/Linux: `make clean`
    1. Windows: `python3 src/main.py`
1. This will start the server on port `5000` on your machine, open any browser (Chrome, Firefox, Safari, etc...) and navigate to `localhost:5000`

### Once you have made your changes, continue to Building the HTML files

# Building the HTML Files
1. While running the server locally is perfect for development, GitHub pages needs raw HTML pages to function
1. The HTML files are all created from Flask templates, so we need to create these files
1. This can be achieved by several methods:
    1. MacOS/Linux: `make build`
    1. Windows: `python3 src/main.py build`
1. This will build all the HTML files and folders in the same folder that you downloaded

### Once you have finished building the site, continue to Making Contributions

# Making Contributions
1. `commit` and `push` the changes to your forked repo's `master` branch
1. Go to your forked copy of the repo on Github, and open a pull request from your master branch to oxyos/oxyos.github.io/master

### You are now done! Enjoy your updates to the site

# Keeping your Project Up-to-date With The Website
1. Run `git pull` to get all the changes

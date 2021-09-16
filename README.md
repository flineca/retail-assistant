# RETAIL-ASSISTANT
## Introduction
Basically a web appilication, but just used in local network, to help retailers manage the warehouse.
This project is aimed to self-learning practice about python backend usage, so it may not be very mature.

## Running Tips
For developers(win):

    cd !!!YOUR DIRECTORY!!!\retail-assistant\
    .\pyenv1\Scripts\activate
    cd RetailAssistant\
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8080

Then use a browser to open http://127.0.0.1:8080/ to look through or open http://127.0.0.1:8080/admin to manage.
If you want to go to the home page quickly you can start another process and run:

    cd !!!YOUR DIRECTORY!!!\retail-assistant\
    python brow.py

## Design Description
### Backend: Django
I may try learning flask in the future, but I decided to begin with django. My study notes is [here](.\addit\studydjango.md).

In total, I've developed these django apps that can be reused:
+ sss
(means Stock-Sale-Storage)  
You can look though the current storage and get further query results.

+ analysis
(to show data in e-charts)

### Frontend: bootstrap+jquery
A simplest site from <bootcss.com>.

Maybe in the future I will try Vue.js since it's more beautiful.

### Database: Sqlite3
You can aquire data in '.\RetailAssistant\db.sqlite3'

Maybe in the future I will introduce mysql.
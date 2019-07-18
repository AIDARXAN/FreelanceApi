Video Converter
===============

Installation
---------------

In the terminal choose the direcory, then put code below to clone the project
    
    git clone https://github.com/AIDARXAN/mp3-video_converter

Make sure that celery and redis are properly installed on your PC
    
    sudo apt-get install redis-server
If you want to check is redis-server working properly type command below

    redis-cli ping
    
It must return 

    PONG


To install all requirements which is needed to run project copy code bellow

    virtualenv mp3_env -p python3
    source mp3_env/bin/activate
    pip install -r requirements.txt

    python3 manage.py migrate

Run server =>  

    python3 manage.py runserver
    
Run celery task manager =>
    
    celery -A AsyncVideoConverter worker -l info

# Production to backup database

# Push Production to a new Github project

# Create a new c9.io blank project and clone Github project

# Setup developing envrionment

    sudo apt-get -y install python3.5
    sudo apt-get -y install python3.5-venv
    python3.5 -m venv myvenv
    pip freeze
    source myvenv/bin/activate
    pip freeze
    pip install --upgrade pip
    
    pip install django
    pip install django-bootstrap3
    pip install django-import-export
    pip install django-ipware
    
    cd cloud001x0920v3
    cd mysite
    cp db.sqlite3x09201033 db.sqlite3
    ./manage.py runserver $IP:$PORT
    
# Change view context, need to restart apache
    sudo service apache2 restart

python3 manage.py startapp f1
python3 manage.py startapp f2
python3 manage.py startapp s1

python3 manage.py startapp s2
--------------------------------------------
python3 manage.py startapp app001
  Not Found: /app001
    mysite/urls.py
      url(r'^app001/', include('app001.urls')),


---------------------------------------------




https://docs.djangoproject.com/en/dev/topics/auth/default/

python3 manage.py runserver $IP:$PORT


https://docs.djangoproject.com/en/1.10/intro/tutorial01/

sudo pip3 install django

python3 --version
=> Python 3.4.3

python3 -m django --version
=>1.10

django-admin startproject mysite

git add .
git commit -m"xxx"
git push -u origin master
-----------------
python3 manage.py startapp polls
python3 manage.py startapp materials


python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver $IP:$PORT



python3 manage.createsuperuser
=> admin/ksxxx
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Hi there! Welcome to Cloud9 IDE!

To get you started, create some files, play with the terminal,
or visit http://docs.c9.io for our documentation.
If you want, you can also go watch some training videos at
http://www.youtube.com/user/c9ide.

Happy coding!
The Cloud9 IDE team

# django002
# django003
# django004
# django004
# django004
# django006
# django007
# cloud001
# cloud001x0920
# cloud001x0920v2
# cloud001x0920v3

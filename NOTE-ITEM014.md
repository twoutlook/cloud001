# Install Python3.5
    sudo apt-get install -y python3.5 python3.5-venv
    


# setup virtual environment
    python3.5 -m venv myvenv
    source myvenv/bin/activate
   
# Install Django and others
    pip install django
    pip install --upgrade pip
    pip install django-import-export
    pip install django-bootstrap3
    pip install django-ipware
    
    
# git clone
    git clone git@github.com:twoutlook/cloud001.git

# make db
     cp db.1.sqlite3 db.sqlite3
     
     ./manage.py runserver $IP:$PORT      
     
# Dev
copy template and modify
add view
add url

### git add . 
### git status
        new file:   mysite/app001/templates/app001/item014.html
        modified:   mysite/app001/urls.py
        modified:   mysite/app001/views.py

### git commit -m"add ITEM014"
### git push -u origin master
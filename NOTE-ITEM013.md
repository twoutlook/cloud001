# Clone git project
    git clone git@github.com:twoutlook/cloud001.git

# Install python3.5
    
    sudo apt-get install -y python3.5 python3.5-venv
    
# Setup Virtual Envrionment 

    python3.5 -m venv myvenv
    source myvenv/bin/activate

# Install Required Modules
    pip install django
    pip install --upgrade pip
    pip install django-import-export
    pip install django-bootstrap3
    pip install django-ipware
    
# Get Production Data
download /home/demo/cloud001/mysite/db.sqlite3 to C:\2016\雲端佈告欄\數據備份\x09280949\
upload db.sqlite3 to c9.io
    
    
# Run Development Server
    cd /home/ubuntu/workspace/cloud001/mysite
    ./manage.py runserver $IP:$PORT
    
# Create a new super user
    ./manage.py createsuperuser

# Migrate DB
    ./manage.py makemigrations
    ./manage.py migrate


# Restart Apache Server
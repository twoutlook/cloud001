# Request
    Derrick陳宏宇:
    @Mark陈炳陵177 
    ITEM012-富鈦-压铸在制订单，富鈦有一個報表上的需求
    1.在機台頓數的分類下的內容，希望用物料代碼f02當作排序標準 ; 
    2.相同的物料代碼下，未生產數量f10合併加總
    我:
    1.在機台頓數的分類下的內容，希望用物料代碼f02當作排序標準 ; <<< 可以直接實現。
    
    
    2.相同的物料代碼下，未生產數量f10合併加總 <<< 不建議在現有html table 做合併，如有必要，可以考慮二次分組。







# Production to backup database

# Push Production to a new Github project

# Create a new c9.io blank project and clone Github project

# Setup c9.io developing envrionment
## install Python 3.5 and venv 

    sudo apt-get install python3.5 python3.5-venv

## setup virtual envrionment

    python3.5 -m venv myvenv
    pip freeze
    source myvenv/bin/activate
    pip freeze
    pip install --upgrade pip
    
    pip install django
    pip install django-bootstrap3
    pip install django-import-export
    pip install django-ipware
    
    cd cloud001
    cd mysite
    cp db.sqlite3x09201033 db.sqlite3
    ./manage.py runserver $IP:$PORT
    
# Change view context, need to restart apache
    sudo service apache2 restart


# Steps

# Clone Github project
git clone https://github.com/twoutlook/cloud001.git

# add model Item012
# register model Item012
# migrate db

    ./manage.py makemigrations
    ./manage.py migrate

# prepare sample data
ensure  f12 is data format in plain text

# login to admin and import
use item012-raw-6.xls sample data to import, use 48 records, done!

# template
# view
# url







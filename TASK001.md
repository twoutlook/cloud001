# Copy models' class

    copy 
    class Item010(models.Model):
    to 
    class Item011(models.Model):

# Migrate DB
    ./manage.py makemigrations
    ./manage.py migrate
    
# Add view


# Add url

# when deploy
    ./manage.py makemigrations
    ./manage.py migrate
    sudo service apache2 restart



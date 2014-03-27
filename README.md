energy_broker
=============

Energy broken prototype written in django
1 - You should have Python 2.7 and Django 1.6.2 installed. 

2 - You should create your database:
python manage.py syncdb

3 - You should populate your database with dummy data
python manage.py shell < energy_app/populate_db.py 

4 - How to run server?
python manage.py runserver

5 - localhost:8080/admin
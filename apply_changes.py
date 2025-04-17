import os
os.system("py manage.py makemigrations sito")
os.system("py manage.py migrate")
os.system("py manage.py runserver")
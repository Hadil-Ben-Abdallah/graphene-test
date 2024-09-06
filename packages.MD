python -m venv venv
pip install -U pip
python.exe -m pip install --upgrade pip
pip install graphene-django
pip freeze > requirements.txt
cd ...
django-admin startproject ...
django-admin startapp ...
python manage.py migrate
python manage.py migrate
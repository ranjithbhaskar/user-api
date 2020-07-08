

## Installation

Create a virtual python3 virtual environment & activate it
Database used is default sqllite.So no need of extra configuration

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.

```bash
pip install requirements.txt
```
Do migrations using 
```bash
python manage.py makemigration
python manage.py migrate

```
Create superuser to see db in the admin

```bash
python manage.py createsuperuser

```

Load dummy data using 
```bash
python manage.py load_dummy_data

```
Please check the app  usermanagement/management/commands folder for its documentation

Application deployed in Heroku
Please check this API link 

[https://user-api-app.herokuapp.com/user_management/activity](https://user-api-app.herokuapp.com/user_management/activity)



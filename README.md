# tree_menu

A simple tree menu implementation in Django.

## To run

Clone the repo

[Optional] create a virtual env in the project directory

```bash
python3 -m venv venv
```

In the terminal, run either:
    
```bash
pip install -r requirements.txt
pip install django
```

the app has no requirements other than django itself

then, cd into the directory with manage.py and populate the db with demo data by running:

```bash
python manage.py demo_db
```

and run the server:

```bash
python manage.py runserver
```

You can access the demo menu at localhost:8000/gpus

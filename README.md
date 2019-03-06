# questions and answers

# Make Sure Everything Is Installed:

Using Python 3.7.2

---

`brew install sqlite3`

`pip3 install virtualenv`

`virtualenv -p python3 env`

`source env/bin/activate`

`pip3 install -r requirements.txt`

---

in virtualenv, in 1st level of data_ingestion, next to manage.py, run: 

`python3 manage.py test`

then run

`python3 manage.py runserver`

---

# Django Admin

in your browser go here:

`http://127.0.0.1:8000/admin/`

---

login with...

---

superuser username: `admin`

password: `iceberg`

---

should take you here:

`http://127.0.0.1:8000/admin/`

---

click on and explore these models:  

`Question sets`
 
`Questions`

`Answers`
 
`Images`

---

got to:

`http://127.0.0.1:8000/`

click on the various endpoints:

```
{
    "question_set": "http://127.0.0.1:8000/question_set/",
    "question": "http://127.0.0.1:8000/question/",
    "answer": "http://127.0.0.1:8000/answer/",
    "image": "http://127.0.0.1:8000/image/"
}
```

You can perform all CRUD functions using the HTML form at the bottom of each page of the API.

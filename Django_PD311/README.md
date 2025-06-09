## Python Django

```
py --version
py -m venv .venv
.venv\Scripts\activate.bat

python.exe -m pip install --upgrade pip

py -m pip install Django
py
>>> import django
>>> print(django.get_version())
>>> exit

py -m django --version
mkdir djangotutorial

django-admin startproject mysite djangotutorial

cd djangotutorial

py manage.py runserver 4891

ctrl+c

py manage.py startapp polls

py manage.py runserver 4891

pip install psycopg2-binary

py manage.py migrate

py manage.py makemigrations polls

py manage.py sqlmigrate polls 0001

py manage.py migrate

deactivate
```

## Робота із табличками через консоль

```
py manage.py shell
>>> Question.objects.all()
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
>>> q.id
>>> q.question_text
>>> q.pub_date
>>> q.question_text = "What's up?"
>>> q.save()
>>> Question.objects.all()
>>> exit()

py manage.py shell
>>> Question.objects.all()
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)

>>> Question.objects.get(id=2)
>>> Question.objects.get(pk=1)

>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()

>>> q = Question.objects.get(pk=1)
>>> q.choice_set.all()

>>> q.choice_set.create(choice_text="Not much", votes=0)
>>> q.choice_set.create(choice_text="The sky", votes=0)
>>> c = q.choice_set.create(choice_text="Just hacking again", votes=0)

>>> c.question
>>> q.choice_set.all()
>>> q.choice_set.count()
>>> Choice.objects.filter(question__pub_date__year=current_year)

>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()
```

## Claer cache git
```
git rm -r --cached .
git add .
git commit -m ".gitignore Fixed"
```

## Clone Project GitClone
```
git clone https://github.com/novakvova/Django_PD311.git

cd Django_PD311

py -m venv .venv

.venv\Scripts\activate.bat

python.exe -m pip install --upgrade pip

py -m pip install Django
pip install psycopg2-binary
pip install Pillow

cd 1.SimpleSite

cd djangotutorial

py manage.py runserver 4891

```

## Робота із зображеннями
```
.venv\Scripts\activate.bat
cd 1.SimpleSite
cd djangotutorial
py manage.py runserver 4891

pip install Pillow

py manage.py makemigrations polls
py manage.py migrate




```
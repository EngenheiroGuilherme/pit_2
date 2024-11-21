# pit_2
 Trabalho acadêmico Cruzeiro, disciplina "Projeto Integrador Transdisciplinar de Engenharia de Software II"


``` bash
python -m venv venv
```

``` bash
venv\Scripts\activate
```

``` bash
pip install -r .\requirements.txt
```

``` bash
django-admin startproject pit_ii .
```

``` bash
python manage.py runserver
```

``` bash
python manage.py startapp app_main
```

``` bash
python manage.py makemigrations
```

``` bash
python manage.py migrate
```

``` bash
python manage.py runserver
```

"""
Acesse as rotas:

/: Lista de tarefas.
/tasks/create: Criar uma nova tarefa.
/tasks/update/<id>: Editar uma tarefa.
/tasks/delete/<id>: Deletar uma tarefa.
"""

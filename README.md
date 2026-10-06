# Sistema de Avaliação

## Como rodar o projeto

```bash
git clone https://github.com/DevAndradeGuilherme/sistema-avaliacao-labprogbackend.git
cd .\sistema-avaliacao-labprogbackend\
cd .\backend\
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## 1. Por que usamos um ambiente virtual em cada projeto?

Para separar as dependências de cada projeto e evitar conflitos entre versões de bibliotecas.

## 2. Por que dividimos o sistema em 3 apps em vez de um só?

Para deixar o projeto mais organizado. Cada app fica responsável por uma parte do sistema: alunos, disciplinas e avaliações.

## 3. Para que servem `makemigrations` e `migrate`, e por que nessa ordem?

`makemigrations` cria os arquivos com as alterações feitas nos models.

`migrate` aplica essas alterações no banco de dados.

Usamos nessa ordem porque primeiro precisamos criar as alterações e depois aplicá-las no banco.
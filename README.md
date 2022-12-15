![example workflow](https://github.com/kozarezov/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
# YaMDB

### _API resource for collect reviews on movies, books, music etc._

If you have an irresistible desire to read or watch something brand new,
and at the same time find out people's opinions regarding a title, our
super-cool API resource will save your time spent on searching for high-quality
content!

Visiting our website, you have a marvelous possibility to see reviews of
various books, films, music track etc. and find out their rating, genre,
category!

Moreover, if you are keen on sharing your opinion with other users and
influence their choice (you may have an influence on what your friend will
check out on Netflix this Friday, is it great?), then just register! It will
also help you to leave comments on the reviews of other respected users.

IMDB can leave you at any time, but reliable YaMDb will always be available

Check it out!

## 1. Technologies:

    - Python 3.8
    - Django 3.0
    - Djangorestframework 3.12.4  
    - Docker  

## 2. How to launch:

The project is assembled using Github Workflow when pushing to the Master branch.

After deployment, the project is available by IP

#### IP adress to deployed project:

```sh
 http://158.160.53.219
 ```

## 3. Environment variables:

    - DB_ENGINE=django.db.backends.postgresql
    - DB_NAME=postgres
    - POSTGRES_USER=postgres
    - POSTGRES_PASSWORD=postgres
    - DB_HOST=db
    - DB_PORT=5432

**Example:** `/infra/example.env`


## 4. API documentation:

#### Go to Redoc documentation on localhost:

```sh
http://localhost/redoc/
 ```

## 5. Requests examples:

#### Authorization:

**POST:** `/api/v1/auth/signup/` - to signup for new user

#### Actions with titles:

**GET:** `/api/v1/titles/` - to get all titles list

**POST:** `/api/v1/titles/` - to add a title

**PATCH:** `/api/v1/titles/{titles_id}/` - to update your title

**DELETE:** `/api/v1/titles/{titles_id}/` - to delete your title

#### Actions with reviews / comments:

**POST:** `/api/v1/titles/{title_id}/reviews/ ` - to create a review

**GET:** `/api/v1/titles/{title_id}/reviews/ ` - to get a title's reviews

Denis Kozarezov [GitHub](https://github.com/kozarezov)
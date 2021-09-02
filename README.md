<div align='center'>
    <img src='https://user-images.githubusercontent.com/55309160/131547708-89c3fc11-f1ac-4d98-a109-2bf31883c814.png'></img><br/><br/>
    <h2><b>Chess Challenge</b></h2>
    <img src='https://img.shields.io/badge/Python-3.8-blue'></img>
    <img src='https://img.shields.io/badge/Django-3.1.7-green'></img>
    <img src='https://img.shields.io/badge/Django_REST_Framework-3.12.3-red'></img>
    <img src='https://img.shields.io/badge/postgres-13-green'></img>
    <img src='https://img.shields.io/badge/Coverage-5.5-red'></img>
    <img src='https://img.shields.io/badge/Pytest-6.2.2-red'></img>
</div>

# Backend Technical Assessment

Technical Assessment to Python Backend Position in Bravi

## Challenge

You must develop an application that allows the registration of chess pieces (type/name
and color). In addition, given a location on a coordinate chosen by the user and the piece id,
if it is a knight, find out all possible locations where the knight can move in 2 turns.
You are expected to build an API.
API
The api should:

● receive the piece type/name and the color and return the piece id;

● receive cell coordinate (in Algebraic notation) and the piece id and return an array
with all possible locations where the knight can move within 2 turns.

## Installation

To run this project you need basically docker and docker compose.

### Run with

```bash
docker-compose up -d
```

### Run migrations with

```bash
docker-compose exec api python manage.py migrate
```

### To run tests

```bash
docker-compose exec api pytest
```

### To get coverage report

```bash
docker-compose exec api coverage report -m
```

### To see logs

```bash
docker-compose logs
```

### Stop with

```bash
docker-compose down
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
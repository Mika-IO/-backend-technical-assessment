<div align='center'>
    <img src='https://user-images.githubusercontent.com/55309160/131540453-713f32a2-202a-48e3-a419-3bc5639ad45e.png'></img><br/><br/>
    <h2><b>Chess Challenge</b></h2>
    <img src='https://img.shields.io/badge/Python-3.8-blue'></img>
    <img src='https://img.shields.io/badge/Django-green'></img>
    <img src='https://img.shields.io/badge/Django_REST_Framework-red'></img>
    <img src='https://img.shields.io/badge/postgres-green'></img>
    <img src='https://img.shields.io/badge/Pytest-red'></img>
</div>

# Backend Technical Assessment

Technical Assessment to Python Backend position in Bravi

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
docker-compose exec api python manage.py migrations
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
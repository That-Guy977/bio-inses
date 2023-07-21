# bio-inses

Bio-INSES is a prototype tool designed to aid farmers in incorporating [biological control](https://en.wikipedia.org/wiki/Biological_pest_control) into insect pest management strategies, by analyzing the insect population and recommending suitable pest control insects.

Tested on Python 3.10, 3.11.

## Setup

- Clone the repo:
```sh
# Using git:
$ git clone https://github.com/that-guy977/bio-inses
# Using gh:
$ gh repo clone that-guy977/bio-inses
```
- Set up `venv` if desired.
- Install dependancies:
```sh
$ pip install -r requirements.txt
```

## Activation

##### Website

Managed via [Django](https://www.djangoproject.com/).
Defaults to `localhost:8000`.
```sh
$ python manage.py runserver [address:port]
```

##### Standalone simulation

```sh
$ python simulation.py
```

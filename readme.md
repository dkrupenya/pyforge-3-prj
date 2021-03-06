# Pyforge-3 project

Demo application with `Flask`, `SQLAlchemy`, and `Requests`.
The application allows to get information about compound from external API and keep compounds cache in PostgreSQL.
## Run Flask locally

```shell script
# create and activate venv
python3 -m venv venv
source venv/bin/activate

# install dependencies
python3 -m pip install -r requirements.txt

# start postgres in docker
docker compose up postgres

# run flask locally
dotenv -f .env.local run -- python3 ./services/web/manage.py run
```

## Run Flask in docker

```shell script
docker compose up
```

## Run CLI
When you have Postgres and Flask running 
you can retrieve compounds information from external API:
```shell script
# run CLI app locally with help
python3 services/main.py --help

# get compound information either from database or from API
python3 services/main.py get_compound --compound=<COMPOUND_CODE>
# or just 
python3 services/main.py get_compound
# and then enter compound code in prompt
```
To check cached records in db:
```shell script
# print compounds in db
python3 services/main.py get-all
```

## Run tests for CLI app
```shell script
pytest
```
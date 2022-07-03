# Pyforge-3 project

Demo application with `Flask`, `SQLAlchemy`, and `Requests`.
The application allows to get information about compound from external API and keep compounds cache in PostgreSQL.
## Run Flask locally

```shell script
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
python3 services/main.py add-compound --compound=<COMPOUND>
# or just 
python3 services/main.py add-compound
# and then enter compound ID in prompt
```
To check cached records in db:
```shell script
# print compounds in db
python3 services/main.py get-all
```
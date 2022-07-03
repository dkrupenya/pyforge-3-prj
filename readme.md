### Run locally

```shell script
# install dependencies
python3 -m pip install -r requirements.txt

# start postgres in docker
docker compose up postgres

# run flask locally
dotenv -f .env.local run -- python3 ./services/web/manage.py run

# run CLI app locally with help
python3 services/main.py --help

# print compounds in db
python3 services/main.py get-all

# add compound to db if it is not in db
python3 services/main.py add-compound --compound=<COMPOUND>
# or just 
python3 services/main.py add-compound
# and enter compound name in prompt
```
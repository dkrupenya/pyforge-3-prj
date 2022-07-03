FROM python:3.9.13-slim-bullseye

ENV APP_HOME=/usr/src/app
WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat

RUN pip install --upgrade pip

# create the app user
RUN addgroup --system app && adduser --system --group app

COPY ./services/web/requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./services/web /usr/src/app/

RUN mkdir -p $APP_HOME/logs
# chown all the files to the app user
RUN chown -R app:app $APP_HOME
USER app

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
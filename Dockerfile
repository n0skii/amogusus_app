FROM python:3.9.7-slim-bullseye

LABEL Pavel Kovalenko <https://github.com/n0skii>

EXPOSE 8000

# RUN python --version
# ADD . /django-comp
# ENV VIRTUAL_ENV=/django-comp
# RUN python -m venv $VIRTUAL_ENV
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# RUN python --version

RUN apt-get update
RUN apt-get -qq -y install apt-utils curl
RUN apt-get install -y gcc python3-dev musl-dev libc-dev build-essential

ADD . /web
WORKDIR /web/web

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python ./amogusus_test/manage.py makemigrations
RUN python ./amogusus_test/manage.py migrate
CMD [ "python", "./amogusus_test/manage.py", "runserver", "0.0.0.0:8000" ]

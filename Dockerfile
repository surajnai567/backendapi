# base image
FROM python:3.7.10
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# use entrypoint shell script
RUN chmod +x build/backend/entrypoint.sh
ENTRYPOINT ["build/backend/entrypoint.sh"]
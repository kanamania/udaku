# pull official base image
FROM python:3.10.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
&& apt-get install curl netcat zsh git -y \
&& apt-get clean

# set work directory
WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN pip install --upgrade pip
# zsh config
RUN curl -L https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh | bash
# copy entrypoint.sh
COPY ./entrypoint.sh /app/entrypoint.sh

COPY . /app/
RUN chmod +x /app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

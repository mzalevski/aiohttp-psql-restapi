FROM python:3.7

# Dependencies for aiohttp
RUN pip install aiohttp psycopg2

# Run & expose the server
COPY . /usr/src/app
WORKDIR /usr/src
CMD [ "python3" "app" ]

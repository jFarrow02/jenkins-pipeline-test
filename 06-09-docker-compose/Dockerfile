FROM node:13-alpine

ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=duracell99

RUN mkdir -p /home/app

COPY /app /home/app

# set default dir so that next commands execute in /home/app
WORKDIR /home/app

# will execute npm install in /home/app
RUN npm install

# no need for /home/app/server.js because of WORKDIR
CMD ["node", "server.js"]
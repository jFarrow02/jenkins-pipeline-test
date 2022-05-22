FROM node:17.0.1-alpine

WORKDIR /test_app

COPY package.json package-lock.json ./

RUN npm install

COPY . ./

RUN ls -l

CMD ["npm", "run", "start"]
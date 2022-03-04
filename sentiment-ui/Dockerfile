FROM node:latest

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
RUN npm install -g npm@8.5.3

COPY . /app

CMD ["npm", "start"]
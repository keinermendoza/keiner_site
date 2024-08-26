# for use in docker-compose.example.yml
FROM node:18.20.4-bullseye
WORKDIR /app
ENV NPM_CONFIG_UPDATE_NOTIFIER=false
COPY ./package*.json ./
RUN npm install
COPY . .
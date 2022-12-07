FROM node:19

WORKDIR /app/frontend

COPY package.json ./

COPY ./ ./

RUN npm install -g npm@latest
RUN npm i

CMD ["npm", "run", "dev"]

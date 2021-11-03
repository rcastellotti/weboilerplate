FROM node:16.10.0-alpine as build-stage
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build
CMD ["node", "build"]

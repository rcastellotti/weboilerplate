FROM node:16.10.0-alpine as build-stage
COPY . .
RUN npm install
RUN npm run build
CMD ["node", "build"]

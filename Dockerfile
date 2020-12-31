FROM python:3-alpine as build
WORKDIR /usr/src/app
RUN apk add --update make
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN make publish

FROM nginx:stable-alpine as run
COPY --from=build /usr/src/app/output /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

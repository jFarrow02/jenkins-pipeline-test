# Writing Dockerfile

Dockerfiles create Docker images through layers of instructions:

`Dockerfile`:

```

FROM nginx:alpine

COPY website /website
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
```
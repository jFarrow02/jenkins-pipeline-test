# Make

**Make** is a popular build tool. It's used to compile and package software.

`Makefile`:

```
.PHONY: run_website

run_website:
    docker build -t {image-name} . && \
        docker run --rm --name {container-name} -p {host-port}:{container-port} {image-name}:{tag}
```
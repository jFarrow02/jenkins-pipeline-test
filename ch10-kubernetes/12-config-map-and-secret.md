# CopnfigMap & Secret Volume Types

## When to Use ConfigMap and Secret Volume Types?
- individual key-value pairs
- files that can be mounted in container

`config-file.yaml`:
```
apiVersion: v1
kind: ConfigMap
metadata:
    name: mosquito-config-file
data:
    mosquito.conf: | // name of file
        log_dest stdout // file contents
        log_type all
        log_timestamp true
        listener 9001
```

`secret-file.yaml`:
```
apiVersion: v1
kind: Secret
metadata:
    name: mosquito-secret-file
type: Opaque
data:
    secret.file: |
    {base-64-secret-string-here}
```
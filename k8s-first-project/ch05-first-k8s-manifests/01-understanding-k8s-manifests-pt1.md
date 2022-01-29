# Understanding K8s Manifests

K8s creates resources thru `.yaml` files called **manifests**.

## Create a Deployment with Manifest

`kubectl create deployment --dry-run=client --image {image-name} {depl-name} --output=yaml > {manifest-filename}`
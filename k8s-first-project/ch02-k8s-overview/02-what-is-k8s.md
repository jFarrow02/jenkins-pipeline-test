# What is K8s?

**Kubernetes** is a planet-scale container orchestration system.

- Can manage large clusters of nodes and pods.

## Fundamental K8s Objects

1. **Pods** are the smallest unit of compute. Pods group similar containers in a logical unit. 
2. Pods get scheduled onto **Nodes**. Nodes host Pods and configure networking between them.
3. **Deployments** scale and manage Pods.
4. **Services** provide a single IP address for a group of related Pods.
5. **Ingresses** and **Ingress Controllers** make your app internet accessible.
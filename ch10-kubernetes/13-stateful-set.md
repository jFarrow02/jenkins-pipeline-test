# What is StatefulSet?

Examples of stateful applications:
- databases
- applications that store state date

Stateless applications
- don't keep record of state
- each request is completely new

Stateless applications are deployed using **Deployment** component in K8s. **Stateful** apps are dployed using **StatefulSet**.

What is the difference?

## StatefulSet vs. Deployment

| StatefulSet                                       | Deployment                                        |
|---------------------------------------------------|---------------------------------------------------|
| Deployed with **StatefulSet**                     | Deployed with **Deployment**                      |
| replicate Pods                                    | Replicate Pods                                    |
| Can't be created/deleted in random order          | Can be created/deleted in random order            |
| Pods **not** identical                            | Pods **identical**                                |
| Pod receives unique, persistent ID                | Pods are interchangeable                          |

## Scaling DB Applications
Why do StatefulSet pods need a unique Id? To maintain data consistency. Only **one** pod can be allowed to update data in a databse.

The **Manager** pod may update data; **Worker** pods cannot. Note that each pod has its **own** physical storage volume (not shared across pods). Continuously synchronize from Manager pod; Manager changes data and each Worker updates itself to reflect.

### Persistent Volumes
Contains data as well as Pod state. When pod dies, the storage gets re-attached to the replacement pod with the identity state intact. MUST use remote storage.

### Pod Identifiers
Stateful set pods get **fixed, ordered** names. The first pod is the Manager. Pods are created and deleted in order/reverse order.

### DNS Endpoints
Each Stateful Set pod gets its own DNS name, which deployment pods do not have.

## Replicating Stateful Apps is HARD
You have to do the following yourself:
- Configure cloning and data synchronization
- Make remote storage available
- Manage and back-up

So, stateful applications are NOT recommended for containerized environments
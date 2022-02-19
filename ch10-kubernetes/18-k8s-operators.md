# K8s Operators

K8s Operators are used for **Stateful** applications.

All replicas in a stateful app has its own state and identity. Creation/destruction order is important. This makes automation difficult. They require someone to "operate" them. **But**, we want to **avoid** manual intervention!

An **Operator** replaces the human operator with a **software** operator to deploy the application, create a cluster of multiple replicas, recover on failure etc.

An operator watches for changes, checks for differences, and takes action in the same way the normal K8s control loop does. It also uses **CRDs** (Custom Resource Definitions), custom K8s components that extend the K8s API.

### Who Creates Operators?
Experts in the business logic of installing and running a specific application cluster (e.g. MySQL, Postgres, etc.). That group creates the Operator. See OperatorHub.io.

An **Operator SDK** exists for teams who want to create their own operators.
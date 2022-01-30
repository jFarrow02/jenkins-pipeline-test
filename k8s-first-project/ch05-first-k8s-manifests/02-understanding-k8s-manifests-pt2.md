# K8s Manifest Pt. 2

## Metadata:
1. **apiVersion**: specifies API that defines the deployment object
2. **kind**: specifies type of object being created
3. **metadata**:
    - creationTimestamp: date/time resource was created
    - labels:
        - app: 
    - name: name of the resource
4. **spec**:
    - replicas: # of resources to create
    - selector: selects pods that belong to this deployment; associates pods with app defined in `labels.app`
    - strategy: Deployment strategy ('Recreate', 'Update', etc.)
5. template: defines templates for pods
    - metadata
    - spec: Pod spec
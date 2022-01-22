# Intro to AWS

A collection of cloud-based services. We will focus on:

1. Compute(EC2): virtual server instances
2. Storage(S3)
3. Networking: VPC (Virtual Private Cloud)
4. Identity & Permission Management: IAM
5. Containers: ECR etc.

## Scopes of Services
 
```
 |-Global: AWS Account --> IAM Users
    |-Region 1 --> S3, VPC, Dynamo DB
        |-AZ 1  --> EC2, EBS etc.
        |-AZ 2
        |-AZ 3
        |-etc
```
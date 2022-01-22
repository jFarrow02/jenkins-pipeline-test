# IAM - Manage Users, Roles, and Permissions

Manage access to AWS services and resources. **Root user** is created by default, with unlimited privileges.

Best practice is to create an **admin user** with less privileges than root user, to create EC2 instances and other services, create users, groups, roles, etc. 

AWS will recommend to create the admin user as first step after creating a new account.

In addition to **human** users, you can also create **system** users, such as Jenkins to deploy containers on EC2, or push images to AWS Docker repo. Admin user can also create these system users.

### Users
**Users** are humans or systems that need access to AWS account or services.

### Groups
Use for granting same permissions to multiple users.

### Roles
For granting AWS services access to other AWS services (policies cannot be assigned directly to services; must assign the policy to the role, then assign the role to the service).

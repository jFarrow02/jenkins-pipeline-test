# Intro to AWS CLI

The **AWS CLI** is a powerful command line tool with commands for every AWS service and resources.

## Installing AWS CLI

**For MacOS**:
```
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```

## Configure AWS CLI to connect to AWS Account
Need an **access key** and **secret access key**.

```
aws configure

AWS Access Key ID [None]: {ACCESS_KEY}
AWS Secret Access Key [None]: {SECRET_ACCESS_KEY}
Default region name [None]: {REGION_NAME}
Default output format [None]: json
```

These values are set in ~/.aws

## AWS CLI Command Structure

`aws <command> <subcommand> [options and parameters]`

#### Create a new Security Group
1. Create SG:
    - `aws ec2 describe-vpcs`
    - `aws ec2 create-security-group --group-name {name} --description "{description} --vpc-id {vpc}"`

2. List info about SG:
    - `aws ec2 describe-security-groups --group-ids {sg-id}`

3. Add firewall rules:
    - `aws ec2 authorize-security-group-ingress --group-id {sg-id} --protocol {protocol} --port {port} --cidr {ip-addr}/{CIDR-block}` 

#### Create a Key Pair for SSH into EC2 instance
1. `aws ec2 create-key-pair --key-name {key-name} --query 'KeyMaterial' --output text > keypair-cli.pem`

#### Create an EC2 Instance from CLI:
1. Get subnet ID:
    - `aws ec2 describe-subnets`

2. Get security group ID:
    - `aws ec2 describe-security-groups`

3. Get image ID:

4. Create Instance
```
aws ec2 run-instances \
--image-id {ami-id} \
--count 1 \
--instance-type t2.micro \
--key-name {keypair-name} \
--security-group-ids {secgroup-id} \
--subnet-id {subnet-id}
```

5. Get instances:
    - `aws ec2 describe-instances`
    - Get public IP addr of instances
    - Change permission on private key:
        `chmod 400 {key-name}.pem`
    - SSH into new instance

### Filter and Query "describe" Commands

You can **filter** the components that a command returns:
`aws {service} {command} --filter`

You can also **query**, or pick **specific attributes** of a component to return:

`aws ec2 describe-instances --filter "Name=instance-type,Values=t2.micro" --query "Reservations[].Instances[].InstanceId"`

## Using IAM CLI Commands

1. Create IAM group:
    - `aws iam create-group --group-name MyGroupCli`
2. Create IAM user:
    - `aws iam create-user --user-name MyUserCli`
3. Add User to Group
    - `aws iam add-user-to-group --user-name MyUserCli --group-name MyGroupCli`
4. Get group
    `aws iag get-group --group-name MyGroupCli`
5. Add permissions to Group
    - Get policy ARN: from Management Console or: `aws iam list-policies --query 'Policies[?PolicyName==`AmazonEC2FullAccess`].{ARN:arn} --output text`

    `aws iam attach-group-policy --group-name MyGroupCli --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess`

    `aws iam list-attached-group-policies --group-name MyGroupCli`

6. Add User credentials:
 - `aws iam create-login-profile --user-name MyUserCli --password Mypwd123test --password-reset-required`

7. Create Password Change Policy and Assign to Group
`changePasswordPolicy.json`:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam.GetAccountPasswordPolicy",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "iam:ChangePassword",
            "Resource": "arn:aws:iam::{12-digit-account-num}:user/$(aws:username)"
        }
    ]
}
```

`aws iam create-policy --policy-name changePwd --policy-document file://changePasswordPolicy.json`

- Capture ARN of policy created in previous step

`aws iam attach-group-policy --group-name MyGroupCli --policy-arn {arn}`

8. Create Access Keys for Programmatic Access
 - `aws iam create-access-key --user-name MyUserCli`

9. Use your New User to Access AWS
**3 Ways** of changing AWS User:
    - Use `aws configure` to change default User
    - Set env vars to act temporarily as a user:
        export AWS_ACCESS_KEY_ID={access-key-id}
        export AWS_SECRET_ACCESS_KEY={secret-access-key}
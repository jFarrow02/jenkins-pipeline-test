# Credentials in Jenkins

## "Credentials Plugin"
Offers a way to store and manage creds centrally, rather than across different plugins/services.
    - Globally scoped

## Credentials Scopes
1. System: only available on Jenkins server. Not visible/accessible by Jenkins jobs
2. Global: accessible everywhere
3. Project: Limited to project, only for multibranch pipelines

## Credentials Types
1. Username & Password
2. Secret File
3. Certificate
4. Secret text
5. New types based on plugins
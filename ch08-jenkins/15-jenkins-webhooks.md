# Automate Jenkins Jobs with Webhooks

We usually want to kick off our pipelines automatically whenever code is pushed to the SCM repo, instead of manually.

2 steps:
1. Configure Webhook plugin in Jenkins
2. Configure Gitlab to send notifications to Jenkins on commit
3. Configure Jenkinsfile

## Configure Webhook Plugin in Jenkins
1. Dashboard > Manage Plugins > search for "Gitlab" plugin > Install w/o restart
2. Manage Jenkins > configure system > Gitlab
3. Configure parameters:
    - Connection Name
    - Gitlab Host URL
    - Credentials > Add > Gitlab API token
    - Paste token, select token ID and add token
4. Dashboard > {pipeline-name} > Build Triggers
    - Verify that "Build when a change is pushed to Gitlab..." is checked

4. Generate API token in Gitlab:
    - Gitlab > user profile > Access Tokens
    - Add token name, expiration date, permissions ("api" in this case)
    - Save your access token in a secure location; you will not be able to access it later

## Configure Gitlab to Send Notifications to Jenkins on Commit

1. Gitlab > Settings > Integrations > Jenkins CI
2. Check boxes for: 
    - Enable Integration > Active
    - Trigger > Push
3. Configure Jenkins connection:
    - Jenkins URL (with port) **NOTE**: Gitlab does not allow localhost connections (if your Jenkins server is running on localhost)
    - Project Name (should be job name in Jenkins)
    - Username: Jenkins login username
    - Password: Jenkins login password
4. Save changes

## Configure Webhooks for MULTIBRANCH Pipelines
1. Manage Plugins > Multibranch Scan Webhook Trigger plugin
2. Dashboard > {multibranch-job} > Scan Multibranch Pipeline Triggers
    - Select "Scan by webhook"
3. Trigger token > add (arbitrary) token name

We will tell Gitlab to send Jenkins a notification on a specific URL including the token. Jenkins will receive the request, check the token, and trigger a multibranch pipeline that has a "Scan by webhook" configured for **that specific token**.

4. Configure Gitlab:
    - Webhooks:
        - URL: add IP addr and port of Jenins server and token name in place of [token]
        - Trigger > Push events
        - Add Webhook
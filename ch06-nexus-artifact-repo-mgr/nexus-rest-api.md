# Nexus REST API

Nexus' REST API allows you to query Nexus Repository for different information:
- What components available?
- What are the versions?
- Which repositories available?
- etc.

This information is needed in your CI/CD pipeline.

## Accessing Nexus REST endpoint
- Use a tool like curl or wget to execute http request
- Provide user and credential of Nexus user

## Query examples
1. List available repositories for user:
`curl -u user:pwd -X GET '<nexus-ip>:8081/service/rest/v1/repositories`

2. List components in a repository:
`curl -u user:pwd -X GET '<nexus-ip>:8081/service/rest/v1/components?repository=<repo-name>`

3. Get a single component:
`curl -u user:pwd -X GET '<nexus-ip>:8081/service/rest/v1/components/<component-id>`


# Intro to Artifact Repository Manager

## I. What is an Artifact Repository?

A. An **artifact repository** stores **artifacts**, or apps built into a single file
    1. JAR, WAR, ZIP, TAR, Docker images etc.
    2. The repository must support the artifact file type
    3. Artifact repo managers manage multiple artifact types

B. Nexus
    1. Nexus is one of the most popular artifact repository managers
    2. Upload, store, and download artifacts
    3. Central storage for your artifacts

    You can use Nexus to host internal artifacts, or as a PROXY for public artifact repo managers. This will allow you to use ONE repo for public and private artifacts

C. Public Repository Managers
    Public artifact repo managers store libraries/frameworks that you use as dependencies in your projects. Examples include:
    
    - Maven     - pypi
    - NuGet     - npm

D. Features of Repository Managers
    1. Integration with LDAP for access management
    2. Flexible and powerful REST API endpoints for integration with other tools
        i. Upload, download artifacts in an AUTOMATED way
        ii. Integrates with other CI/CD tools via REST API
    3. Backup and restore is easily configurable
    4. Supports multiple artifact formats (storage, managing tags and versions, etc)
    5. Cleanup policies: Policies defining how/when to dispose of older versions of artifacts
    6. Search functionality for artifact versions
    7. User token support for system user authentication
        i. Supports auth for system (non-human) users
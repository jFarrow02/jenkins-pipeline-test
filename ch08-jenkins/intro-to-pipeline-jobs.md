# Intro to Pipeline Jobs

## Create a New Pipeline Job
1. Dashboard > New > Pipeline Job > Pipeline > Pipeline Script
    - Pipeline scripts written in Groovy
    - "Use Groovy Sandbox" - allows you to use approved Groovy functions w/o admin approval
    - Best practice is to write your script as part of your **source code**

2. Pipeline script from SCM
    - SCM: select "Git"
    - Repository URL
    - Credentials
    - Branch specifier

3. Create `Jenkinsfile` in project root. Jenkinsfile will contain Groovy script for your pipeline. 2 types of syntax:

|   Scripted                                            |     Declarative                           |
|-------------------------------------------------------|-------------------------------------------|
| first syntax                                          | more recent addition                      |
| Groovy engine                                         | easier to get started, not as powerful    |
| advanced scripting capabilities, difficult to start   | pre-defined structure                     |
| high flexibility                                      |                                           |

    
## Jenkinsfile syntax:
    
`Jenkinsfile`:
    ```
        pipeline { // "pipeline" must be top level
            agent any { // "agent" where to execute
                stages { // where the "work" happens
                    stage("build) { // stage name
                        steps { // stage steps

                        }
                    }
                }
            }
        }

        node {
            // groovy script
        }

    ```
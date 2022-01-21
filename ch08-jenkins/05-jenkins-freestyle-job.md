# Freestyle Jobs in Jenkins

Basic Jenkins job for simple workflows. Would more likely use another type of job in actual projects.

- Test an application
- Build
- Push to repository, etc.

## Create First Freestyle Job

1. New Items > Create New Job > Freestyle Project
2. Name your project
3. Build > Add Build Step > Execute Shell
    - Execute shell commands **directly in the container**
4. Add Build Step > Invoke top-level Maven targets
    - Execute commands installed as **plugins**
5. Dashboard > run build
    - See build output in <build-name> > Console Output

## Installing Build Tools as Plugins vs. Directly on Server
 
- Installing on the **server/container** is **more flexible**, as it gives you greater control in writing scripts and build tool commands are available throughout Jenkins

- Installing build tools as **plugins** require a process similar to the one below:

**Example: Install Nodejs as Plugin**
1. Dashboard > Manage Jenkins > Manage Plugins
2. Search for available plugins for nodejs
3. Dashboard > Global Tool Configuration
4. NodeJS > Add NodeJS
5. NodeJS installation is now available in "Add Build Script" for your job(s)

## Connect Job to Git Repo
1. Dashboard > job > Source Code Management
2. Jenkins needs **credentials** in order to connect to and clone repo on its local file system
3. Credentials > Add > add your Git repo credentials
4. Specify a single branch trigger, or "*" for all branches
5. Jenkins checks out code locally and runs commands (test, build etc.) agains locally checked out code
    - {container} /var/jenkins_home/jobs: Jenkins jobs created here, including builds.
    - /var/jenkins_home/workspace: Local location for checked-out Git repositories
6. Add build triggers OR Build > Execute shell > Command
    - `chmod u=rwx freestyle-build.sh`
    - `./freestyle-build.sh`

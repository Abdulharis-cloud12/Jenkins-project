# Jenkins-project
Jenkins-Python-Socket-Pipeline

Overview:-

This project demonstrates a Jenkins pipeline that pulls a Python script from a GitHub repository and executes it. The Python script, built using the socket module, retrieves the IP address of a given website.

Workflow

1. Python Script:

Uses Python sockets to fetch the IP address of a specified domain.



2. Jenkins Pipeline:

Written in Groovy, it automatically pulls the latest Python script from GitHub.

Executes the script in Jenkins and displays the output.



3. Manual Trigger:

Currently, the pipeline is manually triggered from Jenkins.




Technologies Used:-

Python (Sockets module)

Jenkins (Pipeline execution)

Groovy (For pipeline script)

GitHub (Version control)


Setup Instructions:-

1. Install Jenkins and required plugins.


2. Create a new Pipeline project in Jenkins.


3. Configure Jenkins to pull from your GitHub repository.


4. Add the following Groovy script in the pipeline:


pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout('https://github.com/Abdulharis-cloud12/Jenkins-project.git')
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/Abdulharis-cloud12/Jenkins-project.git'
                bat 'python ip.py'
            }
        }
    }
}



5. Trigger the pipeline and check the output in Jenkins.


Future Enhancements:-

Automate pipeline execution using GitHub webhooks.

Integrate logging for better debugging.

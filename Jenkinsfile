pipeline {
    agent any
    stages {
        // CI build (building and testing if the app is ok)
        stage('Build') {
            steps {
                echo 'Running build automation'
                sh './build.sh'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing the app'
                sh 'source ./env/bin/activate && pytest -v ./yourapp/tests/test_views.py'
            }
        }
        // packaging the image in a docker image
        stage('Build Docker Image') {
            when {
                branch 'master'
            }
            steps {
                script {
                    app = docker.build("devopsstrg/flask-web-app")
                    app.inside {
                        sh 'echo $(curl localhost:8080)'
                    }
                }
            }
        }
        // push it to cocker hub
        stage('Push Docker Image') {
            when {
                branch 'master'
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker_hub_login') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }
        // pull the image and run an instance of it
        stage('DeployToProduction') {
            when {
                branch 'master'
            }
            steps {
                input 'Deploy to Production?'
                milestone(1)
                withCredentials([usernamePassword(credentialsId: 'production_server_login', usernameVariable: 'USERNAME', passwordVariable: 'USERPASS')]) {
                    script {
                        sh "sshpass -p '$USERPASS' -v ssh -o StrictHostKeyChecking=no $USERNAME@$prod_ip \"docker pull devopsstrg/flask-web-app:${env.BUILD_NUMBER}\""
                        try {
                            sh "sshpass -p '$USERPASS' -v ssh -o StrictHostKeyChecking=no $USERNAME@$prod_ip \"docker stop flask-web-app\""
                            sh "sshpass -p '$USERPASS' -v ssh -o StrictHostKeyChecking=no $USERNAME@$prod_ip \"docker rm flask-web-app\""
                        } catch (err) {
                            echo: 'caught error: $err'
                        }
                        sh "sshpass -p '$USERPASS' -v ssh -o StrictHostKeyChecking=no $USERNAME@$prod_ip \"docker run --restart always --name flask-web-app -p 8080:8080 -d devopsstrg/flask-web-app:${env.BUILD_NUMBER}\""
                    }
                }
            }
        }
    }
}

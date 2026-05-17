pipeline {

    agent { label 'ec2-agent-jobtrackr' }

    stages {

        stage('Clone Code') {

            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build Docker Image') {

            steps {

                sh 'docker build -t jobtrackr-app .'

            }
        }

        stage('Remove Old Container') {

            steps {

                sh 'docker rm -f jobtrackr-container || true'

            }
        }

        stage('Deploy Container') {

            steps {

                sh 'docker run -d -p 8000:8000 --name jobtrackr-container jobtrackr-app'

            }
        }

    }
}

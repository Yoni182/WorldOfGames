pipeline {
    agent any

    stages {
        stage('Checkout - my repo') {
            steps {
                git branch: 'main', url:  'https://github.com/yoni182/WorldOfGames'
            }
        }
        stage('Build docker image') {
            steps {
                sh 'docker build -t wog-scores:latest .'
            }
        }
        stage('Run docker image using compose (detached) ') {
            steps {
                sh 'docker-compose up -d'
            }
        }
        stage('Test the score html with selenium') {
            steps {
                sh 'pip3 install selenium'
                sh 'e2e.py'
            }
        }
        stage('Down the docker image and push to repo ') {
            steps {
                sh 'docker-compose down'
                sh 'docker push yoni182/wog-scores:latest'
            }
        }
    }
}

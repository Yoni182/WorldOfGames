pipeline {
    agent any

    stages {
        stage('Checkout - my repo') {
            steps {
                git branch: 'master', url:  'https://github.com/NikitaForGit/WorldOfGames'
            }
        }
        stage('Build docker image') {
            steps {
                bat 'docker build -t wog-scores:latest .'
            }
        }
        stage('Run docker image using compose (detached) ') {
            steps {
                bat 'docker-compose up -d'
            }
        }
        stage('Test the score html with selenium') {
            steps {
                bat 'pip3 install selenium'
                bat 'e2e.py'
            }
        }
        stage('Down the docker image and push to repo ') {
            steps {
                bat 'docker-compose down'
                bat 'docker push nikitafordocker/wog-scores:latest'
            }
        }
    }
}
pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/saniyaa6699/MLOPS-LAB3.git'
            }
        }

      stage('Install Dependencies') {
    steps {
        bat '"C:\\Users\\saniy\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
    }
}

        stage('Run Training Script') {
            steps {
                bat 'python src/train.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t mlops-project .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run --rm mlops-project'
            }
        }

    }
}


pipeline {
  agent any
  stages {
    stage('Create instance (ls)') {
      steps {
        sh 'ls -l'
      }
    }

    stage('error') {
      steps {
        echo 'this is the second step test'
      }
    }

    stage('finish (hostname)') {
      steps {
        sh 'hostname -a'
      }
    }

  }
}
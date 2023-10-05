pipeline {
  agent any
  stages {
    stage('Check for a file on system') {
      steps {
        sh 'ls -l /Users/johnsontran/Desktop/deleteme.txt'
      }
    }

    stage('print message test') {
      steps {
        echo 'this is the second step test'
      }
    }

    stage('hostname') {
      steps {
        sh 'hostname'
      }
    }

    stage('cpu check') {
      steps {
        sh 'top'
      }
    }

    stage('Finished') {
      steps {
        echo 'Competed the Jenkins Job!'
      }
    }

  }
}
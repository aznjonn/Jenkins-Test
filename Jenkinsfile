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

    stage('disk file check') {
      steps {
        sh 'df -h'
      }
    }

    stage('Finished') {
      steps {
        echo 'Competed the Jenkins Job!'
      }
    }

  }
}
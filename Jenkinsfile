pipeline {
    agent any
    options {
       ansiColor('xterm')
    }
    parameters {
        choice(name: 'Command', choices: ['uptime','df','du'],description: 'Select Linux command')
    }

    stages {
        stage('Confirmation') {
            steps {
                script {
                    timeout(time: 10, unit: 'MINUTES') {
                        input "CAUTION! Do you want to run pre-push in ${params.Command}?"
                }
              }
          }
      }
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
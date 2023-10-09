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
                        input "CAUTION! Do you continue to run this with Linux command ${params.Command}?"
                }
              }
          }
      }

        stage('Example') {
            steps {
                script {
                    def output = sh(returnStdout: true, script: 'pwd')
                    echo "Output: ${output}"
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
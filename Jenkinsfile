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

        stage('Path of current directory') {
            steps {
                script {
                    def output = sh(returnStdout: true, script: 'pwd')
                    echo "Output: ${output}"
                }
            }
        }

        stage('Check for a file on system') {
            steps {
                sh 'ls -l /Users/johnsontran/Desktop/Jenkins/Jenkins-Test/README.md'
            }
        }

        stage('Run a Python3 Script on Macbook') {
            steps {
                sh 'python3 /Users/johnsontran/Desktop/Jenkins/Jenkins-Test/linux_commands.py'
            }
        }

        stage('Test Set Deployment Tags output and have it fail if Absent') {
            steps {
                script {
                    def fileContents = sh(script: 'cat /Users/johnsontran/Desktop/Jenkins/Jenkins-Test/setDeploymentTagsOutput.txt', returnStatus: true).trim().toString()

                    if (fileContents.toLowerCase().contains('absent')) {
                        currentBuild.result = 'FAILURE'
                        error('The word "absent" (case-insensitive) was found in the file contents. Failing the step.')
                    }
                }
            }
        }



        // stage('Test Set Deployment Tags output and have it fail if Absent') {
        //     steps {
        //         sh 'cat /Users/johnsontran/Desktop/Jenkins/Jenkins-Test/setDeploymentTagsOutput.txt'
        //     }
        // }

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
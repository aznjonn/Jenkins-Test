pipeline {
  agent any
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
      parallel {
        stage('Get Output of Tags') {
          steps {
            sh 'cat /Users/johnsontran/Desktop/Jenkins/Jenkins-Test/setDeploymentTagsOutput.txt'
          }
        }

        stage('Check for Absent') {
          steps {
            sh '''if ! grep -i "Absent" /Users/johnsontran/Desktop/Jenkins/Jenkins-Test/setDeploymentTagsOutput.txt; then
� echo "Word not found"
� exit 1
else
� echo "Word found"
fi
'''
          }
        }

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
  options {
    ansiColor('xterm')
  }
  parameters {
    choice(name: 'Command', choices: ['uptime','df','du'], description: 'Select Linux command')
  }
}
pipeline {
  agent any
  stages {
    stage('Create instance (ls)') {
      steps {
        sh '''#!/bin/bash

ls -l '''
      }
    }

    stage('') {
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
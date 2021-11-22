pipeline{
    agent any
    environment {
        K8S_DEPLOYMENT = "fastapi"
        DOCKER_HUB_CRED = credentials('DOCKER_HUB_CRED')
        REGISTRY = "docker.io/kvncont"
        IMAGE_NAME = "fastapi"
        TAG = "${env.BUILD_NUMBER}"
    }
    stages{
        stage("Build"){
            steps{
                sh "docker login -u ${DOCKER_HUB_CRED_USR} -p ${DOCKER_HUB_CRED_PSW}"
                sh "docker build --no-cache -t ${REGISTRY}/${IMAGE_NAME}:${TAG} ."
                sh "docker push ${REGISTRY}/${IMAGE_NAME}:${TAG}"
            }
        }
        stage("Deploy Dev"){
            steps{
                sh "kubectl apply -f k8s/dev/."
            }
        }
        stage("Integration Tests"){
            steps{
                sh "pyresttest integration_tests.yaml"
            }
            post{
                failure{
                    sh "kubectl rollout undo deployment/${K8S_DEPLOYMENT}"
                }
            }
        }
        stage("Load Tests"){
            steps{
                sh "locust -f load_tests.py"
            }
            post{
                failure{
                    sh "kubectl rollout undo deployment/${K8S_DEPLOYMENT}"
                }
            }
        }
        stage("Promote Pro"){
            steps{
                echo "Call Promotion Job"
            }
        }
    }
}
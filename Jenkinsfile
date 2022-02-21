pipeline{
    agent{
        label "TakeoPC-teste"
    }
    stages{
        stage("Clone"){
            steps{
                git branch: 'main', credentialsId: '0a14da8d-ac95-47a2-beda-5aec2291c132', url: 'https://github.com/takeofriedrichkwki/-processamento_extratos'
            }
            post{
                always{
                    echo "Cloning actual code"
                }
                success{
                    echo "Repository cloned"
                }
                failure{
                    echo "Error on cloning code"
                }
            }
        }
        stage("Build"){
            steps{
                sh './executar1.sh'
            }
            post{
                always{
                    echo "Build code"
                }
                success{
                    echo "Builded sucessful"
                }
                failure{
                    echo "Error on building code"
                }
            }
        }
        stage("Teste"){
            steps{
                sh './executar_teste1.sh'
            }
            post{
                always{
                    echo "Testing code"
                }
                success{
                    echo "All unit tests executed"
                }
                failure{
                    echo "Error on executing tests"
                }
            }
        }
        stage("Deploy"){
            steps{
                sh './deploy.sh'
            }
            post{
                always{
                    echo "Doing deploy of code"
                }
                success{
                    echo "Code sucessfuly deployed"
                }
                failure{
                    echo "Error on deploying"
                }
            }
        }
    }
    post{
        success{
            echo "Process done"
        }
        failure{
            echo "Erro in the process"
        }
    }
}
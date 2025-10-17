# 🚀 Executando Tarefas Automatizadas com AWS Lambda e S3

## 🧩 Descrição
Laboratório desenvolvido durante a Formação AWS Cloud Foundations (DIO).  
Objetivo: automatizar tarefas de leitura e processamento de arquivos armazenados no Amazon S3 utilizando AWS Lambda.

## ⚙️ Tecnologias e Serviços Utilizados
- AWS Lambda
- Amazon S3
- DynamoDB (opcional)
- API Gateway (opcional)
- LocalStack (para testes locais)
- AWS CLI

## 🪜 Passo a Passo Realizado
1. Criação do bucket `notas-fiscais-ocultas` no S3
2. Upload de arquivos `.json` e `.xml` (válidos e com erro)
3. Criação da função Lambda (`gravaDB`) com trigger do S3
4. Testes de execução e verificação de logs
5. (Opcional) Integração com DynamoDB e API Gateway
6. Simulação de caso real (validação de notas fiscais / placas de veículos)

## 🧠 Aprendizados e Insights
- Configuração de eventos do S3 para disparar funções Lambda
- Tratamento de erros e validação de formatos
- Aplicações práticas de automação em cenários reais (case estacionamento)
- Uso do LocalStack para desenvolvimento local

## 📷 Evidências
Capturas de tela na pasta `/images.src`:
- Criação do bucket S3
- Execução da função Lambda
- Logs de sucesso e erro

## 📚 Referências
- [Documentação AWS Lambda](https://docs.aws.amazon.com/lambda/)
- [Documentação Amazon S3](https://docs.aws.amazon.com/s3/)
- Materiais da DIO (Slides e ZIP do laboratório)

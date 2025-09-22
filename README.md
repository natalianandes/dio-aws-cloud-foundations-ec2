# Desafio AWS Cloud Foundations - EC2

Este repositório faz parte do desafio da DIO para consolidar conhecimentos em **gerenciamento de instâncias EC2** na AWS.

## 📌 Conteúdo Estudado
- **EC2 (Elastic Compute Cloud):** criação e gerenciamento de instâncias virtuais.
- **EBS (Elastic Block Store):** volumes de armazenamento em bloco anexados às instâncias.
- **Snapshots:** backups incrementais armazenados no S3.
- **S3 (Simple Storage Service):** armazenamento de objetos altamente disponível.
- **AMIs (Amazon Machine Images):** imagens que permitem replicar instâncias.
- **Custos:** uso do [AWS Pricing Calculator](https://calculator.aws/#/) para estimativas.

## 📊 Diagramas
Diagrama ilustrando arquitetura simples EC2 + EBS;
Diagrama ilustrando S3 + Lambda:

![Diagrama AWS](./Images/diagrama-aws.png)


*(substitua esses nomes de arquivo pelas imagens reais que você salvar na pasta `Images`)*

## 💡 Insights
- Sempre desligar instâncias que não estão em uso → economia de custos.
- Escolher a classe certa no S3 (Standard, IA, Glacier) faz toda a diferença na fatura.
- AMI ≠ Snapshot: AMI é uma cópia completa da instância, Snapshot é apenas do volume EBS.

## 📖 Referências
- [Documentação Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)  
- [Documentação Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)  
- [Documentação Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)  

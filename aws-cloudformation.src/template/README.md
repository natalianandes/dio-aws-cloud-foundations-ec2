# ☁️ Implementando sua Primeira Stack com AWS CloudFormation

## 🧭 Visão Geral
Este projeto faz parte da formação **AWS Cloud Foundations** da DIO.  
O objetivo é aplicar os conceitos de **Infraestrutura como Código (IaC)** utilizando o **AWS CloudFormation** para automatizar a criação de recursos.

Foram criadas stacks contendo instâncias EC2 e servidores Apache, descritas em templates YAML.

---

## 🎯 Objetivos
- Criar recursos AWS de forma automatizada com **CloudFormation**;
- Entender o conceito de **stack**, **template** e **resource**;
- Praticar uso de parâmetros e boas práticas de versionamento;
- Documentar processos técnicos de forma clara.

---

## ⚙️ Como Executar
1. Acesse o **AWS Console** → **CloudFormation** → *Create stack (with new resources)*  
2. Escolha **Upload a template file** e envie um dos arquivos YAML em `templates/`.  
3. Preencha os parâmetros:
   - **KeyName:** nome do seu par de chaves EC2  
   - **MyIP:** seu IP público com `/32` (exemplo: `123.45.67.89/32`)  
4. Avance e clique em **Create stack**  
5. Aguarde até aparecer `CREATE_COMPLETE`  

---

## 🧩 Templates Incluídos
- **template-ec2.yaml:** Cria uma EC2 simples (SSH só do seu IP).  
- **template-apache.yaml:** Cria uma EC2 com Apache e uma página HTML.  

---

## 🧠 Insights
- O CloudFormation simplifica e padroniza ambientes na nuvem.  
- A estrutura YAML torna o código reutilizável e fácil de ler.  
- Sempre valide a indentação e apague as stacks após o teste para evitar custos.  

---

👩‍💻 **Autora:** Natália Fernandes  
📚 Formação: *AWS Cloud Foundations – DIO*

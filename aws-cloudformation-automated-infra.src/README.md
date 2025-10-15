# ☁️ Implementando Infraestrutura Automatizada com AWS CloudFormation

## 📘 Visão Geral
Este projeto faz parte da formação **AWS Cloud Foundations** da DIO.  
O objetivo é praticar o uso do **AWS CloudFormation** para **implementar uma infraestrutura automatizada** utilizando o conceito de **Infraestrutura como Código (IaC)**.

Durante este laboratório, foram criados templates YAML que descrevem recursos da AWS (EC2, VPC, Security Groups e Apache Server), permitindo a **criação automatizada e padronizada** de ambientes.

---

## 🎯 Objetivos
- Utilizar o AWS CloudFormation para provisionar infraestrutura automaticamente.  
- Compreender o funcionamento de **templates**, **stacks** e **resources**.  
- Aplicar boas práticas de versionamento e reutilização de código.  
- Demonstrar autonomia na criação de ambientes em nuvem com IaC.  

---

## ⚙️ Como Executar
1. Acesse o console da AWS → **CloudFormation** → *Create Stack (with new resources)*  
2. Escolha **Upload a template file** e selecione um dos arquivos da pasta `templates/`.  
3. Preencha os parâmetros:
   - `KeyName`: nome do par de chaves EC2;
   - `MyIP`: seu IP público com `/32` (exemplo: `123.45.67.89/32`).
4. Clique em **Next** → **Create stack**  
5. Aguarde o status **CREATE_COMPLETE**  
6. Veja os **Outputs** para obter o IP público ou a URL do servidor.  

---

## 📂 Templates Criados

| Arquivo | Descrição |
|----------|------------|
| `template-ec2.yaml` | Cria uma instância EC2 simples (t2.micro) com SSH liberado apenas para o IP informado. |
| `template-apache.yaml` | Cria uma EC2 com o servidor Apache configurado automaticamente. |
| `template-full.yaml` | Cria uma EC2, uma VPC, um bucket S3 e uma role IAM para acesso seguro. |

---

## 💡 Benefícios do CloudFormation
- **Automação:** elimina tarefas manuais e acelera deploys.  
- **Padronização:** mantém ambientes consistentes entre equipes e regiões.  
- **Reutilização:** templates podem ser exportados e replicados.  
- **Economia:** reduz tempo de setup e erros humanos.  
- **Segurança:** permite aplicar policies e parâmetros restritivos.  

---

## 🧠 Aprendizados
- A automação com CloudFormation reduz a complexidade de ambientes AWS.  
- O formato YAML é o mais intuitivo, mas requer atenção à indentação.  
- O uso de parâmetros torna os templates dinâmicos e reutilizáveis.  
- Templates podem ser versionados no GitHub e usados em pipelines DevOps.  

---

👩‍💻 **Autora:** Natália Fernandes  
📚 Formação: *AWS Cloud Foundations – DIO*

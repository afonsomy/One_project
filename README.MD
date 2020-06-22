# Arquitetura de Ferramentas de Dados e Análise
### (Eternamente em Construção)

A ideia desse documento é criar uma opção de combinação de ferramenas livres e 
comercias para criar um ambiente de processamento, análise e apresentação de dados.

O objetivo é pensar em um ambiente que seja de custo baixa, mas não necessariamente gratuíto e,
que possa ser expandido rapidamente. Dessa forma, pode ser utilizado para um individo,
que é meu caso, até empresas pequenas e médias. Para grandes empresas, seria necessário 
algumas modificações no Git principalmente.

***

# Arquitetura

![Arquitetura do Ambiente](docs/images/Architecture-v2.0.PNG)

O Windows 10 com o Ubuntu como sub-sistema foi o escolhido por equilibrar a necessidade de um sistema
Unix/Linux com a popularidade do sistema Windows. Talvez o melhor seria um Macbook, mas os preços no Brasil
são absulatemente proibitivos.

Em geral, esse custo extra dos Macbooks eram justificados pelo sua maior capacidade de processamento no longo 
prazo. Mas isso pode ser facilmente substituido utilizando as ferramentas da Amazon como o SageMaker.

*** 

# Indice

1. Configuração do Windows e Ubuntu Subsystem
2. Ubuntu - configuração e associação o Jupyter Notebook
3. 

***

### 1. Configuração do Windows e Ubuntu Subsystem 

A grande verdade é que todas a ferramentas do novo mundo de dados (Python, Spark, etc)
são nativas do mundo do Unix-Linux e se comportam melhor com esse sistema operacional.

Devido a isso a Microsoft lançou um subsistema Linux embutido no seu Windows 10. Não é para todos,
Apenas para aquele poucos usuários que realmente vão precisar das capacidades/compatibildade do Linux.

***

### 2. Ubuntu - configuração e associação o Jupyter Notebook

O subsistema Ubuntu foi introduzido com grande enfase em ser o motor que executa o Python 3 para o
Jupyter notebook. Alguns bibliotecas como o pyarrow e o xgboost simplesmente não são compatíveis com
Windows. Outros como o framework do Spark tem uma configuração muito mais difícil sobre Windows.


A configuração do subsistema Ubuntu é discutido aqui:
https://github.com/afonsomy/One_project/blob/master/linux-install.md



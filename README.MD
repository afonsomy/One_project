# Arquitetura de Ferramentas de Dados e Análise

A ideia desse documento é criar uma opção de combinação de ferramenas livres e 
comercias para criar um ambiente de processamento, análise e apresentação de dados.

O objetivo é pensar em um ambiente que seja de custo baixa, mas não necessariamente gratuíto e,
que possa ser expandido rapidamente. Dessa forma, pode ser utilizado para um individo,
que é meu caso, até empresas pequenas e médias. Para grandes empresas, seria necessário 
algumas modificações no Git principalmente.

***
# Architecture

![Arquitetura do Ambiente](docs/images/Architecture-v2.0.PNG)

O Windows 10 com o Ubuntu como sub-sistema foi o escolhido por equilibrar a necessidade de um sistema
Unix/Linux com a popularidade do sistema Windows. Talvez o melhor seria um Macbook, mas os preços no Brasil
são absulatemente proibitivos.

Em geral, esse custo extra dos Macbooks eram justificados pelo sua maior capacidade de processamento no longo 
prazo. Mas isso pode ser facilmente substituido utilizando as ferramentas da Amazon como o SageMaker.


A configuração do subsistema Ubuntu é discutido aqui:
https://github.com/afonsomy/One_project/blob/master/linux-install.md



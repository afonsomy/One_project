# Arquitetura de Ferramentas de Dados e Análise
### (Eternamente em Construção)

Recentemente decidi começar a compilar um diário de bordo para o conhecimento novo que tenho agregado no estudo 
das novas tecnologias em coleta, armazenamento, transformação e análise de dados. 
A ambição desse documento será de reunir muito do conhecimento necessário para desempenhar diferentes papéis:
- Data Engineer
- Data Science
- Machine Learnning
- Statitician

A ideia desse documento é criar uma opção de combinação de ferramenas livres e comercias para criar um ambiente 
de processamento, análise e apresentação de dados.

O objetivo é pensar em um ambiente que seja de custo baixa, mas não necessariamente gratuíto e, que possa ser 
expandido rapidamente. Dessa forma, pode ser utilizado para um individo, que é meu caso, até empresas pequenas e médias.
Para grandes empresas, seria necessário algumas modificações no Git principalmente.

***

# Arquitetura

![Arquitetura do Ambiente](docs/images/Architecture-v2.0.PNG)

O Windows 10 com o Ubuntu como sub-sistema foi o escolhido por equilibrar a necessidade de um sistema
Unix/Linux com a popularidade do sistema Windows. Talvez o melhor seria um Macbook, mas os preços no Brasil
são absulatemente proibitivos.

Em geral, esse custo extra dos Macbooks eram justificados pelo sua maior capacidade de processamento no longo 
prazo. Mas isso pode ser facilmente substituido utilizando as ferramentas da Amazon como o SageMaker.

Não escolhi ficar com um ambiente puramente Linux devido a necessidade da plataforma de uso diária necessitar ser
mais multifunção, incluindo inevitáveis programas baseados no Windows no dia a dia: Microsoft Office, Power BI,
Tableau, Editores de Video, Jogos e conexão com redes corporativas baseadas no Windows Server.


*** 

# Indice

1. Configuração do Windows e Ubuntu Subsystem
2. Ubuntu - configuração e associação o Jupyter Notebook
3. Configuração do Pycharm com Git (Under Construction)
4. Notebooks: Lista dos Notebooks com Programas do Python (Under Construction)
5. Configuração do R e RStudio (Under Construction)
6. R books: Lista dos programas feitos em R para análise de dados (Under Construction)
7. Projetos no Pycharm configurando a infraestrutura AWS (Under Construction)


***

### 1. Configuração do Windows e Ubuntu Subsystem 

A grande verdade é que todas a ferramentas do novo mundo de dados (Python, Spark, etc)
são nativas do mundo do Unix-Linux e se comportam melhor com esse sistema operacional.

Devido a isso a Microsoft lançou um subsistema Linux embutido no seu Windows 10. Não é para todos,
Apenas para aquele poucos usuários que realmente vão precisar das capacidades/compatibildade do Linux.

A seguir seguem os links que utilizei para a configuração do WSL:
````
Documentação da própria Microsoft:
https://docs.microsoft.com/en-us/windows/wsl/install-win10
````

1.1. Configuração do Pycharm (usando o WSL com execução do Python)
````
Documentação da Jetbrains sobre como ajustar o Pycharm para usar o WSL.
https://www.jetbrains.com/help/pycharm/using-wsl-as-a-remote-interpreter.html
````
Ainda em aberto. Alguma etapa não foi conclída corretamente.

***

### 2. Ubuntu - configuração e associação o Jupyter Notebook

O subsistema Ubuntu foi introduzido com grande enfase em ser o motor que executa o Python 3 para o
Jupyter notebook. Alguns bibliotecas como o pyarrow e o xgboost simplesmente não são compatíveis com
Windows. Outros como o framework do Spark tem uma configuração muito mais difícil sobre Windows.


A configuração do Ubuntu é discutido aqui:

```
https://github.com/afonsomy/One_project/blob/master/linux-install.md
```

A configuração do subsistema é totalmente compatível com o materia anterior.
Especifcamente para podermos usar o kernel python do subsistema temos que seguir alguns passos extras,
que são aborados no seguinte documento:
```
Yadav, Harshit. Jupyter Notebook in Windows Subsystem for Linux |WSL,
https://medium.com/@harshityadav95/jupyter-notebook-in-windows-subsystem-for-linux-wsl-8b46fdf0a536
```



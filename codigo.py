import time
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

#Variaveis de diretorio
caminho = os.path.join("C:", os.sep, "Users", "Jhonata", "Documents", "Contagem dos Votos")
caminho_arquivo = os.path.join(caminho, 'respostas.xlsx')

#lendo o arquivo
df = pd.read_excel(caminho_arquivo)



#Apagando as colunas da segunda parte do formulario
for i in range(20, 31):
    nome = f"Unnamed: {i}"
    df = df.drop(columns=[nome])


#For que preenche as colunas
for i in range(len(df.columns)):
    nome_coluna = f'{df.columns[i]}'
    #funçao que conta a frequencia de cada valor em uma tabela
    #estou passando como parametro a tabela com apenas uma coluna
    ranqueado = pd.value_counts(df[nome_coluna]) 

    #print_de_verificaçao
    print(ranqueado)


    #criando um grafico de barra horizontal
    ranqueado.plot(kind = "barh")


    #definindo a etiqueta do eixo x
    plt.xlabel('Numero de Votos')

    #definindo a etiqueta do eixo y
    plt.ylabel('Pessoas')
   
    #definindo o titulo do grafico
    #separando por underlines
    fragmentado = nome_coluna.split("_")
    for i in range(len(fragmentado)):
        #deixando a primeira palavra de cada em maiusculo
        fragmentado[i] = fragmentado[i].capitalize()


    #definindo titulo do grafico
    titulo_grafico = " ".join(fragmentado)
    plt.title(titulo_grafico)
 
    #definindo os valores que aparecerão no eixo x
    eixo_x = [x for x in range(0, ranqueado.max() + 1, 1)]
    plt.xticks(range(len(eixo_x)))
 
    #ativando o grid para facilitar na visualizaçao
    plt.grid(True)
 
    #salvando o arquivo com o nome da coluna capitalizada
    nome_foto = os.path.join(caminho, titulo_grafico)
    plt.savefig(f"{nome_foto}.jpg")
    plt.close()
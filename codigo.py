import pandas as pd
import os
import matplotlib.pyplot as plt


def criar_diretorio(diretorio):
    if(not os.path.exists(diretorio)):
        os.makedirs(diretorio)

def remover_arquivo(arquivo):
    if(os.path.exists(arquivo)):
        os.remove(arquivo)

def formatar_string(palavra):
    fragmentado = palavra.split("_")
    for i in range(len(fragmentado)):
        #deixando a primeira palavra de cada em maiusculo
        fragmentado[i] = fragmentado[i].capitalize()

    #definindo titulo do grafico
    return " ".join(fragmentado)


def criar_grafico(dados, diretorio):
    criar_grafico_barra(dados, diretorio)
    criar_grafico_pizza(dados, diretorio)

def criar_grafico_barra(dados, diretorio):   

    criar_diretorio(os.path.join(diretorio, 'barra'))

    dados.plot(kind = "barh")
    plt.legend()
    
    plt.xlabel('Pessoas')
    plt.ylabel('Numero')

    
    eixo_x = [x for x in range(0, dados.max() + 1, 1)]
    plt.xticks(range(len(eixo_x)))
    
    plt.grid(True)
    
    titulo_grafico = formatar_string(dados.name)
    plt.title(titulo_grafico)
    
    caminho_arquivo_grafico = f"{os.path.join(diretorio,'barra', titulo_grafico)}.jpg"
    remover_arquivo(caminho_arquivo_grafico)
    plt.savefig(caminho_arquivo_grafico)
    plt.close()

def criar_grafico_pizza(dados, diretorio):
    
    criar_diretorio(os.path.join(diretorio, 'pizza'))

    plt.pie(dados.values, autopct='%1.0f%%')
    plt.legend(dados.index)
    plt.xlabel('')
    plt.ylabel('')
    plt.loc = "center rigth"
    titulo_grafico = formatar_string(dados.name)
    plt.title(titulo_grafico)
    
    caminho_arquivo_grafico = f"{os.path.join(diretorio,'pizza', titulo_grafico)}.jpg"
    remover_arquivo(caminho_arquivo_grafico)
    plt.savefig(caminho_arquivo_grafico)
    plt.close()

def criar_texto(dados, diretorio):
    criar_diretorio(diretorio)
   
    
    titulo_arquivo = formatar_string(dados.name)
    caminho_arquivo_texto = f"{os.path.join(diretorio_textos, titulo_arquivo)}.txt"
    remover_arquivo(caminho_arquivo_texto)
    
    arquivo_de_texto = open(caminho_arquivo_texto, 'a')
    arquivo_de_texto.write(str(dados))
    arquivo_de_texto.close()


#Variaveis de diretorio
diretorio_inicial = os.getcwd()
caminho_arquivo_de_dados = os.path.join(diretorio_inicial, 'respostas.xlsx')

diretorio_textos = os.path.join(diretorio_inicial, 'dados', 'textos')
diretorio_graficos = os.path.join(diretorio_inicial, 'dados', 'imagens')



#lendo o arquivo
df = pd.read_excel(caminho_arquivo_de_dados)

#Apagando as colunas da segunda parte do formulario
for i in range(20, 31):
    nome = f"Unnamed: {i}"
    df = df.drop(columns=[nome])

#lista para ler a lista de vencedores la na frente
lista_vencedores = []

#For que percorre as colunas
for i in range(len(df.columns)):
    categoria = f'{df.columns[i]}'

    #funçao que conta a frequencia de cada valor em uma tabela
    #estou passando como parametro a tabela com apenas uma coluna
    #formatar celula para remover os espaços
      
    categoria_ranqueada = pd.value_counts(df[categoria])
    criar_grafico(categoria_ranqueada, diretorio_graficos)
    criar_texto(categoria_ranqueada, diretorio_textos)


    #for para se criar a contagem de vencedores
    for i in range(len(categoria_ranqueada)):
        numeroDeVotosDaVez = categoria_ranqueada[i]
        #caso essa pessoa tenha o numero de votos maximo
        if(numeroDeVotosDaVez == categoria_ranqueada.max()):
            #dou o nome 'vencedor'ao indice do dicionario por que por algum motivo. os nomes 
            #das pessoas estao sendo colocadas como indices
            vencedor = categoria_ranqueada.index[i]
        
            #Adciona a categoria, o vencedor, e o numero de votos em forma de lista
            lista_vencedores += [[categoria , vencedor, numeroDeVotosDaVez]] 
        #só pra ganhar tempo
        else:
            break

#cria o dataframe com os dados coletados no for acima
lista_vencedores_dataframe = pd.DataFrame(lista_vencedores, columns = ['Categoria', 'Vencedor', 'Votos'])
lista_vencedores_ranqueada = lista_vencedores_dataframe.value_counts('Vencedor')
lista_vencedores_ranqueada.name = "lista_de_vencedores"

criar_grafico(lista_vencedores_ranqueada, diretorio_graficos)
criar_texto(lista_vencedores_ranqueada, diretorio_textos)

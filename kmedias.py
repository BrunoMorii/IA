import math
import random

#inciando leitura de dados
dados = [] #dsera matriz contendo informacao da leitura

# Os três arquivos estão aqui, basta escolher qual
leitura = "datasets\c2ds1-2sp.txt"
#leitura = "datasets\c2ds3-2g.txt"
#leitura = "datasets\monkey.txt"

f = open(leitura, "r");

#lendo linha a linha e colocando nos dados
menorValor = 999999
maiorValor = 0
f.readline()
for dado in f:
    linha = dado.split('\t')
    dados.append([ str(linha[0]), float(linha[1]), float(linha[2]) ])
    menorValor = min(float(linha[1]), float(linha[2]), menorValor)
    maiorValor = max(float(linha[1]), float(linha[2]), maiorValor)
f.close()


#iniciando recebimento de informações
nCluster = input("Digite o número desejado de clusters: ")
nInt = input("Digite o número desejado de iterações: ")

#vetores para armazenar clusters e centroids
vetorCluster = []
vetorCentroids = []

#inicializar clusters aleatorios
#entre menor e maior valor nos dados
for i in range(0, int(nCluster)):
    vetorCentroids.append([ random.randint(menorValor,maiorValor), random.randint(menorValor,maiorValor)])

#roda k media nInt vezes
for i in range(0, int(nInt)):
    #inicializa clusters
    vetorCluster.clear();
    for j in range(0, nCluster):
        vetorCluster.append([])

    #verifica distancias
    for j in dados:
        distInd = -1
        distVal = 0
        for k in vetorCluster:
            dist = math.sqrt()

import math
import random
import pprint

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
nCluster = int(input("Digite o número desejado de clusters: "))
nInt = int(input("Digite o número desejado de iterações: "))

#vetores para armazenar clusters e centroids
vetorCluster = []
vetorCentroids = []

#inicializar clusters aleatorios
#entre menor e maior valor nos dados
for i in range(0, int(nCluster)):
    vetorCentroids.append([ random.randint(int(menorValor),int(maiorValor)), random.randint(int(menorValor),int(maiorValor))])

#roda k media nInt vezes
for i in range(0, int(nInt)):
    #inicializa clusters
    vetorCluster.clear();
    for j in range(0, nCluster):
        vetorCluster.append([])

    #verifica distancias
    for j in dados:
        #incializa comparadores
        distInd = -1
        distVal = 0

        #para cada centroid, verifica o melhor
        for k in vetorCentroids:
            dist = float( math.sqrt(pow( (j[1] - k[0]) , 2) + pow( (j[2] - k[1]) , 2) ) )
            if distInd == -1:
                distVal = dist
                distInd = vetorCentroids.index(k)
            else:
                if distVal > dist:
                    distVal = dist
                    distInd = vetorCentroids.index(k)

        #insere no cluster de menor distancia
        vetorCluster[distInd].append(j)

    #calcula centroids novos
    vetorCentroids.clear()
    for j in range(0, int(nCluster)):
        vetorCentroids.append([ 0.0,0.0])

    for j in range(0, int(nCluster)):
        somaX = 0.0
        somaY = 0.0

        for k in vetorCluster[j]:
            somaX += float(k[1])
            somaY += float(k[2])

        vetorCentroids[j][0] = somaX / len(vetorCentroids[j])
        vetorCentroids[j][1] = somaY / len(vetorCentroids[j])

    print("----------------")
    print("Clusters:")
    pprint.pprint(vetorCentroids)

print("----------------")
print("Clusters Finais:")
pprint.pprint(vetorCentroids)

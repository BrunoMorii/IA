import math
import random

#for rodar in range(2,6):
#for rodar in range(5,13):

#inciando leitura de dados
dados = [] #dsera matriz contendo informacao da leitura
dados.clear();

# Os três arquivos estão aqui, basta escolher qual
#leitura = "datasets\c2ds1-2sp.txt"
#leitura = "datasets\c2ds3-2g.txt"
leitura = "datasets\monkey.txt"

a = open(leitura, "r");

#lendo linha a linha e colocando nos dados
menorValor = 999999
maiorValor = 0
a.readline()
for dado in a:
    linha = dado.split('\t')
    dados.append([ str(linha[0]), float(linha[1]), float(linha[2]) ])
    menorValor = min(float(linha[1]), float(linha[2]), menorValor)
    maiorValor = max(float(linha[1]), float(linha[2]), maiorValor)
a.close()


#iniciando recebimento de informações
nCluster = int(input("Digite o número desejado de clusters: "))
#nCluster = int(rodar)
#print("Iniciando algoritmo com " + str(nCluster) + " clusters...")

nInt = int(input("Digite o número desejado de iterações: "))
#nInt = 1000

#vetores para armazenar clusters e centroids
vetorCluster = []
vetorCentroids = []

#inicializar clusters aleatorios
#entre menor e maior valor nos dados
for i in range(0, int(nCluster)):
    vetorCentroids.append([ random.randint(int(menorValor),int(maiorValor)), random.randint(int(menorValor),int(maiorValor))])
    #vetorCentroids.append([ 5, 5]) #centroids inicias fixos

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
        vetorCentroids.append([0.0,0.0])

    for j in range(0, int(nCluster)):
        somaX = 0.0
        somaY = 0.0
        divisor = 0

        for k in vetorCluster[j]:
            somaX += float(k[1])
            somaY += float(k[2])
            divisor += 1

        #evitar divisao por 0 com cluster vazio
        if(divisor != 0):
            vetorCentroids[j][0] = somaX / divisor
            vetorCentroids[j][1] = somaY / divisor

    #imprime para cada iteracao
    """
    print("-------- Iteração {0} --------".format(i))
    print("======== Custers: ========")
    for cluster in vetorCluster:
        print("------------Cluster [ {0} ]: ".format(vetorCluster.index(cluster)))
        for j in cluster:
            print("   Nome: {0}. Ponto: {1}, {2}".format(j[0], j[1], j[2]))
    print("======== Centroids: ========")
    for j in range(0, int(nCluster)):
        print("------------Centroid [ {0} ]: ".format(j))
        for k in vetorCentroids:
            print("   Centroid: {0}. Ponto: {1}, {2}".format(vetorCentroids.index(k), k[0], k[1]))
    print("-------- ----------- --------")
    """

#imprime valores finais
"""
print("-------- Valores Final --------")
print("======== Custers: ========")
for cluster in vetorCluster:
    print("------------Cluster [ {0} ]: ".format(vetorCluster.index(cluster)))
    for j in cluster:
        print("   Nome: {0}. Ponto: {1}, {2}".format(j[0], j[1], j[2]))
print("======== Centroids: ========")
for j in range(0, int(nCluster)):
    print("Centroid [ {0} ]: {1}, {2}".format(j, vetorCentroids[j][0], vetorCentroids[j][1]))
"""

#iniciando processo de escrita
#escrita = 'resultados\c2ds1-2sp\k' + str(nCluster) + '\c2ds1-2spKmedia.clu' #coloca na pasta de acordo com nCluster
#escrita = 'resultados\c2ds3-2g\k' + str(nCluster) + '\c2ds3-2gKMedia.clu' #coloca na pasta de acordo com nCluster
escrita = 'resultados\monkey\k' + str(nCluster) + '\monkeyKMedia.clu' #coloca na pasta de acordo com nCluster

#para cada dado busca qual cluster esta e escreve
a = open(escrita, "w")
for i in dados:
    for cluster in vetorCluster:
        if i in cluster:
            a.write( "{0}\t{1}\n".format(str(i[0]), vetorCluster.index(cluster)) )
            break

a.close()
#print("Finalizando algoritmo com " + str(nCluster) + " clusters...")

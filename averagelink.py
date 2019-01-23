import math
import random

#for rodar in range(2,6):
for rodar in range(5,13):
    #inciando leitura de dados
    dados = [] #dsera matriz contendo informacao da leitura
    dados.clear()

    # Os tres arquivos estao aqui, basta escolher qual
    #leitura = "datasets\c2ds1-2sp.txt"
    #leitura = "datasets\c2ds3-2g.txt"
    leitura = "datasets\monkey.txt"

    a = open(leitura, "r");

    #lendo linha a linha e colocando nos dados
    a.readline()
    for dado in a:
        linha = dado.split('\t')
        dados.append([ str(linha[0]), float(linha[1]), float(linha[2]) ])
    a.close()


    #iniciando recebimento de informacoes
    #nCluster = int(input("Digite o numero desejado de clusters: "))
    nCluster = int(rodar)
    print("Iniciando algoritmo com " + str(nCluster) + " clusters...")

    #vetor para armazenar clusters
    vetorCluster = []

    #inicia vetor de clusters e coloca cada dado em um cluster
    for i in range(0, len(dados)):
        vetorCluster.append([])
        vetorCluster[i].append(dados[i])


    #roda até ter o numero de clusters pedido
    while(len(vetorCluster) > nCluster):
        #inicia o auxiliar
        menor = 9999
        #comparado as distancias entre dados de clusters diferentes e pegando a media
        for j in range(0, len(vetorCluster)):
            dist = 0.0
            if j+1 < len(vetorCluster):
                for k in range(j+1, len(vetorCluster)):
                    for l in vetorCluster[j]:
                        for m in vetorCluster[k]:
                            dist = dist + float( math.sqrt(pow( (l[1] - m[1]) , 2) + pow( (l[2] - m[2]) , 2) ) )
                    dist = dist/(len(vetorCluster[k])*len(vetorCluster[j]))
                    if dist < menor:
                        menor = dist
                        cluster1 = j
                        cluster2 = k
        #uniao de clusters
        try:
            for j in vetorCluster[cluster2]:
                vetorCluster[cluster1].append(j)
            vetorCluster.pop(cluster2)
        except:
            print (len(vetorCluster))
            print (cluster2)






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
    #escrita = 'resultados\c2ds1-2sp\k' + str(nCluster) + '\c2ds1-2spAverageLink.clu' #coloca na pasta de acordo com nCluster
    #escrita = 'resultados\c2ds3-2g\k' + str(nCluster) + '\c2ds3-2gAverageLink.clu' #coloca na pasta de acordo com nCluster
    escrita = 'resultados\monkey\k' + str(nCluster) + '\monkeyAverageLink.clu' #coloca na pasta de acordo com nCluster

    #para cada dado busca qual cluster esta e escreve
    a = open(escrita, "w")
    for i in dados:
        for cluster in vetorCluster:
            if i in cluster:
                a.write( "{0}\t{1}\n".format(str(i[0]), vetorCluster.index(cluster)) )
                break

    a.close()
    print("Finalizando algoritmo com " + str(nCluster) + " clusters...")

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

colors = ["red", "blue", "yellow", "green", "purple", "violet", "cyan", "black", "gray", "tomato", "sandybrown", "skyblue"]
dados = []
dictionary = {}
# Os tres arquivos estao aqui, basta escolher qual
leitura = input("Coloque o arquivo com os pontos:")

leitura2 = input("Coloque o nome do algoritmo desejado:")
nCluster = int(input("Coloque o número minimo de clusters:"))

#b = open("resultados\\" + leitura + "\k" + str(nCluster) + "\\" + leitura + leitura2 + ".clu", "r");
b = open("datasets\\" + leitura + "Real.clu", "r");

xCluster =[]
yCluster = []
for i in range(0, nCluster):
	xCluster.append([])
	yCluster.append([])
for dado in b:
	linha = dado.split('\t')
	dictionary[str(linha[0])] = int(linha[1])
b.close()

a = open("datasets\\" + leitura + ".txt", "r")
#a.readLine();
i = 0
for dado in a:
    if i > 0:
        linha = dado.split('\t')
        atual = dictionary[str(linha[0])]
        xCluster[atual].append(float(linha[1]))
        yCluster[atual].append(float(linha[2]))
        dados.append([ str(linha[0]), float(linha[1]), float(linha[2])])
    i += 1
a.close()

for i in range(0, nCluster):
	plt.scatter(xCluster[i],yCluster[i],color=colors[i])

plt.show()

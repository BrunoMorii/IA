from sklearn.metrics import adjusted_rand_score

dadosReal = []
dadosResultado = []

#leitura = "datasets\monkeyReal1.clu"
#leitura = "datasets\c2ds1-2spReal.clu"
leitura = "datasets/c2ds3-2gReal.clu"
#leitura2 = "datasets\monkey\k5\monkeyKMedia.clu"
#leitura2 = "datasets\monkey\k6\monkeyKMedia.clu"
#leitura2 = "datasets\monkey\k7\monkeyKMedia.clu"
#leitura2 = "datasets\monkey\k8\monkeyKMedia.clu"
#leitura2 = "datasets\monkey\k9\monkeyKMedia.clu"
#leitura2 = "datasets\monkey\k10\monkeyKMedia.clu"
#leitura2 = "datasets\monkey\k11\monkeyKMedia.clu"
#leitura2 = "datasets\monkey\k12\monkeyKMedia.clu"
#leitura2 = "datasets\c2ds1-2sp\k2\c2ds1-2spKMedia.clu"
#leitura2 = "datasets\c2ds1-2sp\k3\c2ds1-2spKMedia.clu"
#leitura2 = "datasets\c2ds1-2sp\k4\c2ds1-2spKMedia.clu"
#leitura2 = "datasets\c2ds1-2sp\k5\c2ds1-2spKMedia.clu"
#leitura2 = "datasets\c2ds3-2g\k2\c2ds3-2gKMedia.clu"
#leitura2 = "datasets\c2ds3-2g\k3\c2ds3-2gKMedia.clu"
#leitura2 = "datasets\c2ds3-2g\k4\c2ds3-2gKMedia.clu"
#leitura2 = "datasets\c2ds3-2g\k5\c2ds3-2gKMedia.clu"
leitura2 = "resultados/c2ds3-2g/k5/c2ds3-2gSingleLink.clu"


a = open(leitura, "r");
b = open(leitura2, "r")

for dado in a:
    dado = dado.strip()
    linha = dado.split("\t")
    dadosReal.append((linha[1]))
a.close()

for data in b:
    data = data.strip()
    line = data.split("\t")
    dadosResultado.append((line[1]))
b.close()

print(adjusted_rand_score(dadosReal, dadosResultado))

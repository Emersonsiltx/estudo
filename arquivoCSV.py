import  csv

with open('air_quality.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo, delimiter=',')
    for linhas in leitor:
        print(linhas)

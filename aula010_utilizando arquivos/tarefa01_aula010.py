# realizar leitura do arquivo txt

with open('Moby-Dick.txt', 'r', encoding='UTF-8') as file_object:
    conteudo = file_object.readlines()

#imprime por linha o conteudo do arquivo txt
    for l in conteudo:
        print(l)
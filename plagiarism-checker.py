import re
import math

def le_assinatura():
    print('Bem-vindo ao detector automático de COH-PIAH.')
    print('Informe a assinatura típica de um aluno infectado')

    word_mean_size  = float(input('Entre o tamanho médio de palavra: ')) 
    type_token  =float(input('Entre a relação Type-Token: ' ))
    hapax_reason =float(input('Entre a Razão Hapax Legomana: '))
    sentence_mean_size =float(input('Entre o tamanho médio de sentença: ')) 
    sentence_complexity =float(input('Entre a complexidade média da sentença: '))
    phrase_mean =float(input('Entre o tamanho médio de frase: '))
    
    return [word_mean_size, type_token, hapax_reason, sentence_mean_size, sentence_complexity, phrase_mean]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def list_of_lists_concat(lista_de_listas):
    listap = []
    for frase in lista_de_listas:
        for palavra in frase:
            listap.append(palavra)
    return listap

def simple_mean(lista):
    num_carac = 0
    for termo in lista:
        num_carac += len(termo)
    total = len(lista)
    mean = num_carac / total

    return mean

def phrase_mean_size(sentencas, lista_palavras):
    num_carac = 0
    for sentenca in sentencas:
        num_carac += len(sentenca.strip())
    total = len(lista_palavras)
    mean = (num_carac + 1) / total

    return mean

def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    palavras =[]
    num_carac = 0

    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        num_carac += len(sentenca.strip()) 
        
        for frase in frases:
            palavras.append(separa_palavras(frase))

    palavras_all = list_of_lists_concat(palavras)

    word_mean_size = simple_mean(palavras_all)
    type_token = n_palavras_diferentes(palavras_all) / len(palavras_all)
    hapax_reason = n_palavras_unicas(palavras_all) / len(palavras_all)
    sentence_mean_size = simple_mean(sentencas)
    sentence_complexity = len(palavras) / len(sentencas)
    phrase_mean = phrase_mean_size(sentencas, palavras)

    assinatura = [word_mean_size, type_token, hapax_reason, sentence_mean_size, sentence_complexity, phrase_mean]

    return  assinatura

def compara_assinatura(as_a, as_b):
    total = 6
    dif = 0
    for i in range(total):
        dif += abs(as_a[i] - as_b[i])
    g_sim = dif / total
    return g_sim

def avalia_textos(textos, ass_cp):
    ass_cp = [2,4,5,6,3,1]
    graus = []


    for texto in textos: 
        ass = calcula_assinatura(texto)
        graus.append(compara_assinatura(ass_cp,ass))

    menorgrau = min(graus)
    indicetexto = (graus.index(menorgrau) + 1)
    print("O autor do texto {} está infectado com COH-PIAH".format(indicetexto))

    return indicetexto

def main():
    ass_cp = le_assinatura()
    # solicita ao usuário os textos a serem comparados
    textos = le_textos()
    # realiza a avaliação
    avalia_textos(textos, ass_cp)

main()

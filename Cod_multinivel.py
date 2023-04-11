import numpy as np
import matplotlib.pyplot as plt

def Hex(texto):
    hexa = [hex(ord(c))[2:] for c in texto]
    return hexa

def Bin(hexa):
    bina = [bin(int(h, 16))[2:].zfill(8) for h in hexa]
    return bina

def Codificacao1(binarios):
    tensao = []
    sinal_anterior = 1
    pares = []
    for binario in binarios:
        pares += [binario[i:i+2] for i in range(0, len(binario), 2)]
    for par in pares:
        if sinal_anterior > 0:
            if par == "00":
                tensao.append(1)
            elif par == "01":
                tensao.append(3)
            elif par == "10":
                tensao.append(-1)
            elif par == "11":
                tensao.append(-3)
        else:
            if par == "00":
                tensao.append(-1)
            elif par == "01":
                tensao.append(-3)
            elif par == "10":
                tensao.append(1)
            elif par == "11":
                tensao.append(3)
        sinal_anterior = -1 if tensao[-1] < 0 else 1
        par = ""
    return tensao


def Codigo8b6t():
    with open('./source.txt', 'r') as f:
        codigos = {}

        for linha in f:
            pares = linha.strip().split(' ')

            for i in range(0, len(pares), 2):
                codigo_hex = pares[i]
                onda = pares[i+1]

                combinacoes = []

                for c in onda:
                    if c == '+':
                        combinacoes.append(1)
                    elif c == '-':
                        combinacoes.append(-1)
                    else:
                        combinacoes.append(0)

                codigos[codigo_hex] = combinacoes
    return codigos

def Codificacao2(hexadecimais, codi):
    sinais_decodificados = []

    for hexa_c in hexadecimais:
        if hexa_c in codi:
            sinais_decodificados.extend(codi[hexa_c])
        else:
            sinais_decodificados.append(-2)

    return sinais_decodificados

def Codificacao3(binarios):
    pares = []
    dic_binario_tensao = {'00': -2, '01': -1, '10': 1, '11': 2}
    for binario in binarios:
        pares += [binario[i:i+2] for i in range(0, len(binario), 2)]
    vet1 = []
    vet2 = []
    vet3 = []
    vet4 = []

    for i, par in enumerate(pares):
        if i % 4 == 0:
            vet1.append(par)
        elif i % 4 == 1:
            vet2.append(par)
        elif i % 4 == 2:
            vet3.append(par)
        else:
            vet4.append(par)
    matriz_binaria = vet1 + vet2 + vet3 + vet4
    matriz_binaria = np.array(matriz_binaria).reshape((4, int(len(matriz_binaria)/4)))
    matriz_tensao = []
    for linha in matriz_binaria:
        nova_linha = []
        for elemento in linha:
            nova_linha.append(dic_binario_tensao[elemento])
        matriz_tensao.append(nova_linha)
    return matriz_tensao

def Codificacao4(binarios):
    bits = []
    for binary_number in binarios:
        binary_string = str(binary_number).zfill(8)
        for bit in binary_string:
            bits.append(bit)
    tensao = []
    ultima_tensao = '0'
    ultima_tensao_nao_zero = '-1'
    
    for bit in bits:
        if bit == '0':
            tensao.append(int(ultima_tensao))
        else:
            if ultima_tensao == '1' or ultima_tensao == '-1':
                tensao.append(0)
                ultima_tensao = '0'
            elif ultima_tensao == '0' and ultima_tensao_nao_zero == '-1':
                ultima_tensao = '1'
                ultima_tensao_nao_zero = '1'
                tensao.append(1)
            elif ultima_tensao == '0' and ultima_tensao_nao_zero == '1':
                ultima_tensao = '-1'
                ultima_tensao_nao_zero = '-1'
                tensao.append(-1)
    return tensao

def Plotar(sinais_plt):
    tempo = np.arange(0, len(sinais_plt)+1)

    sinal = np.repeat(sinais_plt, 2)

    tempo_sinal = np.zeros(len(sinal))
    tempo_sinal[0::2] = tempo[:-1]
    tempo_sinal[1::2] = tempo[1:]

    fig, ax = plt.subplots()

    ax.plot(tempo_sinal, sinal, linewidth=2)

    ax.set_xlabel('Tempo')
    ax.set_ylabel('Sinais decodificados')

    plt.show()

def Plotar_0(sinais_plt):
    tempo = np.arange(0, len(sinais_plt)+1)

    sinal = np.repeat(sinais_plt, 2)

    tempo_sinal = np.zeros(len(sinal))
    tempo_sinal[0::2] = tempo[:-1]
    tempo_sinal[1::2] = tempo[1:]

    sinal = np.insert(sinal, 0, 0)
    tempo_sinal = np.insert(tempo_sinal, 0, 0)
    fig, ax = plt.subplots()

    ax.plot(tempo_sinal, sinal, linewidth=2)

    ax.set_xlabel('Tempo')
    ax.set_ylabel('Sinais decodificados')

    plt.show()

def Plotar4DPAM5(matriz_tensao):
    fig, axs = plt.subplots(nrows=4, ncols=1, figsize=(8,10.5))

    for i, linha in enumerate(matriz_tensao):
        duracao = np.arange(0, len(linha)+1)
        sinal = np.repeat(linha, 2)

        tempo_sinal = np.zeros(len(sinal))
        tempo_sinal[0::2] = duracao[:-1]
        tempo_sinal[1::2] = duracao[1:]

        sinal = np.insert(sinal, 0, 0)
        tempo_sinal = np.insert(tempo_sinal, 0, 0)

        axs[i].plot(tempo_sinal, sinal, linewidth=2)
        axs[i].set_xlabel('Tempo')
        axs[i].set_ylabel('Tensão')
        axs[i].set_ylim(-3,3)
        axs[i].set_title(f'Sinal {i+1}')
    fig.tight_layout()
    fig.text(0.80, 0.98, 'Definições de tensão no README', ha='center', fontsize=12, color='red')
    fig.subplots_adjust(hspace=0.5)
    plt.show()

escolha = 1
while escolha != '0':
    escolha = input("Escolha 1 para 2B1Q, 2 para 8B6T, 3 para 4DPAM5, 4 para MLT3 e 0 para sair.")
    if escolha == '1':
        while True:
            caracteres = input("Agora, digite um texto com até 4 caracteres: ")
            if len(caracteres) > 0 and len(caracteres) <=4:
                break
            else:
                print("Voce nao digitou nada ou digitou mais que 4 caracteres.\n")
        binaries = Bin(Hex(caracteres))
        sinais = Codificacao1(binaries)
        Plotar(sinais)
    elif escolha == '2':
        while True:
            caracteres = input("Agora, digite um texto com até 4 caracteres: ")
            if len(caracteres) > 0 and len(caracteres) <=4:
                break
            else:
                print("Voce nao digitou nada ou digitou mais que 4 caracteres.\n")
        sinais = Codificacao2(Hex(caracteres), Codigo8b6t())
        Plotar(sinais)
    elif escolha == '3':
        while True:
            caracteres = input("Agora, digite um texto com até 4 caracteres: ")
            if len(caracteres) > 0 and len(caracteres) <=4:
                break
            else:
                print("Voce nao digitou nada ou digitou mais que 4 caracteres.\n")
        binaries = Bin(Hex(caracteres))
        sinais = Codificacao3(binaries)
        Plotar4DPAM5(sinais)
    elif escolha == '4':
        while True:
            caracteres = input("Agora, digite um texto com até 4 caracteres: ")
            if len(caracteres) > 0 and len(caracteres) <=4:
                break
            else:
                print("Voce nao digitou nada ou digitou mais que 4 caracteres.\n")
        binaries = Bin(Hex(caracteres))
        sinais = Codificacao4(binaries)
        Plotar_0(sinais)
    elif escolha != '0':
        print("Voce escolheu um numero invalido.")

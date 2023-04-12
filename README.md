# Codificação Multinível

Nesse projeto foram implementados alguns métodos de codificar um dado em um sinal. Dentre esses meios estão incluídos o 2B1Q, 8B6T, 4DPAM5 e o MLT3.

---

## Definições

Para cada método de codificação tem algumas definições a serem feitas para cada um.

#### 2B1Q:

<table>
    <tr>
        <td></td>
        <td>Nível anterior positivo</td>
        <td>Nível anterior negativo</td>
    </tr>
    <tr>
        <th>Código</th>
        <th colspan=2>Nível seguinte</th>
    </tr>
    <tr>
        <td align='center'>00</td>
        <td align='center'>+1</td>
        <td align='center'>-1</td>
    </tr>
    <tr>
        <td align='center'>01</td>
        <td align='center'>+3</td>
        <td align='center'>-3</td>
    </tr>
    <tr>
        <td align='center'>10</td>
        <td align='center'>-1</td>
        <td align='center'>+1</td>
    </tr>
    <tr>
        <td align='center'>11</td>
        <td align='center'>-3</td>
        <td align='center'>+3</td>
    </tr>
</table>

#### 4DPAM5:

<table>
    <tr>
        <th width=100px>Código</th>
        <th width=100px>Tensão</th>
    </tr>
    <tr>
        <td align='center'>00</td>
        <td align='center'>-2</td>
    </tr>
    <tr>
        <td align='center'>01</td>
        <td align='center'>-1</td>
    </tr>
    <tr>
        <td align='center'>10</td>
        <td align='center'>+1</td>
    </tr>
    <tr>
        <td align='center'>11</td>
        <td align='center'>+2</td>
    </tr>
</table>

#### 8B6T e MLT3:

Para esses dois métodos, as tensões positivas e negativas que estão contidas em suas lógicas foram adotadas como +1 e -1 respectivamente.

---

## Pré-requisitos

- [Python](https://www.python.org/)
- Bibliotecas "Numpy" e "Matplotlib"

---

## Instalação

- Para instalação do python basta seguir o site nos pré-requisitos.
- Para instalação das bibliotecas, é necessário utilizar o comando "pip install NomeDaBiblioteca" no terminal já com o python instalado.

---

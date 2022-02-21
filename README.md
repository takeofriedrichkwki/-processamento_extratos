![](banner.png)

# Sobre

Sistema de processamento de extratos implementado usando a linguagem Python e seus recursos nativos. O sistema consiste em algumas classes que realizam a leitura de um arquivo formatado e ao final exibe o saldo final calculado a partir das operações descritas em um arquivo de entrada.

# Como usar

## > Instalação

Para instalar os recursos necessários para a execução do sistema, é necessário instalar a **versão 3.9.5** (ou superior) **da linguagem Python**.

## > Formatação do arquivo de entrada

O sistema suporta dois tipos de operações:

- Crédito: operação na qual será adicionado um valor à conta.
- Débito: operação na qual será retirado um valor da conta.

Para isso, o arquivo de entrada é composto de linhas contendo operações, onde cada linha possui um código de operação e um valor. São códigos válidos:

- C ou c: operação de crédito
- D ou d: operação de débito

Cada linha deve conter um código de operação e um valor (real ou inteiro) formatado usando um ponto. São valores válidos lidos pelo sistema:

- 4.3
- 4
- .3
- ...

Exemplo de arquivo de entrada válido:

```txt
D 300
c 200
d 100
D 200
```

**Não são permitidos valores negativos**, visto que as operações são inversas, logo, uma operação de crédito negativa corresponde a uma operação de débito positiva.

D -300 <=> C 200


## > Como executar

Para executar o sistema, é necessário informar o arquivo de entrada via argumento. É possível informar um valor de saldo inicial opcional (caso nenhum seja informado, o valor default será 100):

```bash
python3 main.py arquivoEntrada.txt # Executa o programa com saldoInicial = 100
```

```bash
python3 main.py arquivoEntrada.txt 300 # Executa o programa com saldoInicial = 300
```

Importante: ao passar o arquivo de entrada, deve-se passar ou o caminho relativo dentro deste projeto ou o caminho absoluto dentro do sistema operacional.

- Caminho Absoluto:

```bash
python3 main.py $HOME/pastaX/arquivoEntrada.txt 300 # Executa o programa com saldoInicial = 300 e utilizando um arquivo localizado fora da pasta desse projeto
```

- Caminho Relativo: suponto a seguinte estrutura de pastas:

```txt
    > arquivos/
    > arquivos_teste/
    > modelos/
    > novaPasta/
        - arquivoEntrada.txt
    > testes/
    > uteis/
    > main.py
```

Para executar o sistema com o arquivo de entrada dentro da pasta novaPasta, basta:

```bash
python3 main.py novaPasta/arquivoEntrada.txt 300 # Executa o programa com saldoInicial = 300 e utilizando um arquivo localizado dentro da pasta novaPasta
```

# Execução de testes

Para a execução de testes, há três classes contendo testes unitários e de integração, para executá-los, basta:

```bash
python3 -m unittest testes/*.py
```



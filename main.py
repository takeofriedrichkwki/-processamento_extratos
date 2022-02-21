from modelos.conta_bancaria import ContaBancaria
from uteis.processador_textual import ProcessadorTextual
from uteis.messages import argvIncorretos
from uteis.messages import encerrandoValueError
from uteis.messages import encerrandoArquivoNaoEncontrado
import sys
import os

if len(sys.argv) < 2:
    print(argvIncorretos)
    sys.exit()

try:
    conta = ContaBancaria() if len(
        sys.argv) == 2 else ContaBancaria(saldo=float(sys.argv[2]))
except ValueError:
    print(encerrandoValueError)
    conta = ContaBancaria()
    sys.exit()

if not os.path.isfile(sys.argv[1]):
    print(encerrandoArquivoNaoEncontrado)
    sys.exit()

file = open(sys.argv[1])

line = file.readline()
lineCount = 1

while line:

    try:

        operacao = ProcessadorTextual.parseLine(line=line, lineCount=lineCount)

    except Exception as e:

        print(e)
        print('\nENCERRANDO O PROGRAMA!')
        sys.exit()

    if operacao[0] in ['C', 'c']:
        conta.creditar(operacao[1])
    else:
        conta.debitar(operacao[1])

    line = file.readline()
    lineCount += 1

print(conta)

import unittest
from modelos.conta_bancaria import ContaBancaria
from uteis.processador_textual import ProcessadorTextual
import os


class TestGeral(unittest.TestCase):

    def testGeral(self):

        saldo = 250

        conta = ContaBancaria(saldo=250)

        path = os.path.dirname(__file__) + '/../arquivos/input1.txt'

        file = open(path, 'r')

        line = file.readline()
        lineCount = 1

        while(line):

            operacao = ProcessadorTextual.parseLine(line, lineCount)

            opCode = operacao[0]
            opValor = operacao[1]

            if opCode in ['C', 'c']:
                conta.creditar(opValor)
                saldo += opValor

            elif opCode in ['D', 'd']:
                conta.debitar(opValor)
                saldo -= opValor

            line = file.readline()

        file.close()
        self.assertAlmostEqual(conta.getSaldo(), saldo)

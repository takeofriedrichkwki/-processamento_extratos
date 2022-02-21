import unittest
from modelos.conta_bancaria import ContaBancaria


class TestContaBancaria(unittest.TestCase):

    def testConstrutorVazio(self):

        conta = ContaBancaria()
        self.assertAlmostEqual(conta.getSaldo(), 100)

    def testConstrutorSaldoPositivo(self):

        conta = ContaBancaria(saldo=250)
        self.assertAlmostEqual(conta.getSaldo(), 250)

    def testConstrutorSaldoIgualZero(self):

        conta = ContaBancaria(saldo=0)
        self.assertAlmostEqual(conta.getSaldo(), 0)

    def testConstrutorSaldoNegativo(self):

        conta = ContaBancaria(saldo=-250)
        self.assertAlmostEqual(conta.getSaldo(), -250)

    def testOperacoes(self):

        saldo = 0

        conta = ContaBancaria(saldo=0)

        conta.debitar(100)
        saldo -= 100

        conta.creditar(300)
        saldo += 300

        self.assertAlmostEqual(conta.getSaldo(), saldo)

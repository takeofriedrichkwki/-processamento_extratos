import unittest
from uteis.excecoes import ArquivoMalFormatadoException
from uteis.excecoes import OperacaoInvalidaException
from uteis.excecoes import ValorNegativoException
from uteis.excecoes import FormatoInvalidoException
from uteis.processador_textual import ProcessadorTextual
import os


class TestProcessadorTextualMalFormatado(unittest.TestCase):

    # Mal formado
    def testParseMalFormado(self):
        with self.assertRaises(ArquivoMalFormatadoException):
            ProcessadorTextual.parseLine('D\n200', 0)

    def testParseMalFormado2(self):
        with self.assertRaises(ArquivoMalFormatadoException):
            ProcessadorTextual.parseLine('D  200', 0)

    def testParseMalFormado3(self):
        with self.assertRaises(ArquivoMalFormatadoException):
            ProcessadorTextual.parseLine('Dx200', 0)

    # Operação inválida
    def testParseOperacaoInvalida(self):
        with self.assertRaises(OperacaoInvalidaException):
            ProcessadorTextual.parseLine('x 200', 0)

    def testParseOperacaoInvalida2(self):
        with self.assertRaises(OperacaoInvalidaException):
            ProcessadorTextual.parseLine('0 200', 0)

    # Valor negativo
    def testValorNegativo(self):
        with self.assertRaises(ValorNegativoException):
            ProcessadorTextual.parseLine('D -200', 0)

    def testValorNegativo2(self):
        with self.assertRaises(ValorNegativoException):
            ProcessadorTextual.parseLine('C -200', 0)

    # Formato inválido float
    def testFormatoInvalido(self):
        with self.assertRaises(FormatoInvalidoException):
            ProcessadorTextual.parseLine('D 200,3', 0)

    def testFormatoInvalido2(self):
        with self.assertRaises(FormatoInvalidoException):
            ProcessadorTextual.parseLine('D 200.3.4', 0)

from dataclasses import dataclass
from uteis.excecoes import OperacaoInvalidaException
from uteis.excecoes import ArquivoMalFormatadoException
from uteis.excecoes import ValorNegativoException
from uteis.excecoes import FormatoInvalidoException


@dataclass
class ProcessadorTextual:

    def parseLine(line: str, lineCount: int) -> tuple:
        '''Transforma uma string de entrada em uma tupla (codigoOperacao,valor) caso a linha esteja formatada corretamente'''

        splitted = line.split(' ')

        if(len(splitted) != 2):
            raise ArquivoMalFormatadoException(lineCount)

        opCode = ''

        if splitted[0] in ['C', 'c', 'D', 'd']:
            opCode = splitted[0]
        else:
            raise OperacaoInvalidaException(lineCount)

        valor = 0

        try:
            valor = float(splitted[1])
            if valor < 0:
                raise ValorNegativoException(lineCount)
        except ValueError:
            raise FormatoInvalidoException(lineCount)

        return (opCode, valor)

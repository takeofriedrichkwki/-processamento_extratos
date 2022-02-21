from dataclasses import dataclass


@dataclass
class ContaBancaria:
    __saldo: float

    def __init__(self, saldo: float = 100) -> None:
        '''Construtor da classe ContaBancaria, recebe um parâmetro saldo do tipo float, caso nenhum parâmetro seja informado o saldo inicial será 100, exemplos:

    - conta = ContaBancaria()
    - conta = ContaBancaria( saldo = 200 )
    - conta = ContaBancaria( saldo = -200 )        
'''
        self.__saldo = saldo

    def getSaldo(self) -> float:
        '''Acessa a propriedade saldo da ContaBancaria'''
        return self.__saldo

    def creditar(self, valor: float) -> None:
        '''Adiciona um crédito a conta, isto é, incrementa o valor passado como parâmetro, exemplos:

    - conta = ContaBancaria( saldo = 200 )
    - conta.creditar(200) // saldo agora é 400
    - conta.creditar( valor = 100 ) // saldo agora é 500
'''
        self.__saldo += valor

    def debitar(self, valor: float) -> None:
        '''Adiciona um débito a conta, isto é, decrementa o valor passado como parâmetro, exemplos:

    - conta = ContaBancaria( saldo = 200 )
    - conta.debitar(200) // saldo agora é 0
    - conta.debitar( valor = 100 ) // saldo agora é -100
'''
        self.__saldo -= valor

    def __repr__(self) -> str:
        '''Define a representação oficial do objeto, por exemplo:

    - Saldo: 40.30
    - Saldo: 20.00
    '''
        return 'Saldo: {}'.format(round(self.__saldo, 2))

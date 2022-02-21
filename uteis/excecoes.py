class ArquivoMalFormatadoException(Exception):

    def __init__(self, linha):
        '''Define uma exceção para linhas mal formadas que não seguem o padrão operacao espaço valor (OP VALOR), por exemplo:
    D - 300

    C > 100

O correto seria:

    D 300

    C 100
    '''
        super().__init__('Arquivo formatado incorretamente (linha {})'.format(
            linha))


class OperacaoInvalidaException(Exception):

    def __init__(self, linha):
        '''Define uma exceção para linhas mal formados contedo códigos de operações inválidas, são operações válidas:

    - D : operação de débito (retira valor da conta)
    - d : operação de débito (retira valor da conta)
    - C : operação de crédito (adiciona valor da conta)
    - c : operação de crédito (adiciona valor da conta)

'''
        super().__init__('Código de operação não identificado  (linha {})'.format(
            linha))


class ValorNegativoException(Exception):

    def __init__(self, linha):
        '''Define uma exceção para linhas que contenham valores negativos no valor, por exemplo:

    D -300

    C -100

Note que debito é o inverso de crédito, logo, o trecho acima estaria correto na forma:

    C 300

    D 100

'''
        super().__init__('Valor não pode ser negativo  (linha {})'.format(
            linha))


class FormatoInvalidoException(Exception):

    def __init__(self, linha):
        '''Define uma exceção para linhas que contenham valores mal formatados, o padrão float é:

    - XX.XX
    - XX
    - .XX

Exemplos:

    - C 300.00
    - D 200
    - C .200

'''
        super().__init__('Valor deve ser um número no formato XX.XX ou XX ou .XX  (linha {})'.format(
            linha))

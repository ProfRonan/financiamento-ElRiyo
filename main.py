"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    capital = int(input('Digite o valor principal '))
    juros = float(input('Digite o valor da taxa de  juros (por mes)'))
    time = int(input('Digite a quantidade de meses do financiamento '))
    montante = capital * (1 + juros/100) **time
    final = montante - capital 
    print('O valor dos juros é igual à {:.2f}.'.format(final))

if __name__ == '__main__':
    main()

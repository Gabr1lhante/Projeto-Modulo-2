def calcular_emprestimo():    
    emprestimo = float(input('Qual o valor que você quer emprestado?'))
    prazo = int(input("Digite o prazo do empréstimo em meses: "))
    taxa_juros = (prazo/100) + 1 
    valor_final = emprestimo * taxa_juros
    prestacao_mensal = valor_final/prazo
    return prestacao_mensal,valor_final, prazo, taxa_juros

def main():
    renda_minima= 1320

    nome = input('Qual seu nome completo ? : ')
    renda = int(input('Qual sua renda? : '))

    if renda < renda_minima:
        print('Você não pode pegar um empréstimo')
        return
    else:
        print('Você pode pegar um empréstimo')
    prestacao_mensal, valor_final, prazo, taxa_juros = calcular_emprestimo()
    print ("Prestação: ", prestacao_mensal)
    print ("Prazo: ", prazo)
    print ("Juros: ", taxa_juros)
    print ("Valor final a pagar: ", valor_final)

main()
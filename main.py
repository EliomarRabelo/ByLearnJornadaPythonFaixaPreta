
#função principal do projeto semana_faixaPreta
    #05/10 - 09/10 de 2020


#exemplo de for com INTERVALO DIRETO 'vetor'
    #nome = ['eu','mirella','bob','yasmin','isabele']
    #for nomes in nome:
    #print('O nome atual é ',nomes)
#definindo uma função e executando varias vezes
#def funcao(parametro_inicial , parametro_final):
    #esta função soma valores dentro de um intervalo positivo
#   tamanho_intervalo = parametro_final-parametro_inicial
#    soma = parametro_inicial
#    for c in range(parametro_inicial,parametro_final,1):
#        proximo_valor = soma + c+1
#        soma = proximo_valor
#        print(soma, c+1)
#funcao(10,20)


def media(notas):
    soma=0
    for c in range(0,len(notas)):
        soma = soma+float(notas[c])

    print('soma das notas: ',soma)
    print('numero de notas: ',len(notas))
    return soma/len(notas)


n_notas = int(input('Insira o numero de avaliações: '))

avaliacoes = []
for _ in range(n_notas):
    print('insira nota ',_+1,':')
    avaliacoes.append(input())

print('Media: ',media(avaliacoes))


import funcoes
import edicao
import json
from datetime import date

ina, nina, ven, mont = funcoes.inadimplentes()



print('='*45)
print(f'|                                {date.today()} |')
print('|                                           |')
print('|                                           |')
print('|         CADASTRO E ADMINISTRAÇÃO          |')
print('|              DE PASSAGEIROS               |')
print('|                                           |')
print('|                                           |')
print('='*45)
print(f'{ina} Atrasados:')
for cont in range(0, len(nina)):
    print(f'{nina[cont]} {ven[cont]}')
print('\n')
print(f'Ainda há um total de R${mont:.2f} a receber')
print('\n')
while True:
    print("Selecione uma função!")
    menu = input('''
    [1] Cadastrar novo passageiro
    [2] Baixa pagamento
    [3] Gerenciar passageiros
    [4] Sair
    ''')
    if menu == '1':
        funcoes.criar()
    elif menu == '2':
        funcoes.baixa()
    elif menu == '3':
        funcoes.lista()
        li, apelido = funcoes.logar()
        while True:
            print('Selecione uma função')
            menu1 = input('''
    [1] Excluir cadastro
    [2] Editar
    [3] Dar baixa em pagamento
    [4] Sair
            ''')
            if menu1 == '1':
                pass
            if menu1 == '2':
                edicao.editar(apelido)
            if menu1 == '3':
                a = input(f'Confirma a baixa na mensalidade de {li["nome"]}? [S/N]').upper().strip()
                li['aberto'] -= 1
                if a == 'S':
                    funcoes.sobrescrever(apelido, li)
                    print('='*28)
                    print('Baixa realizada com sucesso!')
                    print('='*28)
            if menu1 == '4':
                break
    elif menu == '4':
        break

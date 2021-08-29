import json
import funcoes
import time


def editar(apelido):
    a = open(f'{apelido}.txt')
    li = json.loads(a.read())
    a.close()
    for c in li:
        print(f'{c}: {li[c]}')
    while True:
        items = ['nome', 'cpf', 'endereco', 'inicio', 'valor', 'aberto', 'vencimento']
        a = input(f"Deseja editar o perfil de {li['nome']}? [S/N]").upper()
        if a == 'N':
            break
        if a == 'S':
            a = input('Que item deseja editar?\n nome,\n cpf,\n endereco,'
                      '\n inicio,\n valor,\n aberto,\n vencimento').lower()
            if a in items:
                if a == 'cpf':
                    while True:
                        b = input(f'Digite o novo {a}')
                        if len(b) == 11:
                            b = b.zfill(11)
                            b = f'{b[:3]}.{b[3:6]}.{b[6:9]}-{b[9:]}'
                            li[a] = b
                            break
                        else:
                            print('cpf incorreto!')
                elif a == 'vencimento' or 'aberto':
                    b = int(input(f'Digite o novo {a}'))
                    li[a] = b
                    print('atualizando.', end='')
                    time.sleep(1)
                    print('.', end='')
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    funcoes.sobrescrever(apelido, li)
                    break
                elif a == 'valor':
                    b = float(input(f'Digite o novo {a}'))
                    li[a] = b
                    print('atualizando.', end='')
                    time.sleep(1)
                    print('.', end='')
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    funcoes.sobrescrever(apelido, li)
                    break
                else:
                    b = input(f'Digite o novo {a}')
                    li[a] = b
                    print('atualizando.', end='')
                    time.sleep(1)
                    print('.', end='')
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    funcoes.sobrescrever(apelido, li)
                    break
            else:
                print('Item não identificado...')

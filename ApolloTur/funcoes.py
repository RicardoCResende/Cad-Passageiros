import json
import datetime


def logar():
    while True:
        apelido = input('apelido do passageiro:')
        try:
            a = open(f'{apelido}.txt')
            li = json.loads(a.read())
            a.close()
            return li, apelido
            break
        except:
            print('Não existe nenhum passageiro cadastrado com esse apelido!')
            lista()


def criar():
    nome = input('Nome completo do passageiro:')
    apelido = input('Apelido do passageiro:')
    cpf = input('CPF (só números) do passageiro:')
    cpf = cpf.zfill(11)
    cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    endereco = input('Digite o endereço:')
    inicio = input('Digite a data de inicio do contrato:')
    valor = float(input('Digite o valor da mensalidade:'))
    aberto = int(input('Digite o numero de mensaliades em aberto:'))
    vencimento = int(input('Digite o vencimento das mensalidades:'))
    li = {
        'nome': nome,
        'cpf': cpf,
        'endereco': endereco,
        'inicio': inicio,
        'valor': valor,
        'aberto': aberto,
        'vencimento': vencimento
    }
    sobrescrever(apelido, li)
    a = open('lista.txt', 'a')
    a.write(f'\n{apelido}')
    a.close()


def lista():
    a = open('lista.txt')
    b = a.readlines()
    print('Lista de passageiros')
    print('=' * 20)
    for i, c in enumerate(b):
        print(f'{i + 1} - {c}', end='')
    print('\n')
    print('=' * 20)


def baixa():
    li, apelido = logar()
    a = input(f'confirma a baixa da mensalidade de {li["nome"]} [S/N]').upper().strip()
    if a == 'S':
        li['aberto'] -= 1
        sobrescrever(apelido, li)


def sobrescrever(apelido, li):
    a = open(f'{apelido}.txt', 'w')
    a.write(json.dumps(li))
    a.close()


def inadimplentes():
    ina = 0
    nina = []
    ven = []
    mont = 0.0
    data = datetime.date.today().day
    a = open('lista.txt')
    b = a.read().split('\n')
    a.close()
    for c in b:
        a = open(f'{c}.txt')
        li = json.loads(a.read())
        data1 = li['vencimento']
        if li['aberto'] > 15 - datetime.date.today().month:
            mont += li['valor']
            if data > data1:
                ina = ina + 1
                nina.append(li['nome'])
                ven.append(li['vencimento'])
    return ina, nina, ven, mont


def atribuir():
    li, apelido = logar()
    nome = li['nome']
    cpf = li['cpf']
    endereco = li['endereco']
    inicio = li['inicio']
    valor = li['valor']
    aberto = li['aberto']
    vencimento = li['vencimento']
    return [nome, cpf, endereco, inicio, valor, aberto, vencimento]

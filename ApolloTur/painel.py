import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Checkbox('Cadastrar Novo Passageiro', key='cnp')],
            [sg.Checkbox('Baixa Pagamento', key='bp')],
            [sg.Checkbox('Gerenciar Passageiro', key='gp')],
            [sg.Checkbox('Sair', key='s')],
            [sg.Button('Continuar')],
            [sg.Output(size=(30,20))]
        ]
        janela = sg.Window('Menu Principal').layout(layout)
        self.button, self.values = janela.Read()

    def Iniciar(self):
        return self.values

    def Cadastro(self):
        layout = [
            [sg.Text('Nome:'), sg.Input(key='nome')],
            [sg.Text('Apelido:'), sg.Input(key='apelido')],
            [sg.Text('CPF:'), sg.Input(key='cpf')],
            [sg.Text('Endereço:'), sg.Input(key='endereco')],
            [sg.Text('Inicio:'), sg.Input(key='inicio')],
            [sg.Text('Valor:'), sg.Input(key='valor')],
            [sg.Text('Aberto:'), sg.Input(key='aberto')],
            [sg.Button('Continuar')]
        ]
        janela = sg.Window('Menu Principal').layout(layout)
        self.button, self.values = janela.Read()
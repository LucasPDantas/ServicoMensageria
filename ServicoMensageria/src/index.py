from models.contato import Contato
from models.mensagem import Mensagem
from ui.menu import imprimirMenuPrincipal, limparTela


# FUNÇÕES
def AdicionarContato():
    # ESCREVER LÓGICA AQUI!

    # Exemplo de criação de um contato
    contato = Contato("Nome do Contato", "Numero do Contato")

    print("Usuário Criado com Sucesso!")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def MostrarContatos():
    # ESCREVER LÓGICA AQUI

    print("Mostrando lista de contatos")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def EditarContato():
    # ESCREVER LÓGICA AQUI

    print("Contato editado com sucesso!")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def EscreverMensagem():
    # Exemplo de criação de uma mensagem
    destinatario = Contato("Contato para envio", "Numero para envio")
    mensagem = Mensagem(destinatario, "Mensagem", "01/01/2024")

    print("Mensagem Criada com Sucesso!")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()


# PROGRAMA PRINCIPAL
print("===== SISTEMA DE MENSAGENS =====\n")

fimPrograma = False

while not fimPrograma:
    imprimirMenuPrincipal()
    opcao = input("Escolha uma das opções: ")

    if int(opcao) == 1:
        AdicionarContato()
    elif int(opcao) == 2:
        MostrarContatos()
    elif int(opcao) == 3:
        EditarContato()
    elif int(opcao) == 4:
        EscreverMensagem()
    elif int(opcao) == 0:
        fimPrograma = True
    else:
        print("Opção Errada! Favor escolha uma opção válida")
        input("[APERTE ENTER PARA CONTINUAR]")
        limparTela()

print("===== FIM DO PROGRAMA =====\n")
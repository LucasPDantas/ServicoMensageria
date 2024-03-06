from models.contato import Contato
from models.mensagem import Mensagem
from ui.menu import imprimirMenuPrincipal, limparTela

listaContatos = []
# FUNÇÕES
def AdicionarContato(listaContatos):
    # ESCREVER LÓGICA AQUI!
    nomeContato = input("Nome do contato: ")

    #VERIFICA SE O CONTATO JÁ EXISTE NA LISTA
    for contato in listaContatos:
        if contato.nome == nomeContato:
            print("\nContato existente!\n")
            return
            
    numeroContato = input("numero do contato: ")

    # Exemplo de criação de um contato
    contato = Contato(nomeContato, numeroContato)
    listaContatos.append(contato)

    print("Usuário Criado com Sucesso!")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def MostrarContatos(listaContatos):
    # ESCREVER LÓGICA AQUI
    print("Lista de contatos: ")
    for contato in listaContatos:
        print(f"Nome: {contato.nome}, Numero: {contato.numero}")
    input("[APERTE ENTER PARA CONTINUAR]")
    limparTela()

def EditarContato(listaContatos):
    # ESCREVER LÓGICA AQUI
    print("Lista de contatos: ")
    for i, contato in enumerate(listaContatos):
        print(f"{i+1} Nome: {contato.nome}, Numero: {contato.numero}")

    indice = int(input("digite o numero de contato que deseja editar: ")) -1

    if 0 <= indice < len(listaContatos):
        novoContato = input("digite o novo nome do contato: ")
        novoNumero = input("digite o novo numero do contato: ")

        listaContatos[indice].nome = novoContato
        listaContatos[indice].numero = novoNumero

        print("\nSalvo!\n")
    else:
        print("inválido!")

    #print("Contato editado com sucesso!")
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
        AdicionarContato(listaContatos)
    elif int(opcao) == 2:
        MostrarContatos(listaContatos)
    elif int(opcao) == 3:
        EditarContato(listaContatos)
    elif int(opcao) == 4:
        EscreverMensagem()
    elif int(opcao) == 0:
        fimPrograma = True
    else:
        print("Opção Errada! Favor escolha uma opção válida")
        input("[APERTE ENTER PARA CONTINUAR]")
        limparTela()

print("===== FIM DO PROGRAMA =====\n")
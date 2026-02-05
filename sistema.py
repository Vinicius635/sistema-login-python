import json
import os

ARQUIVO_ESTOQUE = 'estoque.json'
ARQUIVO_USUARIOS = 'usuarios.json'


# Carregar dados
def carregar_dados(arquivo):
    if not os.path.exists(arquivo):
        return {}
    with open(arquivo, 'r') as f:
        return json.load(f)


# Salvar dados
def salvar_dados(arquivo, dados):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)


# Login
def login(usuarios):
    print('===LOGIN===')
    usuario = input('Usuário:').strip()
    senha = input('Senha:').strip()
    if usuario in usuarios and usuarios[usuario] == senha:
        print('Login bem-sucedido!\n')
        return True
    else:
        print('Usuário ou senha incorretos!\n')
        return False


# Ver estoque
def ver_estoque(estoque):
    print('===VER ESTOQUE===')
    if not estoque:
        print('Estoque vazio')
    else:
        for item, dados in estoque.items():
            print(f'{item}: {dados["quantidade"]} | Preço R$: {dados["preco"]:.2f}')
    print()


# Adicionar produto
def adicionar_produto(estoque):
    nome = input('Nome do produto:').strip()
    if nome in estoque:
        print('Produto já existe!.')
    else:
        quantidade = int(input('Quantidade: '))
        preco = float(input('Preço'))
        estoque[nome] = {'quantidade': quantidade, 'preco': preco}
        print('Produto adicionado com sucesso!\n')


# Entrada de estoque
def entrada_estoque(estoque):
    nome = input('Produto:').strip()
    if nome in estoque:
        qtd = int(input('Quantidade a adicionar:'))
        estoque[nome]['quantidade'] += qtd
        print('Estoque atualizado.\n')
    else:
        print('Produto não encontrado!\n')


# Saída de estoque
def saida_estoque(estoque):
    nome = input('Produto:').strip()
    if nome in estoque:
        qtd = int(input('Quantidade a remover:'))
        if estoque[nome]['quantidade'] >= qtd:
            estoque[nome]['quantidade'] -= qtd
            print('Saída registrada.\n')
        else:
            print('Quantidade insuficiente!\n')
    else:
        print('Produto não encontrado\n')


# Menu principal
def menu():
    usuarios = carregar_dados(ARQUIVO_USUARIOS)
    estoque = carregar_dados(ARQUIVO_ESTOQUE)

    if not login(usuarios):
        return

    while True:
        print('===MENU===')
        print('1 - Ver estoque')
        print('2 - Adicionar produto')
        print('3 - Entrada de estoque')
        print('4 - Saída de estoque')
        print('5 - Sair')
        opcao = input('Escolha:')

        if opcao == '1':
            ver_estoque(estoque)
        elif opcao == '2':
            adicionar_produto(estoque)
        elif opcao == '3':
            entrada_estoque(estoque)
        elif opcao == '4':
            saida_estoque(estoque)
        elif opcao == '5':
            salvar_dados(ARQUIVO_ESTOQUE, estoque)
            print('Alterações salvas. Saindo...')
            break
        else:
            print('opcao invalida!\n')


# Inicio do programa
if __name__ == '__main__':
    menu()
# Sistema de Cadastro de Usuários
# Desenvolvido em Python
# Permite adicionar, listar, atualizar e remover usuários

usuarios = []

def adicionar_usuario():
    nome = input("Digite o nome do usuário: ")
    idade = input("Digite a idade: ")
    email = input("Digite o e-mail: ")
    usuario = {"nome": nome, "idade": idade, "email": email}
    usuarios.append(usuario)
    print(f"\nUsuário {nome} adicionado com sucesso!\n")

def listar_usuarios():
    if not usuarios:
        print("\nNenhum usuário cadastrado.\n")
        return
    print("\nLista de usuários:")
    for i, usuario in enumerate(usuarios, 1):
        print(f"{i}. Nome: {usuario['nome']}, Idade: {usuario['idade']}, Email: {usuario['email']}")
    print()

def atualizar_usuario():
    listar_usuarios()
    if not usuarios:
        return
    try:
        indice = int(input("Digite o número do usuário que deseja atualizar: ")) - 1
        if indice < 0 or indice >= len(usuarios):
            print("Usuário inválido.\n")
            return
        nome = input("Novo nome (deixe em branco para manter o atual): ")
        idade = input("Nova idade (deixe em branco para manter a atual): ")
        email = input("Novo e-mail (deixe em branco para manter o atual): ")
        if nome:
            usuarios[indice]["nome"] = nome
        if idade:
            usuarios[indice]["idade"] = idade
        if email:
            usuarios[indice]["email"] = email
        print("\nUsuário atualizado com sucesso!\n")
    except ValueError:
        print("Entrada inválida.\n")

def remover_usuario():
    listar_usuarios()
    if not usuarios:
        return
    try:
        indice = int(input("Digite o número do usuário que deseja remover: ")) - 1
        if indice < 0 or indice >= len(usuarios):
            print("Usuário inválido.\n")
            return
        removido = usuarios.pop(indice)
        print(f"\nUsuário {removido['nome']} removido com sucesso!\n")
    except ValueError:
        print("Entrada inválida.\n")

def menu():
    while True:
        print("=== Sistema de Cadastro de Usuários ===")
        print("1 - Adicionar usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Remover usuário")
        print("5 - Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            adicionar_usuario()
        elif escolha == "2":
            listar_usuarios()
        elif escolha == "3":
            atualizar_usuario()
        elif escolha == "4":
            remover_usuario()
        elif escolha == "5":
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

if __name__ == "__main__":
    menu()

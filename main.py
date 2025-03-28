from database import listar_manifestacoes, inserir_manifestacao, alterar_manifestacao, excluir_manifestacao, contar_reclamacoes

def menu():
    while True:
        print("\n=== Sistema de Ouvidoria ===")
        print("1. Listar manifestações")
        print("2. Inserir manifestação")
        print("3. Alterar manifestação")
        print("4. Excluir manifestação")
        print("5. Contar reclamações")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            manifestacoes = listar_manifestacoes()
            if manifestacoes:
                print("\n=== Lista de Manifestações ===")
                for m in manifestacoes:
                    print(f"ID: {m['id']} | Tipo: {m['tipo']} | Descrição: {m['descricao']}")
            else:
                print("Nenhuma manifestação encontrada.")
        
        elif opcao == "2":
            tipo = input("Digite o tipo da manifestação (Reclamação, Sugestão, Elogio): ").strip()
            descricao = input("Digite a descrição: ").strip()
            inserir_manifestacao(tipo, descricao)
        
        elif opcao == "3":
            id = input("Digite o ID da manifestação a ser alterada: ")
            novo_tipo = input("Digite o novo tipo: ").strip()
            nova_descricao = input("Digite a nova descrição: ").strip()
            alterar_manifestacao(id, novo_tipo, nova_descricao)
        
        elif opcao == "4":
            id = input("Digite o ID da manifestação a ser excluída: ")
            excluir_manifestacao(id)
        
        elif opcao == "5":
            total = contar_reclamacoes()
            print(f"Total de reclamações registradas: {total}")
        
        elif opcao == "6":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()

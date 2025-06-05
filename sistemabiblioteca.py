class Livro:
    def __init__(self, titulo, autor, ano_publicacao, num_copias):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.num_copias = num_copias
        self.copias_disponiveis = num_copias

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, Disponíveis: {self.copias_disponiveis}/{self.num_copias}"

    def emprestar(self):
        if self.copias_disponiveis > 0:
            self.copias_disponiveis -= 1
            return True
        return False

    def devolver(self):
        if self.copias_disponiveis < self.num_copias:
            self.copias_disponiveis += 1
            return True
        return False


class Usuario:
    def __init__(self, nome, id_usuario, contato):
        self.nome = nome
        self.id_usuario = id_usuario
        self.contato = contato
        self.livros_emprestados = []

    def __str__(self):
        return f"Nome: {self.nome}, ID: {self.id_usuario}, Contato: {self.contato}"

    def adicionar_livro_emprestado(self, livro):
        self.livros_emprestados.append(livro)

    def remover_livro_emprestado(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            return True
        return False


class GerenciadorBiblioteca:
    def __init__(self):
        self.livros = {}
        self.usuarios = {}

    def cadastrar_livro(self, titulo, autor, ano_publicacao, num_copias):
        if titulo in self.livros:
            raise ValueError("Livro com este título já cadastrado.")
        livro = Livro(titulo, autor, ano_publicacao, num_copias)
        self.livros[titulo] = livro
        print(f"Livro '{titulo}' cadastrado com sucesso.")

    def cadastrar_usuario(self, nome, id_usuario, contato):
        if id_usuario in self.usuarios:
            raise ValueError("Usuário com este ID já cadastrado.")
        usuario = Usuario(nome, id_usuario, contato)
        self.usuarios[id_usuario] = usuario
        print(f"Usuário '{nome}' cadastrado com sucesso.")

    def emprestar_livro(self, id_usuario, titulo_livro):
        try:
            usuario = self.usuarios[id_usuario]
            livro = self.livros[titulo_livro]

            if not livro.emprestar():
                raise ValueError("Livro indisponível para empréstimo.")

            usuario.adicionar_livro_emprestado(livro)
            print(f"Livro '{titulo_livro}' emprestado para '{usuario.nome}'.")
        except KeyError:
            print("Erro: Usuário ou livro não encontrado.")
        except ValueError as e:
            print(f"Erro ao emprestar livro: {e}")

    def devolver_livro(self, id_usuario, titulo_livro):
        try:
            usuario = self.usuarios[id_usuario]
            livro = self.livros[titulo_livro]

            if not usuario.remover_livro_emprestado(livro):
                raise ValueError("Este livro não foi emprestado por este usuário.")

            livro.devolver()
            print(f"Livro '{titulo_livro}' devolvido por '{usuario.nome}'.")
        except KeyError:
            print("Erro: Usuário ou livro não encontrado.")
        except ValueError as e:
            print(f"Erro ao devolver livro: {e}")

    def consultar_livro(self, termo_busca, tipo_busca="titulo"):
        resultados = []
        for livro in self.livros.values():
            if tipo_busca == "titulo" and termo_busca.lower() in livro.titulo.lower():
                resultados.append(livro)
            elif tipo_busca == "autor" and termo_busca.lower() in livro.autor.lower():
                resultados.append(livro)
            elif tipo_busca == "ano" and str(termo_busca) == str(livro.ano_publicacao):
                resultados.append(livro)

        if not resultados:
            print("Nenhum livro encontrado com o termo de busca fornecido.")
        else:
            print("\nResultados da Consulta:")
            for livro in resultados:
                print(livro)
        return resultados

    def gerar_relatorio_livros_disponiveis(self):
        print("\n--- Relatório de Livros Disponíveis ---")
        disponiveis = [livro for livro in self.livros.values() if livro.copias_disponiveis > 0]
        if not disponiveis:
            print("Não há livros disponíveis no momento.")
        else:
            for livro in disponiveis:
                print(livro)

    def gerar_relatorio_livros_emprestados(self):
        print("\n--- Relatório de Livros Emprestados ---")
        emprestados = []
        for usuario in self.usuarios.values():
            for livro in usuario.livros_emprestados:
                emprestados.append(f"'{livro.titulo}' por '{usuario.nome}' (ID: {usuario.id_usuario})")

        if not emprestados:
            print("Não há livros emprestados no momento.")
        else:
            for item in emprestados:
                print(item)

    def gerar_relatorio_usuarios_cadastrados(self):
        print("\n--- Relatório de Usuários Cadastrados ---")
        if not self.usuarios:
            print("Não há usuários cadastrados.")
        else:
            for usuario in self.usuarios.values():
                print(usuario)


def exibir_menu():
    print("\n--- Gerenciando sua Biblioteca ---") # Título alterado aqui
    print("1. Cadastrar Livro")
    print("2. Cadastrar Usuário")
    print("3. Emprestar Livro")
    print("4. Devolver Livro")
    print("5. Consultar Livro")
    print("6. Gerar Relatórios")
    print("0. Sair")

def menu_relatorios():
    print("\n--- Menu de Relatórios ---")
    print("1. Livros Disponíveis")
    print("2. Livros Emprestados")
    print("3. Usuários Cadastrados")
    print("0. Voltar ao Menu Principal")

def main():
    print("------------------------------------------")
    print("  Bem-vindo(a) à Biblioteca do Seu Zé! ")
    print("------------------------------------------")
    biblioteca = GerenciadorBiblioteca()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Cadastrar Livro ---")
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano_publicacao = input("Ano de Publicação: ")
            try:
                num_copias = int(input("Número de Cópias: "))
                biblioteca.cadastrar_livro(titulo, autor, ano_publicacao, num_copias)
            except ValueError as e:
                print(f"Erro: {e}")
            except Exception as e:
                print(f"Erro inesperado: {e}")

        elif opcao == "2":
            print("\n--- Cadastrar Usuário ---")
            nome = input("Nome: ")
            id_usuario = input("ID do Usuário: ")
            contato = input("Contato: ")
            try:
                biblioteca.cadastrar_usuario(nome, id_usuario, contato)
            except ValueError as e:
                print(f"Erro: {e}")
            except Exception as e:
                print(f"Erro inesperado: {e}")

        elif opcao == "3":
            print("\n--- Emprestar Livro ---")
            id_usuario = input("ID do Usuário: ")
            titulo_livro = input("Título do Livro: ")
            biblioteca.emprestar_livro(id_usuario, titulo_livro)

        elif opcao == "4":
            print("\n--- Devolver Livro ---")
            id_usuario = input("ID do Usuário: ")
            titulo_livro = input("Título do Livro: ")
            biblioteca.devolver_livro(id_usuario, titulo_livro)

        elif opcao == "5":
            print("\n--- Consultar Livro ---")
            print("Consultar por: ")
            print("1. Título")
            print("2. Autor")
            print("3. Ano de Publicação")
            tipo_busca_opcao = input("Escolha o tipo de busca: ")
            termo_busca = input("Digite o termo de busca: ")

            if tipo_busca_opcao == "1":
                biblioteca.consultar_livro(termo_busca, "titulo")
            elif tipo_busca == "2":
                biblioteca.consultar_livro(termo_busca, "autor")
            elif tipo_busca_opcao == "3":
                biblioteca.consultar_livro(termo_busca, "ano")
            else:
                print("Opção de busca inválida.")

        elif opcao == "6":
            while True:
                menu_relatorios()
                opcao_relatorio = input("Escolha uma opção de relatório: ")
                if opcao_relatorio == "1":
                    biblioteca.gerar_relatorio_livros_disponiveis()
                elif opcao_relatorio == "2":
                    biblioteca.gerar_relatorio_livros_emprestados()
                elif opcao_relatorio == "3":
                    biblioteca.gerar_relatorio_usuarios_cadastrados()
                elif opcao_relatorio == "0":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "0":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
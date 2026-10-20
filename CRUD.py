import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        NOME TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
        CPF TEXT NOT NULL,
        IDADE INTEGER NOT NULL,
        Cidade TEXT NOT NULL
        )
""")
print ("=" * 30)
print ("Cadastro de Clientes")
print ("=" * 30)
while True:

    print ("\n1. Adicionar cliente")
    print ("2. Listar clientes")
    print ("3. Deletar cliente")
    print ("4. Editar cliente")
    print ("5. Sair")
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        nome = input ("Digite o nome do cliente:")
        email = input ("Digite o email do cliente:")
        cpf = input ("Digite o CPF do cliente:")
        idade = int(input ("Digite a idade do cliente:"))
        cidade = input ("Digite a cidade do cliente:")
        cursor.execute("INSERT INTO clientes (NOME, EMAIL, CPF, IDADE, Cidade) VALUES (?, ?, ?, ?, ?)", (nome, email, cpf, idade, cidade))
        conn.commit()
        print ("Cadastro Realizado com sucesso!")

    elif opcao == "2":
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        for cliente in clientes:
            id, nome, email, cpf, idade, cidade = cliente
            print (f"ID: {id}, Nome: {nome}, Email: {email}, CPF: {cpf}, Idade: {idade}, Cidade: {cidade}")
    elif opcao == "3":
        id_cliente = int(input("Digite o ID que deseja deletar:"))
        cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
        if cursor.rowcount > 0:
            conn.commit()
            print("Cliente deletado com sucesso!")
        else: 
            print("Cliente não encontrado!")

    elif opcao == "4":
        id_cliente = int(input("Digite o ID que deseja editar:"))
        cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_cliente,))
        cliente = cursor.fetchone()
        if cliente: 
            id, nome, email, idade, cpf, cidade = cliente 
            novo_nome = input(f"Digite o novo nome do cliente (atual: {nome}):") or nome 
            novo_email = input(f"Digite o Email atualizado do cliente (atual: {email}):") or email
            novo_cpf = input(f"Digite o CPF atualizado do cliente (atual:{cpf}):") or cpf 

            nova_idade = input(f"Digite a idade atualizada do cliente (atual: {idade}): ")
            if nova_idade:
                nova_idade = int(nova_idade)
            else:
                nova_idade = idade

            nova_cidade = input(f"Digite a cidade atualizada do cliente (atual: {cidade}): ") or cidade 
            cursor.execute("UPDATE clientes SET NOME = ?, EMAIL = ?, IDADE = ?, Cidade = ?, CPF = ? WHERE id = ?", (novo_nome, novo_email, nova_idade, nova_cidade, novo_cpf, id_cliente))
            conn.commit ()
            print ("Atualização realizada com sucesso!")

        else: 
            print("Cliente não encontrado!")

    elif opcao == "5":
        break; 

conn.close()
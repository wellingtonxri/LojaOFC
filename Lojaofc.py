from ConexãoOfc import * #Importando recursos da ConexãoOfc.py
from time import sleep
import os
import time
#=======Sistema GERAL DOS MENUS=======
def sistema_geral():
    os.system("cls")
    try:
        cl=int(input('''
    ╔════•ೋೋ•════╗ 
         LOJA
    ╚════•ೋೋ•════╝   
    1.Cliente
    2.Produto
    3.Fornecedor
    4.Venda
    5.Vendedor
    0.Sair\n'''))
        os.system("cls")
        if cl == 1:
            cliente()
        elif cl == 2:
            produto()
        elif cl == 3:
            fornecedor()
        elif cl == 4:
            venda()
        elif cl == 5:
            vendedor()
        elif cl == 0:
            print("\033[1;35mFinalizando programa... \033[m")
            sleep(1)
            print('''\033[1;94m	
    30%
    ███▒▒▒▒▒▒▒
    \033[m''')
            sleep(0.5)
            os.system("cls")
            print('''\033[1;94m	
    45%
    █████▒▒▒▒▒
    \033[m''')
            sleep(0.6)
            os.system("cls")
            print('''\033[1;94m	
    70%
    ███████▒▒▒
    \033[m''')
            sleep(1)
            os.system("cls")
            print('''\033[1;94m	
    100%
    ██████████
    \033[m''')
            print("\033[1;35mProgama finalizado.\033[m")
            sleep(1)
            os.system("cls")
            print("\033[1;35mVolte sempre.\033[m")
            sleep(1.5)
            banco.close
        else:
            print("\033[31mOpção inexistente.\033[m")
            sleep(2.5)
            sistema_geral()
    except ValueError:
        print("\033[31mERRO: por favor digite um número inteiro válido.\033[m")
        sleep(2.5)
        sistema_geral()
#=======Sistema principal dos CLIENTES=======
def cliente():
    try:
        op=int(input('''
    »»————MENU CLIENTES————««

        1.Listar  
        2.Cadastrar
        3.Editar
        4.Excluir
        5.Pesquisar
        0.Voltar\n'''))
        if op == 1:
            listar_cliente()
        elif op == 2:
            cadastrar_cliente()
        elif op == 3:
            editar_cliente()
        elif op == 4:
            excluir_cliente()
        elif op == 5:
            pesquisar_cliente()
        elif op == 0:
            os.system("cls")
            sistema_geral()
        else:
            os.system("cls")
            print("\033[31mOpção inexistente.\033[m")
            cliente()
    except ValueError:
        os.system("cls")
        print("\033[31mERRO: por favor digite um número inteiro válido.\033[m")
    finally:
        cliente()
#Função listar clientes
def listar_cliente():
    cursor = banco.cursor()
    comando_sql = "select * from cliente"
    cursor.execute(comando_sql)
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        print("Código:",i[0])
        print("Cliente:",i[1])
        print("CPF:",i[2])
        print("Data de nascimento:",i[3])
        print("Telefone:",i[4])
        print("——————"*6)
    cliente()
    os.system("cls")
#Função cadastrar clientes
def cadastrar_cliente():
    os.system("cls")
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO cliente (nome_cliente, cpf_cliente, data_nascimento, telefone_cliente)values (%s,%s,%s,%s)"
    try:
        nome=input("Digite o nome: ")
        cpf=input("Digite o CPF: ")
        nasc=input("Digite a data de nascimento: ")
        tel=input("Digite o telefone: ")
    except: ValueError
    else:
        dados = (nome,cpf,nasc,tel)
        cursor.execute(comando_SQL,dados)
        banco.commit()
        cliente() 
    finally:
        os.system("cls")
        print("\033[31mERRO Cadastrar: por favor digite a data de nascimento correto.\nNesse formato: 'AAAA-MM-DD'\nExemplo: 2021-10-11\033[m")
        cliente()
#Função editar cliente
def editar_cliente():
    os.system("cls")
    cursor = banco.cursor()
    comando_SQL = "UPDATE cliente set telefone_cliente = %s where cod_cliente = %s"
    try:
        cod=int(input("Digite o código do cliente: "))
        tel=input("Digite o telefone: ")
    except ValueError:
        os.system("cls")
        print("\033[31mERRO: por favor digite apenas número inteiro para código do cliente.\033[m")
    else:
        dados = (tel,cod)
        cursor.execute(comando_SQL,dados)
        banco.commit()
        cliente()
    finally:
        cliente()
#Função excluir cliente
def excluir_cliente():
    os.system("cls")
    cursor = banco.cursor()
    try:
        cod=int(input("Digite o código do cliente: "))
    except ValueError:
        os.system("cls")
        print("\033[31mERRO: por favor digite apenas número inteiro para código do cliente.\033[m")
    else:
        comando_SQL = "DELETE from cliente where cod_cliente = {}".format(cod)
        cursor.execute(comando_SQL)
        banco.commit()
        cliente()
    finally:
        cliente()
#Função pesquisar cliente
def pesquisar_cliente():
    os.system("cls")
    achei = 0
    cursor = banco.cursor()
    comando_sql = 'select * from cliente'
    cursor.execute(comando_sql)
    print("——————"*7)
    nome = input('Digite o nome do cliente: ')
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        if i[1] == nome:
         print("Código: ",i[0])
         print("Nome: ",i[1])
         print("CPF: ",i[2])
         print("Data de nascimento: ",i[3])
         print("Telefone: ",i[4])
         print("——————"*7)
         achei = 1
    if achei == 0:
        print('Produto não encontrado')
    banco.commit()
    cliente()
#=======Sistema principal de PRODUTOS=======
def produto():
    try:
        op=int(input('''
        »»————MENU PRODUTOS————««
        
        1.Listar
        2.Cadastrar
        3.Editar
        4.Excluir
        5.Pesquisar
        0.Voltar\n'''))
        print("——————"*7)
        if op == 1:
            listar_produto()
        elif op == 2:
            cadastrar_produto()
        elif op == 3:
            editar_produto()
        elif op == 4:
            excluir_produto()
        elif op == 5:
            pesquisar_produtos()
        elif op == 0:
            os.system("cls")
            sistema_geral()
        else:
            os.system("cls")
            print("\033[31mOpção inexistente.\033[m")
            cliente()
    except ValueError:
        os.system("cls")
        print("\033[31mERRO: por favor digite um número inteiro válido.\033[m")
    finally:
        produto()
#Função de Cadastrar
def cadastrar_produto():
    os.system("cls")
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produto (nome_produto,desc_produto,preco,cod_fornecedor)values (%s,%s,%s,%s)"
    try:
        nome=input("Digite o nome do produto: ")
        desc=input("Digite a descrição do produto: ")
        preco=float(input("Digite o preço do produto: "))
        fornec=int(input("Digite o código do fornecedor: "))
    except ValueError:
        os.system("cls")
        print("\033[31mERRO: por favor digite um número decimal para o preço.\033[m")
        print("\033[31mExemplo '150.00'\033[m")
        print("\033[31mE um número inteiro para o código do produto\033[m")
    else:
        dados = (nome,desc,preco,fornec)
        cursor.execute(comando_SQL,dados)
        banco.commit()
        produto()
    finally:
        produto()
#Função de listar produtos
def listar_produto():
    os.system("cls")    
    cursor = banco.cursor()
    comando_sql = "SELECT * FROM produto"
    cursor.execute(comando_sql)
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        print("Código: ",i[0])
        print("Produto: ",i[1])
        print("Descrição: ",i[2])
        print("Preço: ",i[3])
        print("Fornecedor: ",i[4])
        print("——————"*7)
    produto()
#Função de editar produtos
def editar_produto():
    os.system("cls")
    cursor = banco.cursor()
    comando_SQL = "UPDATE produto set preco = %s where cod_produto = %s"
    try:
        cod=int(input("Digite o código do produto: "))
        preco=float(input("Digite o preço do produto: "))
    except ValueError:
        os.system("cls")
        print("\033[31mERRO: por favor digite apenas número inteiro para código do produto.\033[m")
    else:
        dados = (preco,cod)
        cursor.execute(comando_SQL,dados)
        banco.commit()
    finally:
        produto()
    produto()
#Função de Excluir produtos
def excluir_produto():
    os.system("cls")
    cursor = banco.cursor()
    try:
        cod=int(input("Digite o código do produto: "))
    except ValueError:
        os.system("cls")
        print("\033[31mERRO: por favor digite apenas número inteiro para código do produto.\033[m")
    else:
        comando_SQL = "DELETE from produto where cod_produto = {}".format(cod)
        cursor.execute(comando_SQL)
        banco.commit()
        produto()
    finally:
        produto()
#Função de Pesquisar produtos
def pesquisar_produtos():
    os.system("cls")
    achei = 0
    cursor = banco.cursor()
    print("——————"*7)
    comando_sql = 'select * from produto'
    cursor.execute(comando_sql)
    nome = input('Digite o nome do produto: ')
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        if i[1] == nome:
         print("Código: ",i[0])
         print("Produto: ",i[1])
         print("Descrição: ",i[2])
         print("Preço: ",i[3])
         print("Fornecedor: ",i[4])
         print("——————"*7)
         achei = 1
    if achei == 0:
        print('Produto não encontrado')
    banco.commit()
    produto()
#=======Sistema principal de FORNECEDORES=======
def fornecedor():
    try:
        op=int(input(''' 
        »»————MENU FORNECEDORES————««
    
        1.Listar
        2.Cadastrar
        3.Editar
        4.Excluir
        5.Pesquisar
        0.Voltar\n'''))
        print("——————"*7)
        if op == 1:
            listar_fornecedor()
        elif op == 2:
            cadastrar_fornecedor()
        elif op == 3:
            editar_fornecedor()
        elif op == 4:
            excluir_fornecedor()
        elif op == 5:
            pesquisar_fornecedor()
        elif op == 0:
            os.system("cls")
            sistema_geral()
        else:
            os.system("cls")
            print("\033[31mOpção inexistente.\033[m")
            cliente()
    except ValueError:
        os.system("cls")
        print("\033[31mERRO: por favor digite um número inteiro válido.\033[m")
    finally:
        fornecedor()
#Função listar fornecedores
def listar_fornecedor():
    os.system("cls")
    cursor = banco.cursor()
    comando_sql = "select * from fornecedor"
    cursor.execute(comando_sql)
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        print("Código:",i[0])
        print("Fornecedor:",i[1])
        print("CNPJ:",i[2])
        print("Telefone:",i[3])
        print("——————"*7)

    fornecedor()
#Função cadastrar fornecedores
def cadastrar_fornecedor():
    os.system("cls")
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO fornecedor (nome_fornecedor, cnpj, telefone)values (%s,%s,%s)"
    nome=input("Digite o nome: ")
    cnpj=input("Digite o CNPJ: ")
    tel=input("Digite o telefone: ")
    dados = (nome,cnpj,tel)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    fornecedor() 
#Função editar fornecedor
def editar_fornecedor():
    os.system("cls")
    cursor = banco.cursor()
    comando_SQL = "UPDATE fornecedor set telefone = %s where cod_fornecedor = %s"
    try:
        cod=int(input("Digite o código do fornecedor: "))
        tel=input("Digite o telefone: ")
    except ValueError:
        os.system("cls")
        print("\033[31mERRO: por favor digite apenas número inteiro para código do fornecedor.\033[m")
    else:
        dados = (tel,cod)
        cursor.execute(comando_SQL,dados)
        banco.commit()
        fornecedor()
    finally:
        fornecedor()
#Função excluir fornecedor
def excluir_fornecedor():
    os.system("cls")
    cursor = banco.cursor()
    try:
        cod=int(input("Digite o código do fornecedor: "))
    except ValueError:
        os.system("cls")
        print("\033[31mERRO: por favor digite apenas número inteiro para código do fornecedor.\033[m")
    else:
        comando_SQL = "DELETE from fornecedor where cod_fornecedor = {}".format(cod)
        cursor.execute(comando_SQL)
        banco.commit()
        fornecedor()
    finally:
        fornecedor()
#Função pesquisar fornecedores
def pesquisar_fornecedor():
    os.system("cls")
    achei = 0
    cursor = banco.cursor()
    comando_sql = 'select * from fornecedor'
    cursor.execute(comando_sql)
    print("——————"*7)
    nome = input('Digite o nome do fornecedor: ')
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        if i[1] == nome:
         print("Código: ",i[0])
         print("Nome: ",i[1])
         print("CNPJ: ",i[2])
         print("Telefone: ",i[3])
         print("——————"*7)
         achei = 1
    if achei == 0:
        print('Produto não encontrado')
    banco.commit()
    fornecedor()
#=======Sistema principal de Venda=======
def venda():
    try:
        op=int(input('''
        »»————MENU VENDAS————««
        
        1.Listar
        2.Cadastrar
        3.Editar
        4.Excluir
        5.Pesquisar
        0.Voltar\n'''))
        if op == 1:
            listar_venda()
        elif op == 2:
            cadastrar_venda()
        elif op == 3:
            editar_venda()
        elif op == 4:
            excluir_venda()
        elif op == 5:
            pesquisar_venda()
        elif op == 0:
            os.system("cls")
            sistema_geral()
        else:
            os.system("cls")
            print("\033[31mOpção inexistente.\033[m")
            cliente()
    except ValueError:
        os.system("cls")
        print("\033[31mERRO: por favor digite um número inteiro válido.\033[m")
    finally:
        venda()
#Função listar venda
def listar_venda():
    os.system("cls")
    cursor = banco.cursor()
    comando_sql = "SELECT cod_venda, data_venda, quantidade_produto, nome_produto, desc_produto, preco * quantidade_produto, nome_cliente, nome_vendedor FROM cliente AS c INNER JOIN produto AS p ON c.cod_cliente = p.cod_produto INNER JOIN venda AS v ON v.cod_venda = p.cod_produto INNER JOIN vendedor AS ve ON  ve.matricula = p.cod_produto"
    cursor.execute(comando_sql)
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        print("Código:",i[0])
        print("Data da venda:",i[1])
        print("Quantidade de produto:",i[2])
        print("Nome do produto:",i[3])
        print("Descrição do produto:",i[4])
        print("Preço total:",i[5])
        print("Nome do cliente:",i[6])
        print("Nome do vendedor:",i[7])
        print("——————"*10)
    venda()
#Função cadastrar vendas
def cadastrar_venda():
    os.system("cls")
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO venda (data_venda, quantidade_produto)values (%s,%s)"
    nome=input("Digite a data da venda: ")
    quant=int(input("Digite a quantidade do produto: "))
    dados = (nome,quant)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    venda() 
#Função editar vendas
def editar_venda():
    os.system("cls")
    cursor = banco.cursor()
    comando_SQL = "UPDATE venda set quantidade_produto = %s where cod_venda = %s"
    try:
        cod=int(input("Digite o código da venda: "))
        quant=int(input("Digite a quantidade: "))
    except ValueError:
        os.system("cls")
        print("\033[31mERRO: por favor digite apenas número inteiro para código da venda.\033[m")
    else:
        dados = (quant,cod)
        cursor.execute(comando_SQL,dados)
        banco.commit()
        venda()
    finally:
        venda()
#Função excluir venda
def excluir_venda():
    os.system("cls")
    cursor = banco.cursor()
    try:
        cod=int(input("Digite o código da venda: "))
    except ValueError:
        os.system("cls")
        print("\033[31mERRO: por favor digite apenas número inteiro para código da venda.\033[m")
    else:
        comando_SQL = "DELETE from venda where cod_venda = {}".format(cod)
        cursor.execute(comando_SQL)
        banco.commit()
        venda()
    finally:
        venda()
#Função pesquisar vendas
def pesquisar_venda():
    os.system("cls")
    achei = 0
    cursor = banco.cursor()
    comando_sql = 'SELECT cod_venda, nome_produto, data_venda, quantidade_produto FROM venda AS v INNER JOIN produto AS p ON v.cod_venda = p.cod_produto'
    cursor.execute(comando_sql)
    print("——————"*7)
    vendas=input('Digite o nome do produto: ')
    data_lida = cursor.fetchall()
    for i in data_lida:
        if i[1] == vendas:
            print("Código da venda: ",i[0])
            print("Nome do produto: ",i[1])
            print("Data da venda: ",i[2])
            print("Quantidade do produto: ",i[3])

            print("——————"*7)
            achei = 1
    if achei == 0:
        print('Produto não encontrado')
    banco.commit()
    venda()
#=======Sistema principal dos VENDEDOR=======
def vendedor():
    try:
        op=int(input('''
        »»————MENU VENDEDORES————««
        
        1.Listar
        2.Cadastrar
        3.Editar
        4.Excluir
        5.Pesquisar
        0.Voltar\n'''))
        if op == 1:
            listar_vendedor()
        elif op == 2:
            cadastrar_vendedor()
        elif op == 3:
            editar_vendedor()
        elif op == 4:
            excluir_vendedor()
        elif op == 5:
            pesquisar_vendedor()
        elif op == 0:
            os.system("cls")
            sistema_geral()
        else:
            os.system("cls")
            print("\033[31mOpção inexistente.\033[m")
            cliente()
    except ValueError:
        os.system("cls")
        print("\033[31mERRO: por favor digite um número inteiro válido.\033[m")
    finally:
        vendedor()
#Função listar vendedor
def listar_vendedor():
    os.system("cls")
    cursor = banco.cursor()
    comando_sql = "select * from vendedor"
    cursor.execute(comando_sql)
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        print("Matricula:",i[0])
        print("Vendedor:",i[1])
        print("Setor:",i[2])
        print("Email:",i[3])
        print("——————"*7)
    vendedor()
#Função cadastrar vendedor
def cadastrar_vendedor():
    os.system("cls")
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO vendedor (nome_vendedor, setor, email)values (%s,%s,%s)"
    nome=input("Digite o nome: ")
    setor=input("Digite o setor: ")
    email=input("Digite o email: ")
    dados = (nome,setor,email)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    vendedor() 
#Função editar vendedor
def editar_vendedor():
    os.system("cls")
    cursor = banco.cursor()
    comando_SQL = "UPDATE vendedor set setor = %s, email = %s where matricula = %s"
    try:
        cod=int(input("Digite a matricula do vendedor: "))
        setor=input("Digite o setor: ")
        email=input("Digite o email: ")
    except ValueError:
        os.system("cls")
        print("\033[31mERRO: por favor digite apenas número inteiro para código do vendedor.\033[m")
    else:
        dados = (setor,email,cod)
        cursor.execute(comando_SQL,dados)
        banco.commit()
        vendedor()
    finally:
        vendedor()
#Função excluir vendedor
def excluir_vendedor():
    os.system("cls")
    cursor = banco.cursor()
    try:
        cod=int(input("Digite o código do vendedor: "))
    except ValueError:
        os.system("cls")
        print("\033[31mERRO: por favor digite apenas número inteiro para código do vendedor.\033[m")
    else:
        comando_SQL = "DELETE from vendedor where matricula = {}".format(cod)
        cursor.execute(comando_SQL)
        banco.commit()
        vendedor()
    finally:
        vendedor()
#Função pesquisar vendedor
def pesquisar_vendedor():
    os.system("cls")
    achei = 0
    cursor = banco.cursor()
    comando_sql = 'select * from vendedor'
    cursor.execute(comando_sql)
    print("——————"*7)
    nome = input('Digite o nome do vendedor: ')
    valores_lidos = cursor.fetchall()
    for i in valores_lidos:
        if i[1] == nome:
         print("Código: ",i[0])
         print("Nome: ",i[1])
         print("Setor: ",i[2])
         print("Email: ",i[3])
         print("——————"*7)
         achei = 1
    if achei == 0:
        print('Produto não encontrado')
    banco.commit()
    vendedor()
#===Função Bem vindo===#
def bem_vindo():
    time.strftime('%H%M', time.localtime())
    hora=time.strftime('%H%M', time.localtime())

    if hora >= '0600' and hora <='1259':
        os.system("cls")
        print("\033[1;35mBom dia! Seja bem vindo!\033[m")
        sleep(1)
        print("\033[1;32m乂❤‿❤ 乂\033[m")
        sleep(1.5)
    elif hora >= '1300' and hora <='1759':
        os.system("cls")
        print("\033[1;35mBoa tarde! Seja bem vindo!\033[m")
        sleep(1)
        print("\033[1;32m乂❤‿❤ 乂\033[m")
        sleep(1.5)
    elif hora >= '1800' and hora <='2359':
        os.system("cls")
        print("\033[1;35mBoa noite! Seja bem vindo!\033[m")
        sleep(1)
        print("\033[1;32m乂❤‿❤ 乂\033[m")
        sleep(3.5)
    else:
        print("Já é madrugada, não está na hora de ir dormir não?!")
bem_vindo()
sistema_geral()
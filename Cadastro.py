import datetime

class Cliente:
    def __init__(self, nome, endereco, telefone, complemento, praga_alvo, data_execucao, valor_servico):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.complemento = complemento
        self.praga_alvo = praga_alvo
        self.data_execucao = data_execucao
        self.valor_servico = valor_servico
        self.garantia = None

    def verificar_garantia(self):
        if self.data_execucao:
            data_atual = datetime.datetime.now().date()
            data_garantia = self.data_execucao + datetime.timedelta(days=180)
            if data_atual <= data_garantia:
                self.garantia = 'Dentro da garantia'
            else:
                self.garantia = 'Fora da garantia'
        else:
            self.garantia = 'Data de execução do serviço não informada'

clientes = []

def cadastrar_cliente():
    nome = input('Digite o nome do cliente: ')
    endereco = input('Digite o endereço do cliente: ')
    telefone = input('Digite o telefone do cliente: ')
    complemento = input('Digite o complemento do endereço: ')
    praga_alvo = input('Digite a praga alvo: ')
    data_execucao = input('Digite a data de execução do serviço (no formato dd/mm/aaaa): ')
    valor_servico = float(input('Digite o valor do serviço: '))

    data_execucao = datetime.datetime.strptime(data_execucao, '%d/%m/%Y').date() if data_execucao else None

    cliente = Cliente(nome, endereco, telefone, complemento, praga_alvo, data_execucao, valor_servico)
    clientes.append(cliente)
    print('Cliente cadastrado com sucesso!')

def consultar_cliente_por_endereco():
    endereco_consulta = input('Digite o endereço do cliente para consulta: ')
    cliente_encontrado = None
    for cliente in clientes:
        if cliente.endereco.lower() == endereco_consulta.lower():
            cliente_encontrado = cliente
            break

    if cliente_encontrado:
        print('Dados do cliente encontrado:')
        print('Nome:', cliente_encontrado.nome)
        print('Endereço:', cliente_encontrado.endereco)
        print('Telefone:', cliente_encontrado.telefone)
        print('Complemento:', cliente_encontrado.complemento)
        print('Praga Alvo:', cliente_encontrado.praga_alvo)
        print('Data de Execução do Serviço:', cliente_encontrado.data_execucao.strftime('%d/%m/%Y') if cliente_encontrado.data_execucao else 'Não informada')
        print('Valor do Serviço: R$', cliente_encontrado.valor_servico)
        cliente_encontrado.verificar_garantia()
        print('Garantia:', cliente_encontrado.garantia)
    else:
        print('Cliente não encontrado.')

def editar_cadastro():
    endereco_consulta = input('Digite o endereço do cliente para editar o cadastro: ')
    cliente_encontrado = None
    for cliente in clientes:
        if cliente.endereco.lower() == endereco_consulta.lower():
            cliente_encontrado = cliente
            break

    if cliente_encontrado:
        print('Dados atuais do cliente:')
        print('Nome:', cliente_encontrado.nome)
        print('Endereço:', cliente_encontrado.endereco)
        print('Telefone:', cliente_encontrado.telefone)
        print('Complemento:', cliente_encontrado.complemento)
        print('Praga Alvo:', cliente_encontrado.praga_alvo)
        print('Data de Execução do Serviço:', cliente_encontrado.data_execucao.strftime('%d/%m/%Y') if cliente_encontrado.data_execucao else 'Não informada')
        print('Valor do Serviço: R$', cliente_encontrado.valor_servico)

        print('\nDigite as novas informações:')
        nome = input('Digite o novo nome do cliente: ')
        endereco = input('Digite o novo endereço do cliente: ')
        telefone = input('Digite o novo telefone do cliente: ')
        complemento = input('Digite o novo complemento do endereço: ')
        praga_alvo = input('Digite a nova praga alvo: ')
        data_execucao = input('Digite a nova data de execução do serviço (no formato dd/mm/aaaa): ')
        valor_servico = float(input('Digite o novo valor do serviço: '))

        data_execucao = datetime.datetime.strptime(data_execucao, '%d/%m/%Y').date() if data_execucao else None

        cliente_encontrado.nome = nome
        cliente_encontrado.endereco = endereco
        cliente_encontrado.telefone = telefone
        cliente_encontrado.complemento = complemento
        cliente_encontrado.praga_alvo = praga_alvo
        cliente_encontrado.data_execucao = data_execucao
        cliente_encontrado.valor_servico = valor_servico

        print('Cadastro do cliente atualizado com sucesso!')
    else:
        print('Cliente não encontrado.')

def excluir_cadastro():
    endereco_consulta = input('Digite o endereço do cliente para excluir o cadastro: ')
    cliente_encontrado = None
    for cliente in clientes:
        if cliente.endereco.lower() == endereco_consulta.lower():
            cliente_encontrado = cliente
            break

    if cliente_encontrado:
        clientes.remove(cliente_encontrado)
        print('Cadastro do cliente excluído com sucesso!')
    else:
        print('Cliente não encontrado.')

# Exemplo de uso:
while True:
    print('1 - Cadastrar cliente')
    print('2 - Consultar cliente por endereço')
    print('3 - Editar cadastro do cliente')
    print('4 - Excluir cadastro do cliente')
    print('0 - Sair')

    opcao = input('Digite uma opção: ')

    if opcao == '1':
        cadastrar_cliente()
    elif opcao == '2':
        consultar_cliente_por_endereco()
    elif opcao == '3':
        editar_cadastro()
    elif opcao == '4':
        excluir_cadastro()
    elif opcao == '0':
        break
    else:
        print('Opção inválida. Tente novamente.')

def linha(tam=44):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(44))
    print(linha())

def menu(lista):
    cabecalho('\033[1;97mMenu do Restaurante')
    c = 1
    for item in lista:
        print(f'\033[1;31m{c}-{item}')
        c += 1
    print(linha())  

class Sistema:
  def __init__(self,id_ususario,senha,data_cadastro):
    self.id_usuario = id_ususario
    self.senha = senha
    self.data_cadastro = data_cadastro

  def verifLogin(self):
    print("Acesso autorizado")

class Funcionario(Sistema):
  def __init__(self,nome_adm,email):
    self.nome_adm = nome_adm
    self.email = email

  def atualizCatalogo(self):
    print("Catalago atualaizado")

class Cliente(Sistema):
  def __init__(self,nome_cliente,endereco,email,dadosCartao,saldoConta,num_cel):
    self.nome_cliente = nome_cliente
    self.endereco = endereco
    self.emai = email
    self.dadosCartao = dadosCartao
    self.saldoConta = saldoConta
    self.num_cel = num_cel

  def cadastro(self):
    print(self.nome_cliente)
    print(self.edereco)
    print(self.email)
    print(self.senha)
    print("Cadastro Realziado")

  def login(self,email,senha):
    print("Login Aceito")

  def atualizarCadastro(self):
    print("atualização de cadastro feita")

  def atualizarPerfil(self):
    print("perfil Atualizado")
    
class Produtos:
  def __init__(self,id_produto,nome_produto,sabor,preco_un,descricao):
    self.id_produto = id_produto
    self.nome_produto = nome_produto
    self.sabor = sabor
    self.preco_und = preco_un
    self.descricao = descricao

  def exibirProduto(self):
    print("Este é o produto:",self.id_produto,self.nome_produto,self.preco_und,self.sabor,self.descricao)

class Pedido:
  def __init__(self,id_pedido,id_produto,data_prod):
    self.id_pedido = id_pedido
    self.id_produto = id_produto
    self.data_prod = data_prod
    self.detalhesPedido = []
    self.carrinho =[]

  def carrinho(self,id_carrinho,quant,data):
    self.carrinho.append(CarrinhodeCompras(id_carrinho,quant,data))

  def lista_carrinho(self):
    for CarrinhodeCompras in self.carrinho:
      print(CarrinhodeCompras.id_carrinho,CarrinhodeCompras.quant,CarrinhodeCompras.data)

  def detalhesPedido(self,nome_produto,quant,preco,subtotal):
    self.detalhes.append(DetalhePedido(nome_produto, quant, preco, subtotal))
  
  def lista_detalhes(self):
    for DetalhePedido in self.detalhesPedido:
      print(DetalhePedido.nome_produto,DetalhePedido.quant,DetalhePedido.preco,DetalhePedido.subtotal)

  def finalizarPedido(self):
    print("Seu pedido stá sendo finalizado")

class CarrinhodeCompras:
  def __init__(self,id_carrinho,id_pedido,quant,data):
    self.id_carrinho = id_carrinho
    self.id_pedido = id_pedido
    self.quant = quant
    self.data = data
  
  def addItem(self):
    print(self.id_pedido,"Foi adicionado ao carrinho")
    
  def atualizarQuant(self):
    print("A quantidade agora é:",self.quant)

  def addObserv(self):
    input("Adicione sua observação aqui:")

  def verCarrinho(self):
    print(self.id_carrinho)

  def continuarCompra(self):
    pass

class DetalhePedido:
  def __init__(self,id_pedido,nome_produto,id_produto,quant,preco,subtotal):
    self.id_pedido = id_pedido
    self.nome_produto = nome_produto
    self.id_produto = id_produto
    self.quant = quant
    self.preco = preco
    self.subtotal = subtotal
    self.infoEnvio =[]
  
  def infoEnvio(self,num_envio,forma_envio,endereco,prev_chegada,num_cel):
    self.infoEnvio.append(InformacaoEnvio(num_envio,forma_envio,endereco,prev_chegada,num_cel))

  def lista_infos(self):
    for InformacaoEnvio in self.infoEnvio:
      print(InformacaoEnvio.num_envio,InformacaoEnvio.forma_envio,InformacaoEnvio.endereco,InformacaoEnvio.prev_chegada,InformacaoEnvio.num_cel)

  def exibirDetalhes(self):
    print('os detalhes do seu pedido:',self.id_pedido,self.nome_produto,self.id_produto,self.quant,self.preco,self.subtotal)

  def calcularPreco(self):
    print("O preço é:",self.preco)

class InformacaoEnvio:
  def __init__(self,num_envio,forma_envio,endereco,prev_chegada,num_cel):
    self.num_envio = num_envio
    self.forma_envio = forma_envio
    self.endereco = endereco
    self.prev_chegada = prev_chegada
    self.num_cel = num_cel

  def calcularEnvio(self):
    print("A Taxa de entrega é grátis para todo lugar!")

  def atualizarInfoEnvio(self):
    print("Desejar mudar o endereço?:",self.endereco)
    print("Deseja mudar o número de celular?:",self.num_cel)

#Menu inicial
while True:
  menu(['Cadastro','Login','Cárdapio','Locais de entrega','Suporte'])
  print()
  start = input('\033[1;39mQual Opção que você deseja?')
   
  if start == '4':
    print('\033[1;35mEntregamos em toda a cidade sem taxas!')
    print('\033[1;35mPs: Está sujeito a alterações no futuro')

  if start == '2':
    input('\033[1;36mInsira seu email:') 
    try:
      r = input('\033[1;36mInsira a sua senha:')
      r = int(r)
    except ValueError:
      print("\033[1;39mSenha somente com números por favor")
  
  if start == '3':
    print("\033[1;32mO Cárdapio é esse:")
    lanche1=Produtos('001','Burgão','Divino','R$12,00','Carne 250g,cheddar,barbecue e pão')
    lanche1.exibirProduto()
    
    lanche2 = {'Nº do lanche':'002','Nome':'ovinho','Sabor':'Gostosão','Valor':'R$5,00','Descrição': ' Pão com carne e ovo'}
    print(lanche2)

    pedir = input('\033[1;39mQual lanche voce quer ??')

    if pedir == '001': #basta colocar o id_produto#
        detalhe1=DetalhePedido('Código pedido:1345','Nome do lanche: Burgão','Código Produto: 001','Quantidade: 01','O lanche é R$12,00','Taxa de Entrega: R$0,00','Valor final: R$12,00' )
        detalhe1.exibirDetalhes()
        break
  
    if pedir == '002':
      detalhe2=['Código pedido:1342','Nome do lanche: Ovinho','Código Produto: 002','Quantidade: 01','O lanche é R$5,00','Valor final: R$5,00']
      detalhe2.append("Valor Final: R$5,00")
      detalhe2.pop(5)
      detalhe2.insert(5,'Taxa de entrega: R$0,00')
      print(detalhe2)
      break

  if start == '1':
    try:
      input('\033[1;34mInsira seu nome completo:')
      input('\033[1;34mInsira seu email:')
      n = input('\033[1;34mInsira sua senha:')
      n = int(n)
      input('\033[1;34mInsira seu endereço:')
    except ValueError as erro:
      raise ValueError('\033[1;39mSenha Somente com números por favor')
    else:
      print('\033[1;34mCadastro Completo!')

  if start == '5':
    print('\033[1;33mBem vindo ao suporte!! Como podemos te ajudar?')
    input('\033[1;39m')
    print('\033[1;33mSugestão enviada!Muito obrigado')

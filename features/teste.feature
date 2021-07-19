#language:pt

Funcionalidade: Teste

  @teste
  Esquema do Cenario: realizar teste
    #Dado que eu tenho um novo "DVD" em meu carrinho
    #E tenho um novo "livro" em meu carrinho
    #E tenho outros "<produtos>" no carrinho
    Quando eu clico em "Next"
      """
        {
          "nome_produto": "DVD",
          "descricao": "DVD Harry Potter",
          "preco": "R$ 10"
        }
      """
    #Entao devo visualizar "Sucesso"
    #  | thing         | other thing |
    #  | Red Tree Frog | mush        |

    Exemplos: produtos
      | produtos  |
      | Carro     |
      | Moto      |
      | Bicicleta |



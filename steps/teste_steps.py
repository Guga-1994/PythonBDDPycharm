from json import loads
from behave import given, then, when

@given('que eu tenho um novo "{item}" em meu carrinho')
def novo_item_carrinho(context, item):
    """
    o "context" é usado quando se quer ter acesso a variáveis que são passadas
    por parâmetro ou é definida dentro de um step, de modo que essas variáveis
    podem ser compartilhadas por outros steps. Nesse caso, foi usado o recurso
    do contexte para tornar acessível o parâmetro "item", logo foi possivel usar
    no step a baixo.
    """
    context.item = "Mobdick"
    context.teste1 = "O senhor dos aneis"
    print(" O novo item é: {}".format(item))

@given(u'tenho um novo "{livro}" em meu carrinho')
def novo_livro_carrinho(context, livro):
    print(" o novo item é: {}".format(livro))
    print(context.item)
    print(context.teste1)

@given(u'tenho outros "{produto}" no carrinho')
def step_impl(context, produto):
    raise NotImplementedError(u'STEP: Given tenho outros "Carro" no carrinho')

@when(u'eu clico em "Next"')
def clicar_next(context):
    """
    essa forma de criar massa de dados se chama dicionario, sendo uma alternativa ao
    uso de tabelas. Ao usar as 3 aspas de comentário, o texto será associado ao step
    e estara disponivel como o atributo ".text" na "context" variável passada por cada
    função da etapa
    """
    texto_do_step = loads(context.text)
    print(texto_do_step['nome_produto'])
    print(texto_do_step['descricao'])
    print(texto_do_step['preco'])


@then(u'devo visualizar "Sucesso"')
def step_impl(context):
    """
    pode ser associado uma tabela de dados a uma etapa. A tabela esta disponível para o step
    como o atributo ".table" no context variável passada para cada função da etap. Ex:
    @given('a set of specific users')
    def step_impl(context):
    for row in context.table:
    model.add_user(name=row['name'], department=row['department'])
    """


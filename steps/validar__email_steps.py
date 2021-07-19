from behave import given, then, when

@given('que eu tenho um email {email}')
def step_impl(context, email):
    context.email = email


@when('eu o valido')
def step_impl(context):
    #context.result=validador(context.eamil)


@then('eu devo pegar o {result}')
def step_impl(context, result):
    assert str(context.result)==result, '%s should be %s' % (context.email, result)


#language:pt

@validar
Funcionalidade: Validacao de email

    Esquema do Cenario: emails validados
      Dado que eu tenho um email <email>
      Quando eu o valido
      Entao eu devo pegar o <status>

    Exemplos: emails validos
      | email                             | status |
      | gwsthavopotter@gmail.com          | True   |
      | gustavoalmeidasilva1994@gmail.com | True   |


    Exemplos: emails nao-validos
      | email                  | status |
      | gugapotter@gmail.com   | False  |
      | gustaalmeida@gmail.com | False  |
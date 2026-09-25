# language: pt

Funcionalidade: Login
  Como um usuário do sistema
  Eu quero fazer login na aplicação
  Para acessar minha conta

  Cenário: Login com credenciais válidas
    Dado que estou na página de login
    Quando informo um email e senha válidos
    E clico no botão de entrar
    Então devo ser redirecionado para a página inicial logada

  Cenário: Login com credenciais inválidas
    Dado que estou na página de login
    Quando informo um email ou senha inválidos
    E clico no botão de entrar
    Então devo ver uma mensagem de erro de login
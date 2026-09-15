from pytest_bdd import scenarios, given, when, then
from pages.login_page import LoginPage

# Carrega os cenários do arquivo .feature
scenarios('../features/login.feature')


@given('que estou na página de login', target_fixture="login_page")
def acessar_pagina_login(page):
    page.goto("https://www.automationexercise.com/login")
    return LoginPage(page)


@when('informo um email e senha válidos')
def preencher_login_valido(login_page):
    login_page.email_input.fill("idnareis.teste@gmail.com")
    login_page.password_input.fill("Teste123!")


@when('informo um email ou senha inválidos')
def preencher_login_invalido(login_page):
    login_page.email_input.fill("email_invalido@teste.com")
    login_page.password_input.fill("senhaerrada")


@when('clico no botão de entrar')
def clicar_entrar(login_page):
    login_page.login_button.click()


@then('devo ser redirecionado para a página inicial logada')
def verificar_login_sucesso(login_page):
    assert login_page.logged_in_as.is_visible()


@then('devo ver uma mensagem de erro de login')
def verificar_login_erro(login_page):
    assert login_page.error_message.is_visible()
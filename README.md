# 🧪 Testes de Ponta a Ponta (E2E) — Automation Exercise

Suíte de automação de testes end-to-end desenvolvida com **Python + Playwright + Pytest**, cobrindo a jornada completa de um e-commerce: cadastro, login, produtos, carrinho e checkout.

> Projeto de portfólio desenvolvido por **Idna Reis**, estudante de Análise e Desenvolvimento de Sistemas, com foco em Automação de Testes (QA).

---

## 📌 Sobre o projeto

Este projeto automatiza cenários reais de um site de e-commerce de testes ([Automation Exercise](https://automationexercise.com)), simulando a jornada de um usuário: criar conta, fazer login, navegar pelos produtos, montar o carrinho e finalizar uma compra — validando cada etapa com asserções específicas.

O objetivo foi praticar e demonstrar:
- Estruturação de um projeto de automação seguindo boas práticas (Page Object Model)
- Cobertura de cenários positivos e negativos
- Geração de evidências (screenshots, vídeos e traces) para cada execução
- Debug de testes a partir de mensagens de erro reais do Playwright

---

## 🎯 Objetivos

- Validar o fluxo completo de compra (cadastro → login → carrinho → checkout → pedido confirmado)
- Cobrir cenários de login (válido, inválido, campos vazios, logout)
- Cobrir cenários de busca e navegação de produtos
- Gerar relatórios e evidências visuais de cada teste executado

---

## 🛠️ Tecnologias

- **Python 3.14**
- **Playwright** — automação do navegador
- **Pytest** — framework de testes
- **pytest-playwright** — integração Playwright + Pytest
- **pytest-html** — geração de relatório HTML
- **Page Object Model (POM)** — padrão de arquitetura

---

## 🏗️ Arquitetura

O projeto segue o padrão **Page Object Model**, separando a lógica de interação com cada página (`pages/`) dos cenários de teste (`tests/`). Isso deixa os testes mais legíveis e facilita manutenção quando o site muda.

```
playwright-e2e-python/
│
├── pages/                     # Page Objects — um arquivo por página do site
│   ├── base_page.py
│   ├── login_page.py
│   ├── signup_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/                     # Cenários de teste
│   ├── test_login.py
│   ├── test_login_valid.py
│   ├── test_signup.py
│   ├── test_products.py
│   ├── test_products_extra.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── evidencias/                 # Screenshots, vídeos e traces gerados a cada execução
├── reports/                    # Relatório HTML da suíte
├── pytest.ini                  # Configuração do Pytest
└── requirements.txt
```

---

## 🧪 Cenários automatizados

**16 testes automatizados**, cobrindo:

| Área | Cenários |
|---|---|
| **Cadastro** | Elementos da página de cadastro / cadastro com dados válidos |
| **Login** | Elementos da página / credenciais inválidas / email vazio / senha vazia / login com credenciais válidas / logout |
| **Produtos** | Elementos da página / busca de produto existente / busca de produto inexistente / visualizar detalhes do produto / adicionar múltiplos produtos ao carrinho |
| **Carrinho** | Elementos / adicionar produto / validar nome, quantidade e preço do item / remover produto |
| **Checkout (fluxo completo)** | Cadastro → login automático → adicionar produto → carrinho → checkout → validação de endereço → pagamento → confirmação do pedido |

---

## ▶️ Como executar

**Pré-requisitos:** Python 3.10+ instalado.

```bash
# Clonar o repositório
git clone https://github.com/IdnaReis/testes-e2e-playwright-python.git
cd testes-e2e-playwright-python

# Criar e ativar ambiente virtual
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Linux/Mac

# Instalar dependências
pip install -r requirements.txt
playwright install

# Rodar toda a suíte
pytest -v

# Rodar um arquivo específico
pytest tests/test_checkout.py -v
```

---

## 📊 Relatórios

Após a execução, um relatório HTML é gerado automaticamente em `reports/report.html`, com o status de cada teste, tempo de execução e detalhes de falhas (quando houver).

---

## 📸 Evidências

A cada execução, o projeto gera automaticamente, para **cada teste**, dentro da pasta `evidencias/`:

- 📷 **Screenshot** da tela ao final do teste
- 🎥 **Vídeo** da execução completa
- 🔍 **Trace** (linha do tempo detalhada, navegável no [Playwright Trace Viewer](https://playwright.dev/python/docs/trace-viewer))

Para visualizar um trace:
```bash
playwright show-trace evidencias/<pasta-do-teste>/trace.zip
```

---

## 🔄 CI/CD

O projeto conta com um pipeline no **GitHub Actions**, que executa toda a suíte de testes automaticamente a cada push, instalando as dependências e o navegador do Playwright em um ambiente limpo — garantindo que os testes continuam passando de forma independente da máquina local.

---

## 📫 Contato

**Idna Reis**
🔗 [LinkedIn](https://www.linkedin.com/in/idna-reis)
💻 [GitHub](https://github.com/IdnaReis)

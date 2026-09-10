# Testes E2E com Playwright + Python

![Testes E2E](https://github.com/IdnaReis/testes-e2e-playwright-python/actions/workflows/tests.yml/badge.svg)

Projeto de automação de testes end-to-end (E2E) desenvolvido com **Python**, **Playwright** e **Pytest**, seguindo o padrão de projeto **Page Object Model (POM)**. Os testes cobrem os principais fluxos do site [Automation Exercise](https://automationexercise.com), incluindo cadastro, login, navegação de produtos, carrinho de compras e checkout.

## 🎯 Objetivo

Este projeto foi desenvolvido como parte do meu portfólio de QA, com o objetivo de demonstrar habilidades práticas em automação de testes web, incluindo:

- Organização de código com Page Object Model
- Integração contínua (CI) com GitHub Actions
- Geração de relatórios de execução em HTML
- Boas práticas de testes automatizados

## 🛠️ Tecnologias utilizadas

- **Python 3.12**
- **Playwright** — automação de navegador
- **Pytest** — framework de testes
- **pytest-playwright** — integração do Playwright com o Pytest
- **pytest-html** — geração de relatórios em HTML
- **GitHub Actions** — pipeline de integração contínua

## 📁 Estrutura do projeto

```
playwright-e2e-python/
├── pages/                  # Page Objects (elementos e ações de cada página)
│   ├── base_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── login_page.py
│   ├── products_page.py
│   └── signup_page.py
├── tests/                  # Casos de teste
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_login.py
│   ├── test_login_valid.py
│   ├── test_products.py
│   ├── test_products_extra.py
│   └── test_signup.py
├── utils/                  # Funções e dados auxiliares
├── reports/                # Relatórios HTML gerados após a execução
├── evidencias/             # Capturas de tela de falhas
├── requirements.txt        # Dependências do projeto
├── pytest.ini              # Configurações do Pytest
└── .github/workflows/      # Pipeline de CI (GitHub Actions)
```

## ✅ Cenários testados

- **Cadastro de usuário** — criação de nova conta
- **Login** — cenários de login válido e inválido
- **Produtos** — busca, visualização de detalhes e listagem
- **Carrinho** — adição e verificação de itens
- **Checkout** — finalização do processo de compra

## 🚀 Como rodar o projeto localmente

**Pré-requisitos:** Python 3.12+ instalado

1. Clone o repositório:
```bash
git clone https://github.com/IdnaReis/testes-e2e-playwright-python.git
cd testes-e2e-playwright-python
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
playwright install --with-deps
```

4. Execute os testes:
```bash
pytest -v
```

5. O relatório HTML será gerado em `reports/report.html`.

## 🔄 Integração Contínua (CI)

Este projeto conta com um pipeline configurado no **GitHub Actions** (`.github/workflows/tests.yml`), que executa automaticamente todos os testes a cada push na branch `main`. O pipeline realiza:

1. Checkout do código
2. Configuração do ambiente Python
3. Instalação das dependências
4. Execução dos testes com Pytest

## 📊 Relatórios

Após cada execução, um relatório HTML detalhado é gerado, contendo o status de cada teste e evidências (screenshots) em caso de falha.

![Relatório de testes](docs/relatorio-testes.png)

## 👩‍💻 Autora

**Idna Reis**
Profissional de QA | Estudante de Análise e Desenvolvimento de Sistemas

- LinkedIn: [linkedin.com/in/idna-reis](https://linkedin.com/in/idna-reis)
- GitHub: [@IdnaReis](https://github.com/IdnaReis)

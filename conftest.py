import re

import pytest

# Domínios de anúncios e rastreamento que deixam os testes instáveis
# (pop-ups, vinhetas do Google e carregamento lento da página)
DOMINIOS_ANUNCIOS = re.compile(
    r"googlesyndication|doubleclick|googleadservices|adservice\.google"
    r"|google-analytics|googletagmanager|fundingchoicesmessages|amazon-adsystem"
)


def _bloquear_anuncios(route):
    if DOMINIOS_ANUNCIOS.search(route.request.url):
        route.abort()
    else:
        route.continue_()


@pytest.fixture(autouse=True)
def configurar_pagina(page):
    """Aplicada a todos os testes: timeout padrão e bloqueio de anúncios."""
    page.set_default_timeout(60000)
    page.route("**/*", _bloquear_anuncios)
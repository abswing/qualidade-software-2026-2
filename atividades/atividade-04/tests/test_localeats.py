# Testes funcionais do LocalEats com Playwright
# Responsável: Antonio Bernardo
import re

from playwright.sync_api import Page, expect

URL_LOCALEATS = "https://local-eats-unisenac.vercel.app/"


# TF01 - login com credenciais inválidas exibe mensagem de erro
def test_login_com_credenciais_invalidas_exibe_erro(page: Page):
    page.goto(URL_LOCALEATS)

    page.get_by_placeholder("teste@teste.com").fill("naoexiste@teste.com")
    page.get_by_placeholder("Sua senha secreta").fill("senhaerrada")
    page.locator("#loginForm").get_by_role("button", name="Entrar").click()

    # Assertion 1: a mensagem de erro aparece com o texto do sistema
    expect(page.locator("#errorMsg")).to_have_text("Invalid credentials")
    # Assertion 2: o usuário continua na tela de login
    expect(page).to_have_url(re.compile(r"login\.html"))
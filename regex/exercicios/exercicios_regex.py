import re

def validar_email(email):
    estrutura_email = r'^[A-Za-z0-9]+([+.-_][A-Za-z0-9]+)*@[A-Za-z0-9]+([-.][A-Za-z0-9]+)*\.[A-Za-z]{2,}$'

    if re.match(estrutura_email, email):
        return True
    return False

def extrair_telefones(telefone):
    estrutura_telefone = r'(\+\d{1,3})?\s*(\(?\d{1,3}\)?)?\s*\d{4,5}-?\d{4}'
    
    if re.search(estrutura_telefone, telefone):
        return True
    return False

def substituir_urls(url):
    estrutura_url = r'https?://[A-Za-z0-9]+(-[A-Za-z0-9]+)*\.?[A-Za-z0-9]+(-[A-Za-z0-9]+)*(\.[A-Za-z]{2,})+'
    
    return re.sub(estrutura_url, "[LINK]", url)

if __name__ == '__main__':

    print(substituir_urls("Visite o nosso site em: https://www.nossosite.com.br"))
    
    print(extrair_telefones("(84) 99921-3645"))

    print(validar_email("meuemail123@gmail.com"))
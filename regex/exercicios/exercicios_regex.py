import re

def validar_email(email):
    estrutura_email = r'^[A-Za-z0-9]+([+.-_][A-Za-z0-9]+)*@[A-Za-z0-9]+([-.][A-Za-z0-9]+)*\.[A-Za-z]{2,}$'

    if re.match(estrutura_email, email):
        return True
    else:
        return False

def extrair_telefones(telefone):
    estrutura_telefone = r'(\+\d{1,3})?\s*(\(?\d{1,3}\)?)?\s*\d{4,5}-?\d{4}'
    
    return re.findall(estrutura_telefone, telefone)

def substituir_urls(url):
    estrutura_url = r'https?://[A-Za-z0-9]+(-[A-Za-z0-9]+)*\.?[A-Za-z0-9]+(-[A-Za-z0-9]+)*(\.[A-Za-z]{2,})+'
    
    return re.sub(estrutura_url, "[LINK]", url)

if __name__ == '__main__':

    print(validar_email("exemplo@dominio.com")) 
    print(validar_email("exemplo@dominio"))
    
    texto = "Visite nosso site em http://www.exemplo.com ou https://exemplo.com.br para mais informações."
    print(substituir_urls(texto))

    telefone = "Contate-nos no 123-456-789 ou 987 654 321."
    print(extrair_telefones(telefone))
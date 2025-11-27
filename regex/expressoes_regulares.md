# 🔠 Expressões Regulares (Regex)

**Expressões Regulares (ou regex)** é um recurso da programação usado para **definir padrões de texto** e **localizar**, **verificar** e **extrair** esses padrões dentro de **strings**.

---

## ❓ Onde é Usada

As expressões regulares são amplamente utilizadas nas mais diversas áreas do mercado da TI, por ser algo **simples e eficiente**. Com essa ferramenta, é possível **definir padrões** para **capturar**, **verificar** e **validar dados de forma precisa**, garantindo a integridade das informações e o funcionamento correto das aplicações.

---

### ⬇️ Exemplos de Uso

1. **👤 Validar dados do usuário:**

- 🔤 Nome
- 📧 E-mail
- 🔑 Senha
- ☎️ Telefone...

---

2. **⌨️ Determinar Padrões Para Escrita de Dados:**

**📞 Telefone:**

- 11 99999-9999 ✅
- 1199999-9999 ❌
- 11 99999 9999 ❌
- (11) 99999-9999 ✅

**📧 E-mail:**

- email..aleatorio@gmail.com ❌
- emailaleatorio123@gmail.com ✅
- emailaleatori.o@gmail.com ✅
- email-aleatorio@%gmail.com ❌

**🔑 Senha:**

- 1234abc ✅
- 123 abc ❌
- 123892ab ✅
- abc ❌

**🔗 URL:**

- https://-google.com ❌
- https://google.com ✅
- http://link-aleatorio ✅
- https://linkaleatorio.com..br ❌

---

3. **🔍 Localizar Padrões Definidos Em Strings:**

Padrão definido ➡️ **AB2$-**
(Duas letras, um número, dois caracteres especiais)

- ABC12.- ❌
- C65.+ ❌
- LP0&# ✅
- YR4.? ✅
# 🤝 Boas Práticas de Códigos
Ter noções de **boas práticas no desenvolvimento de programas** é essencial para qualquer profissional da área de tecnologia. Seguir convensões, adotar padrões de código, escrever documentações e comentários explicativos são práticas **cruciais para o bom funcionamento e manutenção de sistemas, além de facilitar a cooperação entre times de desenvolvedores.**

---

## ⚙️ Desenvolvimento de algorítmos

### 🔤 1. Nomeação de funções, variáveis e classes

Saber nomear funções, variáveis e classes de forma **clara** e **objetiva** é fundamental para a compreensão do código. É necessário que esses elementos tenham nomes que indiquem claramente os seus propósitos dentro do algoritmo.

**⬇️ Exemplo de má prática:**
```python
def calcular(a, b):
    return a + b

a = int(input("Informe um número: "))
b = int(input("Informe outro número: "))

print(f"Resultado: {calcular(a, b)}")
```
Perceba que as variáveis que recebem números possuem nomes **ilógicos e sem sentido** ("a", "b"). Imagine se esse tipo de nomeação fosse aplicado no desenvolvimento de grandes sistemas — seria muito difícil entender a lógica extremamente desgastante. 

Além disso, a função se chama apenas `calcular`, mas **não especifica o que está calculando**. Isso pode gerar confusão em códigos maiores.

**⬇️ Exemplo de boa prática:**
```python
def calcular_soma(numero1, numero2):
    return numero1 + numero2

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))

print(f"A soma de {numero1} + {numero2} = {calcular_soma(numero1, numero2)}")
```
Agora:
- As variáveis possuem nomes descritivos (`numero1`, `numero2`) indicando que armazenam valores númericos.
- A função se chama `calcular_soma`, deixando explícito que o **cálculo realizado é uma soma**.

**✅ Conclusão:**
Nomes **claros, compreensíveis e lógicos** tornam o código mais **legível**, **fácil de manter** e mais **colaborativo em equipes de desenvolvimento**.
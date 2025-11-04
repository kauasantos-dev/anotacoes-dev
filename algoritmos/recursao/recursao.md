# ⚙️ Recursão

Anotações de estudo sobre **recursão**.

---

## ❗Definição

Recursão é uma técnica de programação em que uma **função chama a si mesma para solucionar um problema**, **dividindo-o em partes menores a cada chamada recursiva** até atingir um **caso base**, ou seja, **uma codição** que **encerra as chamadas recursivas** onde todo o problema é solucionado.

---

## 🗣️ Chamada Recursiva

A **chamada recursiva** ocorre cada vez que a **função chama a si própria durante a execução**, passando **valores modificados** a cada chamada para alcançar o **caso base**.

---

## ✅ Caso Base

**Caso base** é a **condição de parada da recursão**, ou seja, é o momento em que o **problema é solucionado por completo** e as chamadas recursivas são encerradas.

---

## ⬇️ Exemplo De Recursão

Função que calcula o **fatorial** de um número `n`:

```python
def fatorial(numero):
    if numero == 1 or numero == 0:  # Caso base (condição de parada)
        return 1
    else:
        return numero * fatorial(numero - 1)  # Chamada recursiva (função chamando a si própria)

numero = int(input("Digite um número positivo: "))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")
```
📝 **Explicação:**
A cada **chamada recursiva**, o valor de `número` é multiplicado pelo seu antecessor `fatorial(numero - 1)`. Quando o `número` chega a `0` ou a `1`, o **caso base** é atingidoo e a **função começa a retornar os resultados acumulados**, **resolvendo todas as chamadas pendentes**.

---

## ⚖️ Leis da Recursão

---

1. **A função precisa chamar a si própria**
Para que a recursão ocorra, a função precisa chamar a si mesma durante a execução do código até que o caso base seja atingido, sem isso, não há recursão, pois a função será executada apenas uma vez e o problema não será resolvido.

---
2. **Toda recursão possui um caso base**
Obrigatoriamente, toda função recursiva necessita de um caso base para que a recursão seja finalizada, pois sem isso, o código entra num loop infinito e a função será chamada infinitamente.

---

3. **A recursão deve se aproximar de seu caso base a cada chamada recursiva**
A cada chamada recursiva, o problema deve se aproximar de sua resolução até alcançar o caso base, onde ele é solucionado por completo.
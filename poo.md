# ⚙️ Programação Orientada a Objetos - (POO)

Anotações de estudo sobre POO.

---

## 📝 Definição

Programação Orientada a Objetos é uma forma de se programar utilizando códigos para representar objetos do mundo real, sendo eles abstratos ou não.

---

## ⁉️ Conceitos Fundamentais

### 📦 1. Classe

- É o molde que define como o objeto será
- Dentro da classe, ficam os atributos (características) e os métodos (ações) do objeto
- Com apenas uma classe, é possível criar uma quantidade N de objetos.

---

### ♟️ 2. Objeto

- É uma instância da classe, ou seja, é o exemplo real do objeto em ação
- Os objetos de uma mesma classe possuem os mesmos atributos e métodos, mas os dados de cada objeto são exclusivos.

---

### 🅰️ 3. Atributos
São as características que compõem o objeto.

**⬇️ Exemplo:**
```python
class InstrumentoDeCorda:
    def __init__(self, nome, numero_cordas, cor, tamanho):
        self.nome = nome
        self.numero_cordas = numero_cordas
        self.cor = cor
        self.tamanho = tamanho
```
No exemplo acima, cada ítem é um atributo da classe, ou seja, características do objeto.

---

### Ⓜ️ 4. Métodos
São as ações que o objeto realiza.

**⬇️ Exemplo:**
```python
class InstrumentoDeCorda:
    def __init__(self, nome, numero_cordas, cor, tamanho):
        self.nome = nome
        self.numero_cordas = numero_cordas
        self.cor = cor
        self.tamanho = tamanho
    
    def tocar_instrumento(self):    # método de tocar o instrumento
        print("Tocando o instrumento")
```
Como visto no exemplo acima, o método `tocar_instrumento` realiza a ação de tocar o instrumento, e é isso o que os métodos fazem, executam ações relacionadas ao objeto. 

---

### 🔐 5. Encapsulamento

É o princípio de proteger os dados internos de um objeto para promover segurança e estabilidade. Os dados podem e devem ser acessados apenas por meio de métodos específicos que controlam o acesso a esses dados.

**⬇️ Exemplo:**
```python
class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # atributo privado
    
    def ver_saldo(self):      # método que retorna o valor do atributo privado
        return self.__saldo
    
    def alterar_saldo(self, novo_saldo):    # método que valida os dados antes de alterar o atributo privado
        try:
            novo_saldo = float(novo_saldo)
        except ValueError:
            raise ValueError("O saldo deve conter apenas números")

        if novo_saldo < 0:
            raise ValueError("O saldo não pode ser menor que zero.")
        
        self.__saldo = novo_saldo
```

---

### 👨‍👩‍👧‍👦 6. Herança

Permite criar várias classes que herdam atributos e métodos de outras classes. Isso é algo essencial para reutilização de código, evitando assim repetição e desperdício de tempo.

**⬇️ Exemplo:**
```python
class Veiculo:
    def mover(self):
        print("Veículo em movimento")

class Carro(Veiculo):   # Essa classe herda o mesmo método da classe Veiculo
    pass

carro = Carro()
carro.mover()   # chamando o método herdado
```

---

### 🎭 7. Polimorfismo

Polimorfismo significa "muitas formas" e ocorre quando um mesmo método se comporta de formas diferentes de acordo com a classe que o utiliza.

**⬇️ Exemplo:**
```python
class Animal:
    def emitir_som(self):
        print("Som do animal")
    
class Cachorro(Animal):
    def emitir_som(self):
        print("Au Au!")

class Gato(Animal):
    def emitir_som(self):
        print("Miau Miau!")
```
Note que o mesmo `emitir_som` se comporta de maneira diferente nas classes acima. Isso é polimorfismo.
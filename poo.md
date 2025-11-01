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

---

### ➕➖ 8. Sobrecarga de operadores

**Sobrecarga de operadores** é um recurso de POO que permite redefinir o comportamento de operadores aritméticos e lógicos quando aplicados a objetos de classes definidas pelo programador.

### 🔮 Métodos Especiais

O comportamento dos operadores é definido pelos **métodos especiais (ou métodos mágicos)** que são implementados dentro das classes. Cada operador possui o seu próprio método especial.

**⬇️ Exemplo:**
```python
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def __gt__(self, other):  # Método especial do operador '>'
        return self.altura > other.altura  # Compara a altura entre dois objetos

clara = Pessoa("Maria Clara", 18, 60, 1.63)
joao = Pessoa("João Lucas", 19, 70, 1.73)
print("Clara é maior que João?")
print(clara > joao)  # Operador '>' sendo usado entre os objetos e chamando o seu método especial __gt__
```
No exemplo acima, o operador `>` foi usado entre dois objetos `clara` e `joao` para comparar a altura de ambos. **O operador chama o seu método especial** `__gt__` presente na classe **Pessoa** e o método **executa sua ação**, comparando a altura entre os objetos e retornando **True** ou **False**.

---

### ⚡ Principais Operadores e seus Métodos Especiais

| Operador | Método Especial |
|----------|----------------|
| `+`      | `__add__`      |
| `-`      | `__sub__`      |
| `*`      | `__mul__`      |
| `/`      | `__truediv__`  |
| `//`     | `__floordiv__` |
| `%`      | `__mod__`      |
| `**`     | `__pow__`      |
| `==`     | `__eq__`       |
| `!=`     | `__ne__`       |
| `>`      | `__gt__`       |
| `<`      | `__lt__`       |
| `>=`     | `__ge__`       |
| `<=`     | `__le__`       |
| `+=`     | `__iadd__`     |
| `-=`     | `__isub__`     |
| `*=`     | `__imul__`     |
| `/=`     | `__itruediv__` |
| `str()`  | `__str__`      |
| `repr()` | `__repr__`     |
| `len()`  | `__len__`      |
| `[]`     | `__getitem__`  |
| `in`     | `__contains__` |

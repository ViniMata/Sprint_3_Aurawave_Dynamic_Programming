import random
from datetime import datetime, timedelta

# Gerar dados simulados
def gerar_insumos(qtd=10):
    nomes = ["Reagente A", "Reagente B", "Reagente C", "Pipeta", "Luvas",
             "Seringa", "Tubo de Ensaio", "Álcool", "Gaze", "Kit Teste"]
    insumos = []
    for i in range(qtd):
        insumos.append({
            "id": i + 1,
            "nome": random.choice(nomes),
            "quantidade": random.randint(1, 50),
            "validade": (datetime.now() + timedelta(days=random.randint(1, 365))).strftime("%d/%m/%Y")
        })
    return insumos


# Estrutura de Dados: Fila
class Fila:
    def __init__(self):
        self.lista = []
        self.proximo = 0

    def insere(self, elemento):
        self.lista.append(elemento)

    def remove(self):
        if self.vazia():
            return None
        resposta = self.lista[self.proximo]
        self.proximo += 1
        return resposta

    def vazia(self):
        return self.proximo >= len(self.lista)

    def mostrar(self):
        return self.lista[self.proximo:]


# Estrutura de Dados: Pilha
class Pilha:
    def __init__(self):
        self.lista = []

    def empilha(self, elemento):
        self.lista.append(elemento)

    def desempilha(self):
        if self.vazia():
            return None
        return self.lista.pop()

    def vazia(self):
        return len(self.lista) == 0

    def mostrar(self):
        return self.lista[::-1]


# Buscas
def busca_sequencial(lista, nome):
    for item in lista:
        if item["nome"].lower() == nome.lower():
            return item
    return None

def busca_binaria(lista, nome):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        atual = lista[meio]["nome"].lower()
        if atual == nome.lower():
            return lista[meio]
        elif atual < nome.lower():
            inicio = meio + 1
        else:
            fim = meio - 1
    return None


# Ordenações
def merge_sort(lista, chave="quantidade"):
    if len(lista) > 1:
        meio = len(lista) // 2
        esq, dir = lista[:meio], lista[meio:]
        merge_sort(esq, chave)
        merge_sort(dir, chave)

        i = j = k = 0
        while i < len(esq) and j < len(dir):
            if esq[i][chave] < dir[j][chave]:
                lista[k] = esq[i]
                i += 1
            else:
                lista[k] = dir[j]
                j += 1
            k += 1
        while i < len(esq):
            lista[k] = esq[i]
            i += 1
            k += 1
        while j < len(dir):
            lista[k] = dir[j]
            j += 1
            k += 1
    return lista

def quick_sort(lista, chave="quantidade"):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x[chave] < pivo[chave]]
    iguais = [x for x in lista if x[chave] == pivo[chave]]
    maiores = [x for x in lista if x[chave] > pivo[chave]]
    return quick_sort(menores, chave) + iguais + quick_sort(maiores, chave)


# Testes
def teste_fila(insumos):
    fila = Fila()
    for item in insumos:
        fila.insere(item)
    print("=== FILA (ordem cronológica) ===")
    for f in fila.mostrar():
        print(f)


def teste_pilha(insumos):
    pilha = Pilha()
    for item in insumos:
        pilha.empilha(item)
    print("\n=== PILHA (últimos consumos primeiro) ===")
    for p in pilha.mostrar():
        print(p)


def teste_buscas(insumos):
    print("\n=== BUSCA SEQUENCIAL (Luvas) ===")
    print(busca_sequencial(insumos, "Luvas"))

    insumos_ordenados = merge_sort(insumos.copy(), "nome")
    print("\n=== BUSCA BINÁRIA (Luvas) ===")
    print(busca_binaria(insumos_ordenados, "Luvas"))


def teste_ordenacoes(insumos):
    print("\n=== MERGE SORT (por quantidade) ===")
    for o in merge_sort(insumos.copy(), "quantidade"):
        print(o)

    print("\n=== QUICK SORT (por quantidade) ===")
    for o in quick_sort(insumos.copy(), "quantidade"):
        print(o)


# Execução principal
def main():
    insumos = gerar_insumos(10)
    print(insumos)
    teste_fila(insumos)
    teste_pilha(insumos)
    teste_buscas(insumos)
    teste_ordenacoes(insumos)


if __name__ == "__main__":
    main()

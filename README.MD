# Sistema de Controle de Consumo de Insumos

Este projeto simula o controle de consumo diário de insumos (reagentes e descartáveis) em unidades de diagnóstico.  
O objetivo é organizar os dados de forma eficiente utilizando **estruturas de dados** e **algoritmos clássicos**.

---

## Estruturas Implementadas

### 1. Fila
- Representa o **consumo em ordem cronológica**.
- Cada novo insumo consumido é inserido no final da fila.
- Permite remover e consultar na ordem em que os consumos aconteceram.

### 2. Pilha
- Representa consultas em **ordem inversa** (últimos consumos primeiro).
- O último insumo consumido é o primeiro a ser consultado.

---

## Algoritmos de Busca

### Busca Sequencial
- Percorre todos os registros de consumo até encontrar o insumo procurado.
- Útil quando os dados **não estão ordenados**.

### Busca Binária
- Requer que os dados estejam **ordenados** previamente.
- Divide a lista ao meio sucessivamente até encontrar o insumo desejado.
- Mais eficiente em grandes volumes de dados.

---

## Algoritmos de Ordenação

### Merge Sort
- Algoritmo de **divisão e conquista**.
- Divide a lista em partes menores, ordena recursivamente e mescla os resultados.

### Quick Sort
- Escolhe um **pivô** e reorganiza os elementos menores à esquerda e os maiores à direita.
- Também baseado em **divisão e conquista**, sendo rápido em média.

---

## Tópico Extra: Classes em Python
- Foi utilizada a implementação de **classes para Fila e Pilha**, conforme a documentação fornecida pelo professor.
- Isso permite encapsular **comportamentos e dados** relacionados a cada estrutura, tornando o código mais organizado e legível.
- Métodos como `insere`, `remove`, `empilha` e `desempilha` foram criados para manipular os dados internamente.

---
## Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/ViniMata/Sprint_3_Aurawave_Dynamic_Programming
   cd Sprint_3_Aurawave_Dynamic_Programming


2. Execute o script em Python:

   ```bash
   python main.py
   ```

3. O programa exibirá:

   * Consumos registrados na fila (ordem cronológica).
   * Consumos registrados na pilha (ordem inversa).
   * Resultados das buscas (sequencial e binária).
   * Dados ordenados por quantidade consumida (Merge Sort e Quick Sort).

---

## Contexto no Problema

* **Fila** → Representa o consumo real dos insumos, conforme acontecem no dia a dia.
* **Pilha** → Permite consultar os últimos consumos rapidamente, útil em diagnósticos.
* **Busca Sequencial e Binária** → Auxiliam na localização de insumos específicos em relatórios.
* **Merge Sort e Quick Sort** → Permitem organizar os insumos por critérios como quantidade consumida ou validade, ajudando na previsão de reposição.


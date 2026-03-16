# Representacao de Grafo com Listas de Adjacencias - TDE1

Projeto referente a matéria *Resolução de Problemas com Grafos* que implementa um grafo direcionado, ponderado e rotulado utilizando listas de adjacências em Python. O programa permite criar e remover arestas, rotular vértices, consultar adjacentes e visualizar a matriz de adjacências.

## 1. Como executar

```zsh
python main.py
```

Para rodar a simulação de exemplo:

```zsh
python simulador.py
```

## 2. Estrutura do Repositório

```
.
├── aresta.py      # Classe Aresta, armazena o destino e o peso de uma aresta
├── vertice.py     # Classe Vertice, armazena id, rotulo e lista de adjacências
├── grafo.py       # Classe Grafo, implementa as operacoes sobre o grafo (criar/remover adjacência, imprimir matriz, setar informação, listar adjacentes)
├── main.py        # Menu interativo para manipular o grafo via terminal
├── simulador.py   # Exemplo pronto que cria um grafo de 5 locais e demonstra as operacoes
└── README.md      
```

## 3. Operações disponíveis

- cria_adjacencia(i, j, P) - cria uma aresta direcionada de i para j com peso P
- remove_adjacencia(i, j) - remove a aresta de i para j
- imprime_adjacencias() - exibe a matriz de adjacências do grafo
- seta_informacao(i, V) - define o rótulo do vértice i com a string V
- adjacentes(i, adj) - retorna a quantidade de adjacentes do vértice i e preenche o vetor adj com eles

## 4. Exemplo de uso 

Saída do programa simulador.py, que cria um grafo de 5 locais e demonstra as operacoes:

```
==================================================
   SIMULAÇÃO DE GRAFOS (MAPA)
==================================================
[*] Inicializando o mapa com 5 locais...
[*] Estabelecendo rotas e distâncias (em km/minutos)...

--------------------------------------------------
Matriz de Adjacências:
Casa            |	0	10	25	0	0
Trabalho        |	0	0	0	40	0
Faculdade       |	0	0	0	35	5
Academia        |	0	0	0	0	0
Parque          |	0	0	0	0	0
--------------------------------------------------

[Análise de Rotas] A partir da Faculdade (índice 2) você tem acesso a 2 local(is).
Índices de destino: [3, 4]
Nomes dos Lugares: ['Academia', 'Parque']
==================================================
```

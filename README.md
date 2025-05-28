# Belo Horizonte Route Agent

Este projeto implementa um **agente conversacional** especializado em sugerir rotas a pé entre restaurantes na cidade de **Belo Horizonte**, utilizando **algoritmos de busca** e **modelos de linguagem**.

O agente interage com o usuário e planeja rotas através de dois algoritmos: **Busca em Largura (BFS)** e **A**\*, utilizando um grafo gerado com dados do **OpenStreetMap** através da biblioteca **OSMnx**.

## Tecnologias utilizadas

* **Python**
* **OSMnx** — para construção e manipulação de grafos geográficos.
* **NetworkX** — para os algoritmos de busca.
* **Matplotlib** — para visualização.
* **smolagents** — para construção do agente conversacional.
* **LiteLLM** — integração com modelo de linguagem.
* **imageio** — para geração de GIFs.
* **scikit-learn** — suporte a operações diversas.

## Instalação

Requisitos: Python >= 3.8

Instale as dependências com:

```bash
pip install osmnx networkx matplotlib smolagents imageio "smolagents[litellm]" scikit-learn
```

## Funcionamento

1. **Construção do Grafo**:

   * O grafo pedestre da cidade de Belo Horizonte é gerado com OSMnx.
   * Extração de restaurantes e associação aos nós do grafo.

2. **Algoritmos de busca implementados**:

   * **BFS**: busca em largura, sem custo heurístico.
   * **A\***: busca informada, com otimização baseada em distância.

3. **Agente Conversacional**:

   * O agente recebe um prompt com o local de origem e destino.
   * Corrige nomes de restaurantes semelhantes.
   * Traça a rota com ambos os algoritmos.
   * Exibe visualização gráfica e, opcionalmente, gera um GIF animado.

4. **Análises realizadas**:

   * Comparação do número de passos e distância entre BFS e A\*.
   * Geração de gráficos comparativos.
   * Avaliação de eficiência dos algoritmos.

# Como executar

1. Clone o repositório:

2. Instale as dependências conforme acima.

3. Execute o notebook ou script principal. O agente será iniciado com:

```python
print("Olá! Eu sou um agente inteligente de rotas entre restaurantes para Belo Horizonte.")
```

4. Envie um prompt:
   Exemplos:

   * "Find a route from A Porca Voadora to A Granel with a gif"
   * "Route between Wakanda and Maria das Tranças"

5. O agente responderá com:

   * Rotas traçadas.
   * Gráfico comparativo.
   * (Opcional) GIF da rota.

# Análises gráficas:

* **Relação entre número de passos e distância** para cada algoritmo.
* **Comparação entre BFS e A**\* em termos de eficiência.

## Visualizações

* Exibição das rotas traçadas diretamente sobre o grafo.
* Geração de **GIFs animados** mostrando o progresso da rota.

## Arquitetura do projeto

* **Extração de dados** → **Construção do grafo** → **Implementação dos algoritmos** → **Criação do agente** → **Análises e visualização**.

## Licença

Este projeto é de uso acadêmico, desenvolvido para a disciplina de **Introdução à Inteligência Artificial**.

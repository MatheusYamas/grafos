from grafo import Grafo

def main():
    print("="*50)
    print("   SIMULAÇÃO DE GRAFOS (MAPA)")
    print("="*50)
    
    print("[*] Inicializando o mapa com 5 locais...")
    grafo = Grafo(5)
    
    grafo.seta_informacao(0, "Casa")
    grafo.seta_informacao(1, "Trabalho")
    grafo.seta_informacao(2, "Faculdade")
    grafo.seta_informacao(3, "Academia")
    grafo.seta_informacao(4, "Parque")
    
    print("[*] Estabelecendo rotas e distâncias (em km/minutos)...")
    grafo.cria_adjacencia(0, 1, 10)  
    grafo.cria_adjacencia(0, 2, 25)  
    grafo.cria_adjacencia(1, 3, 40)
    grafo.cria_adjacencia(2, 3, 35)
    grafo.cria_adjacencia(2, 4, 5)
    
    print("\n" + "-"*50)

    grafo.imprime_adjacencias()
    print("-"*50)
    
    vetor_adj = []
    qtd = grafo.adjacentes(2, vetor_adj)
    
    print(f"\n[Análise de Rotas] A partir da Faculdade (índice 2) você tem acesso a {qtd} local(is).")
    print(f"Índices de destino: {vetor_adj}")
    
    nomes_conectados = [grafo.vertices[idx].informacao for idx in vetor_adj]
    print(f"Nomes dos Lugares: {nomes_conectados}")
    print("="*50)

if __name__ == "__main__":
    main()
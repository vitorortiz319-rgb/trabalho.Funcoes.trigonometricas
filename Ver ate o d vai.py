import numpy as np

# ============================================
# ENCONTRANDO ONDE A ONDA COMEÇA A SUBIR
# ============================================

# Parâmetros da nossa onda senoidal
frequencia = 369  # Hz (Hertz - ciclos por segundo)
amplitude = 1     # altura da onda

# Começamos do tempo zero
tempo_atual = 0

# Tamanho de cada passo que vamos dar no tempo
passo_tempo = 0.000000000000001  # temoppo adiconado

print("=" * 60)
print("PROCURANDO ONDE A ONDA COMEÇA A SUBIR")
print("=" * 60)
print()

encontrou = False

while not encontrou:
    # ===== PASSO 1: Calcular o valor da onda neste momento =====
    # Fórmula: A * sin(2π * f * t)
    # A = amplitude
    # f = frequência
    # t = tempo
    
    angulo = 2 * np.pi * frequencia * tempo_atual
    valor_onda = amplitude * np.sin(angulo)
    
    # ===== PASSO 2: Calcular a derivada (taxa de mudança) =====
    # A derivada do seno é: A * cos(2π * f * t) * (2π * f)
    # Isso nos diz se a onda está subindo ou descendo
    
    derivada_do_seno = np.cos(angulo)
    fator_cadeia = 2 * np.pi * frequencia
    derivada = amplitude * derivada_do_seno * fator_cadeia
    
    # ===== PASSO 3: Verificar as condições =====
    # A onda começa a subir quando:
    # 1. A derivada é positiva (está subindo)
    # 2. A onda está perto de zero (saindo do ponto zero pra cima)
    
    derivada_positiva = derivada > 0
    onda_perto_de_zero = abs(valor_onda) < 0.01
    
    # ===== PASSO 4: Verificar se encontramos o ponto =====
    if derivada_positiva and onda_perto_de_zero:
        print("PONTO encontrado!")
        print()
        print(f"Tempo exato: {tempo_atual:.10f} segundos")
        print(f"Valor da onda: {valor_onda:.10f}")
        print(f"Derivada: {derivada:.10f}")
        print()
        print("Interpretação:")
        print(f"  → A onda vale {valor_onda:.6f}")
        print(f"  → Está subindo com taxa de {derivada:.6f}")
        print(f"  → Em {tempo_atual*1000:.6f} milissegundos")
        encontrou = True
    
    # Se não encontrou, avança para o próximo tempo
    tempo_atual = tempo_atual + passo_tempo

print()
print("=" * 60)


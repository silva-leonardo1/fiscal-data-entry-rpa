import pyautogui
import time
import keyboard

GATILHO_TECLA = 'f8' # Tecla pra capturar a coordenada
DELAY_POS_CAPTURA = 0.5 # Um pequeno delay para evitar capturas duplas

def get_position(prompt):
    """Função auxiliar para capturar a posição do mouse com uma tecla."""
    print(f"\n{prompt}")
    print(f"Posicione o mouse com calma e pressione '{GATILHO_TECLA}' para capturar.")
    
    # Pausa o script e espera ATÉ que a tecla seja pressionada
    keyboard.wait(GATILHO_TECLA)
    
    # Pega a posição ATUAL do mouse
    pos = pyautogui.position()
    
    print(f"Posição capturada: {pos}")
    
    # Pequena pausa para você soltar a tecla e se preparar para o próximo passo
    print(f"Aguarde {DELAY_POS_CAPTURA} seg...")
    time.sleep(DELAY_POS_CAPTURA) 
    return pos

print("--- Calibrador de Mapa de Colunas ---")
print("Vamos mapear as coordenadas X de todas as colunas.")

# Mapear Y e Y_OFFSET ---
pos1 = get_position("Posicione na PRIMEIRA CÉLULA da automação (ex: Requerimento da linha 1).")
pos2 = get_position("Posicione na MESMA COLUNA, mas na SEGUNDA LINHA (ex: Requerimento da linha 2).")

START_Y = pos1.y
Y_OFFSET = pos2.y - pos1.y

print("\n--- Mapeamento de Y Concluído ---")
print(f"START_Y = {START_Y}")
print(f"Y_OFFSET = {Y_OFFSET}")
print("----------------------------------\n")

# Mapear Colunas X
print("Agora vamos mapear as coordenadas X.")
print("Você informará uma 'palavra-chave' e depois apontará para a coluna.")
print("Use palavras-chave simples, em minúsculas.")
print("Exemplos: 'requerimento', 'endereco', 'alvara', 'terreno', 'geral', etc.")

colunas_x = {}

# Mapear colunas de texto primeiro
print("Vamos começar com as colunas de texto (Requerimento e Endereço).")

# Requerimento
req_pos = get_position("Posicione na coluna 'REQUERIMENTO' (na primeira linha, Y já foi pego).")
colunas_x['requerimento'] = req_pos.x

# Endereço
end_pos = get_position("Posicione na coluna 'ENDEREÇO' (na primeira linha).")
colunas_x['endereco'] = end_pos.x

print("\n--- Agora vamos mapear as colunas de Vistoria (onde vai o 'X') ---")

while True:
    keyword = input("\nDigite a palavra-chave (o que está nos parênteses, ex: 'terreno', 'geral')\n"
                    "ou digite 'q' para terminar: ").lower().strip()
    
    if keyword == 'q':
        break
    
    if not keyword:
        continue
        
    pos = get_position(f"Posicione na coluna que corresponde a '{keyword}' (na primeira linha).")
    colunas_x[keyword] = pos.x
    print(f"Mapeado! '{keyword}' -> X={pos.x}")

print("\n\n--- CALIBRAÇÃO CONCLUÍDA! ---")
print("Copie o bloco de configuração abaixo e cole no seu script principal:\n")
print("# --- INÍCIO DA CONFIGURAÇÃO (copiado do calibrador) ---")
print(f"START_Y = {START_Y}")
print(f"Y_OFFSET = {Y_OFFSET}")
print(f"COLUNAS_X = {colunas_x}")
print("# --- FIM DA CONFIGURAÇÃO ---")
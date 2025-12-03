import pyautogui
import pyperclip
import time
import re

# Dados transcritos
dados_para_colar = [
    "1234/56 - Rua Abcd, 123 (geral)",
    "5555/44 - Rua Efg Hijk, 321 (geral)",
    "Dado/0123/25 - Endereco Qualquer, 333 (obra)",
    # Adicione quantos dados quiser
]

# Cole aqui os valores gerados pelo script 'get_coords_full_map.py'
START_Y = 201
Y_OFFSET = 15
COLUNAS_X = {'requerimento': 91, 'endereco': 328, 'alvara': 456, 'passeio': 484, 'aparato': 515, 'terreno': 546, 'obra': 571, 'embargo': 592, 'interdicao': 656, 'interdicao atividade': 654, 'remocao': 690, 'apreensao': 725, 'ai': 766, 'geral': 803}

# --- Configurações de Tempo ---
TEMPO_ESPERA_FOCO = 5
TEMPO_ESPERA_ACAO = 0.3 # Tempo entre cliques e teclas
DURACAO_MOVER = 0.1     # Velocidade do mouse

# Padrão de Regex para extrair os 3 pedaços de informação
# Formato: "REQ" - "ENDERECO" ("TIPO")
# ^(.*?)\s*-\s*(.*?)\s*\((.*?)\)$
# Grupo 1: Requerimento
# Grupo 2: Endereço
# Grupo 3: Tipo de Vistoria
regex_pattern = re.compile(r"^(.*?)\s*-\s*(.*?)\s*\((.*?)\)$")

print(f"A automação começará em {TEMPO_ESPERA_FOCO} segundos.")
print("Por favor, clique na janela da sua planilha.")
print("Não mexa o mouse ou teclado.")
time.sleep(TEMPO_ESPERA_FOCO)

# Loop Principal
current_y = START_Y

for i, item_completo in enumerate(dados_para_colar):
    
    match = regex_pattern.match(item_completo)
    
    if not match:
        print(f"AVISO: O item '{item_completo}' está fora do formato esperado. Pulando.")
        continue
        
    requerimento, endereco, tipo_vistoria = match.groups()
    
    # Limpa a palavra-chave
    tipo_vistoria_limpo = tipo_vistoria.strip().lower()
    
    # Define o Y atual para esta linha
    current_y = START_Y + (i * Y_OFFSET)
    
    
    # Cola o requerimento
    try:
        x_req = COLUNAS_X['requerimento']
        pyautogui.moveTo(x_req, current_y, duration=DURACAO_MOVER)
        pyautogui.doubleClick()
        time.sleep(TEMPO_ESPERA_ACAO)
        pyperclip.copy(requerimento.strip())
        pyautogui.hotkey('ctrl', 'v')
        
    except KeyError:
        print("AVISO: Chave 'requerimento' não encontrada no mapa de colunas.")
        
        
    # Cola o endereço
    try:
        x_end = COLUNAS_X['endereco']
        pyautogui.moveTo(x_end, current_y, duration=DURACAO_MOVER)
        pyautogui.doubleClick()
        time.sleep(TEMPO_ESPERA_ACAO)
        pyperclip.copy(endereco.strip())
        pyautogui.hotkey('ctrl', 'v')
        
    except KeyError:
        print("AVISO: Chave 'endereco' não encontrada no mapa de colunas.")

        
    # Marca X na coluna
    if tipo_vistoria_limpo in COLUNAS_X:
        x_vistoria = COLUNAS_X[tipo_vistoria_limpo]
        pyautogui.moveTo(x_vistoria, current_y, duration=DURACAO_MOVER)
        pyautogui.doubleClick()
        time.sleep(TEMPO_ESPERA_ACAO)
        pyautogui.write("X") 
        
    else:
        print(f"AVISO: Não foi encontrada uma coluna mapeada para a chave '{tipo_vistoria_limpo}' na linha {i+1}.")

    # Pressiona Enter para confirmar a linha
    pyautogui.press('enter')
    time.sleep(TEMPO_ESPERA_ACAO / 2) # Pequena pausa

print("Automação concluída!")
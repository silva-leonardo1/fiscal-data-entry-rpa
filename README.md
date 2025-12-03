# 🚀 Automação de Lançamento de Processos Fiscais (RPA)

> **Status:** Em desenvolvimento (MVP Funcional)

Este projeto é uma ferramenta de **RPA (Robotic Process Automation)** em Python para automatizar a entrada de dados de processos administrativos e fiscais em sistemas governamentais legados.  
O objetivo é eliminar tarefas manuais repetitivas, reduzir erros e acelerar o lançamento de relatórios mensais.

---

## 🎥 Demonstração (GIF)

Abaixo você pode ver uma demonstração do robô em funcionamento:

![Image](https://github.com/user-attachments/assets/6f4bf6dd-6269-4e86-a5a2-9b085a13dd09)

---

## ⚙️ O Problema
O lançamento manual de processos fiscais exige:

- Ler strings grandes e irregulares  
- Separar dados como **número do processo**, **endereço** e **tipo de vistoria**  
- Preencher campo a campo na interface  

Isso torna o processo:

- Lento e repetitivo  
- Propenso a erros humanos  
- Desgastante fisicamente  

---

## 💡 A Solução
O script funciona como um "robô" que lê os dados brutos, interpreta a informação e controla mouse e teclado automaticamente para preencher o sistema.

### Funcionalidades:
- **Parsing inteligente com Regex**  
- **Mapeamento automático de coordenadas (calibrador)**  
- **Automação real de GUI via PyAutoGUI**  
- **Sistema de colunas dinâmico baseado em tipo de vistoria**

---

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **PyAutoGUI**
- **Pyperclip**
- **Keyboard**
- **Regex (re)**

---

## 📐 Arquivo de Calibração de Coordenadas (Incluso no Projeto)

Para que a automação funcione em QUALQUER monitor, você deve rodar o script:

### `calibrador_colunas.py`
Esse script permite registrar:

- A coordenada inicial Y da primeira linha  
- O espaçamento entre linhas (Y_OFFSET)  
- A posição X de todas as colunas (Requerimento, Endereço e tipos de vistoria)  

### Como funciona
1. Você pressiona **F8** para capturar coordenadas da tela.  
2. O script salva todas as coordenadas necessárias.  
3. Ao final, ele gera automaticamente:

```python
START_Y = ...
Y_OFFSET = ...
COLUNAS_X = {...}
```

Basta copiar esse bloco e colar dentro do seu `auto.py`.

## 🚀 Como Usar a Automação

### 1. Instalar Dependências

```bash
pip install pyautogui pyperclip keyboard
```

---

## 2. Rodar o Calibrador de Colunas

Antes de executar o robô, você precisa calibrar as coordenadas:

```
python calibrador_colunas.py
```

Ao final, ele exibirá um bloco como:

```python
START_Y = 180
Y_OFFSET = 22
COLUNAS_X = {'requerimento': 300, 'endereco': 550, 'terreno': 900, ...}
```

➡️ **Copie e cole isso no seu arquivo `auto.py`.**

---

## 3. Inserir os Dados

No script principal, coloque sua lista de processos em:

```python
dados_para_colar = [...]
```

---

## 4. Executar o Robô

```bash
python auto.py
```

⚠️ Durante a execução:

- Não mova o mouse  
- Não use teclado  
- Deixe o sistema alvo em primeiro plano  

---

## 🚧 Roadmap e Melhorias Futuras

- [ ] Reconhecimento de imagem (`locateOnScreen`) para remover dependência de coordenadas  
- [ ] Interface gráfica para colar processos sem editar código  
- [ ] Leitura de arquivos `.txt` / `.csv`  
- [ ] Logs de sucesso/erro ao final da automação  

---

## ⚠️ Disclaimer
Este software foi desenvolvido para uso interno e educativo.  
Todos os dados usados nos testes são fictícios.

---

Desenvolvido por **Leonardo Silva**

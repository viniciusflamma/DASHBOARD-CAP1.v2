
# Dashboard Principal - Sistema Integrado Agro
# main.py - Dashboard Principal Streamlit
import streamlit as st
import sys
import os

from phase2.src.main import fase2
from phase3.main import fase3
from phase5.main import fase5
from phase6.main import fase6

# Adiciona as pastas das fases ao path para importação
sys.path.append('phase1')
sys.path.append('phase2')
sys.path.append('phase4')
sys.path.append('phase7')
# Futuramente: sys.path.append('phase2'), etc.

# Importações das fases
# ========================= FASE 1 ============================
try:
    from phase1 import adicionar_dados, listar_dados, calcular_manejo, executar_analise
    FASE1_PRONTA = True
except ImportError as e:
    st.error(f"Erro ao importar Fase 1: {e}")
    FASE1_PRONTA = False

# ========================= FASE 2 ============================
try:
    from phase2.main import carregar_tabelas, executar_consultas
    FASE2_PRONTA = True
except ImportError as e:
    st.error(f"Erro ao importar Fase 2: {e}")
    FASE2_PRONTA = False

# Importação da Fase 4 (sensores)
from phase4.sensores import ler_sensores_simulado   # <<--- ADICIONADO AQUI

# Configuração da página
st.set_page_config(
    page_title="Sistema Integrado Agro",
    page_icon="🌱",
    layout="wide"
)

# Título principal
st.title("🌱 Sistema Integrado de Gestão Agrícola")
st.markdown("Dashboard consolidando todas as fases do projeto")

# Sidebar para navegação entre fases
st.sidebar.title("Navegação")
fase_selecionada = st.sidebar.radio(
    "Selecione a Fase:",
    ["Fase 1 - Dados e Cálculos", "Fase 2 - Banco de Dados", "Fase 3 - IoT", 
    "Fase 5 - Cloud", "Fase 6 - Visão Computacional",
    "Fase 7 - Integração e banco de dados"]
)

# ==================== FASE 1 ====================
if fase_selecionada == "Fase 1 - Dados e Cálculos":
    st.header("📊 Fase 1 - Dados de Plantio e Cálculos")
    
    if not FASE1_PRONTA:
        st.error("Fase 1 não está disponível. Verifique a importação.")
    else:
        # Abas para organizar as funcionalidades da Fase 1
        tab1, tab2, tab3, tab4 = st.tabs(["Adicionar Dados", "Listar Dados", "Cálculo de Manejo", "Análise R"])

        with tab1:
            st.subheader("Adicionar Novo Plantio")
            
            cultura = st.selectbox("Cultura", ["Café", "Milho"], key="cultura_add")
            insumo = st.text_input("Insumo", placeholder="Ex: fosfato, ureia...", key="insumo_add")
            
            if cultura == "Café":
                col1, col2 = st.columns(2)
                with col1:
                    largura = st.number_input("Largura (m)", min_value=0.0, value=10.0, format="%.2f", key="largura_cafe")
                with col2:
                    comprimento = st.number_input("Comprimento (m)", min_value=0.0, value=20.0, format="%.2f", key="comprimento_cafe")
                raio = None
            else:  # Milho
                raio = st.number_input("Raio (m)", min_value=0.0, value=10.0, format="%.2f", key="raio_milho")
                largura = None
                comprimento = None

            if st.button("Adicionar Dados", key="btn_add"):
                if cultura and insumo and (largura is not None or raio is not None):
                    resultado, mensagem = adicionar_dados(
                        cultura, 
                        insumo, 
                        largura=largura, 
                        comprimento=comprimento, 
                        raio=raio
                    )
                    if resultado:
                        st.success(mensagem)
                        st.json(resultado)
                    else:
                        st.error(mensagem)
                else:
                    st.warning("Preencha todos os campos!")

        with tab2:
            st.subheader("Dados Cadastrados")
            dados = listar_dados()
            if dados:
                # Formata os dados para exibição
                dados_formatados = []
                for i, dado in enumerate(dados):
                    dados_formatados.append({
                        "ID": i,
                        "Cultura": dado["cultura"],
                        "Área (m²)": f"{dado['area']:.2f}",
                        "Insumo": dado["insumo"]
                    })
                st.table(dados_formatados)
            else:
                st.info("Nenhum dado cadastrado ainda.")

        with tab3:
            st.subheader("Cálculo de Manejo de Insumos")
            dados = listar_dados()
            if dados:
                # Seleciona o plantio para cálculo
                plantio_options = [f"{i} - {d['cultura']} (Área: {d['area']}m²)" for i, d in enumerate(dados)]
                selected_plantio = st.selectbox("Selecione o plantio:", plantio_options, key="select_plantio")
                indice = int(selected_plantio.split(" - ")[0])
                
                if st.button("Calcular Manejo", key="btn_manejo"):
                    resultado = calcular_manejo(indice)
                    if "erro" not in resultado:
                        st.success("**Resultado do Cálculo:**")
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Cultura", resultado['cultura'])
                        with col2:
                            st.metric("Área", f"{resultado['area']:.2f} m²")
                        with col3:
                            st.metric("Insumo", resultado['insumo'])
                        
                        st.info(f"**Quantidade Necessária:** {resultado['quantidade_insumos']:.2f} {resultado['unidade']}")
                    else:
                        st.error(resultado["erro"])
            else:
                st.info("Adicione dados primeiro na aba 'Adicionar Dados'.")

        with tab4:
            st.subheader("Análise Estatística e Clima (R)")
            st.info("Esta análise calcula estatísticas dos dados e consulta a API meteorológica")
            
            if st.button("Executar Análise R", key="btn_r"):
                with st.spinner("Executando análise R..."):
                    resultado = executar_analise()
                
                st.subheader("Resultado da Análise:")
                st.text_area("", resultado, height=200, key="resultado_r")

# ==================== FASE 2 ====================

elif fase_selecionada == "Fase 2 - Banco de Dados":
    fase2()

# ==================== FASE 3 ====================
elif fase_selecionada == "Fase 3 - IoT":
    fase3()

# ==================== FASE 5 ====================
elif fase_selecionada == "Fase 5 - Cloud":
    st.header("☁️ Fase 5 - Cloud Computing")

    st.markdown("""
    A Fase 5 é responsável pela parte de **Cloud Computing** do projeto,
    incluindo deploy, infraestrutura em nuvem, containers, serviços gerenciados
    e integração com o backend.
    """)

    fase5()

# ==================== FASE 6 ====================
elif fase_selecionada == "Fase 6 - Visão Computacional":

    st.header("👁️ Fase 6 - Visão Computacional")

    st.markdown("""
    A Fase 6 é responsável por implementar recursos de **Visão Computacional** no projeto,
    como análise de imagens, detecção de pragas, classificação de folhas ou reconhecimento
    de padrões visuais em plantações.
    """)

    fase6()

# ============================
# FASE 7 – Integração com Banco de Dados Oracle
# ============================

elif fase_selecionada == "Fase 7 - Integração e banco de dados":
    st.header("🗄️ Fase 7 - Integração com Banco de Dados Oracle")

    st.markdown("### 🔌 Conexão e Consulta de Dados")

    st.markdown("""
    Nesta fase, o sistema se conecta diretamente ao banco Oracle para consultar:

    - 📡 **Registros dos sensores (T_REGISTROS)**  
    - 🐛 **Alertas de pragas (ALERTAS_PRAGAS)**  
    - ⚙️ **Configurações gerais do sistema (T_CONFIGURACOES)**  

    Esses dados são fornecidos pelo módulo oficial do time responsável pela Fase 2.
    """)

    # --- IMPORTA OS MÉTODOS DA PHASE7 ---
    from phase7.db_queries import (
        get_registros_sensores,
        get_alertas_pragas,
        get_configuracoes
    )

    st.divider()

    # ==============================
    #     REGISTROS DOS SENSORES
    # ==============================
    st.subheader("📡 Últimos Registros dos Sensores")

    if st.button("Carregar Dados dos Sensores"):
        registros = get_registros_sensores()

        if registros:
            st.success("Dados carregados com sucesso!")
            st.dataframe(registros)
        else:
            st.error("Não foi possível carregar os registros ou a tabela está vazia.")

    st.divider()

    # ==============================
    #     ALERTAS DE PRAGAS
    # ==============================
    st.subheader("🐛 Alertas de Pragas Registrados")

    if st.button("Carregar Alertas de Pragas"):
        alertas = get_alertas_pragas()

        if alertas:
            st.success("Alertas carregados com sucesso!")
            st.dataframe(alertas)
        else:
            st.warning("Nenhum alerta encontrado ou erro ao consultar o banco.")

    st.divider()

    # ==============================
    #     CONFIGURAÇÕES DO SISTEMA
    # ==============================
    st.subheader("⚙️ Configurações Gerais do Sistema")

    if st.button("Mostrar Configurações"):
        conf = get_configuracoes()

        if conf:
            st.success("Configurações carregadas!")
            st.json({
                "ID da Configuração": conf[0],
                "Limite de Umidade (%)": conf[1],
                "pH Mínimo": conf[2],
                "pH Máximo": conf[3]
            })
        else:
            st.error("Não foi possível carregar as configurações.")


# Rodapé
st.markdown("---")
st.markdown("**Sistema Integrado Agro** - Fase 7 | Desenvolvido por [Nome do Time]")

# Status do sistema na sidebar
st.sidebar.markdown("---")
st.sidebar.subheader("Status do Sistema")
if FASE1_PRONTA:
    st.sidebar.success("✅ Fase 1 - Pronta")
    st.sidebar.success("✅ Fase 2 - Pronta")
    st.sidebar.success("✅ Fase 3 - Pronta")
    st.sidebar.success("✅ Fase 5 - Pronta")
    st.sidebar.success("✅ Fase 6 - Pronta")
else:
    st.sidebar.error("❌ Fase 1 - Com problemas")



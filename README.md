<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600&display=swap" rel="stylesheet">

<p align="center" 
   style="
        font-family: 'Montserrat', sans-serif;
        font-size: 28px;
        color: #5C0011;
        font-weight: 600;
        padding: 12px 20px;
        border: 2px solid #5C0011;
        border-radius: 10px;
        display: inline-block;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.25);
        background: #fff;
   ">
    FIAP - Faculdade de Informática e Administração Paulista
</p>


<p align="center">
<a href= "https://www.fiap.com.br/"><img src="agro_system/assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

## Nome do projeto
####  • PROJETO FASE  7 – A CONSOLIDAÇÃO DE UM SISTEMA

## Nome do grupo
#### • Equipe Fiap

## 👨‍🎓 Integrantes:
- <a href="endrewalves42@gmail.com"> Endrew Alves dos Santos  • RM563646</a>
- <a href="nisoxds@gmail.com"> Vinícius Divino dos Santos  • RM566269</a>
- <a href="carlos.souza004@gmail.com"> Carlos Eduardo de Souza  • RM566487</a>
- <a href="esteves.tayna96@gmail.com"> Tayná Esteves  • RM562491</a>
- <a href="fontesjoaovittor@gmail.com"> João Vittor Fontes  • RM565999</a>


## 👩‍🏫 Professores:
#### Tutor(a) 
- <a href="profandre.chiovato@fiap.com.br">André Godoi Chiovato</a>
#### Coordenador(a)
- <a href="proflucas.moreira@fiap.com.br">Lucas Gomes Moreira</a>

## 📜 Descrição

Este projeto apresenta a consolidação de um ecossistema inteligente de gestão, inicialmente desenvolvido para o agronegócio, mas estruturado de forma totalmente flexível para ser adaptado a qualquer outro setor da economia, bastando inserir os dados correspondentes a cada domínio operacional.

A solução integra sensores IoT, análise de séries temporais, visão computacional, inteligência artificial e dashboards interativos, formando um sistema unificado capaz de monitorar ambientes, interpretar informações críticas e apoiar decisões estratégicas.

Além do uso no campo, o sistema também incorpora uma camada avançada de análise industrial, permitindo detectar comportamentos anormais em equipamentos por meio de algoritmos especializados em anomalias temporais, garantindo segurança, eficiência e continuidade das operações.

# 🎯 Objetivos do Sistema Consolidado

    • Reduzir falhas inesperadas por meio de monitoramento contínuo e análises preditivas.

    • Identificar anomalias em tempo real, tanto na lavoura quanto em ambientes industriais.

    • Fornecer recomendações inteligentes baseadas em algoritmos de IA e modelos preditivos.

    • Integrar sensores físicos, inteligência artificial e dashboards em uma arquitetura única e escalável.

# 📁 Estrutura de pastas

## 🌱Estrutura do Repositório

### 📘 phase1 — Preparação Inicial
Contém scripts e rotinas necessárias para organizar os datasets brutos, remover inconsistências básicas e padronizar formatos.

### 📙 phase2 — Limpeza e Tratamento de Dados
Envolve tratamento de outliers, normalização, substituição de valores ausentes e ajustes finos na integridade do dataset.

### 📗 phase3 — Feature Engineering
Geração de novas variáveis, enriquecimento dos dados e transformações avançadas necessárias para melhorar o modelo.

### 📕 phase4 — Modelagem
Modelos preliminares, testes exploratórios e validação cruzada inicial.

### 📔 phase5 — Otimização
Overfitting control, tuning de hiperparâmetros e melhorias na performance dos modelos.

### 📓 phase6 — Avaliação
Relatórios, métricas, gráficos comparativos e documentação dos resultados.

### 📒 phase7 — Deploy / Pipeline Final
Scripts de entrega final, pipeline automatizado, integração com dashboards e APIs.

---

## 📂 Arquivos Gerais

- **README.md** — Documentação oficial do projeto  
- **main.py** — Script principal, coordenando todo o pipeline  
- **tst.py** — Arquivos de teste/diagnóstico  

## 📊 Bases de Dados

| Arquivo | Descrição |
|--------|-----------|
| `cocoa.csv` | Dados sobre produção de cacau |
| `oil_palm.csv` | Informações sobre a cultura de palma de óleo |
| `rice.csv` | Indicadores e métricas do arroz |
| `rubber.csv` | Dados da produção de borracha |

## 🤖 Modelo
```
<div style="
    background: linear-gradient(135deg, #000000, #1a001f, #ff007f);
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 0 20px #ff007f88;
    font-family: 'Segoe UI', Tahoma, sans-serif;
    color: #ffffff;
    border: 2px solid #ff007f;
    background-image: url('data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' width=\'200\' height=\'200\'><rect width=\'100%\' height=\'100%\' fill=\'none\'/><circle cx=\'50\' cy=\'50\' r=\'3\' fill=\'%23ff00aa33\'/><circle cx=\'150\' cy=\'150\' r=\'2\' fill=\'%23ff00aa22\'/></svg>');
    background-size: 200px;
">

    <marquee behavior="alternate" scrollamount="5">
        <h1 style="font-size: 36px; color: #ff4dc4; text-shadow: 0 0 10px #ff4dc4;">
            🚀✨ ESTRUTURA DO PROJETO — AGRO SYSTEM ✨🚀
        </h1>
    </marquee>

    <pre style="
        font-size: 16px;
        background: #0a0a0a88;
        padding: 20px;
        border-radius: 12px;
        overflow-x: auto;
        border: 1px solid #ff4dc4;
        box-shadow: inset 0 0 15px #ff008855;
        color: #ffb3e6;
        white-space: pre;
    ">

📦 <span style="color:#ff4dc4;">agro_system/</span>
├── 📁 <span style="color:#ff66cc;">phase1/</span>        — Pré-processamento inicial dos dados e organização das bases.
├── 📁 <span style="color:#ff66cc;">phase2/</span>        — Limpeza avançada, tratamento de outliers e padronização.
├── 📁 <span style="color:#ff66cc;">phase3/</span>        — Feature Engineering e geração de variáveis derivadas.
├── 📁 <span style="color:#ff66cc;">phase4/</span>        — Modelagem inicial, testes de algoritmos e validações.
├── 📁 <span style="color:#ff66cc;">phase5/</span>        — Treinamento avançado e otimização de hiperparâmetros.
├── 📁 <span style="color:#ff66cc;">phase6/</span>        — Avaliação de performance, métricas, gráficos e relatórios.
├── 📁 <span style="color:#ff66cc;">phase7/</span>        — Deploy, integração, pipeline final e automação do sistema.

├── 📄 <span style="color:#ff99dd;">README.md</span>              — Documentação geral do projeto.
├── 📄 <span style="color:#ff99dd;">main.py</span>                — Script principal do pipeline do Agro System.
├── 📄 <span style="color:#ff99dd;">tst.py</span>                 — Arquivos de testes rápidos e utilitários.

├── 📄 <span style="color:#ffb3e6;">cocoa.csv</span>              — Base de dados referente à cultura de cacau.
├── 📄 <span style="color:#ffb3e6;">oil_palm.csv</span>           — Base relacionada ao cultivo de dendê (oil palm).
├── 📄 <span style="color:#ffb3e6;">rice.csv</span>               — Dados sobre produção e indicadores do arroz.
├── 📄 <span style="color:#ffb3e6;">rubber.csv</span>             — Base referente à cultura da borracha natural.

├── 📦 <span style="color:#ff4dc4;">modelo_caneca_pote.h5</span>  — Modelo treinado em Deep Learning (HDF5).
    </pre>
</div>

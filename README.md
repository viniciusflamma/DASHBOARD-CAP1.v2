<p align="center" style="font-size: 26px; color: #5C0011; font-weight: bold; margin: 0;">
    FIAP - Faculdade de Informática e Administração Paulista
</p>

<img width="1807" height="517" alt="image" src="https://github.com/user-attachments/assets/16bdb7ba-b770-4151-845d-221179f57a2b" />


## Nome do projeto
##  • PROJETO FASE  7 – A CONSOLIDAÇÃO DE UM SISTEMA

## Nome do grupo
## • Equipe Fiap

## 👨‍🎓 Integrantes:
- <a href="https://www.linkedin.com/in/endrew-alves-dos-santos-2ab783336/"> Endrew Alves dos Santos  • RM563646</a>
- <a href="nisoxds@gmail.com"> Vinícius Divino dos Santos  • RM566269</a>
- <a href="https://www.linkedin.com/in/carlos-eduardo-b40b932a/"> Carlos Eduardo de Souza  • RM566487</a>
- <a href="esteves.tayna96@gmail.com"> Tayná Esteves  • RM562491</a>
- <a href="https://www.linkedin.com/in/jo%C3%A3ovittorfontes/"> João Vittor Fontes  • RM565999</a>


## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="profandre.chiovato@fiap.com.br">André Godoi Chiovato</a>
### Coordenador(a)
- <a href="proflucas.moreira@fiap.com.br">Lucas Gomes Moreira</a>

## 📜 Descrição

Este projeto apresenta a consolidação de um ecossistema inteligente de gestão, inicialmente desenvolvido para o agronegócio, mas estruturado de forma totalmente flexível para ser adaptado a qualquer outro setor da economia, bastando inserir os dados correspondentes a cada domínio operacional.

A solução integra sensores IoT, análise de séries temporais, visão computacional, inteligência artificial e dashboards interativos, formando um sistema unificado capaz de monitorar ambientes, interpretar informações críticas e apoiar decisões estratégicas.

Além do uso no campo, o sistema também incorpora uma camada avançada de análise industrial, permitindo detectar comportamentos anormais em equipamentos por meio de algoritmos especializados em anomalias temporais, garantindo segurança, eficiência e continuidade das operações.

# 🎯 Objetivos do Sistema Consolidado

O projeto busca unificar e entregar um sistema robusto, capaz de:

    • Reduzir falhas inesperadas por meio de monitoramento contínuo e análises preditivas.

    • Identificar anomalias em tempo real, tanto na lavoura quanto em ambientes industriais.

    • Fornecer recomendações inteligentes baseadas em algoritmos de IA e modelos preditivos.

    • Integrar sensores físicos, inteligência artificial e dashboards em uma arquitetura única e escalável.

# 📁 Estrutura de pastas

## 🌱 Fase 1 — Cálculo de Manejo

O sistema calcula automaticamente a quantidade de insumo necessária para uma área baseada em:
-  • Cultura plantada
-  • Tipo de insumo (ex.: ureia, fósforo, NPK etc.)
-   • Dimensões da área (largura × comprimento)
-   • O cálculo de manejo determina quanto insumo o produtor deve usar e, consequentemente, comprar. 
    
Cada cultura exige quantidades diferentes, mesmo para áreas iguais.

## 🐛 Fase 2 — Diagnóstico Climático e Risco de Pragas

O sistema avalia o risco de pragas usando:
-   • Cultura selecionada
-   • Cidade informada
-   • Dados climáticos obtidos via API em tempo real

A lógica compara:
-   • Temperatura atual
-   • Parâmetros da cultura

E retorna diagnósticos, como:
-   • Alto risco
-   • Risco moderado
-   •  Baixo risco

## 💧 Fase 3 — Automação da Bomba de Água

A bomba é acionada automaticamente com base na saúde do solo.

Parâmetros informados pelo usuário:
-   •  pH
-   • Umidade
-   • Presença de fósforo
-   • Presença de potássio

Condições para ligar a bomba:
-   • Umidade abaixo de 30%
-   • pH entre 5 e 7
-   • Solo contém fósforo e potássio
    
    Caso um dos requisitos falhe, a bomba permanece desligada.

## 🤖 Fase 5 — Machine Learning para Produtividade

Modelos utilizados:
-   • XGBoost
-   •  Random Forest
-   • Regressão Linear

Objetivo:
-   • Identificar padrões entre clima, umidade, chuva e época do ano
-   •  Prever produtividade agrícola
-   • Encontrar condições ótimas ou prejudiciais à produção

Dataset: fornecido pela FIAP, com variáveis climáticas e resultados históricos de produção.

## 🖼️ Fase 6 — Visão Computacional com CNN

Sistema de classificação de imagens para identificar:
-   • Caneca
-   • Pote

Dataset:
-   • Imagens diversas
-   • Arquivos TXT contendo as bounding boxes (coordenadas dos objetos)

A CNN aprende a reconhecer padrões visuais e realiza a classificação final.


# 🤖 Modelo

<img width="816" height="372" alt="image" src="https://github.com/user-attachments/assets/43fd6bac-f92a-4364-87b0-79293ebb666b" />



# 🔷 Fluxograma Geral

<img width="586" height="592" alt="image" src="https://github.com/user-attachments/assets/fa7bae97-e3a6-4d00-819c-7518b77da6a9" />


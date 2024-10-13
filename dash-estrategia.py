import streamlit as st
import pandas as pd
import plotly.express as plotly_express
import plotly.graph_objects as go
from sqlalchemy.util import ordered_column_set
from streamlit import title

# Configurar o layout da página
st.set_page_config(layout="wide")

df = pd.read_csv("estrategias.csv", sep=";", decimal=",")
print(df)

###### Indicador 1 - Consultas ######
consulta_plano_estrategico = df.loc[df['nomeEstrategia'] == 'Plano estrategico conjunto para diagnosticos e formacao']
consulta_plano_estrategico.set_index('index', inplace=True)
selected_columns_plano_estrategico = consulta_plano_estrategico[['mes','valor', 'nomeEstrategia']]

consulta_financiamento_estudantil = df.loc[df['nomeEstrategia'] == 'Consolidar financiamento estudantil']
consulta_financiamento_estudantil.set_index('index', inplace=True)
selected_columns_financiamento_estudantil = consulta_financiamento_estudantil[['mes','valor', 'nomeEstrategia']]

###### Indicador 2 - Consultas ######

consulta_iniciacao_docencia = df.loc[df['nomeEstrategia'] == 'Ampliar programa de iniciacao a docencia']
consulta_iniciacao_docencia.set_index('index', inplace=True)
selected_columns_iniciacao_docencia = consulta_iniciacao_docencia[['mes','valor', 'nomeEstrategia']]

consulta_plataforma_digital = df.loc[df['nomeEstrategia'] == 'Expandir plataforma digital de matriculas']
consulta_plataforma_digital.set_index('index', inplace=True)
selected_columns_plataforma_digital = consulta_plataforma_digital[['mes','valor', 'nomeEstrategia']]

###### Indicador 3 - Consultas ######

consulta_formacao_especiais = df.loc[df['nomeEstrategia'] == 'Programas de formacao para areas especiais']
consulta_formacao_especiais.set_index('index', inplace=True)
selected_columns_formacao_especiais = consulta_formacao_especiais[['mes','valor', 'nomeEstrategia']]

consulta_reforma_curricular = df.loc[df['nomeEstrategia'] == 'Reforma curricular dos cursos de licenciatura']
consulta_reforma_curricular.set_index('index', inplace=True)
selected_columns_reforma_curricular = consulta_reforma_curricular[['mes','valor', 'nomeEstrategia']]

###### Indicador 4 - Consultas ######

consulta_praticas_ensino = df.loc[df['nomeEstrategia'] == 'valorizar as praticas de ensino e os estagios']
consulta_praticas_ensino.set_index('index', inplace=True)
selected_columns_praticas_ensino = consulta_praticas_ensino[['mes','valor', 'nomeEstrategia']]

consulta_cursos_programas_especiais = df.loc[df['nomeEstrategia'] == 'Implementar cursos e programas especiais para formacao de docentes']
consulta_cursos_programas_especiais.set_index('index', inplace=True)
selected_columns_cursos_programas_especiais = consulta_cursos_programas_especiais[['mes','valor', 'nomeEstrategia']]

##### Gráficos ####

#### Grafico Indicador A ####

multi = '''**INDICADOR 15A** - Proporção de docências da educação infantil com professores cuja formação superior está adequada à área de conhecimento que lecionam.
'''
st.markdown(multi)
grafico_plano_estrategico = plotly_express.line(selected_columns_plano_estrategico, x='mes', y='valor', color='nomeEstrategia', title='Plano estrategico conjunto para diagnosticos e formacao')
grafico_financiamento_estudantil = plotly_express.line(selected_columns_financiamento_estudantil, x='mes', y='valor', color='nomeEstrategia', title='Consolidar financiamento estudantil')


#st.plotly_chart(fig)
col1, col2, = st.columns(2)

with col1:
    st.plotly_chart(grafico_plano_estrategico )

with col2:
    st.plotly_chart(grafico_financiamento_estudantil)


#### Grafico Indicador B ####

multi = '''**INDICADOR 15B** - Proporção de docências dos anos iniciais do ensino fundamental com professores cuja formação
superior está adequada à área de conhecimento que lecionam.
'''
st.markdown(multi)
grafico_iniciacao_docencia = plotly_express.line(selected_columns_iniciacao_docencia, x='mes', y='valor', color='nomeEstrategia', title='Ampliar programa de iniciacao a docencia')
grafico_plataforma_digital = plotly_express.line(selected_columns_plataforma_digital, x='mes', y='valor', color='nomeEstrategia', title='Expandir plataforma digital de matriculas')

#st.plotly_chart(fig)
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(grafico_iniciacao_docencia)

with col2:
    st.plotly_chart(grafico_plataforma_digital)


#### Grafico Indicador C ####

multi = '''**INDICADOR 15C** - Proporção de docências dos anos finais do ensino fundamental com professores cuja formação
superior está adequada à área de conhecimento que lecionam.
'''
st.markdown(multi)

grafico_formacao_especiais = plotly_express.line(selected_columns_formacao_especiais, x='mes', y='valor', color='nomeEstrategia', title='Programas de formacao para areas especiais')
grafico_reforma_curricular = plotly_express.line(selected_columns_reforma_curricular, x='mes', y='valor', color='nomeEstrategia', title='Reforma curricular dos cursos de licenciatura')

#st.plotly_chart(fig)
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(grafico_formacao_especiais)

with col2:
    st.plotly_chart(grafico_reforma_curricular)


#### Grafico Indicador D ####

multi = '''**INDICADOR 15D** - Proporção de docências do ensino médio com professores cuja formação superior está adequada
à área de conhecimento que lecionam.
'''
st.markdown(multi)

grafico_praticas_ensino = plotly_express.line(selected_columns_praticas_ensino, x='mes', y='valor', color='nomeEstrategia', title='valorizar as praticas de ensino e os estagios')
grafico_cursos_programas_especiais = plotly_express.line(selected_columns_cursos_programas_especiais, x='mes', y='valor', color='nomeEstrategia', title='Implementar cursos e programas especiais para formacao de docentes')

#st.plotly_chart(fig)
col1, col2= st.columns(2)

with col1:
    st.plotly_chart(grafico_praticas_ensino)

with col2:
    st.plotly_chart(grafico_praticas_ensino)
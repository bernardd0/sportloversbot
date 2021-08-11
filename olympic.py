from datetime import date
import pandas as pd
import dataframe_image as dfi
from prettytable import PrettyTable
import os

today = date.today().strftime('%Y-%m-%d')
temp_path = "imgs/output.png"
path_olympic_today = os.path.join("data/", hoje+".csv")
df_olympics_today = pd.read_csv(path_olympic_today, index_col=0).set_index()

sports_today = df_olympics_today.Esporte.unique()
sport_modalities = df_olympics_today['Mod.'].unique()

# /esportes - lista de esportes que terão eventos no dia
def listar_esportes():
    lista_esportes = ""
    for i in range(len(sports_today)):
        lista_esportes = lista_esportes + "{} - {}\n".format(i+1, sports_today)

# /modalidades - lista de modalidades que terão eventos no dia
def listar_modalidades():
    lista_modalidades = ""
    for i in range(len(sport_modalities)):
        lista_modalidades = lista_modalidades + "{} - {}\n".format(i+1, sports_modalities)

# /horarioesporte - lista de horários por esporte
def horarios_por_esporte(sports_indice):
    horarios = df_olympics_today[df_olympics_today.Esporte == sports_today[sport_indice-1].reset_index()]
    horarios.index = horarios.index+1
    dfi.export(horarios, temp_path)
    return horarios

def format_for_print2(df):
    table = PrettyTable(list(df.columns))
    for row in df.itertuples():
        table.add_row(row[1:])
    return str(table)

# /horariosmodalidade - lista de horarios por modalidade
def horarios_por_modalidade(mods_indice):
    horarios = df_olympics_today[df_olympics_today['Mod.'] == sport_modalities[mods_indice-1].reset_index()]
    horarios.index = horarios.index+1
    dfi.export(horarios, temp_path)
    return horarios

# /help - lista todos os comandos
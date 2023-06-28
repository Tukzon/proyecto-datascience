import pandas as pd
import os

def obtenerpos(id):
    arr=[]
    dataframe_path = os.path.join(os.path.dirname(__file__), '.', 'ubicaciones_unicas.csv')
    dataframe = pd.read_csv(dataframe_path,header=0)
    fila = dataframe.loc[dataframe['ID'] == id]
    arr.append(fila['x_pos_terminal'].values[0])
    arr.append(fila['y_pos_terminal'].values[0])
    return arr
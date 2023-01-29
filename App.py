import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import plotly.figure_factory as ff
#import plotly.express as px
#import time
from PIL import Image


# Configuration de la page 

st.set_page_config(
    page_title="Mon logement Nexity",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Importation des données
@st.cache
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/EuniceKOFFI/ProjetPython/main/data/dataf.csv')
    data = data.drop('Unnamed: 0', axis=1)
    return data
data = load_data()

#--------------------------------------------------------------Sélecteurs dans la partie gauche----------------------------------------------------
# Ajouter des sélecteurs dans une barre sur le côté
add_tile = st.sidebar.subheader("Sélection de filtres")

# Je modifie la table avec les diffécrents sélecteurs

# Type de logement
add_selectbox = st.sidebar.selectbox(
    'Quel type de Logement recherchez-vous ?',
    ("Appartement", "Appartement étudiant", "Appartement en résidence sénior", "Maison")
)

# Loyer maximum
loyer_max = st.sidebar.number_input("Loyer maximum", min_value=500, max_value=10000, value=500, step=200)

# Cave terrain balcon terrasse
add_cave = st.sidebar.selectbox(
    'Cave',
    ("Oui", "Non")
)

add_balcon = st.sidebar.selectbox(
    'balcon',
    ("Oui", "Non")
)

add_terrasse = st.sidebar.selectbox(
    'terrasse',
    ("Oui", "Non")
)

# Nouvelle table 

table = data[ (data['Type'] == add_selectbox) & (data['loyer'] <= loyer_max ) & (data['Cave'] == add_cave ) & (data['Balcon'] == add_balcon ) & (data['Terrasse'] == add_terrasse )]

#---------------------------------------------------------------Résultats des recherches dans la partie droite ----------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------
st.markdown("<h1 style='font-family:Lucida Caligraphy;font-size:60px;color:DarkSlateBlue;text-align: center;'> Bienvenue sur notre site de logement </h1>", unsafe_allow_html=True)

st.image('https://github.com/EuniceKOFFI/ProjetPython/raw/main/data/logement1.jpg',use_column_width ='always')

st.markdown("<h1 style='font-family:Lucida Caligraphy;font-size:40px;color:DarkSlateBlue;text-align: center;'> Les résultats de vos recherches </h1>", unsafe_allow_html=True)

nombre = table.shape[0]
#st.write(nombre)

if nombre == 0 :
    st.write("Désolé, .... Nous n'avons trouvé aucun résultats correspondant aux critères que vous avez sélctionné. \n Veuillez modifier les critères de vos recherches")
    st.image('https://github.com/EuniceKOFFI/ProjetPython/raw/main/data/excuses-so-sorry.gif')
    st.write("N'hésitez pas à revenir sur notre site, les offres sont constamment mises à jour en fonction des disponibilités et des offres.")
else :
    st.write(f"Nous avons trouvé {nombre} résultats correspondants à vos recherches.")

    # Afficher les données uniquement si l'utilisateur souhaite les voir
    if st.checkbox('Afficher la base de données'):
        st.subheader('Base de données')
        st.write(table)

    # Faire deux colonnes 
    left_column, right_column = st.columns(2)

    with left_column:
        st.write("Vous cherchez un logement avec ces caractéristiques : ")
        left_column.write(f"Type de logement : {add_selectbox}")
        left_column.write(f"Loyer maximum : {loyer_max} €")
        left_column.write(f"Avec cave : {add_cave}")
        left_column.write(f"Avec balcon : {add_balcon}")
        left_column.write(f"Avec terrasse : {add_terrasse}")
        
    loyer_moyen = np.round(table["loyer"].mean(), 2)
    loyer_max   = np.round(table["loyer"].max(), 2)
    loyer_min   = np.round(table["loyer"].min(), 2)
    nb_pieces_moyen = int(table["nb_piece"].mode())

    right_column.write("Les caractériques des logements dont nous disposons pour ce type sont :")
    right_column.write(f"Loyer moyen : {loyer_moyen} €")
    right_column.write(f"Loyer maximum : {loyer_max} €")
    right_column.write(f"Loyer minimum : {loyer_min} €")
    right_column.write(f"Nombre de pièces : {nb_pieces_moyen} pièces")

     #Afficher le nombre de logement disponible en fonction du département
    logement_count = table.groupby("Departement").size()
    st.markdown("<h1 style='font-family:Lucida Caligraphy;font-size:30px;color:DarkSlateBlue;text-align: center;'> Nombre de logements disponibles en fonction des départements </h1>", unsafe_allow_html=True)
    st.bar_chart(logement_count)
    
    st.markdown("<h1 style='font-family:Lucida Caligraphy;font-size:30px;color:DarkSlateBlue;text-align: center;'> Affichez les informations d'un logement spécifique </h1>", unsafe_allow_html=True)
    index = table.index.tolist()
    
    st.markdown("<h1 style='font-family:cursive;font-size:15px;color:Red;font-style: italic;text-align: center;'> Choisissez le numéro d'un logement pour obtenir plus de détails </h1>", unsafe_allow_html=True)
        
    index_selected = st.selectbox(
    "",
    index)
    
    
    table_selected = table[table.index==index_selected]
    
    log_description   = table_selected['Description'].tolist()
    log_dep           = table_selected['Dep'].tolist()
    log_charges       = table_selected['charges'].tolist()
    log_superficie    = table_selected['Superficie'].tolist()
    log_loyer         = table_selected['loyer'].tolist()
    log_nb_piece      = table_selected['nb_piece'].tolist()
    log_garantie      = table_selected['Garantie'].tolist()
    log_etage         = table_selected['Etage'].tolist()
    log_ascenseur     = table_selected['Ascenseur'].tolist()
    log_WC_separe     = table_selected['WC_separe'].tolist()
    log_cave          = table_selected['Cave'].tolist()
    log_interphone    = table_selected['Interphone'].tolist()
    log_terrain       = table_selected['Terrain_extérieur'].tolist()
    log_terrasse      = table_selected['Terrasse'].tolist()
    log_balcon        = table_selected['Balcon'].tolist()
    log_stationnement = table_selected['stationnement'].tolist()
    log_chauffage     = table_selected['Chauffage'].tolist()
    
    # st.write('Hello, *World!* :sunglasses:')
    st.write(log_description[0])
    left_column_side, right_column_side = st.columns(2)
    left_column_side.write(f":round_pushpin: :world_map: Localisation : {log_dep[0]}")
    left_column_side.write(f":moneybag: Loyer CC : {log_loyer[0]} €")
    left_column_side.write(f":moneybag: Charges : {log_charges[0]} €")
    left_column_side.write(f":moneybag: Garantie : {log_garantie[0]} €")
    left_column_side.write(f":bed: Nombre de pièces : {log_nb_piece[0]}")

    #left_column_side.write(f":office: N° Etage : {log_etage[0]}")
    left_column_side.write(f":information_source: Ascenceur : {log_ascenseur[0]}")
    
    
    right_column_side.write(f":toilet: WC séparé :  {log_WC_separe[0]}")
    right_column_side.write(f":information_source:  Cave : {log_cave[0]}")
    right_column_side.write(f":phone: Interphone : {log_interphone[0]}")
    right_column_side.write(f":information_source:  Terrain extérieur : {log_terrain[0]}")
    right_column_side.write(f":information_source:  Terrasse : {log_terrasse[0]}")
    right_column_side.write(f":information_source:  Balcon : {log_balcon[0]}")
    #right_column_side.write(f":car: Parking : {log_stationnement[0]}")
    #right_column_side.write(f":thermometer: Chauffage : {log_chauffage[0]}")

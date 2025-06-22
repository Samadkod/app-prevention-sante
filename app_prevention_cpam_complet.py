
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Configuration
st.set_page_config(page_title="Prévention Santé - CPAM", layout="wide")
st.title("📊 Application Prévention Santé & Relances - CPAM")

# Chargement des données
@st.cache_data
def load_data():
    df = pd.read_csv("donnees_prevention_cpam.csv")
    return df

df = load_data()

# Onglets
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Accueil", "🔎 Exploration", "📈 KPI", "🧠 Scoring", "🧭 Recommandations"])

# 🏠 Accueil
with tab1:
    st.header("Contexte & Objectif")
    st.markdown("""
    Cette application interactive s'inscrit dans la stratégie **Aller Vers** de la CPAM.
    Elle vise à :
    - Suivre la participation des assurés aux campagnes de prévention santé
    - Identifier ceux qui risquent de ne pas répondre
    - Aider les équipes à cibler les relances

    **Les données ici sont simulées à des fins de démonstration.**
    """)

# 🔎 Exploration
with tab2:
    st.header("Exploration des données")
    st.subheader("Répartition des âges")
    st.plotly_chart(px.histogram(df, x="Âge", nbins=20), use_container_width=True)

    st.subheader("Participation après relance")
    fig = px.histogram(df, x="Participation_post_relance", color="Sexe",
                       barmode="group", title="Taux de participation post-relance")
    fig.update_xaxes(tickvals=[0,1], ticktext=["Non", "Oui"])
    st.plotly_chart(fig, use_container_width=True)

# 📈 KPI
with tab3:
    st.header("Indicateurs clés")
    col1, col2 = st.columns(2)
    col1.metric("🎯 Taux de participation post-relance", f"{df['Participation_post_relance'].mean():.2%}")
    col2.metric("📉 Score isolement moyen", f"{df['Score_isolement'].mean():.2f}")

    st.subheader("Score isolement par sexe")
    st.plotly_chart(px.box(df, x="Sexe", y="Score_isolement", color="Sexe"), use_container_width=True)

# 🧠 Scoring
with tab4:
    st.header("Modèle de prédiction du risque")
    st.markdown("""
    🎯 **Pourquoi ce modèle ?**  
    Il nous aide à estimer la probabilité qu’un assuré **ne participe pas** à une action de prévention, **même après relance**.

    📊 Le modèle est basé sur plusieurs facteurs :
    - L’âge, le sexe
    - Le niveau d’isolement
    - La situation géographique (QPV, ZRR)
    - Le revenu et le statut de relance

    🔍 Plus le **score est élevé**, plus l’assuré est considéré **à risque** et doit être relancé **en priorité**.
    """)
    st.subheader("Distribution du score de risque")
    st.plotly_chart(px.histogram(df, x="Score_risque", nbins=20, title="Distribution des scores de risque"),
                    use_container_width=True)

    seuil_score = st.slider("Choisissez un seuil de priorité :", 0.0, 1.0, 0.6, 0.05)
    prioritaire = df[df["Score_risque"] >= seuil_score]

    st.success(f"{prioritaire.shape[0]} assurés à risque élevé identifiés.")
    st.dataframe(prioritaire[["ID_Assuré", "Âge", "Sexe", "Score_risque"]])

    st.download_button("📥 Télécharger les assurés prioritaires", data=prioritaire.to_csv(index=False),
                       file_name="prioritaires_score.csv", mime="text/csv")

# 🧭 Recommandations
with tab5:
    st.header("Synthèse & Recommandations")
    st.markdown("""
    ✅ **Cibler les relances selon le score de risque**  
    Utilisez le seuil pour identifier automatiquement les assurés à recontacter.

    ✅ **Cibler les zones sensibles**  
    Prioriser les territoires avec isolement élevé, bas revenus, ou faible participation passée.

    ✅ **Appui aux équipes de terrain**  
    Exporter les listes, planifier les appels, et suivre l’impact des relances avec les bons indicateurs.
    """)

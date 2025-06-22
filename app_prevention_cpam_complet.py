import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Configuration
st.set_page_config(page_title="Prévention Santé - CPAM", layout="wide")
st.title("📊 Application Prévention Santé & Relances - CPAM")

# Chargement des données
@st.cache_data
def load_data():
    return pd.read_csv("donnees_prevention_cpam.csv")

df = load_data()

# Encodage et modèle
def prepare_and_score(df):
    df_model = df.copy()
    le_sexe = LabelEncoder()
    le_depistage = LabelEncoder()
    df_model["Sexe"] = le_sexe.fit_transform(df_model["Sexe"])
    df_model["Dépistage"] = le_depistage.fit_transform(df_model["Dépistage"])

    features = ["Âge", "Sexe", "QPV", "ZRR", "Niveau_revenu", "Score_isolement", "Dépistage", "Relancé_par_CPAM"]
    target = "Participation_post_relance"

    X = df_model[features]
    y = df_model[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    df["Score_risque"] = model.predict_proba(X)[:, 1]
    return df

df = prepare_and_score(df)

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 Accueil", "🔎 Exploration", "📈 KPI", "🧠 Scoring", "🧭 Recommandations"])

# 🏠 Accueil
with tab1:
    st.header("Contexte & Objectif")
    st.markdown("""
    Cette application s'inscrit dans la mission **Aller Vers** de la CPAM.
    Elle permet de :
    - Suivre la participation aux campagnes de prévention santé
    - Identifier les assurés les plus à risque de non-participation
    - Aider à prioriser les relances de manière intelligente

    **NB : Données simulées. Projet de démonstration.**
    """)

# 🔎 Exploration
with tab2:
    st.header("Exploration des données")
    st.plotly_chart(px.histogram(df, x="Âge", nbins=20, title="Répartition des âges"), use_container_width=True)
    fig = px.histogram(df, x="Participation_post_relance", color="Sexe", barmode="group",
                       title="Participation après relance")
    fig.update_xaxes(tickvals=[0, 1], ticktext=["Non", "Oui"])
    st.plotly_chart(fig, use_container_width=True)

# 📈 KPI
with tab3:
    st.header("Indicateurs clés")
    col1, col2 = st.columns(2)
    col1.metric("🎯 Taux de participation post-relance", f"{df['Participation_post_relance'].mean():.2%}")
    col2.metric("📉 Score isolement moyen", f"{df['Score_isolement'].mean():.2f}")
    st.plotly_chart(px.box(df, x="Sexe", y="Score_isolement", color="Sexe", title="Score d'isolement par sexe"),
                    use_container_width=True)

# 🧠 Scoring
with tab4:
    st.header("Modèle de prédiction du risque")
    st.markdown("""
    🔍 Le score de risque estime la probabilité qu’un assuré **ne participe pas** après relance.
    Il est basé sur :
    - Le sexe, l’âge
    - L’isolement social
    - Le revenu, la relance, la zone géographique
    """)
    st.plotly_chart(px.histogram(df, x="Score_risque", nbins=20, title="Distribution des scores de risque"),
                    use_container_width=True)

    seuil = st.slider("Seuil de priorisation :", 0.0, 1.0, 0.6, 0.05)
    prioritaires = df[df["Score_risque"] >= seuil]
    st.success(f"{len(prioritaires)} assurés à relancer en priorité.")
    st.dataframe(prioritaires[["ID_Assuré", "Âge", "Sexe", "Score_risque"]])
    st.download_button("📥 Télécharger la liste", data=prioritaires.to_csv(index=False),
                       file_name="assures_a_relancer.csv", mime="text/csv")

# 🧭 Recommandations
with tab5:
    st.header("Synthèse & Recommandations")
    st.markdown("""
    ✅ **Relancer les profils à risque élevé**  
    ➤ Isolement élevé, relancés mais inactifs

    ✅ **Cibler les territoires sensibles**  
    ➤ Zones QPV/ZRR avec participation faible

    ✅ **Piloter les appels de manière stratégique**  
    ➤ Suivre les résultats et affiner les relances dans le temps
    """)

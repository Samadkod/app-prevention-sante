# 📊 [Application Prévention Santé & Relances – CPAM](https://app-prevention-sante-cpam-f9gmpfa2h7swk2wrppdsoi.streamlit.app/)

**Objectif** : Anticiper la non-participation des assurés aux campagnes de prévention santé afin d'optimiser les relances personnalisées dans le cadre de la mission "Aller Vers".

---

##  Contexte

Dans le cadre de la COG 2023-2027 de l’Assurance Maladie, la stratégie **“Aller Vers”** vise à améliorer la participation des assurés aux dépistages via des **relances téléphoniques ciblées**.  
Cette application simule un outil de pilotage à destination des équipes chargées des relances sur le terrain.

---

## 🧠 Méthodologie

### Données simulées (CSV) :
| Colonne                | Description                                                    |
|------------------------|----------------------------------------------------------------|
| `Âge`                  | Âge de l’assuré                                                |
| `Sexe`                 | Sexe de l’assuré                                               |
| `QPV` / `ZRR`          | Zone prioritaire ou rurale                                     |
| `Niveau_revenu`        | Niveau de revenu estimé (1 à 5)                                |
| `Score_isolement`      | Score simulé d’isolement social (entre 0 et 1)                |
| `Dépistage`            | Type de dépistage concerné                                     |
| `Relancé_par_CPAM`     | Relance effectuée en 2023 (Oui/Non)                            |
| `Participation_2023`   | Participation sans relance                                     |
| `Participation_post_relance` | Participation après relance téléphonique                |

### Étapes clés :
- 🧼 **Préparation des données** : encodage, normalisation, features
- 🧠 **Modèle prédictif** : Random Forest (scikit-learn) sur les variables comportementales et sociales
- 🎯 **Scoring** : probabilités de non-participation → priorisation intelligente
- 📈 **Visualisations** : KPI interactifs, distribution des scores, boxplots dynamiques (Plotly)

---

## 🖥️ Aperçu de l'application

| Fonctionnalité | Description |
|----------------|-------------|
| `🏠 Accueil` | Présentation du contexte et des enjeux de la prévention santé |
| `🔎 Exploration` | Analyse de la population : âge, sexe, participation, isolement |
| `📈 KPI` | Taux avant/après relance, score d’isolement, indicateurs clés |
| `🧠 Scoring` | Score de risque individuel, seuil de priorisation ajustable |
| `🧭 Recommandations` | Synthèse des actions à mettre en place |

---

## 📊 Exemple d’interprétation

### 🔹 Score d’isolement (entre 0 et 1) :
- `0.1` → Très bien entouré (zone urbaine, interactions fréquentes)
- `0.5` → Isolement modéré (peu de contacts médicaux)
- `0.9` → Très isolé (rural, pas de suivi connu)

> *Ex. : Un assuré de 82 ans en ZRR sans dépistage → score d’isolement élevé*

### 🔹 Score de risque (non-participation après relance) :
- `0.85` → Très peu de chance de participer → **à relancer en priorité**
- `0.30` → Profil déjà engagé → effort non nécessaire

---

## 💬 Recommandations opérationnelles

✔️ **Cibler en priorité les profils avec :**
- Score d’isolement élevé
- Score de risque > 0.6
- Non participation antérieure malgré relance

✔️ **Adapter les campagnes selon les territoires (QPV/ZRR)**  
✔️ **Piloter les relances avec souplesse grâce au seuil ajustable**

---

## 📂 Arborescence

├── app_prevention_cpam.py ← Code Streamlit

├── donnees_prevention_cpam.csv ← Jeu de données simulé

├── README.md ← Documentation


---

## 🚀 Démo en ligne

👉 [Accéder à l’application Streamlit](https://app-prevention-sante-cpam-f9gmpfa2h7swk2wrppdsoi.streamlit.app/)

---

## 👤 Auteur

**Samadou KODON**  
📌 Data Analyst & Prévention Santé  
📧 samadkod@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/skodon/)  
📂 [Portfolio](https://samadkod.github.io)

---

## 🛠️ Tech Stack

- `Python` (Pandas, Scikit-learn)
- `Streamlit` pour l’interface interactive
- `Plotly` pour les visualisations
- `GitHub` pour le versioning

---

## 📌 Mentions

> Ce projet est une **démonstration pédagogique** basée sur des données simulées. Il vise à **illustrer la faisabilité technique et métier** d’un outil de priorisation dans un contexte Assurance Maladie.

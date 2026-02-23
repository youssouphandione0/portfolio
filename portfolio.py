import streamlit as st
from PIL import Image

# Configuration de la page
st.set_page_config(page_title="Mon CV Digital", page_icon="🐍", layout="wide")

# --- STYLE CSS PERSONNALISÉ ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Infos de contact) ---
with st.sidebar:
    st.title("Contact")
    st.write("📍 mbour,senegal")
    st.write("📧 mon.email@exemple.com")
    st.write("🔗 [LinkedIn](https://linkedin.com)")
    st.write("💻 [GitHub](https://github.com)")
    st.divider()
    st.button("📥 Télécharger le CV (PDF)")

# --- EN-TÊTE ---
col1, col2 = st.columns([1, 3], gap="small")
with col1:
    # Remplacez par votre photo
    st.image("https://via.placeholder.com/150", width=150)

with col2:
    st.title("youssoupha developpeur")
    st.write("Développeur Full-Stack Python | Spécialiste Data & IA")
    st.info("Passionné par l'automatisation et la création d'interfaces intuitives.")

st.divider()

# --- CORPS DU CV ---
left_col, right_col = st.columns([2, 1], gap="large")

with left_col:
    st.header("🛠 Expériences Professionnelles")
    
    with st.expander("Développeur Python Senior - Tech Solutions", expanded=True):
        st.write("**2021 - Présent**")
        st.write("""
        - Développement d'outils internes de monitoring avec Streamlit.
        - Optimisation de scripts ETL traitant +1Go de données/jour.
        - Mentorat de 3 développeurs juniors.
        """)

    with st.expander("Développeur Junior - Web Agency"):
        st.write("**2019 - 2021**")
        st.write("""
        - Création d'API REST avec FastAPI.
        - Maintenance de bases de données PostgreSQL.
        """)

with right_col:
    st.header("🚀 Compétences")
    
    # Utilisation de widgets progress pour les skills
    skills = {"Python": 95, "SQL": 80, "Docker": 65, "Streamlit": 90}
    for skill, level in skills.items():
        st.write(f"**{skill}**")
        st.progress(level)

    st.header("🎓 Formation")
    st.write("**geomatique formation**")
    
import pandas as pd
import numpy as np
import plotly.express as px

# Configuration de la page
st.set_page_config(page_title="Portfolio - Youssoupha", layout="wide")

# --- SECTION 1: EXPÉRIENCES PROFESSIONNELLES (Version Riche) ---
st.markdown("## 🛠 Expériences Professionnelles")

with st.expander("🚀 Développeur Python Senior - Tech Solutions (2021 - Présent)", expanded=True):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **Missions clés :**
        * **Architecture ETL :** Optimisation de pipelines traitant **+1Go de données/jour**, réduisant la latence de 40%.
        * **Outils Internes :** Développement de dashboards de monitoring sous **Streamlit** utilisés par l'équipe produit.
        * **Mentorat :** Accompagnement technique de 3 développeurs juniors sur les bonnes pratiques Python et Git.
        """)
    with col2:
        st.info("**Stack :** Python, PostgreSQL, Docker, Pandas, Plotly")

with st.expander("💻 Développeur Junior - Web Agency (2019 - 2021)"):
    st.markdown("""
    * **Full-Stack :** Développement d'API REST avec FastAPI et intégration front-end.
    * **Automatisation :** Création de scripts de scraping pour l'analyse concurrentielle.
    """)

# --- SECTION 2: COMPÉTENCES & TABLEAU DE BORD ---
st.markdown("## 📊 Compétences & Démonstration Data")

tab1, tab2 = st.tabs(["Expertise Technique", "Démonstration Interactive"])

with tab1:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("🧠 Data & IA")
        st.write("- Pandas, Polars, NumPy")
        st.write("- Scikit-Learn (ML)")
        st.write("- Plotly & Altair")
    with c2:
        st.subheader("⚙️ Backend")
        st.write("- Python (Asynchrone)")
        st.write("- FastAPI / Flask")
        st.write("- SQL (PostgreSQL)")
    with c3:
        st.subheader("🐳 DevOps")
        st.write("- Docker & Docker Compose")
        st.write("- CI/CD (GitHub Actions)")
        st.write("- Déploiement Cloud")

with tab2:
    st.subheader("Exemple de Dashboard Intégré")
    st.write("Voici une simulation de monitoring de données ETL en temps réel.")
    
    # Création de données fictives
    df = pd.DataFrame({
        'Heure': pd.date_range(start='2024-01-01', periods=24, freq='H'),
        'Volume (Mo)': np.random.randint(50, 200, size=24),
        'Erreurs': np.random.randint(0, 5, size=24)
    })

    # Graphique interactif
    fig = px.line(df, x='Heure', y='Volume (Mo)', title="Flux de données (Dernières 24h)",
                  markers=True, template="plotly_dark")
    
    st.plotly_chart(fig, use_container_width=True)

    # Indicateurs clés
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Volume Total", f"{df['Volume (Mo)'].sum()} Mo", "+12%")
    kpi2.metric("Taux de succès", "98.5%", "0.5%")
    kpi3.metric("Temps moyen ETL", "1.2s", "-0.3s")

# --- CSS PERSONNALISÉ POUR LE LOOK ---
st.markdown("""
    <style>
    .stExpander { border: 1px solid #4CAF50; border-radius: 10px; margin-bottom: 10px; }
    [data-testid="stMetricValue"] { color: #4CAF50; }
    </style>
    """, unsafe_allow_html=True)

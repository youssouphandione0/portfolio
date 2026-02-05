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
    st.caption("université virtuel du sénégal | 2026")
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="ChatBot IA - Semiconductores 2026",
    page_icon="🤖",
    layout="centered",
)

st.markdown("""
<style>
    .stApp { background-color: #0d1117; }
    .chat-header {
        background: linear-gradient(135deg, #1a1f2e, #0f1117);
        border: 1px solid #30363d;
        border-radius: 14px;
        padding: 18px 22px;
        margin-bottom: 18px;
    }
    .chat-title { color: #58a6ff; font-size: 1.5rem; font-weight: 800; margin: 0; }
    .chat-sub   { color: #8b949e; font-size: 0.82rem; margin: 2px 0 0; }
    .stButton > button {
        background: #161b22 !important;
        color: #58a6ff !important;
        border: 1px solid #30363d !important;
        border-radius: 20px !important;
        font-size: 0.78rem !important;
        padding: 6px 14px !important;
        width: 100% !important;
        transition: all 0.2s !important;
    }
    .stButton > button:hover { border-color: #58a6ff !important; background: #1f3a5f !important; }
    .msg-user {
        background: #1f3a5f; color: #93c5fd;
        border-radius: 14px 14px 4px 14px;
        padding: 10px 15px; margin: 4px 0;
        font-size: 0.88rem; max-width: 80%; margin-left: auto; line-height: 1.6;
    }
    .msg-bot {
        background: #161b22; color: #e6edf3;
        border: 1px solid #30363d;
        border-radius: 14px 14px 14px 4px;
        padding: 10px 15px; margin: 4px 0;
        font-size: 0.88rem; max-width: 85%; line-height: 1.6;
    }
    .msg-label-user { text-align: right; font-size: 0.7rem; color: #8b949e; margin-bottom: 2px; }
    .msg-label-bot  { font-size: 0.7rem; color: #8b949e; margin-bottom: 2px; }
    .stTextInput > div > div > input {
        background: #161b22 !important; color: #e6edf3 !important;
        border: 1px solid #30363d !important; border-radius: 10px !important;
    }
    .stTextInput > div > div > input:focus { border-color: #58a6ff !important; }
    .chips-label { color: #8b949e; font-size: 0.72rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 8px; }
    hr { border-color: #21262d; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="chat-header">
    <div style="display:flex;align-items:center;gap:14px;">
        <div style="font-size:2rem">🤖</div>
        <div>
            <p class="chat-title">ChatBot IA — Semiconductores 2026</p>
            <p class="chat-sub">Powered by DeepSeek · Análisis del sector · Empresas · Impacto educativo</p>
        </div>
        <div style="margin-left:auto;display:flex;align-items:center;gap:6px;">
            <div style="width:8px;height:8px;border-radius:50%;background:#22c55e;"></div>
            <span style="color:#8b949e;font-size:0.75rem;">En línea</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Clase ChatbotIA (igual que el original) ────────────────────────────────────
class ChatbotIA:
    def __init__(self, api_key):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com/v1"
        )
        self.historial = [
            {
                "role": "system",
                "content": (
                    "Eres un asistente experto en semiconductores y sistemas digitales en 2026. "
                    "Responde de forma clara, académica y bien estructurada en español. "
                    "Incluye datos concretos sobre empresas líderes como NVIDIA, TSMC, Intel, AMD, Qualcomm, Samsung, ASML. "
                    "Cuando pregunten sobre educación, responde en profundidad sobre: "
                    "1) Innovación en la Educación con semiconductores y sistemas digitales, "
                    "2) Novedad e impacto de proyectos de sistemas digitales en la educación, "
                    "3) Sistemas digitales y semiconductores en el futuro. "
                    "Usa máximo 250 palabras por respuesta para mantener fluidez."
                )
            }
        ]

    def enviar_mensaje(self, mensaje_usuario):
        self.historial.append({"role": "user", "content": mensaje_usuario})
        respuesta = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=self.historial
        )
        reply = respuesta.choices[0].message.content
        self.historial.append({"role": "assistant", "content": reply})
        return reply

# ── Estado de sesión ──────────────────────────────────────────────────────────
API_KEY = "sk-2d5996dc3b04479e9dacbf5d0085ce60"

if "bot" not in st.session_state:
    st.session_state.bot = ChatbotIA(API_KEY)
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []
if "input_key" not in st.session_state:
    st.session_state.input_key = 0

def enviar(texto):
    if not texto.strip():
        return
    st.session_state.mensajes.append({"role": "user", "content": texto})
    try:
        respuesta = st.session_state.bot.enviar_mensaje(texto)
        st.session_state.mensajes.append({"role": "assistant", "content": respuesta})
    except Exception as e:
        st.session_state.mensajes.append({"role": "assistant", "content": f"⚠️ Error: {e}"})
    st.session_state.input_key += 1

# ── Botones rápidos ───────────────────────────────────────────────────────────
st.markdown('<p class="chips-label">⚡ Temas rápidos del parcial</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📈 Tendencias 2026"):
        enviar("Analiza la temática de los semiconductores en el año 2026: tendencias, mercado y avances tecnológicos.")
        st.rerun()
    if st.button("🎓 Innovación educativa"):
        enviar("Explica la innovación en la educación con semiconductores y sistemas digitales.")
        st.rerun()
with col2:
    if st.button("🏭 Empresas líderes"):
        enviar("Expón las empresas más relevantes del sector de semiconductores en 2026 y su impacto en los sistemas digitales.")
        st.rerun()
    if st.button("📚 Proyectos en educación"):
        enviar("Cuéntame sobre la novedad e impacto de proyectos de sistemas digitales en la educación en 2026.")
        st.rerun()
with col3:
    if st.button("🚀 Futuro del sector"):
        enviar("¿Cuál es el futuro de los sistemas digitales y los semiconductores?")
        st.rerun()
    if st.button("🔬 Análisis completo"):
        enviar("Haz un análisis completo del sector de semiconductores en 2026: empresas, tendencias e impacto educativo.")
        st.rerun()

st.markdown("<hr>", unsafe_allow_html=True)

# ── Mensajes ──────────────────────────────────────────────────────────────────
if not st.session_state.mensajes:
    st.markdown('<p class="msg-label-bot">🤖 Bot</p><div class="msg-bot">👋 Hola! Soy tu asistente especializado en <strong>semiconductores y sistemas digitales 2026</strong>. Usa los botones de arriba o escríbeme directamente.</div>', unsafe_allow_html=True)
else:
    for msg in st.session_state.mensajes:
        if msg["role"] == "user":
            st.markdown(f'<p class="msg-label-user">Tú</p><div class="msg-user">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p class="msg-label-bot">🤖 Bot</p><div class="msg-bot">{msg["content"]}</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────────────────────
col_input, col_btn = st.columns([5, 1])
with col_input:
    user_text = st.text_input(
        label="",
        placeholder="Escribe tu pregunta...",
        key=f"input_{st.session_state.input_key}",
        label_visibility="collapsed"
    )
with col_btn:
    if st.button("Enviar ➤", key="send"):
        if user_text:
            enviar(user_text)
            st.rerun()

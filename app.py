import streamlit as st

st.set_page_config(
    page_title="JAMBO — AI Navigation Device",
    page_icon="🦯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main { padding: 0rem; }
.block-container { padding-top: 1rem; padding-bottom: 2rem; max-width: 1100px; }

.hero {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    border-radius: 20px;
    padding: 60px 40px;
    text-align: center;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: "";
    position: absolute; top: 0; left: 0; right: 0; bottom: 0;
    background: radial-gradient(circle at 30% 50%, rgba(99,179,237,0.15) 0%, transparent 60%),
                radial-gradient(circle at 70% 50%, rgba(159,122,234,0.15) 0%, transparent 60%);
}
.hero-badge {
    display: inline-block;
    background: rgba(99,179,237,0.2);
    border: 1px solid rgba(99,179,237,0.4);
    color: #63b3ed;
    padding: 6px 16px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 20px;
}
.hero h1 {
    font-size: 2.8rem;
    font-weight: 800;
    color: white;
    margin: 0 0 16px 0;
    line-height: 1.2;
}
.hero p {
    font-size: 1.1rem;
    color: rgba(255,255,255,0.7);
    max-width: 600px;
    margin: 0 auto 24px auto;
    line-height: 1.6;
}
.hero-tags {
    display: flex;
    gap: 10px;
    justify-content: center;
    flex-wrap: wrap;
}
.hero-tag {
    background: rgba(255,255,255,0.1);
    color: rgba(255,255,255,0.85);
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 13px;
    border: 1px solid rgba(255,255,255,0.15);
}

.stats-row { display: flex; gap: 16px; margin-bottom: 2rem; flex-wrap: wrap; }
.stat-card {
    flex: 1; min-width: 160px;
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 24px 20px;
    text-align: center;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.stat-number { font-size: 2rem; font-weight: 800; color: #2d3748; margin-bottom: 4px; }
.stat-label { font-size: 13px; color: #718096; font-weight: 500; }
.stat-icon { font-size: 1.5rem; margin-bottom: 8px; }

.section-header {
    font-size: 1.4rem;
    font-weight: 700;
    color: #1a202c;
    margin-bottom: 1rem;
    padding-bottom: 8px;
    border-bottom: 2px solid #e2e8f0;
}

.feature-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 20px;
    height: 100%;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.feature-icon { font-size: 2rem; margin-bottom: 12px; }
.feature-title { font-size: 1rem; font-weight: 700; color: #2d3748; margin-bottom: 8px; }
.feature-desc { font-size: 13px; color: #718096; line-height: 1.6; }

.pipeline {
    background: #f7fafc;
    border-radius: 14px;
    padding: 24px;
    margin-bottom: 1.5rem;
    border: 1px solid #e2e8f0;
}
.pipeline-flow {
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
    justify-content: center;
}
.pipeline-step {
    background: white;
    border: 2px solid #3182ce;
    border-radius: 10px;
    padding: 12px 18px;
    text-align: center;
    min-width: 110px;
    box-shadow: 0 2px 6px rgba(49,130,206,0.15);
}
.pipeline-step .step-icon { font-size: 1.4rem; }
.pipeline-step .step-name { font-size: 12px; font-weight: 600; color: #2d3748; margin-top: 4px; }
.pipeline-arrow { font-size: 1.4rem; color: #3182ce; font-weight: bold; }

.tech-badge {
    display: inline-block;
    background: #ebf8ff;
    color: #2b6cb0;
    padding: 6px 14px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 600;
    margin: 4px;
    border: 1px solid #bee3f8;
}

.team-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.team-avatar {
    width: 56px; height: 56px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.4rem;
    margin: 0 auto 12px auto;
    color: white;
    font-weight: 700;
}
.team-name { font-size: 14px; font-weight: 700; color: #2d3748; margin-bottom: 4px; }
.team-role { font-size: 12px; color: #718096; }

.link-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 10px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.link-icon { font-size: 1.5rem; }
.link-title { font-size: 14px; font-weight: 600; color: #2d3748; }
.link-sub { font-size: 12px; color: #718096; }

.divider { height: 1px; background: #e2e8f0; margin: 2rem 0; }
</style>
""", unsafe_allow_html=True)

# ─── HERO ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div style="position:relative; z-index:1;">
        <div class="hero-badge">🏆 Inha University in Tashkent · 2025</div>
        <h1>🦯 AI Navigation Device<br>for the Visually Impaired</h1>
        <p>A wearable AI assistant enabling fully independent mobility — combining real-time computer vision, natural-language voice interaction, and solar-powered hardware.</p>
        <div class="hero-tags">
            <span class="hero-tag">🤖 OpenCV</span>
            <span class="hero-tag">🗣️ Voice AI</span>
            <span class="hero-tag">☀️ Solar-powered</span>
            <span class="hero-tag">🧪 User-tested</span>
            <span class="hero-tag">🎓 Top Grade</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── STATS ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-row">
    <div class="stat-card">
        <div class="stat-icon">📡</div>
        <div class="stat-number">10m</div>
        <div class="stat-label">Detection Range</div>
    </div>
    <div class="stat-card">
        <div class="stat-icon">⚡</div>
        <div class="stat-number">≤2s</div>
        <div class="stat-label">Voice Latency</div>
    </div>
    <div class="stat-card">
        <div class="stat-icon">👥</div>
        <div class="stat-number">6</div>
        <div class="stat-label">Real Users Tested</div>
    </div>
    <div class="stat-card">
        <div class="stat-icon">☀️</div>
        <div class="stat-number">100%</div>
        <div class="stat-label">Off-grid Operation</div>
    </div>
    <div class="stat-card">
        <div class="stat-icon">🏆</div>
        <div class="stat-number">A+</div>
        <div class="stat-label">Final Grade</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── PROBLEM & SOLUTION ─────────────────────────────────────────────────────
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<div class="section-header">🎯 Problem Statement</div>', unsafe_allow_html=True)
    st.markdown("""
    Visually impaired individuals in Uzbekistan face significant barriers to independent mobility,
    often relying on another person for daily navigation.

    **Limitations of existing tools:**
    - 🦯 White cane — limited situational awareness, detects only physical obstacles
    - 🐕 Guide dogs — expensive and not accessible to everyone
    - 📱 Mobile apps — require the user to look at a screen

    **Our goal:** Build an affordable, wearable AI navigation assistant that gives visually impaired users full independence — without needing another person.
    """)

with col2:
    st.markdown('<div class="section-header">💡 Our Solution</div>', unsafe_allow_html=True)
    st.markdown("A wearable device that uses a camera to see the environment, processes it with AI, and speaks to the user in real time — while also listening and responding to their questions.")
    st.markdown("""
    <div class="pipeline">
        <div class="pipeline-flow">
            <div class="pipeline-step">
                <div class="step-icon">📷</div>
                <div class="step-name">Camera</div>
            </div>
            <div class="pipeline-arrow">→</div>
            <div class="pipeline-step">
                <div class="step-icon">🧠</div>
                <div class="step-name">OpenCV AI</div>
            </div>
            <div class="pipeline-arrow">→</div>
            <div class="pipeline-step">
                <div class="step-icon">🔊</div>
                <div class="step-name">TTS Engine</div>
            </div>
            <div class="pipeline-arrow">⇅</div>
            <div class="pipeline-step">
                <div class="step-icon">🎤</div>
                <div class="step-name">Voice Input</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ─── FEATURES ───────────────────────────────────────────────────────────────
st.markdown('<div class="section-header">✨ Key Features</div>', unsafe_allow_html=True)

features = [
    ("🎥", "Real-time Obstacle Detection", "OpenCV-based computer vision detects obstacles up to 10 meters away"),
    ("🔊", "Voice-based Situational Awareness", "Continuous low-latency audio feedback — user is always informed"),
    ("🗣️", "Two-way Conversation", "Natural language interface — users can ask questions freely, not just receive one-way alerts"),
    ("☀️", "Off-grid Operation", "Solar charging panel for fully portable, outdoor use without any power outlet"),
    ("🔬", "User-validated Design", "Tested with 6 visually impaired users at the Tashkent Library for the Blind"),
    ("🏗️", "Custom Hardware", "Sensor module and microcontroller housing designed in Autodesk Fusion 360"),
]

cols = st.columns(3, gap="medium")
for i, (icon, title, desc) in enumerate(features):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <div class="feature-title">{title}</div>
            <div class="feature-desc">{desc}</div>
        </div>
        <br>
        """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ─── TECH & RESEARCH ────────────────────────────────────────────────────────
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<div class="section-header">💻 Tech Stack</div>', unsafe_allow_html=True)
    st.markdown("""
    <div>
        <span class="tech-badge">🐍 Python</span>
        <span class="tech-badge">👁️ OpenCV</span>
        <span class="tech-badge">🔊 pyttsx3 (TTS)</span>
        <span class="tech-badge">🎤 SpeechRecognition</span>
        <span class="tech-badge">🔢 NumPy</span>
        <span class="tech-badge">🐧 Linux (RPi)</span>
        <span class="tech-badge">⚙️ Fusion 360</span>
        <span class="tech-badge">🎨 FigJam</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">🔧 Hardware Components</div>', unsafe_allow_html=True)

    hardware = [
        ("📷", "Camera module", "Real-time video stream"),
        ("🎤", "Microphone", "Captures voice commands"),
        ("🔊", "Speaker", "Audio output for feedback"),
        ("☀️", "Solar panel", "Off-grid power supply"),
        ("🧠", "Microcontroller", "Custom PCB design"),
        ("📡", "Sensor array", "Environmental data collection"),
    ]
    for icon, name, desc in hardware:
        st.markdown(f"**{icon} {name}** — {desc}")

with col2:
    st.markdown('<div class="section-header">🔬 User Research</div>', unsafe_allow_html=True)
    st.info("🏛️ Conducted structured interviews with **6 visually impaired users** at the **Tashkent Library for the Blind**")

    insights = [
        ("⚡", "Voice feedback within 1–2 seconds", "Optimized for a low-latency audio pipeline"),
        ("💬", "Ability to ask questions freely", "Led to a conversational interface, not one-way alerts"),
        ("🌳", "Outdoor portability is critical", "Led to solar panel integration for off-grid use"),
    ]

    for icon, finding, action in insights:
        st.markdown(f"""
        <div style="background:#f0fff4; border-left:4px solid #38a169; border-radius:8px; padding:14px; margin-bottom:12px;">
            <div style="font-weight:700; color:#276749; margin-bottom:4px;">{icon} {finding}</div>
            <div style="font-size:13px; color:#4a5568;">→ {action}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ─── TEAM ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-header">👥 Team JAMBO — Inha University in Tashkent</div>', unsafe_allow_html=True)

team = [
    ("OR", "Ro'zimurodov Ozodbek", "AI / Software Lead\nHardware Integration", "U2410209"),
    ("RB", "Ryazanov Bogdan", "Hardware Design\nFusion 360", "U2410214"),
    ("SA", "Sagatov Abdfayyoz", "User Research", "U2410215"),
    ("SJ", "Sarsenov Jandaulet", "Ideation & Prototyping", "U2410218"),
    ("RM", "Rustamov Muhammadamin", "Presentation\n& Documentation", "U2410210"),
]

cols = st.columns(5, gap="small")
for i, (initials, name, role, sid) in enumerate(team):
    with cols[i]:
        st.markdown(f"""
        <div class="team-card">
            <div class="team-avatar">{initials}</div>
            <div class="team-name">{name}</div>
            <div class="team-role">{role.replace(chr(10),'<br>')}</div>
            <div style="font-size:11px; color:#a0aec0; margin-top:6px;">{sid}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ─── LINKS ──────────────────────────────────────────────────────────────────
st.markdown('<div class="section-header">🔗 Project Links</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <a href="https://www.canva.com/design/DAGmgoRM7cE/eb0-v_aGojJFRVCt-7tJeg/edit" target="_blank" style="text-decoration:none;">
    <div class="link-card" style="border-left:4px solid #e53e3e; cursor:pointer;">
        <div class="link-icon">🎨</div>
        <div>
            <div class="link-title">Canva Presentation</div>
            <div class="link-sub">Full project slide deck</div>
        </div>
        <div style="margin-left:auto; font-size:1.2rem;">↗</div>
    </div></a>

    <a href="https://www.figma.com/board/qg7lBPsjFeo03SOgxDdStl/User-Reasearch?node-id=0-1" target="_blank" style="text-decoration:none;">
    <div class="link-card" style="border-left:4px solid #805ad5; cursor:pointer;">
        <div class="link-icon">🔬</div>
        <div>
            <div class="link-title">FigJam — User Research</div>
            <div class="link-sub">Interview results and key findings</div>
        </div>
        <div style="margin-left:auto; font-size:1.2rem;">↗</div>
    </div></a>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <a href="https://www.figma.com/board/MpUXXWDuAU2LpKEcIu8xjI/Ideation?node-id=0-1" target="_blank" style="text-decoration:none;">
    <div class="link-card" style="border-left:4px solid #38a169; cursor:pointer;">
        <div class="link-icon">💡</div>
        <div>
            <div class="link-title">FigJam — Ideation</div>
            <div class="link-sub">Design process and solution exploration</div>
        </div>
        <div style="margin-left:auto; font-size:1.2rem;">↗</div>
    </div></a>

    <a href="https://github.com/Ozse97/ai-navigation-device" target="_blank" style="text-decoration:none;">
    <div class="link-card" style="border-left:4px solid #2d3748; cursor:pointer;">
        <div class="link-icon">💻</div>
        <div>
            <div class="link-title">GitHub Repository</div>
            <div class="link-sub">Source code, CAD files, documentation</div>
        </div>
        <div style="margin-left:auto; font-size:1.2rem;">↗</div>
    </div></a>
    """, unsafe_allow_html=True)

# ─── FOOTER ─────────────────────────────────────────────────────────────────
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; padding:20px 0; color:#a0aec0; font-size:13px;">
    🦯 <strong style="color:#4a5568;">JAMBO</strong> · Inha University in Tashkent · Creative Engineering & Design · 2025<br><br>
    <em>"Built with purpose — for real people, with real needs."</em><br><br>
    📧 ruzimurodovozodbek5@gmail.com ·
    <a href="https://linkedin.com/in/ozodbek-ruzimurodov-931733359/" target="_blank" style="color:#3182ce;">LinkedIn</a> ·
    <a href="https://github.com/Ozse97" target="_blank" style="color:#3182ce;">GitHub</a>
</div>
""", unsafe_allow_html=True)

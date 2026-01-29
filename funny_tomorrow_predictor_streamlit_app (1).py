import streamlit as st
import random
import datetime
import time

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Tomorrow Predictor 🔮",
    page_icon="🔮",
    layout="centered"
)

# ------------------ MATRIX BACKGROUND ------------------
st.markdown(
    """
    <style>
    body {
        background: black;
    }

    .matrix {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        background: repeating-linear-gradient(
            90deg,
            rgba(0,255,65,0.15) 0px,
            rgba(0,255,65,0.15) 1px,
            transparent 1px,
            transparent 20px
        );
        animation: matrixMove 6s linear infinite;
    }

    @keyframes matrixMove {
        from { background-position: 0 0; }
        to { background-position: 0 100%; }
    }

    .terminal {
        background-color: black;
        border: 1px solid #00ff41;
        color: #00ff41;
        padding: 10px;
        font-family: monospace;
        font-size: 14px;
        margin-top: 8px;
    }
    </style>

    <div class="matrix"></div>
    """,
    unsafe_allow_html=True
)

# ------------------ TITLE ------------------
st.title("🔮 Tomorrow Prediction App )")
st.markdown(
    "<span style='color:#00ff41'>Ultra-advanced prediction system powered by vibes, chai & Mars 🚀</span>",
    unsafe_allow_html=True
)

# ------------------ USER INPUT ------------------
name = st.text_input("Enter your name:", "Ankit")

# ------------------ TYPEWRITER (FIXED VISIBILITY) ------------------
def type_writer(text, delay=0.04):
    placeholder = st.empty()
    output = ""
    for char in text:
        output += char
        placeholder.markdown(
            f"""
            <div style="
                color:#00ff41;
                font-family: monospace;
                font-size:16px;
                background-color:black;
                padding:6px;
                border-left:3px solid #00ff41;
            ">
            {output}<span style="animation:blink 1s infinite">▌</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        time.sleep(delay)

# ------------------ BUTTON ------------------
if st.button("🚀 Start Prediction"):

    progress = st.progress(0)
    terminal_box = st.empty()
    status = st.empty()

    steps = [
        "📡 Aligning jugaad antenna towards ISRO headquarters…",
        "☎️ Putting ISRO scientists on hold (music playing)…",
        "🧠 Double-checking math with Elon Musk (he said 'interesting')…",
        "🤝 Consulting with Elon Musk for final approval…",
        "🚀 Borrowing fuel from SpaceX for Mars trip…",
        "🪐 Signal bounced via Jupiter, Saturn & neighbor's WiFi…",
        "🛸 Decoding alien message: 'Try turning it off and on again'…",
        "🧪 Mixing chai + code to stabilize predictions…",
        "📊 Pretending this took 10,000 GPU hours…"
    ]

    # ------------------ LOADING STEPS ------------------
    for i, step in enumerate(steps):
        with st.spinner("🛰️ Processing signals…"):
            type_writer(step)

        terminal_box.markdown(
            f"""
            <div class="terminal">
            [LOG {i+1:02}] {step}<br>
            📡 BEEP… BEEP… Signal locked ✔
            </div>
            """,
            unsafe_allow_html=True
        )

        progress.progress(int((i + 1) / len(steps) * 100))
        time.sleep(2.5)  # slow enough to read

    # ------------------ SATELLITE / MARS ANIMATION ------------------
    sat = st.empty()
    frames = ["🛰️", "➡️", "🌍", "➡️", "🌕", "➡️", "🔴"]

    for _ in range(2):
        for f in frames:
            sat.markdown(f"<h2 style='color:#00ff41'>{f}</h2>", unsafe_allow_html=True)
            time.sleep(0.3)

    # ------------------ CONFIDENCE SCORE ------------------
    confidence = random.randint(75, 99)
    for i in range(0, confidence, 5):
        status.markdown(
            f"<span style='color:#00ff41'>🧠 Calculating confidence using vibes… {i}%</span>",
            unsafe_allow_html=True
        )
        time.sleep(0.15)

    st.success(f"🧠 Prediction Confidence: {confidence}% (Certified by Mars)")

    # ------------------ FINAL PREDICTION ------------------
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)

    energy = random.choice(["High ⚡", "Medium 🙂", "Low 🪫"])
    productivity = random.choice([
        "🔥 Extremely Productive",
        "🙂 Decent work done",
        "😴 Productivity went on leave",
        "📱 Busy pretending to work"
    ])
    luck = random.randint(1, 10)

    events = [
        "You will say 'kal se pakka' at least once 😂",
        "You will open WhatsApp and forget why 🤔",
        "You will feel hungry right after eating 🍔",
        "You will plan life decisions at 2 AM 🌙",
        "You will check phone for no reason 📱"
    ]

    st.markdown("---")
    st.markdown(f"<span style='color:#00ff41'>📅 Prediction for {tomorrow}</span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color:#00ff41'>👤 Name: <b>{name}</b></span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color:#00ff41'>⚡ Energy Level: <b>{energy}</b></span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color:#00ff41'>📊 Productivity: <b>{productivity}</b></span>", unsafe_allow_html=True)
    st.markdown(f"<span style='color:#00ff41'>🍀 Luck Level: <b>{luck}/10</b></span>", unsafe_allow_html=True)
    st.info(f"😂 Special Event: {random.choice(events)}")

    if luck >= 8:
        st.balloons()
        st.write("🎉 Mars says: Tomorrow is your lucky day!")
    elif luck <= 3:
        st.warning("⚠️ Mars warning: Keep snacks & patience ready 🍫")

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("⚠️ Disclaimer: Accuracy improves after chai ☕")

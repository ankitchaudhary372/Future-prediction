import streamlit as st
import random
import datetime
import time

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Tomorrow Predictor 🔮", page_icon="🔮", layout="centered")

# ------------------ MATRIX BACKGROUND & TERMINAL STYLE ------------------
st.markdown(
    """
    <style>
    body {
        background: black;
        color: #00ff41;
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
        background-color: #000000;
        border: 1px solid #00ff41;
        padding: 10px;
        font-family: monospace;
        font-size: 14px;
    }
    </style>

    <div class="matrix"></div>
    """,
    unsafe_allow_html=True
)

# ------------------ BACKGROUND ANIMATION ------------------
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364);
        background-size: 400% 400%;
        animation: gradientBG 10s ease infinite;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #00ffcc, #00ccff);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ TITLE ------------------
st.title("🔮 Tomorrow Prediction App )")
st.write("Ultra‑advanced prediction system powered by ISRO + Mars + Elon Musk 🚀😂")

# ------------------ USER INPUT ------------------
name = st.text_input("Enter your name:", "Ankit")

# ------------------ BUTTON ------------------
if st.button("🚀 Start Prediction"):

    progress = st.progress(0)
    status = st.empty()

    # Fake scientific loading steps
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

    for i, step in enumerate(steps):
        status.write(step)
        time.sleep(2.5)
        progress.progress(int((i + 1) / len(steps) * 100))

    status.write("✅ Prediction Complete!")

    # ------------------ PREDICTION LOGIC ------------------
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    energy = random.choice(["High ⚡", "Medium 🙂", "Low 🪫"])
    luck = random.randint(1, 10)

    productivity = random.choice([
        "🔥 Extremely Productive",
        "🙂 Decent Work Done",
        "😴 Productivity went on leave",
        "📱 Busy pretending to work"
    ])

    events = [
        "You will say 'kal se pakka' at least once 😂",
        "You will open WhatsApp and forget why 🤔",
        "You will feel hungry right after eating 🍔",
        "You will plan big things at night 🌙",
        "You will check phone for no reason 📱"
    ]

    # ------------------ OUTPUT ------------------
    st.success(f"📅 Prediction for {tomorrow}")
    st.write(f"👤 Name: **{name}**")
    st.write(f"⚡ Energy Level: **{energy}**")
    st.write(f"📊 Productivity: **{productivity}**")
    st.write(f"🍀 Luck Level: **{luck}/10**")
    st.info(f"😂 Special Event: {random.choice(events)}")

    if luck >= 8:
        st.balloons()
        st.write("🎉 Mars says: Tomorrow is your lucky day!")
    elif luck <= 3:
        st.warning("⚠️ Mars warning: Keep snacks & patience ready 🍫")

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("⚠️ Disclaimer: This app is more accurate than most horoscopes 😎")

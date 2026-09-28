import streamlit as st
import ollama


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Friendly AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* ---------------- BACKGROUND ---------------- */

.stApp {
    background: linear-gradient(
        135deg,
        #f8f9ff 0%,
        #eef2ff 50%,
        #f5f3ff 100%
    );
}


/* ---------------- MAIN WIDTH ---------------- */

.block-container {
    max-width: 850px;
    padding-top: 45px;
    padding-bottom: 50px;
}


/* ---------------- TITLE ---------------- */

h1 {
    text-align: center;

    font-size: 42px !important;

    font-weight: 800 !important;

    color: #312e81 !important;

    margin-bottom: 5px !important;
}


/* ---------------- SUBTITLE ---------------- */

.subtitle {
    text-align: center;

    color: #64748b;

    font-size: 17px;

    margin-bottom: 35px;
}


/* ---------------- BOT ICON ---------------- */

.bot-icon {
    text-align: center;

    font-size: 55px;

    margin-bottom: 5px;
}


/* ---------------- QUESTION AREA ---------------- */

.question-title {
    font-size: 18px;

    font-weight: 700;

    color: #1e293b;

    margin-bottom: 8px;
}


/* ---------------- TEXT INPUT ---------------- */

.stTextArea textarea {

    background-color: white !important;

    color: #1e293b !important;

    border: 2px solid #e2e8f0 !important;

    border-radius: 14px !important;

    padding: 15px 18px !important;

    font-size: 16px !important;

    line-height: 1.5 !important;

    box-shadow: 0 4px 15px rgba(15, 23, 42, 0.06);

    box-sizing: border-box !important;

    resize: vertical !important;
}

.stTextArea textarea:focus {

    border-color: #6366f1 !important;

    box-shadow:
        0 0 0 3px rgba(99, 102, 241, 0.12) !important;
}

.stTextArea textarea::placeholder {

    color: #94a3b8 !important;
}


.stTextInput input:focus {

    border-color: #6366f1 !important;

    box-shadow:
        0 0 0 3px rgba(99, 102, 241, 0.12) !important;
}


/* ---------------- ASK BUTTON ---------------- */

.stButton > button {

    width: 100%;

    height: 50px;

    border-radius: 14px;

    border: none;

    background: linear-gradient(
        135deg,
        #6366f1,
        #7c3aed
    );

    color: white;

    font-size: 16px;

    font-weight: 700;

    transition: all 0.2s ease;

    box-shadow:
        0 6px 18px rgba(99, 102, 241, 0.25);
}


.stButton > button:hover {

    background: linear-gradient(
        135deg,
        #4f46e5,
        #6d28d9
    );

    transform: translateY(-2px);

    box-shadow:
        0 10px 25px rgba(99, 102, 241, 0.35);
}


/* ---------------- CHAT MESSAGE ---------------- */

[data-testid="stChatMessage"] {

    background: white;

    border: 1px solid #e2e8f0;

    border-radius: 18px;

    padding: 15px;

    margin-top: 15px;

    box-shadow:
        0 5px 20px rgba(15, 23, 42, 0.06);
}


/* ---------------- WARNING ---------------- */

[data-testid="stAlert"] {

    border-radius: 12px;
}


/* ---------------- FOOTER ---------------- */

.footer {

    text-align: center;

    color: #94a3b8;

    font-size: 13px;

    margin-top: 35px;
}


/* ---------------- MOBILE ---------------- */

@media (max-width: 600px) {

    .block-container {
        padding: 25px 15px 40px 15px;
    }

    h1 {
        font-size: 32px !important;
    }

    .subtitle {
        font-size: 15px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="bot-icon">🤖</div>',
    unsafe_allow_html=True
)

st.title("Friendly AI Chatbot")

st.markdown(
    '<div class="subtitle">'
    'Ask questions and get simple, helpful answers powered by AI.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# QUESTION
# =========================================================

st.markdown(
    '<div class="question-title">💬 Ask your question</div>',
    unsafe_allow_html=True
)

question = st.text_area(
    "Question",
    placeholder="Example: Explain artificial intelligence in simple words...",
    height=120,
    label_visibility="collapsed"
)


# =========================================================
# ASK AI BUTTON
# =========================================================

if st.button("✨ Ask AI"):

    if not question.strip():

        st.warning("Please enter a question first.")

    else:

        with st.spinner("🤖 AI is thinking..."):

            try:

                response = ollama.chat(
                    model="llama3.2",
                    messages=[
                        {
                            "role": "system",
                            "content": """
You are a friendly and helpful AI chatbot.

Answer questions accurately and clearly.

Use simple language that beginners can understand.

Keep answers concise unless the user asks for more detail.

Be polite and friendly.
"""
                        },
                        {
                            "role": "user",
                            "content": question
                        }
                    ]
                )

                answer = response["message"]["content"]

                # ---------------- USER MESSAGE ----------------

                with st.chat_message("user", avatar="👤"):
                    st.write(question)

                # ---------------- AI MESSAGE ----------------

                with st.chat_message("assistant", avatar="🤖"):
                    st.write(answer)

            except Exception as e:

                st.error(
                    "Unable to connect to Ollama. "
                    "Make sure Ollama is running and Llama 3.2 is installed."
                )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer">'
    'Powered by Ollama • Llama 3.2 🚀'
    '</div>',
    unsafe_allow_html=True
)
import streamlit as st
import random

# Khởi tạo danh sách từ vựng nếu chưa có
if "vocab_list" not in st.session_state:
    st.session_state.vocab_list = []

# --- Sidebar: Nhập từ mới ---
st.sidebar.header("📥 Add New Vocabulary")
new_word = st.sidebar.text_input("English Word")
new_meaning = st.sidebar.text_input("Vietnamese Meaning")

if st.sidebar.button("➕ Add Word"):
    if new_word and new_meaning:
        st.session_state.vocab_list.append({
            "word": new_word.strip(),
            "meaning": new_meaning.strip()
        })
        st.sidebar.success(f"Added '{new_word}'!")
    else:
        st.sidebar.warning("Please enter both word and meaning.")

# --- Main App ---
st.title("🧠 English Vocabulary Flashcards")

# Shuffle để tạo cảm giác "học flashcard"
random.shuffle(st.session_state.vocab_list)

if st.session_state.vocab_list:
    for idx, vocab in enumerate(st.session_state.vocab_list):
        with st.expander(f"📘 Word {idx+1}: {vocab['word']}"):
            st.write(f"👉 Meaning: **{vocab['meaning']}**")
else:
    st.info("No vocabulary added yet. Use the sidebar to add some!")

# --- Extra: Export (Optional) ---
st.divider()
if st.button("🗃 Export Vocabulary (Text)"):
    output = "\n".join([f"{v['word']} - {v['meaning']}" for v in st.session_state.vocab_list])
    st.download_button("📄 Download .txt", output, file_name="vocab_list.txt")


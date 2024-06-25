import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def page2():
    local_css("style2.css")  

    st.markdown('<div class="title">Galava</div>', unsafe_allow_html=True)

    # Additional content for Page 2...
    st.markdown("""
        <h2 class="vault-header">Ask me anything regarding your database cluster</h2>
    """, unsafe_allow_html=True)
    
    # Text input for user's question
    user_question = st.text_input("Your question", key='user_question')

    # Button to submit the question
    ask_button = st.button("Enter")

    if ask_button:
        # Placeholder for handling the user's question
        st.write(f"You asked: {user_question}")
        # Here you would include the logic for processing the question

if __name__ == "__main__":
    page2()

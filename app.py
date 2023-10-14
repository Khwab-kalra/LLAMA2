import streamlit as st

import llama

messages = []

def main():
    st.title("LLAMA 2 : An unprecedented LLM experience")

    if ' chat_history' not in st.session_state:
        st.session_state.chat_history = ""

    st.info("Please Enter your queries")
    input_text = st.text_area("Send a Message")
   
    if input_text is not None:
        if st.button("Send"):
            st.info("Hey! Glad to answer about "+ input_text)
            st.session_state.chat_history += "User:" + " " + str(input_text) + "\n"
            result = llama.get_res(input_text)
            st.session_state.chat_history += "Buddy:" + " "+str(result)+ "\n"
            st. success("Result: " + str(result))
        session_data = "\n" + st.session_state.chat_history+"\n"        
        st.text_area("History: ", value = session_data, height=300)
        messages.append(session_data)

if __name__ == "__main__":
    main()


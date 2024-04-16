import streamlit as st
from streamlit_chat import message

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

openai_api_key = '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'

def main():

    chat = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key)

    # initialize message history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are a helpful assistant for a tea production company.")
        ]

    st.header("Tea Production Company ChatGPT 🤖")

    # sidebar with user input
    with st.sidebar:
        user_input = st.text_input("Your message: ", key="user_input")

        # handle user input
        if user_input:
            st.session_state.messages.append(HumanMessage(content=user_input))
            with st.spinner("Thinking..."):
                response = chat(st.session_state.messages)

            st.session_state.messages.append(
                AIMessage(content=response.content))
            
    try:
        st.text_area("Bot:", value=response.content, height=200)

    except:
        pass
    # display message history
    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            st.text_area("Bot:", value=response.content, height=200)
        else:
            st.text_area("Bot:", value=response.content, height=200)


if __name__ == '__main__':
    main()

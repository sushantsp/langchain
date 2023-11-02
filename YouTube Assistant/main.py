import streamlit as st 
import langchain_helper as lch 
import textwrap


st.title("YouTube Assistant - Ask questions about the video !")

with st.sidebar:
    with st.form(key="my_form"):
        youtube_url = st.sidebar.text_area(
            label = "what is the YouTube URL ?",
            max_chars= 50
        )

        query = st.sidebar.text_area(
            label = "what is your query ?",
            max_chars= 50,
            key= "query"
        )

        # open_ai_api_key = st.sidebar.text_input(
        #     label = "Open AI API Key",
        #     key = "langchain_search_api_key_openai",
        #     max_chars=50,
        #     type= "password"
        # )

        # "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
        # "[View the source code](https://github.com/rishabkumar7/pets-name-langchain/tree/main)"
        submit_button = st.form_submit_button(label="Submit")




if query and youtube_url:

    if not open_ai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    else:
        db = lch.create_vector_db_from_youtube_url(youtube_url)
        response, docs = lch.response_from_query(db, query)

        st.subheader("Answer")
        st.text(textwrap.fill(response, width= 80))

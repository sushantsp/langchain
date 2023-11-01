import langchain_helper as lch 
import streamlit as st 


st.title("Pet Name Generator")

user_animal_type = st.sidebar.selectbox("What is your pet ?", ("cat", "dog", "cow", "hamster"))

if user_animal_type == "cat":
    pet_color = st.sidebar.text_area("What color is your cat ?", max_chars=15)

if user_animal_type == "dog":
    pet_color = st.sidebar.text_area("What color is your dog ?", max_chars=15)

if user_animal_type == "cow":
    pet_color = st.sidebar.text_area("What color is your cow ?", max_chars=15)

if user_animal_type == "hamster":
    pet_color = st.sidebar.text_area("What color is your hamster ?", max_chars=15)


if pet_color:
    response = lch.generate_pet_names(user_animal_type, pet_color)
    st.text(response)
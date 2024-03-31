import streamlit as st
st.title("Hey all")
name = st.text_input("Type your name")
 st.write(name, "How are you?")
 bla = st.text_input("FIne or Not fine")
 if bla == "Fine":
  st.write("Cool!")
 else:
  st.write("Poor guy, deal with it...hehe")

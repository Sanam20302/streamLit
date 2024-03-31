import streamlit as st
st.title("Hey all")
bla = st.text_input("How are you? fine/not fine")
if bla == "fine":
  st.write("Cool!") 
elif bla == " ":
  print("type something")
else:
  st.write("Whatever deal with it...hehe")

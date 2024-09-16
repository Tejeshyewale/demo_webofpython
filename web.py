import streamlit as st
st.title("----Welcome to the Tejesh yewale's Website----")
name=st.text_input("Enter Your Name :")
Fathers_name=st.text_input("Enter Your Fathers Name : ")
add=st.text_area("Enter Your Text :")
classd=st.selectbox("Enter Your Class:",(1,2,3,4,5,6,7,8,9))
b=st.button("Done")
if b : st.markdown(f"name :{name} fathers name :{Fathers_name} Address :{add}")
import streamlit as st


name = st.text_input("Enter your Name : ")
fname = st.text_input("Enter your father name : ")
adr = st.text_area("Enter your Text")
classdata = st.selectbox("Enter your Class Name :",(1,2,3,4,5))

button = st.button("Submit")

if button :
    st.markdown(f"""
        Name : {name}  
        Father Name : {fname}
        Address : {adr}
        Class: {classdata}""")


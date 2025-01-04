import streamlit as st
import numpy as np

st.header("IriseCHat 1.0")
st.subheader("Irise chat answer questions about our services and other areas, you can ask questions in Haitian Creole, english, or spanish")

st.text("")




with st.chat_message("user"):
    st.write("Hello, /nBonjou, /nHola /n👋, /nhow can I help, ")
    st.write("how can I help?, /n komanm ka ede?, /ncomo puedo ayudar? ")
    st.line_chart(np.random.randn(30, 3))
    
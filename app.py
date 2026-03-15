import streamlit as st

st.title("Mental Stress Detection App")

st.write("This simple AI app predicts stress level based on behaviour.")

typing_speed = st.slider("Typing Speed",20,100,50)
typing_errors = st.slider("Typing Errors",0,10,2)
screen_time = st.slider("Screen Time (hours)",0,10,3)

if st.button("Predict Stress"):

    if typing_errors <= 2:
        st.success("Relaxed")

    elif typing_errors <=5:
        st.warning("Moderate Stress")

    else:
        st.error("High Stress")
      

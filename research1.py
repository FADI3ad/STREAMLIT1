import streamlit as st

def show():
    # صورة من الجهاز
    st.image(
        "humen.jpg",   # اسم الملف عندك
        width=300,
        
        caption="Astronauts aboard the International Space Station (ISS)",
        use_container_width=True
    )

    # العنوان
    st.markdown(
        """
        <h1 style="color:white;">🔬The Effects of Space on Humans</h1>
        """,
        unsafe_allow_html=True
    )
    
    # النصوص
    st.markdown(
        """
        <p style="color:white; font-size:16px;">
        Space has a strong impact on the human body and mind.  
        In microgravity, muscles and bones become weaker because they are not used as much.  
        Astronauts can lose bone density and muscle mass over time.  
        The heart and blood circulation also change, which can cause dizziness when returning to Earth.  
        Exposure to cosmic radiation increases the risk of cancer and other diseases.  
        Space can also affect vision and cause swelling in the head due to fluid shifting.  
        In addition, astronauts may suffer from stress, isolation, and sleep problems because of the unusual environment and long missions.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.success(
        "✅ Summary: Space has strong effects on the human body and mind, requiring medical protocols and training to reduce risks."
    )

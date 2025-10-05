import streamlit as st

def show():
    
    st.image(
        "micro.jpg",   # اسم الملف عندك
        caption="Astronauts aboard the International Space Station (ISS)",
        use_container_width=True
    )
    st.markdown(
        """
        <h1 style="color:white;">🦠The Effect of Space on Microorganisms</h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <p style="color:white; font-size:16px;">
        Space has significant effects on microorganisms.  
        Microgravity, radiation, and the closed space environment can change microbial growth, gene expression, and resistance.  
        Some microbes may become more virulent or resistant to antibiotics in space, while others may show slower growth.  
        This makes studying microorganisms in space important for astronaut health and future space missions.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.success(
        "✅ Summary: Space can alter microbial growth and resistance, making research essential for astronaut safety and long-term missions."
    )

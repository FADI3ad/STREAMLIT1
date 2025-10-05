import streamlit as st

def show():
    st.image(
        "planets.jpg",   # اسم الملف عندك
        caption="Astronauts aboard the International Space Station (ISS)",
        use_container_width=True
    )

        
    st.markdown(
        """
        <h1 style="color:white;">🌱 The Effects of Space on Plants</h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <p style="color:white; font-size:16px;">
        Plants in space experience many challenges due to the lack of gravity.  
        Without gravity, their roots do not know which direction to grow, and stems may not grow upward as on Earth.  
        Microgravity also changes how water and nutrients move in the soil, which affects growth.  
        In addition, space radiation can damage plant cells and slow development.  
        However, plants are very important for space missions because they provide food, oxygen, and help recycle air.  
        Scientists study how plants adapt to space to support future long-term missions to the Moon and Mars.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.success(
        "✅ Summary: Plants face many challenges in space, but they are essential for providing food, oxygen, and life support in long-term missions."
    )

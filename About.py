import streamlit as st

def show():
    # صورة من الجهاز
    st.image(
        "nasa.jpg",   # اسم الملف عندك
        
        caption="Astronauts aboard the International Space Station (ISS)",
        use_container_width=True
    )

    # العنوان
    st.markdown(
        """
        <h1 style="color:white;">🚀 About NASA</h1>
        """,
        unsafe_allow_html=True
    )
    
    # النصوص
    st.markdown(
        """
        <p style="color:white; font-size:16px;">
        <b>NASA</b> stands for the <b>National Aeronautics and Space Administration</b>, 
        which is the United States government agency responsible for the nation’s civilian space program, 
        as well as research in aeronautics (the science of flight) and aerospace.  
        It was established in 1958, replacing the National Advisory Committee for Aeronautics (NACA), 
        to lead U.S. space exploration efforts and scientific discoveries beyond Earth.
        </p>

        <h3 style="color:#FFD700;">🌌 Why NASA’s Research Is Important:</h3>

        <ul style="color:white; font-size:16px;">
            <li><b>1. Space Exploration & Discovery –</b> NASA helps humanity understand the universe, other planets, and our place in space, including the search for life beyond Earth.</li>
            <li><b>2. Earth Science & Climate Monitoring –</b> NASA satellites and missions track weather, natural disasters, and climate change, providing critical data for environmental protection and sustainability.</li>
            <li><b>3. Technology Innovation –</b> Many technologies we use today (GPS enhancements, memory foam, water purification systems, medical imaging improvements) came from NASA research.</li>
            <li><b>4. Aeronautics Advancements –</b> NASA develops safer, faster, and more fuel-efficient aircraft designs, shaping the future of air travel.</li>
            <li><b>5. Inspiration & Education –</b> NASA’s work inspires curiosity, innovation, and global collaboration in science, technology, engineering, and mathematics (STEM).</li>
            <li><b>6. National Security & Leadership –</b> NASA’s exploration and research maintain U.S. leadership in science and technology, fostering international partnerships.</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

    st.success(
        "✅ Summary: NASA plays a vital role in exploration, science, technology, climate monitoring, and inspiring future generations."
    )

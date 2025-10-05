import streamlit as st
import base64
import About, research1, research2, research3
from streamlit_option_menu import option_menu

# دالة لتحويل الصورة Base64
def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# استدعاء الصورة
img = get_base64("s.jpg")

# CSS للخلفية + تنسيق الأزرار
page_bg = f"""
<style>
.stApp {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

.sidebar .sidebar-content {{
    background: rgba(255,255,0,0.8); /* لون شفاف */
    padding: 20px;
    border-radius: 15px;
}}

button[data-baseweb="button"] {{
    font-size: 18px !important; /* حجم مناسب */
    font-weight: bold;
    padding: 10px 15px;
    margin: 8px 0;
    border-radius: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
}}
button[data-baseweb="button"]:hover {{
    background-color: #45a049;
    color: #fff;
}}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

st.title("NASA Jet Propulsion")

# القائمة الجانبية
with st.sidebar:
    selected = option_menu(
        "NASA RESEARCHES",
        ["About NASA","🌌👨 The impact of space on humans", "🌌🌱 The effect of space on plants", "🌌🦠 The effect of space on microorganisms"],
      
        menu_icon="cast",
        default_index=0,
        styles={
            "nav-link": {"font-size": "18px", "font-weight": "bold", "text-align": "left", "margin":"10px"},
            "nav-link-selected": {"background-color": "#4CAF50", "color": "white"},
        }
    )

# عرض المحتوى حسب الاختيار
if selected == "About NASA":
    About.show()
    

elif selected == "🌌👨 The impact of space on humans":
    research1.show()


elif selected == "🌌🌱 The effect of space on plants":
    research2.show()


elif selected == "🌌🦠 The effect of space on microorganisms":
    research3.show()   # ده ملف جديد للكائنات الدقيقة

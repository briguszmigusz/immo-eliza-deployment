import streamlit as st
from predict import predict_price
import base64

# Setting up the page
st.set_page_config(page_title="Immo Eliza Price Predictor",
    page_icon="🏡",
    layout="wide")

# Sidebar information
st.sidebar.markdown("""
ℹ️
**Immo Eliza Price Predictor** estimates real estate prices in Belgium  
based on property features such as size, location, condition, and amenities.

## 📌 Disclaimer
- This tool is part of a **learning project** created during the AI Bootcamp at **BeCode.org**.
- Predictions are **not 100% accurate** and should **not** be used as professional financial advice.
- The model is trained on a limited dataset and provides only an **approximate** estimation.
""")

# Setting up the background picture
def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <style>
        body {{
                text-align: center;
        }}
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)

# Adding a togglebar on the right to change dark and light mode using columns
col_toggle_1, col_toggle_2 = st.columns([6,1])
with col_toggle_2:
    mode = st.toggle("🌗 Dark/Light mode")

# Changing background according to dark/light mode
if mode:
    set_bg("background_dark.jpg")
else:
    set_bg("background_light.jpg")

# Themes for light and dark mode
light_css = """
<style>
.form-card {
    background-color: rgba(255,255,255,0.75);
    backdrop-filter: blur(8px);
    padding: 25px;
    border-radius: 18px;
    max-width: 500px;
    margin: auto;
}
label, p, span, h1, h2, h3 {
    color: black !important;
}
</style>
"""

dark_css = """
<style>
.form-card {
    background-color: rgba(0,0,0,0.55);
    backdrop-filter: blur(8px);
    padding: 25px;
    border-radius: 18px;
    max-width: 500px;
    margin: auto;
}
label, p, span, h1, h2, h3 {
    color: white !important;
}
</style>
"""

st.markdown(dark_css if mode else light_css, unsafe_allow_html=True)

# For better looks
st.markdown("""
<style>

/* Section dividers */
.section-divider {
    height: 2px;
    margin: 2px 0 6px 0;
    border-radius: 5px;
}
.light-divider { background: rgba(0,0,0,0.3); }
.dark-divider { background: rgba(255,255,255,0.3); }


/* Nice Button */
.stButton { display: flex; justify-content: center; }
.stButton > button {
    background-color: #6949FD !important;
    color: white !important;
    padding: 18px 48px !important;
    border-radius: 14px !important;
    font-size: 22px !important;
    font-weight: bold !important;
    border: none !important;
    cursor: pointer !important;
    box-shadow: 0px 4px 16px rgba(105,73,253,0.35);
    transition: 0.2s ease-in-out;
}
.stButton > button:hover {
    background-color: #5833e3 !important;
    transform: scale(1.05);
}

/* Footer */
.footer {
    margin-top: 45px;
    text-align: center;
    opacity: 0.6;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# Title and description
st.title("🏡 Immo Eliza – Property Price Predictor")
st.write("Enter the details of your property below to estimate its ~value.")

# Property details
st.markdown("### 🏠 Property Details")
st.markdown("<div class='section-divider {}'></div>".format("dark-divider" if mode else "light-divider"), unsafe_allow_html=True)

ui_property_types = ["Apartment", "House", "Villa", "Cottage", "Bungalow","Studio", "Office", "Land", "Penthouse"]

type_mapping = {"Apartment": "apartment",
    "House": "master house",
    "Villa": "villa",
    "Cottage": "cottage",
    "Bungalow": "bungalow",
    "Studio": "studio",
    "Office": "office space",
    "Land": "land",
    "Penthouse": "penthouse",}

state_options = ["Excellent",
    "Fully renovated",
    "New",
    "Normal",
    "To be renovated",
    "To restore",
    "Under construction"]

state_mapping = {"To be renovated": "To renovate"}


heating_type_options = ["Gas", "Electricity", "Fuel oil", "Wood",
    "Coal", "Solar energy", "Hot air", "Not specified",]

ui_choice = st.selectbox("🏘 Property type", ui_property_types)
model_property_type = type_mapping[ui_choice]

# Condition and heating
st.markdown("### 🔥 Condition & Heating")
st.markdown("<div class='section-divider {}'></div>".format("dark-divider" if mode else "light-divider"),unsafe_allow_html=True)

colA, colB = st.columns(2)

with colA:
    heating_type = st.selectbox("🔥 Type of heating", heating_type_options)

with colB:
    state = st.selectbox("🏗 State of the property", state_options)

# Size and structure
st.markdown("### 📐 Size & Structure")
st.markdown("<div class='section-divider {}'></div>".format("dark-divider" if mode else "light-divider"), unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input("🛏 Bedrooms", 0, 10, 2)
    bathrooms = st.number_input("🚿 Bathrooms", 0, 5, 1)
    facades = st.number_input("🏢 Number of facades", 1, 4, 2)

with col2:
    living_surface = st.number_input("📐 Livable surface (m²)", 10, 1000, 75)
    toilets = st.number_input("🚽 Toilets", 0, 5, 1)
    postal_code = st.number_input("📍 Postal code", 1000, 9999, 1000)

# Extra features
st.markdown("### 🌿 Extra Features")
st.markdown("<div class='section-divider {}'></div>".format("dark-divider" if mode else "light-divider"),unsafe_allow_html=True)

garden = st.checkbox("🌳 Garden")
terrace = st.checkbox("🌅 Terrace")
elevator = st.checkbox("🛗 Elevator")

# Predict button
if st.button("# 💶 __*Predict Price*__"):
    state_for_model = state_mapping.get(state, state)

    data = {"State of the property": state,
        "Number of bedrooms": bedrooms,
        "Livable surface": living_surface,
        "Number of bathrooms": bathrooms,
        "Number of toilets": toilets,
        "Type of heating": heating_type,
        "Elevator": int(elevator),
        "Number of facades": facades,
        "Garden": int(garden),
        "Terrace": int(terrace),
        "type": model_property_type,
        "postal_code": postal_code,}

    try:
        price = predict_price(data)
        # Choose correct card style
        st.success(f"💶 Estimated price: ~{price:,.0f} €")
    except Exception as e:
        st.error(f"Something went wrong: {e}")

# Footer on the bottom
st.markdown("<div class='footer'>Created during the AI Bootcamp at BeCode.org • 2025</div>", unsafe_allow_html=True)
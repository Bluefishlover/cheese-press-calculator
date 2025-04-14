
import streamlit as st
import math
from PIL import Image

st.set_page_config(page_title="Cheese Press Force Calculator", layout="centered")

st.markdown("## 🧀 Cheese Press Force Calculator")
press_type = st.radio("Select your press type:", ["Lever Press", "Direct Top Press"])

if press_type == "Lever Press":
    image = Image.open("lever_press.png")
    with st.expander("📸 See Lever Press Diagram"):
        st.image(image, use_container_width=True)
else:
    image = Image.open("direct_top_press.png")
    with st.expander("📸 See Direct Top Press Diagram"):
        st.image(image, use_container_width=True)

unit_system = st.radio("Choose unit system:", ["Imperial (lbs)", "Metric (N)"])
if "Imperial" in unit_system:
    gravity = 1
    unit_weight = "lbs"
    unit_length = "in"
    unit_force = "lbs"
else:
    gravity = 9.81
    unit_weight = "kg"
    unit_length = "cm"
    unit_force = "N"

st.markdown("## Enter Press Parameters")

if press_type == "Lever Press":
    weight = st.number_input(f"Applied Weight ({unit_weight})", min_value=0.0)
    L1 = st.number_input(f"Distance from Pivot to Cheese (L1) [{unit_length}]", min_value=0.01)
    L2 = st.number_input(f"Distance from Pivot to Weight (L2) [{unit_length}]", min_value=0.0)
else:
    weight = st.number_input(f"Weight Applied to Top Board ({unit_weight})", min_value=0.0)
    L1 = L2 = 1  # dummy values not used

st.markdown("## Force Applied to Cheese")
if weight and L1:
    if press_type == "Lever Press":
        force = (weight * L2 / L1) * gravity
    else:
        force = weight * gravity

    st.success(f"Applied Force on Cheese: {force:.2f} {unit_force}")
else:
    st.warning("Please fill in all required fields to see results.")

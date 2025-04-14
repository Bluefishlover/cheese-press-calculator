
import streamlit as st
import math
from PIL import Image

st.set_page_config(page_title="Cheese Press Pressure Calculator", layout="centered")

st.markdown("## 🧀 Cheese Press Pressure Calculator")
press_type = st.radio("Select your press type:", ["Lever Press", "Direct Top Press"])

image = Image.open("Press weight calculations.png")
with st.expander("📸 See Press Diagram"):
    st.image(image, use_container_width=True)

unit_system = st.radio("Choose unit system:", ["Imperial (lbs/in²)", "Metric (kg/cm²)"])
if "Imperial" in unit_system:
    gravity = 1
    unit_weight = "lbs"
    unit_length = "in"
    unit_area = "in²"
    unit_pressure = "lbs/in²"
else:
    gravity = 9.81
    unit_weight = "kg"
    unit_length = "cm"
    unit_area = "cm²"
    unit_pressure = "kg/cm²"

st.markdown("## Enter Press Parameters")

if press_type == "Lever Press":
    weight = st.number_input(f"Applied Weight ({unit_weight})", min_value=0.0)
    L1 = st.number_input(f"Distance from Pivot to Cheese (L1) [{unit_length}]", min_value=0.01)
    L2 = st.number_input(f"Distance from Pivot to Added Weight (L2) [{unit_length}]", min_value=0.0)
elif press_type == "Direct Top Press":
    weight = st.number_input(f"Applied Weight ({unit_weight})", min_value=0.0)
    L1 = L2 = 1  # dummy values not used

shape = st.radio("Cheese Shape", ["Round", "Rectangular", "Manual"])
if shape == "Round":
    diameter = st.number_input(f"Diameter of cheese ({unit_length})", min_value=0.01)
    area = math.pi * (diameter / 2) ** 2
elif shape == "Rectangular":
    length = st.number_input(f"Length of cheese ({unit_length})", min_value=0.01)
    width = st.number_input(f"Width of cheese ({unit_length})", min_value=0.01)
    area = length * width
else:
    area = st.number_input(f"Enter surface area directly ({unit_area})", min_value=0.01)

st.markdown("## Pressure on Cheese")
if weight and L1 and area:
    if press_type == "Lever Press":
        force = (weight * L2 / L1) * gravity
    else:
        force = weight * gravity

    if "Metric" in unit_system:
        pressure = (force / 9.81) / area
    else:
        pressure = force / area

    st.success(f"Pressure on Cheese: {pressure:.3f} {unit_pressure}")
else:
    st.warning("Please fill in all required fields to see results.")

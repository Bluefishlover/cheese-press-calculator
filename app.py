
import streamlit as st
import math
from PIL import Image

st.set_page_config(page_title="Cheese Press Pressure Calculator", layout="centered")

st.markdown("""
# 🧀 Cheese Press Pressure Calculator
Use this tool to calculate the pressure applied to your cheese curds using a lever-arm cheese press.
""")

# Load image
image = Image.open("Press weight calculations.png")
with st.expander("📸 See Lever Press Diagram"):
    st.image(image, use_column_width=True)

st.markdown("## Step 1: Select Units")
unit_system = st.radio("Choose unit system:", ["Imperial (lbs/in²)", "Metric (kg/cm²)"])
if "Imperial" in unit_system:
    gravity = 1
    unit_weight = "lbs"
    unit_length = "in"
    unit_area = "in²"
    unit_force = "lbs"
    unit_pressure = "lbs/in²"
else:
    gravity = 9.81
    unit_weight = "kg"
    unit_length = "cm"
    unit_area = "cm²"
    unit_force = "N"
    unit_pressure = "kg/cm²"

st.markdown("## Step 2: Enter Lever Press Parameters")
weight = st.number_input(f"Applied Weight ({unit_weight})", min_value=0.0)
L1 = st.number_input(f"Distance from Pivot to Weight (L1) [{unit_length}]", min_value=0.01)
L2 = st.number_input(f"Distance from Pivot to Cheese (L2) [{unit_length}]", min_value=0.0)

st.markdown("## Step 3: Describe Cheese Surface Area")
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

st.markdown("## Step 4: Results")
if weight and L1 and area:
    # Correct formula: Force = Weight × (L2 / L1)
    force = (weight * L2 / L1) * gravity
    if "Metric" in unit_system:
        pressure = (force / 9.81) / area  # convert N to kg, then divide by cm²
    else:
        pressure = force / area

    st.success(f"Applied Force on Cheese: {force:.2f} {unit_force}")
    st.success(f"Pressure on Cheese: {pressure:.3f} {unit_pressure}")
else:
    st.warning("Please fill in all required fields to see results.")

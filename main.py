import streamlit as st
import pandas as pd
import math
import numpy as np

def convertTORadians(degree):
    return degree * math.pi / 180

GRAVITY = -9.8

st.title("Projectile Motion Calculator")

st.write("### Input Data")
col1, col2, col3 = st.columns(3)
velocity = col1.number_input("Velocity", min_value=0, value=10)
omega = convertTORadians(col2.slider("Angle From Ground", min_value=0, value=45, max_value=180))
alpha = convertTORadians(col3.slider("Incline", min_value=0, value=0, max_value=180))

ux = round(2 * velocity * math.cos(omega), 5)
uy = round(2 * velocity * math.sin(omega), 5)

gx = GRAVITY * math.sin(alpha)
gy = GRAVITY * math.cos(alpha)

TOF = -2*uy/gy
MAX_HEIGHT = -(uy**2)/(2*gy)

time = np.arange(0, TOF, 0.001)

x = ux * time + 1/2 * gx * (time**2)
y = uy * time + 1/2 * gy * (time**2)

RANGE = ux * TOF + 1/2 * gx * (TOF**2)

st.write("### Values")
col4, col5, col6 = st.columns(3)
col4.metric(label = "Time of flight", value = f"{round(TOF, 2)}")
col5.metric(label = "Max Height", value = f"{round(MAX_HEIGHT, 2)}")
col6.metric(label = "Range", value = f"{round(RANGE, 2)}")

df = pd.DataFrame(y, x)

st.write("### Trajectory")
payments_df = df
st.line_chart(payments_df)
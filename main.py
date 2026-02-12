import time
from collections import deque

import serial
import streamlit as st

PORT = "/dev/ttyUSB0"
BAUD = 9600

irrigation = False

st.set_page_config(page_title="Soil Monitoring", layout="wide")
st.title("Soil Monitoring")

placeholder = st.empty()
warning_placeholder = st.empty()

data = deque(maxlen=50)
t0 = time.time()


if "ser" not in st.session_state:
    st.session_state.ser = serial.Serial(PORT, BAUD, timeout=1)
ser = st.session_state.ser

with serial.Serial(PORT, baudrate=BAUD) as ser:
    while True:
        line = ser.readline().decode(errors='ignore').strip()
        if line:
            try:
                val = int(line)
                data.append(val)
            except:
                pass

        placeholder.line_chart(list(data))

        if len(data) > 0 and data[-1] < 30:
            irrigation = True
            warning_placeholder.warning("Irrigation required")
        else:
            irrigation = False
            warning_placeholder.empty()

        time.sleep(1)
# SoilMonitoring

A small IoT prototype I built to monitor soil moisture in real time and trigger irrigation alerts when the soil gets too dry.

The system uses an Arduino Nano to read data from a capacitive soil moisture sensor and sends it over serial to a Raspberry Pi. On the Pi side, there's a simple Streamlit app that shows a live chart and warns you when the moisture drops below 30%.

This project was made for a research preprint I published on ResearchGate.

## How it works

The Arduino reads the sensor value from pin A3 every second and maps it to a 0–100% scale, then prints it to serial at 9600 baud. The Python app reads that stream and plots the last 50 readings on a live chart. If the latest value is below 30%, it shows an irrigation warning on screen.

## Run

Make sure the Arduino sketch is uploaded and connected via USB, then install the dependencies:

```bash
pip install streamlit pyserial
```

Run the dashboard:

```bash
streamlit run main.py
```

The default port is `/dev/ttyUSB0`. You can change it at the top of `main.py` if your system uses a different one.

import streamlit as st
import amplitude
from amplitude import BaseEvent, EventOptions
import time

# Initialize Amplitude client with your API key
AMPLITUDE_API_KEY = '98b11c5f413004992c62dacea60f6170'  # Your Amplitude API key
amplitude_client = amplitude.Amplitude(AMPLITUDE_API_KEY)

# Function to send events to Amplitude
def send_amplitude_event(event_name, event_properties=None):
    event = BaseEvent(
        event_type=event_name,
        event_properties=event_properties
    )
    amplitude_client.track(event)

# Example: Track a page view event
send_amplitude_event('Page View')

# Your original Streamlit app code
st.title('My Streamlit App')

# Track button clicks with Amplitude
if st.button('Click Me'):
    send_amplitude_event('Button Click')

# Track text input interaction
text_input = st.text_input('Enter something:')
if text_input:
    send_amplitude_event('Text Input', {'input_value': text_input})

# Log time spent on the page (page view duration)
start_time = time.time()

# When the user clicks this button, log the duration
if st.button('Log Time'):
    duration = time.time() - start_time
    send_amplitude_event('Page View Duration', {'duration_seconds': duration})

import streamlit as st
import random
import time

# Define the moves for each mode
kickboxer_moves = [
    "Jab",
    "Cross",
    "Roundhouse Kick",
    "Front Kick",
    "Hook Punch",
    "Uppercut",
    "Side Kick",
    "Elbow Strike"
]

chi_sau_moves = [
    "Tan Sau (Palm-Up Block)",
    "Bong Sau (Wing Arm)",
    "Fuk Sau (Resting Hand)",
    "Pak Sau (Slapping Hand)",
    "Lap Sau (Pulling Hand)",
    "Jum Sau (Sinking Hand)",
    "Huen Sau (Circling Hand)",
    "Wu Sau (Protecting Hand)"
]

def run_reaction_drill(moves, duration, mode):
    """Runs the reaction drill with given moves and duration."""
    start_time = time.time()
    placeholder = st.empty()

    while time.time() - start_time < duration * 60:
        move = random.choice(moves)
        interval = random.randint(3, 10)

        with placeholder.container():
            if mode == "Vs Kickboxer":
                st.subheader(f"Defend against: {move}")
            else:
                st.subheader(f"Perform: {move}")
            st.write(f"Next move in {interval} seconds")

        time.sleep(interval)

    placeholder.empty()
    st.write("Drill complete! Good job!")

# Streamlit app
st.title("Wing Chun Reaction Drill")

# Select mode
mode = st.selectbox(
    "Select Mode:",
    ("Vs Kickboxer", "Chi Sau")
)

# Set duration
duration = st.slider(
    "Select drill duration (minutes):", 
    min_value=1, max_value=30, value=5, step=1
)

# Start drill
if st.button("Start Drill"):
    st.write("Starting drill...")
    if mode == "Vs Kickboxer":
        run_reaction_drill(kickboxer_moves, duration, mode)
    elif mode == "Chi Sau":
        run_reaction_drill(chi_sau_moves, duration, mode)

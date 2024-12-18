import streamlit as st
import os
import openai
import random
import time
import tkinter as tk
from playsound import playsound
import pygame
from threading import Thread
from dotenv import load_dotenv
import sys
import signal


# Global flag to stop the session
stop_flag = False

# Stop the session function
def stop_session():
    global stop_flag
    stop_flag = True
    st.info("Session stopped!")

# Load environment variables
load_dotenv(".env")
openai.api_key = os.environ["OPENAI_API_KEY"]

# Initialize OpenAI client and specify model
client = openai.OpenAI()
model = 'gpt-4o-mini'

# Randomly select a reward
def randomly_select_reward():
    Rewards = ["Play Age of Mythology for 2 games", "Watch Naruto", "Age of mythology 1 game", "Watch an interesting YouTube video", "Choose yourself"]
    return random.choice(Rewards)

# Generate a compliment message with OpenAI
def get_compliment(work_type, random_reward):
    person = "Fabian is a student that likes AI, programming, video games, medievel magical worlds, and Nordic mythology"
    prompt = f"Return a short, simple yet creative compliment related to effort, dedication, the type of person and the type of work being done. Its important that the compliment is related to effort and dedication. In the end of the message, kindly provide the random reward and tell the user to enjoy it. Random reward = {random_reward}. Work type = {work_type}. Person = {person}."
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.with_raw_response.create(
        messages=messages,
        model=model,
    )
    return response.parse().choices[0].message.content.strip()

# Show the reward popup with sound and topmost window, with golden theme
def show_reward(compliment):
    pygame.mixer.init()
    pygame.mixer.music.load("reward_sound.mp3")
    pygame.mixer.music.play()

    root = tk.Tk()
    root.withdraw()

    custom_popup = tk.Toplevel(root)
    custom_popup.title("🎉 Reward! 🎉")
    custom_popup.geometry("800x600")
    custom_popup.attributes("-topmost", True)
    custom_popup.configure(bg="#FFD700")

    label = tk.Label(custom_popup, text=compliment, wraplength=380, justify="center", bg="#FFD700", fg="black", font=("Arial", 14))
    label.pack(pady=20, padx=20)

    ok_button = tk.Button(custom_popup, text="LETS GO", command=custom_popup.destroy, bg="#FFA500", fg="white", font=("Arial", 12))
    ok_button.pack(pady=10)

    root.mainloop()
    pygame.mixer.music.stop()

# Show end-of-session popup if no reward was received
def show_boring_break():
    root = tk.Tk()
    root.withdraw()

    boring_popup = tk.Toplevel(root)
    boring_popup.title("Session Complete")
    boring_popup.geometry("600x400")
    boring_popup.attributes("-topmost", True)
    boring_popup.configure(bg="#FFD700")

    label = tk.Label(boring_popup, text="Good job, session is done! This time you will have a boring break by laying in bed or staring at the wall.", wraplength=400, justify="center", bg="#FFD700", fg="black", font=("Arial", 14))
    label.pack(pady=20, padx=20)

    ok_button = tk.Button(boring_popup, text="OK", command=boring_popup.destroy, bg="#FFA500", fg="white", font=("Arial", 12))
    ok_button.pack(pady=10)

    root.mainloop()



# Main function that controls the work session
def run_session(work_type, session_time, num_reward):
    global stop_flag
    stop_flag = False  # Reset the flag at the start of a new session
    session_time_seconds = int(session_time) * 60
    interval_duration = session_time_seconds / int(num_reward)
    elapsed_time = 0
    reward_given = False

    while elapsed_time < session_time_seconds:
        if stop_flag:
            st.warning("Session stopped by user.")
            break

        time.sleep(interval_duration)
        elapsed_time += interval_duration
        # 20% chance to show the reward popup at each interval
        if random.random() < 0.2:
            random_reward = randomly_select_reward()
            compliment = get_compliment(work_type, random_reward)
            show_reward(compliment)
            reward_given = True

    # 75% chance to show the reward popup at the end of the session
    if not reward_given and random.random() < 0.75:
        random_reward = randomly_select_reward()
        compliment = get_compliment(work_type, random_reward)
        show_reward(compliment)
    elif not reward_given:
        # Show a "boring break" popup if no reward was received during the session
        show_boring_break()




# Streamlit interface
def main():
    st.title("Intermittent Reward Timer")

    work_type = st.text_input("What kind of work are you doing?")
    session_time = st.text_input("How many minutes are you planning to work?", "30")
    num_reward = st.text_input("How many rewards do you want to potentially receive?", "3")

    if st.button("Start Session"):
        if work_type and session_time.isdigit() and num_reward.isdigit():
            st.success("Your session has started! You can minimize this window.")
            Thread(target=run_session, args=(work_type, session_time, num_reward)).start()
        else:
            st.error("Please enter valid information for all fields.")
    if st.button("Stop Session"):
        stop_session()
if __name__ == "__main__":
    main()

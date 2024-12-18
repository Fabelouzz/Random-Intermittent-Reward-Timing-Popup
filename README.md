# Random Intermittent Reward Timing (RIRT) Productivity Script

### Overview

Random Intermittent Reward Timing (RIRT) is a method from behavioral psychology that uses unpredictable rewards to sustain engagement. Rather than receiving rewards at fixed intervals, users receive them randomly, creating a sense of anticipation that activates the brain’s dopamine system. Dopamine, associated with pleasure and motivation, spikes not only when a reward is received but also in the anticipation of it, making this method highly effective for maintaining focus and attention. RIRT leverages this response, adding excitement to work sessions and breaking up potential monotony, as the brain is kept alert, waiting for the next potential reward.

### How it Works

This script harnesses RIRT to enhance productivity by delivering random rewards during work sessions. The user sets their work type, session duration, and maximum number of rewards. From these, the script calculates intervals for checking reward chances, dividing the session duration by the number of rewards. Every interval, there is a 20% chance of a reward, giving users a regular but unpredictable chance for encouragement. If no rewards appear by the end of the session, the script performs a final check with a 75% chance of reward, adding closure to the session. If this check still yields no reward, a humorous popup suggests a “boring break,” gently encouraging anticipation for future rewards.

When a reward is triggered, the script uses OpenAI to generate a motivational message tailored to the user’s work, along with a fun activity suggestion. The message is delivered through a “golden” themed popup with a rewarding sound effect, reinforcing a pleasant experience. By introducing surprise elements and a hint of humor, the script keeps users engaged, effectively breaking up long sessions with brief, dopamine-boosting moments. In this way, the script uses RIRT principles to transform typical work sessions into more engaging, enjoyable experiences, supporting sustained productivity and motivation.

---

### Setup Guide

To use this script, follow the steps below:

#### 1. Install Dependencies
In your terminal, navigate to the project directory and run the following command to install the required dependencies:
```bash
pip install -r requirements.txt
```

#### 2. Create .env File
You will need to create a .env file in the project directory with your OpenAI API key. The file should look like this:

```bash
OPENAI_API_KEY=your-api-key-here
```

You can get your OpenAI API key by signing up at OpenAI's website.

#### 3. Adjust Reward Sound and Compliment Messages
Reward Sound: The default reward sound used in the script is the World of Warcraft leveling-up sound. You can replace it with any custom MP3 sound of your choice. Simply place your desired .mp3 file in the project directory and name it reward_sound.mp3.

Custom Compliment Messages: The get_compliment function generates motivational messages using OpenAI's chat completion API. You should modify this function to include instructions that match your preferences, such as the type of compliments you want or the name and interests you would like to be referenced. For example, you can instruct OpenAI to tailor the message to your specific work type or preferred motivational tone.

To modify the message, update the prompt in the **get_compliment function**

**Reward Types:**
You should also modify the randomly_select_reward function to match the type of rewards you want. This can include anything from activities like "Play a game" to practical rewards like "Take a break." Adjust the list of rewards in the function to suit your preferences

#### 4. Run the app
To run the app, simply write the following in your terminal browsing the project repository. This should open the app locally in your browser. 
```bash
streamlit run app.py
```



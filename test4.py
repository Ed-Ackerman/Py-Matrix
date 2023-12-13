import random
import time
from rich import print
import pyfiglet
import threading

source_1 = """
import numpy as np

class SelfImprovingAI:
    def __init__(self, num_states, num_actions, learning_rate=0.1, discount_factor=0.9):
        self.num_states = num_states
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

        # Initialize Q-table with zeros
        self.q_table = np.zeros((num_states, num_actions))

    def choose_action(self, state):
        # Exploration-exploitation trade-off
        if np.random.uniform(0, 1) < 0.1:  # Exploration
            return np.random.choice(self.num_actions)
        else:  # Exploitation
            return np.argmax(self.q_table[state, :])

    def update_q_table(self, state, action, reward, next_state):
        # Q-value update using the Bellman equation
        current_q_value = self.q_table[state, action]
        max_future_q_value = np.max(self.q_table[next_state, :])
        new_q_value = (1 - self.learning_rate) * current_q_value + self.learning_rate * (reward + self.discount_factor * max_future_q_value)
        self.q_table[state, action] = new_q_value

    def train(self, episodes):
        for episode in range(episodes):
            state = 0  # Initial state
            total_reward = 0

            while state != self.num_states - 1:  # Continue until reaching the goal state
                action = self.choose_action(state)
                # Simulate environment and get reward and next state
                next_state = state + 1 if action == 1 else state  # Simple environment
                reward = 1 if next_state == self.num_states - 1 else 0  # Reward is 1 if the goal state is reached
                total_reward += reward

                # Update Q-table
                self.update_q_table(state, action, reward, next_state)

                # Move to the next state
                state = next_state

            print(f"Episode {episode + 1}, Total Reward: {total_reward}")

if __name__ == "__main__":
    num_states = 5  # Number of states in the environment
    num_actions = 2  # Number of possible actions (0 or 1)
    learning_rate = 0.1
    discount_factor = 0.9

    ai = SelfImprovingAI(num_states, num_actions, learning_rate, discount_factor)
    ai.train(episodes=1000)

""" 
source_2 = """
import time
import random

class GodsEyeSimulator:
    def __init__(self, user):
        self.user = user
        self.target_coordinates = None

    def track_target(self, target):
        print(f"Initiating God's Eye tracking sequence for {target}...")
        time.sleep(2)
        self.target_coordinates = (random.uniform(-90, 90), random.uniform(-180, 180))
        print(f"Target {target} located at coordinates: {self.target_coordinates}")

    def hack_target(self):
        if self.target_coordinates:
            print("Initiating God's Eye hacking sequence...")
            time.sleep(3)
            print("Access granted. Gathering information...")
            # Simulated information gathering
            user_data = {
                'name': 'John Doe',
                'location': 'City XYZ',
                'email': 'john.doe@example.com',
                'phone': '555-1233.3'
            }
            print(f"Information gathered: {user_data}")
            return user_data
        else:
            print("No target coordinates available. Please track a target first.")

class Hacker:
    def __init__(self, gods_eye_simulator):
        self.gods_eye_simulator = gods_eye_simulator

    def compromise_gods_eye(self):
        print("Attempting to compromise God's Eye...")
        time.sleep(2)
        print("Compromised! Taking control...")
        self.gods_eye_simulator.target_coordinates = None
        print("God's Eye compromised. Target coordinates reset.")

if __name__ == "__main__":
    user = "Your Character"
    gods_eye = GodsEyeSimulator(user)

    target = "Target Person"
    gods_eye.track_target(target)

    hacker = Hacker(gods_eye)
    hacker.compromise_gods_eye()

    gods_eye.track_target(target)  # Attempting to track again after compromise
    gods_eye.hack_target()  # Attempting to hack again after compromise

"""

def draw_matrix_1(height, width, stop_flag):
    columns = width // 2
    drops = [1] * columns

    char_index_1 = 0

    while not stop_flag.is_set():
        for i in range(columns):
            text = source_1[char_index_1 % len(source_1)]
            char_index_1 += 1

            print(f"[green]{text}", end='', flush=True)
            drops[i] += 1

            if drops[i] > height and char_index_1 % len(source_1) == 0:
                drops[i] = 0

        time.sleep(0.0002)

def draw_matrix_2(height, width, stop_flag):
    columns = width // 2
    drops = [1] * columns

    char_index_2 = 0

    while not stop_flag.is_set():
        for i in range(columns):
            text = source_2[char_index_2 % len(source_2)]
            char_index_2 += 1

            print(f"[green]{text}", end='', flush=True)
            drops[i] += 1

            if drops[i] > height and char_index_2 % len(source_2) == 0:
                drops[i] = 0

        time.sleep(0.01)


def type_animation_with_pyfiglet():
    txt = pyfiglet.figlet_format("Pantheon Project")    
    for char in txt:
        print(char, end='', flush=True)
        time.sleep(0.03)  # Adjust the sleep time as needed

def main():
    height, width = 20, 60

    # Create an Event flag to control the matrix animation loop
    stop_flag = threading.Event()

    # Run the matrix animation in a separate thread
    matrix_thread = threading.Thread(target=draw_matrix_1, args=(height, width, stop_flag))
    matrix_thread.start()

    # Wait for the matrix to run for some time
    time.sleep(3.21)  # Adjust the duration as needed

    # Stop the matrix animation
    stop_flag.set()
    matrix_thread.join()

    # Run the Pyfiglet animation
    type_animation_with_pyfiglet()

    # Wait for "Pantheon" to run for some time
    time.sleep(3.3)  # Adjust the duration as needed

    # Restart the matrix animation
    stop_flag.clear()
    matrix_thread = threading.Thread(target=draw_matrix_2, args=(height, width, stop_flag))
    matrix_thread.start()

    # Wait for the matrix to run for some time
    time.sleep(3)  # Adjust the duration as needed

    # Stop the matrix animation
    stop_flag.set()
    matrix_thread.join()

if __name__ == "__main__":
    main()

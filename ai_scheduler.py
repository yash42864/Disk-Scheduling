# ai_scheduler.py
import numpy as np

class AI_DiskScheduler:
    def __init__(self, disk_size=200, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.disk_size = disk_size
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = np.zeros((disk_size, disk_size))

    def choose_action(self, state):
        """Epsilon-Greedy Policy"""
        if np.random.rand() < self.epsilon:
            return np.random.randint(0, self.disk_size)
        return np.argmax(self.q_table[state])

    def update_q_table(self, state, action, reward, next_state):
        """Q-Learning Update Rule"""
        best_next_action = np.argmax(self.q_table[next_state])
        self.q_table[state, action] += self.alpha * (reward + self.gamma * self.q_table[next_state, best_next_action] - self.q_table[state, action])

    def train(self, requests, episodes=1000):
        """Train AI to optimize scheduling"""
        for _ in range(episodes):
            state = np.random.choice(requests)
            for _ in range(len(requests)):
                action = self.choose_action(state)
                reward = -abs(state - action)  # Minimize seek time
                next_state = action
                self.update_q_table(state, action, reward, next_state)
                state = next_state

    def schedule(self, requests, head):
        """Get optimized disk scheduling sequence"""
        sequence = [head]
        total_seek = 0
        while requests:
            action = self.choose_action(head)
            if action in requests:
                total_seek += abs(head - action)
                sequence.append(action)
                requests.remove(action)
                head = action
        return sequence, total_seek

import numpy as np
from sklearn.ensemble import RandomForestClassifier
import random

def generate_training_data(n_samples=1000):
    X = []
    y = []
    algorithms = ['FCFS', 'SSTF', 'SCAN', 'C-SCAN']
    
    for _ in range(n_samples):
        # Generate random sequence and head
        seq_length = random.randint(5, 15)
        requests = [random.randint(0, 199) for _ in range(seq_length)]
        head = random.randint(0, 199)
        
        # Calculate features
        features = [
            len(requests),
            np.var(requests) if requests else 0,
            np.mean([abs(x - head) for x in requests]) if requests else 0,
            head
        ]
        
        # Simulate algorithms
        seek_times = [
            fcfs(requests, head)[1],
            sstf(requests, head)[1],
            scan(requests, head)[1],
            cscan(requests, head)[1]
        ]
        
        # Label is the algorithm with minimum seek time
        best_algo = algorithms[np.argmin(seek_times)]
        X.append(features)
        y.append(best_algo)
    
    return np.array(X), y

def fcfs(requests, head):
    sequence = [head] + requests
    total_seek = sum(abs(sequence[i] - sequence[i-1]) for i in range(1, len(sequence)))
    return sequence, total_seek

def sstf(requests, head):
    remaining = requests.copy()
    sequence = [head]
    total_seek = 0
    current = head
    
    while remaining:
        min_dist = float('inf')
        next_pos = None
        for pos in remaining:
            dist = abs(current - pos)
            if dist < min_dist:
                min_dist = dist
                next_pos = pos
        total_seek += min_dist
        current = next_pos
        sequence.append(current)
        remaining.remove(current)
    
    return sequence, total_seek

def scan(requests, head, direction='right'):
    sequence = [head]
    total_seek = 0
    sorted_requests = sorted(requests)
    current = head
    
    if direction == 'right':
        right = [x for x in sorted_requests if x >= current]
        left = [x for x in sorted_requests if x < current][::-1]
        for pos in right:
            total_seek += abs(current - pos)
            current = pos
            sequence.append(current)
        if left:
            total_seek += abs(current - 199)
            current = 199
            sequence.append(current)
            for pos in left:
                total_seek += abs(current - pos)
                current = pos
                sequence.append(current)
    else:
        left = [x for x in sorted_requests if x <= current][::-1]
        right = [x for x in sorted_requests if x > current]
        for pos in left:
            total_seek += abs(current - pos)
            current = pos
            sequence.append(current)
        if right:
            total_seek += abs(current - 0)
            current = 0
            sequence.append(current)
            for pos in right:
                total_seek += abs(current - pos)
                current = pos
                sequence.append(current)
    
    return sequence, total_seek

def cscan(requests, head):
    sequence = [head]
    total_seek = 0
    sorted_requests = sorted(requests)
    current = head
    
    right = [x for x in sorted_requests if x >= current]
    left = [x for x in sorted_requests if x < current]
    
    for pos in right:
        total_seek += abs(current - pos)
        current = pos
        sequence.append(current)
    if left:
        total_seek += abs(current - 199)
        current = 199
        sequence.append(current)
        total_seek += abs(199 - 0)
        current = 0
        sequence.append(current)
        for pos in sorted(left):
            total_seek += abs(current - pos)
            current = pos
            sequence.append(current)
    
    return sequence, total_seek

# Train model
X, y = generate_training_data()
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

def predict_optimal_algorithm(requests, head):
    features = [
        len(requests),
        np.var(requests) if requests else 0,
        np.mean([abs(x - head) for x in requests]) if requests else 0,
        head
    ]
    prediction = model.predict([features])[0]
    return prediction
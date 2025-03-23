# traditional_algorithms.py
def fcfs(requests, head):
    """First Come First Serve (FCFS)"""
    seek_sequence = [head] + requests
    total_seek = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence)-1))
    return seek_sequence, total_seek

def sstf(requests, head):
    """Shortest Seek Time First (SSTF)"""
    requests = requests[:]
    seek_sequence = [head]
    total_seek = 0
    while requests:
        next_request = min(requests, key=lambda r: abs(head - r))
        total_seek += abs(head - next_request)
        seek_sequence.append(next_request)
        head = next_request
        requests.remove(next_request)
    return seek_sequence, total_seek

def scan(requests, head, direction="right", disk_size=200):
    """SCAN (Elevator Algorithm)"""
    requests = sorted(requests)
    if direction == "right":
        right = [r for r in requests if r >= head]
        left = [r for r in requests if r < head]
        seek_sequence = [head] + right + [disk_size-1] + left[::-1]
    else:
        left = [r for r in requests if r <= head]
        right = [r for r in requests if r > head]
        seek_sequence = [head] + left[::-1] + [0] + right
    total_seek = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence)-1))
    return seek_sequence, total_seek
# traditional_algorithms.py
def fcfs(requests, head):
    """First Come First Serve (FCFS)"""
    seek_sequence = [head] + requests
    total_seek = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence)-1))
    return seek_sequence, total_seek

def sstf(requests, head):
    """Shortest Seek Time First (SSTF)"""
    requests = requests[:]
    seek_sequence = [head]
    total_seek = 0
    while requests:
        next_request = min(requests, key=lambda r: abs(head - r))
        total_seek += abs(head - next_request)
        seek_sequence.append(next_request)
        head = next_request
        requests.remove(next_request)
    return seek_sequence, total_seek

def scan(requests, head, direction="right", disk_size=200):
    """SCAN (Elevator Algorithm)"""
    requests = sorted(requests)
    if direction == "right":
        right = [r for r in requests if r >= head]
        left = [r for r in requests if r < head]
        seek_sequence = [head] + right + [disk_size-1] + left[::-1]
    else:
        left = [r for r in requests if r <= head]
        right = [r for r in requests if r > head]
        seek_sequence = [head] + left[::-1] + [0] + right
    total_seek = sum(abs(seek_sequence[i] - seek_sequence[i+1]) for i in range(len(seek_sequence)-1))
    return seek_sequence, total_seek

import time

def measure_execution_time(action):
    start = time.time()
    action()
    end = time.time()
    return round(end - start, 2)

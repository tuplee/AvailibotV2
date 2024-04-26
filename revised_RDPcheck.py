from flask import Flask, request

app = Flask(__name__)

rdp_status = False  # Initial status

@app.route('/update-rdp-status', methods=['POST'])
def update_rdp_status():
    global rdp_status
    rdp_status = request.json.get('rdp_status', False)
    return 'RDP status updated successfully', 200

@app.route('/get-rdp-status')
def get_rdp_status():
    global rdp_status
    return {'rdp_status': rdp_status}

if __name__ == '__main__':
    app.run(debug=True)

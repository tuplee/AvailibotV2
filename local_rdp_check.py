import requests
import psutil
import time

# Function to check RDP connection status
def check_rdp_connections():
    rdp_connections = False
    for conn in psutil.net_connections():
        if conn.status == 'ESTABLISHED' and conn.laddr.port == 3389:  # RDP port
            rdp_connections = True
            break
    return rdp_connections

# Flask app URL
FLASK_API_URL = ''

# Main loop
while True:
    # Check RDP connection status
    rdp_status = check_rdp_connections()

    # Send status update to Flask app
    try:
        response = requests.post(FLASK_API_URL, json={'rdp_status': rdp_status})
        response.raise_for_status()
        print('RDP status updated successfully')
    except requests.exceptions.RequestException as e:
        print('Error updating RDP status:', e)

    # Sleep for a certain interval before checking again
    time.sleep(60)  # Check every minute

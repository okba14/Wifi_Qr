import qrcode
import subprocess
import re
import os

def get_current_wifi_info():
    try:
        # Get the SSID (name of the currently connected Wi-Fi network)
        ssid = subprocess.check_output("iwgetid -r", shell=True, encoding='utf-8').strip()

        if not ssid:
            print("SSID not found.")
            return None, None

        # Get the password (from NetworkManager's configuration files)
        password = ''
        network_file_path = f"/etc/NetworkManager/system-connections/{ssid}"

        if os.path.exists(network_file_path):
            with open(network_file_path, 'r') as file:
                content = file.read()
                match = re.search(r'psk=\s*(\S+)', content)
                if match:
                    password = match.group(1)
                else:
                    print("Password not found.")
                    password = ''

        return ssid, password

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while trying to get network information: {e}")
        return None, None

def generate_wifi_qr(ssid, password, encryption='WPA'):
    # Create the Wi-Fi configuration string
    wifi_config = f"WIFI:S:{ssid};T:{encryption};P:{password};;"
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_config)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save("wifi_qr.png")
    print("QR code generated and saved as 'wifi_qr.png'.")

# Get the SSID and password of the currently connected network
ssid, password = get_current_wifi_info()

# If network information is available, generate the QR Code
if ssid and password:
    generate_wifi_qr(ssid, password)

Wi-Fi QR Code Generator

This Python script generates a QR code that allows others to easily connect to your Wi-Fi network by scanning the QR code. The script retrieves the SSID (network name) and password of the currently connected Wi-Fi network and creates a corresponding QR code for easy sharing.

Features

Automatically retrieves the current Wi-Fi network's SSID and password.
Generates a QR code containing the Wi-Fi credentials.
Saves the QR code as an image file (wifi_qr.png).
Works on Linux-based systems with NetworkManager.
Prerequisites
Python 3.x installed on your system.

qrcode library installed. If you don't have it, install it using:

bash
Copier le code
pip install qrcode
How to Use
Clone the repository or download the script to your local machine.

Run the script with elevated privileges (using sudo), since network information requires root access:

bash
Copier le code
sudo python3 generate_wifi_qr.py
The script will generate and save the QR code as wifi_qr.png in the current directory.

Share the QR code with others to allow them to easily connect to your Wi-Fi network by scanning the code.

Important Notes
This script is designed to work on Linux systems with NetworkManager. It may not work on Windows or macOS.
The script retrieves the password from the system’s network configuration files. Make sure your system is configured to store Wi-Fi passwords.
Troubleshooting
If the script doesn’t find your network information, ensure you're connected to a Wi-Fi network and your system is managing the connection with NetworkManager.
The script requires root privileges to access network configuration files, so use sudo to run the script.

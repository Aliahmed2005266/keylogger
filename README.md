Keylogger Project – Intro to Cybersecurity (AASTMT)
This keylogger was developed strictly for educational purposes as part of the Introduction to Cybersecurity course at the Arab Academy for Science, Technology & Maritime Transport (AASTMT)

 Project Overview
The project consists of two main components:

Attacker Side (Listener)
This side uses netcat (nc) or a Python listener script to receive keystroke data from the victim's machine.

Victim Side (Keylogger)
A simple script that monitors and logs all keystrokes on the victim’s machine and sends them to the IP address specified in the script.

 How to Use (Educational Lab Environment Only)
Note: Use only in a controlled lab environment with proper authorization.

Steps:
Deploy the Keylogger
Send the script to the target machine. It can optionally be embedded as a backdoor within another file (e.g., an image), though this requires additional modification.

Execution on Victim's Machine
Once the script is executed by the victim, it will begin monitoring all keyboard activity and transmitting the data to the attacker.

Start Listener on Attacker Side
Use the following command to start listening for incoming data:

nc -lvp [PORT]

python3 listener.py


⚠️ Legal Disclaimer
This script is intended solely for educational purposes to demonstrate basic cybersecurity concepts such as keylogging and remote data transmission.
The developer is not responsible for any misuse, illegal activity, or unauthorized deployment of this code.

Unauthorized use of this script may violate local, national, or international laws. Always obtain proper consent and operate within legal and ethical boundaries.

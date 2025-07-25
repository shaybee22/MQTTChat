# MQTTChat
MQTT Chat is s simple encrypted chat program that uses any mqtt server you have access to for relaying encrypted messages
# MQChat 💬🔒  
**Encrypted Group Chat over MQTT**  
Created by James Powell  

MQChat is a lightweight, secure group chat application that uses MQTT as its message relay protocol. Designed for privacy and simplicity, it features end-to-end encryption, room presets, presence tracking, and a GUI-friendly interface built with Python and Tkinter.

---

## 🧠 Key Features

- 🔐 End-to-end encrypted messages using Fernet (AES)
- 🌐 MQTT-based real-time message relay
- 👤 Presence tracking (online/offline status)
- 💾 Save and load favorite chat rooms
- 📋 GUI with tabs for Connection, Chat, and Room Management
- 🛠️ Support for MQTT authentication (optional)
- 🚀 Quick Connect and saved room profiles
- 📥 Import/Export chat room configurations
- ✅ Compatible with anonymous or authenticated MQTT brokers

---

## 🖥️ Desktop App (Python)

### 🛠 Requirements

- Python 3.x
- `paho-mqtt`
- `cryptography`
- `tkinter` (included with most Python installations)

### 📦 Installation

1. Clone the repo:
    ```bash
    git clone https://github.com/yourusername/mqchat.git
    cd mqchat
    ```

2. Install dependencies:
    ```bash
    pip install paho-mqtt cryptography
    ```

3. Run the app:
    ```bash
    python mqchat.py
    ```

---

## 📦 Creating a Portable Windows Executable

You can generate a self-contained `.exe` using `pyinstaller` and the included batch script.

### 🔧 One-click Build (Windows)

1. Install [PyInstaller](https://pyinstaller.org/):
    ```bash
    pip install pyinstaller
    ```

2. Run the batch script:
    ```bash
    build_desktop_app.bat
    ```

This will compile `mqchat.py` into a portable executable inside the `dist/` folder.

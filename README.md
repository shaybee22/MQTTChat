# MQChat 💬🔒

**Encrypted Group Chat over MQTT**
Created by James Powell

MQChat is a lightweight, secure group chat application that uses MQTT as its message relay protocol. Designed for privacy and simplicity, it features end-to-end encryption, room presets, presence tracking, and a GUI-friendly interface built with Python and Tkinter.

---

## 🧠 Key Features

* 🔐 End-to-end encrypted messages using Fernet (AES)
* 🌐 MQTT-based real-time message relay
* 👤 Presence tracking (online/offline status)
* 💾 Save and load favorite chat rooms
* 📋 GUI with tabs for Connection, Chat, and Room Management
* 🛠️ Support for MQTT authentication (optional)
* 🚀 Quick Connect and saved room profiles
* 📥 Import/Export chat room configurations
* ✅ Compatible with anonymous or authenticated MQTT brokers

---

## 🖥️ Desktop App (Python)

### 🛠 Requirements

* Python 3.x
* `paho-mqtt`
* `cryptography`
* `tkinter` (included with most Python installations)

### 📦 Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/shaybee22/MQTTChat.git
   cd MQTTChat
   ```

2. Install dependencies:

   ```bash
   pip install paho-mqtt cryptography
   ```

3. Run the app:

   ```bash
   python mqchat.py
   ```

[View the code on GitHub](https://github.com/shaybee22/MQTTChat/blob/main/mqchat.py)

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

[View the batch script](https://github.com/shaybee22/MQTTChat/blob/main/build_desktop_app.bat)

---

## 📱 Android Version

An Android version of MQChat is available! It's written using Kivy and Buildozer for packaging.

📂 [View the Android App on GitHub](https://github.com/shaybee22/MQTTChat/tree/main/AndroidApp)

Inside the AndroidApp folder, you'll find installation and build instructions using **Buildozer**.

---

## 📁 File Structure

```
📁 MQTTChat/
├── mqchat.py                 # Main Python desktop app
├── build_desktop_app.bat     # Batch script to create Windows .exe
├── mqtt_chat_rooms.json      # Encrypted saved room profiles (created at runtime)
├── AndroidApp/               # Android version using Kivy/Buildozer
├── LICENSE                   # Custom MIT Non-Commercial License
└── README.md                 # You're reading it!
```

---

## 🔒 Security Note

MQChat uses **Fernet encryption**, which is AES-128 in CBC mode with HMAC for integrity. Only users with the same shared encryption key can read each other's messages. Never share your key over insecure channels!

---

## 🔧 Roadmap

* [ ] Add file/image sharing
* [ ] Push notifications
* [ ] Android/Desktop cross-device syncing
* [ ] Encrypted voice calls (stretch goal)

---

## 📜 License

This project is licensed under the [MIT Non-Commercial License](https://github.com/shaybee22/MQTTChat/blob/main/LICENSE) — free for personal use, credit required for modifications, and written permission required for commercial or resale purposes. 🥥🌴😉

---

## 🙋‍♂️ Author

**James Powell** (a.k.a. shaybee22)
If you enjoy this project, consider giving it a ⭐ on [GitHub](https://github.com/shaybee22/MQTTChat)! 💙


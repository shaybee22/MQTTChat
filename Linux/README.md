# MQChat for Linux 🐧💬🔐

**Portable Encrypted Group Chat over MQTT**
By James Powell (aka shaybee22)

MQChat is a cross-platform, end-to-end encrypted group chat client that uses MQTT as the relay server. This version is built for Linux systems and can be compiled into a single, portable executable using PyInstaller—no Python installation required on the target machine!

---

## 🚀 Features

* 🧠 Fully GUI-based (Tkinter)
* 🔐 End-to-end encryption using Fernet (AES)
* 🧵 Real-time group chat via MQTT broker
* 💾 Saved room configs with encryption
* 📥 Import/export rooms
* 👥 Online presence tracking
* ✅ Anonymous or authenticated MQTT login

---

## 📦 Requirements (to build)

* Python 3
* pip
* PyInstaller
* GTK (pre-installed on most Linux distros)

---

## 🛠 Build Instructions (Linux)

### 🔧 One-Click Build:

Use the included `build_linux_portable.sh` script:

```bash
chmod +x build_linux_portable.sh
./build_linux_portable.sh
```

This will:

* Install PyInstaller
* Clean previous builds
* Compile `mqchat.py` into a standalone executable
* Output it in a `portable/` directory

Once complete, you’ll have a single binary file named `MQChat` that can be copied to other Linux systems.

### Manual Build:

```bash
pip3 install pyinstaller
pyinstaller --onefile --windowed --name="MQChat" --distpath="./portable" mqchat.py
```

---

## 🧪 Running the App

Once built, run it like so:

```bash
./portable/MQChat
```

You can also run it directly from Python (if you don't need portability):

```bash
python3 mqchat.py
```

---

## 📁 File Overview

```
📁 MQTTChat_Linux/
├── mqchat.py                  # Main app
├── build_linux_portable.sh    # Bash script to build Linux executable
├── portable/                  # Output folder for standalone binary (created at build)
```

---

## 📝 License

MIT Non-Commercial License – Personal use only. Commercial use or resale requires permission. Full credit required for forks/derivatives. See [LICENSE](../LICENSE) for full terms.

---

## 🙋‍♂️ Author

**James Powell** (shaybee22)
Check out the full project and other platform versions at:
[https://github.com/shaybee22/MQTTChat](https://github.com/shaybee22/MQTTChat)

If you enjoy it, give it a ⭐ and share it with fellow Linux geeks!

---

Stay encrypted. Stay private. Stay chatty. 🔐💬🐧

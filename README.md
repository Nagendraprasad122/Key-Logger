# Keyboard Event Logger (Educational Use Only)

This project demonstrates how to use the `pynput` Python library to listen for
keyboard events and record them to a text file.  
It is intended **strictly for learning purposes**, such as:

- Understanding how keyboard hooks work
- Debugging keyboard input in personal applications
- Building accessibility tools
- Monitoring your *own* device for key event testing

> ⚠️ **IMPORTANT WARNING**  
> This script records keystrokes typed on the machine.  
> Using it on any device you do NOT own or without explicit permission is  
> **illegal and violates privacy laws**.  
> Use responsibly and ethically.

---

## 📌 Features
- Captures alphanumeric keys
- Logs special keys like space, enter, shift, ctrl, etc.
- Saves all keypresses into `log.txt`
- Runs continuously until manually stopped

---

## 🛠 Requirements
Install `pynput` library:

```bash
pip install pynput

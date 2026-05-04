# Windows Login Monitor
- Created by Jyoti Maity

## 🔐 Project Description
Windows Login Monitor is a Python-based security monitoring tool that analyzes
Windows Security Event Logs to identify authentication activities and
privilege escalation events.

It helps detect:
- Failed login attempts
- Successful login attempts
- Administrative privilege assignments

This project is useful for basic intrusion detection and forensic analysis
on Windows systems.

---

## 🛠️ Technologies Used
- Python 3
- Windows Security Event Logs
- pywin32 library

---

## 📋 Event IDs Monitored
| Event ID | Description |
|--------|------------|
| 4625 | Failed login attempt |
| 4624 | Successful login |
| 4672 | Admin privilege assignment |

---

## ⚙️ Requirements
- Windows Operating System
- Python 3.x
- Administrator privileges
- pywin32 library

Install dependency:
```bash
pip install pywin32

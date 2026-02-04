import win32evtlog
from datetime import datetime

SERVER = 'localhost'
LOG_TYPE = 'Security'

FAILED_ID = 4625
SUCCESS_ID = 4624
ADMIN_ID = 4672

failed_logins = []
successful_logins = []
admin_logins = []

print("\n🔐 Windows Security Log Monitoring Report")
print("Generated on:", datetime.now())

try:
    handle = win32evtlog.OpenEventLog(SERVER, LOG_TYPE)
except Exception as e:
    print("❌ Administrator privileges required to access Security logs.")
    print("Error:", e)
    exit()

flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

while True:
    events = win32evtlog.ReadEventLog(handle, flags, 0)
    if not events:
        break

    for event in events:
        event_id = event.EventID & 0xFFFF

        if event_id == FAILED_ID:
            failed_logins.append(event.StringInserts)

        elif event_id == SUCCESS_ID:
            successful_logins.append(event.StringInserts)

        elif event_id == ADMIN_ID:
            admin_logins.append(event.StringInserts)


def print_section(title, data):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)
    if not data:
        print("No records found.")
    else:
        for item in data[:10]:
            print(item)
        print(f"\nTotal Events: {len(data)}")


print_section("FAILED LOGIN ATTEMPTS (4625)", failed_logins)
print_section("SUCCESSFUL LOGINS (4624)", successful_logins)
print_section("ADMIN PRIVILEGE LOGONS (4672)", admin_logins)

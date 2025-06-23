import psutil
import time
import platform

def get_battery_status(threshold=20):
    battery = psutil.sensors_battery()

    if battery is None:
        print(" Battery information not available on this device.")
        return

    percent = battery.percent
    charging = battery.power_plugged
    status = "Charging " if charging else "Not Charging "

    print(f"\n Battery Status: {percent}% ({status})")

    if not charging and percent <= threshold:
        print(f" Battery low! ({percent}%) - Please plug in the charger.")

def monitor_battery(interval=60):
    print(f" Starting Battery Monitor (checks every {interval} seconds)...")
    try:
        while True:
            get_battery_status()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n Monitoring stopped.")

if __name__ == "__main__":
   
    get_battery_status()

  

import psutil

def list_processes():
    print("\n Running Processes")
    print("-" * 60)
    print(f"{'PID':<10}{'Name':<25}{'Memory (MB)':>15}")
    print("-" * 60)
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            pid = proc.info['pid']
            name = proc.info['name'] or "Unknown"
            memory = proc.info['memory_info'].rss / (1024 * 1024)  # in MB
            print(f"{pid:<10}{name:<25}{memory:>15.2f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

def kill_process(pid):
    try:
        p = psutil.Process(pid)
        p.terminate()
        p.wait(timeout=3)
        print(f"\n Process {pid} terminated successfully.")
    except psutil.NoSuchProcess:
        print(f"\n No process found with PID {pid}.")
    except psutil.AccessDenied:
        print(f"\n Access denied to terminate PID {pid}. Run as admin.")
    except Exception as e:
        print(f"\n Error: {e}")

def main():
    while True:
        list_processes()
        choice = input("\nEnter PID to kill or 'q' to quit: ").strip()
        if choice.lower() == 'q':
            break
        elif choice.isdigit():
            kill_process(int(choice))
        else:
            print(" Invalid input. Please enter a valid PID or 'q'.")

if __name__ == "__main__":
    main()

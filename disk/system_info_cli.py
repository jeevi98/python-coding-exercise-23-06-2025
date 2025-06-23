import psutil
import platform
import socket

def get_size(bytes, suffix="B"):
 
    for unit in ["", "K", "M", "G", "T"]:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= 1024

def system_info():
    print("\n System Information")
    print("-" * 40)

    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

  
    print("\nCPU Info")
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Total cores: {psutil.cpu_count(logical=True)}")
    print(f"CPU Usage per core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"  Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

 
    print("\n Memory Info")
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")

  
    print("\n Disk Info")
    partitions = psutil.disk_partitions()
    for p in partitions:
        try:
            usage = psutil.disk_usage(p.mountpoint)
            print(f"Drive: {p.device}")
            print(f"  Total: {get_size(usage.total)}")
            print(f"  Used: {get_size(usage.used)}")
            print(f"  Free: {get_size(usage.free)}")
            print(f"  Usage: {usage.percent}%")
        except PermissionError:
            continue

    print("\n Network Info")
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"Local IP: {ip_address}")

if __name__ == "__main__":
    system_info()

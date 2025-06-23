import shutil
import psutil
import platform

def format_size(bytes):
   
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024

def show_disk_usage():
    print("\n Disk Usage Monitor")
    print("-" * 30)
    
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"\nDrive: {partition.device}")
            print(f"  Mountpoint: {partition.mountpoint}")
            print(f"  File system type: {partition.fstype}")
            print(f"  Total size: {format_size(usage.total)}")
            print(f"  Used: {format_size(usage.used)}")
            print(f"  Free: {format_size(usage.free)}")
            print(f"  Usage: {usage.percent}%")
        except PermissionError:
            continue

if __name__ == "__main__":
    print(f"System: {platform.system()} {platform.release()}")
    show_disk_usage()

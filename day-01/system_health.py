import psutil
def system_health_check():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    cpu_threshold = int(input("Enter CPU usage threshold percentage: "))
    if cpu_usage > cpu_threshold:
        print(f"Warning: CPU usage is at {cpu_usage}% which is above the threshold of {cpu_threshold}%")
    else:
        print(f"CPU usage is at {cpu_usage}%, which is within the acceptable range.")
    
    memory_threshold = int(input("Enter Memory usage threshold percentage: "))
    if memory.percent > memory_threshold:
        print(f"Warning: Memory usage is at {memory.percent}% which is above the threshold of {memory_threshold}%")
    else:
        print(f"Memory usage is at {memory.percent}%, which is within the acceptable range.")
    disk_threshold = int(input("Enter Disk usage threshold percentage: "))
    if disk.percent > disk_threshold:
        print(f"Warning: Disk usage is at {disk.percent}% which is above the threshold of {disk_threshold}%")   
    else:
        print(f"Disk usage is at {disk.percent}%, which is within the acceptable range.")

system_health_check()
import psutil
print(f"RAM usage: {psutil.virtual_memory().percent}%")

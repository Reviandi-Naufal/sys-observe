from emc.formatters import text
from emc.core import system_info
from emc.core import disk_info

def main():
    print()
    print("WELCOME TO EMC (EXPLAIN MY COMPUTER)")
    print()

    # OS Detail
    os_data = system_info.os_info()
    print(text.os_detail(os_data))
    print()

    # # CPU Detail
    cpu_data = system_info.cpu_info()
    print(text.cpu_detail(cpu_data))
    print()

    # # GPU Detail
    # # gpus = GPUtil.getGPUs()
    # # for gpu in gpus:
    # #     print(f"GPU Name: {gpu.name}")
    # #     print(f"Total Memory: {gpu.memoryTotal}MB")
    # #     print(f"Used Memory: {gpu.memoryUsed}MB")
    # #     print(f"GPU Load: {gpu.load*100}%")
    # #     print("-" * 20)

    # Memory Detail
    mem_data = system_info.mem_info()
    print(text.mem_detail(mem_data))
    print()

    # Disk Detail
    disk_data = disk_info.os_storage_info()
    print(text.disk_detail(disk_data))
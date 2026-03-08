from emc.core.models import *

def os_detail(os_data: OSInfo) -> str:
    # OS Detail
    return(
        "Operating System (OS) Info\n"
        "-----------------------------\n"
        f"{'Username':<18}: {os_data.usr_name}\n"
        f"{'OS Name':<18}: {os_data.os_name}\n"
        f"{'OS Version':<18}: {os_data.os_ver}\n"
        f"{'OS System Type':<18}: {os_data.os_sys_type}s"
    )

# CPU Detail
def cpu_detail(cpu_data: CPUInfo) -> str: 
    return(
        "Processor(CPU) Info\n"
        "--------------------\n"
        f"{'CPU Name':<18}: {cpu_data.cpu_name}\n" 
        f"{'CPU Cores':<18}:{cpu_data.cpu_cores}\n"
        f"{'CPU Threads':<18}:{cpu_data.cpu_threads}\n"
        f"{'CPU Name':<18}: {cpu_data.cpu_name}\n" 
        f"{'CPU Cores':<18}:{cpu_data.cpu_cores}\n"
        f"{'CPU Threads':<18}:{cpu_data.cpu_threads}"
    )

# # GPU Detail
# # gpus = GPUtil.getGPUs()
# # for gpu in gpus:
# #     print(f"GPU Name: {gpu.name}")
# #     print(f"Total Memory: {gpu.memoryTotal}MB")
# #     print(f"Used Memory: {gpu.memoryUsed}MB")
# #     print(f"GPU Load: {gpu.load*100}%")
# #     print("-" * 20)

# Memory Detail
def mem_detail(mem_data: MEMInfo) -> str:
    return(
        "Memory(RAM) Info\n"
        "-----------------\n"
        f"{'Total RAM':<18}: {mem_data.total_ram:.2f} GB\n"
        f"{'Available memory':<18}: {mem_data.avail_ram:.2f} GB\n"
        f"{'Used memory':<18}: {mem_data.used_ram:.2f} GB\n"
        f"{'Memory usage percentage':<18}: {mem_data.percent_ram} %"
    )


# Disk Detail
def disk_detail(disk_data: DISKInfo) -> str:
    return(
        "Storage(SSD/HDD) Info\n"
        "----------------------\n"
        f"{'Total OS Storage':<18}: {disk_data.sum_os_storage:.2f} GB\ns"
        f"{'Free OS Storage':<18}: {disk_data.free_os_storage:.2f} GB"
    )
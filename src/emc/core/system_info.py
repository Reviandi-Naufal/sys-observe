import platform
import sys
import psutil
import cpuinfo
from emc.core.models import OSInfo, CPUInfo, MEMInfo

# OS Detail
def os_info() -> OSInfo:
    return OSInfo(
        usr_name = platform.node(),
        os_name = platform.system(),
        os_ver = platform.version(),
        os_sys_type = "64-bit operating system, x64-based processor" if sys.maxsize > 2**32 else "32-bit operating system, x32-based processor"
    )

#CPU Detail
def cpu_info() -> CPUInfo:
    # Get a dictionary with comprehensive CPU information
    cpu_info_dict = cpuinfo.get_cpu_info()
    return CPUInfo (
    cpu_name = cpu_info_dict['brand_raw'],
    cpu_cores = psutil.cpu_count(logical=False),
    cpu_threads = psutil.cpu_count(logical=True)
    )

def mem_info() -> MEMInfo:
    # Memory Detail
    mem = psutil.virtual_memory()
    return MEMInfo (
        total_ram = mem.total / (1024**3), #in GB
        avail_ram = mem.available / (1024**3), #in GB
        used_ram = mem.used / (1024**3), #in GB
        percent_ram = mem.percent #in %
    )
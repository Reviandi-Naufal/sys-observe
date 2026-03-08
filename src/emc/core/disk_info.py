import platform
import psutil
from emc.core.models import DISKInfo

def os_storage_info() -> DISKInfo:
    # Disk Detail
    if  platform.system() == 'Windows':
        path = 'C:\\'
    else:
        path = '/'

    disk_info = psutil.disk_usage(path)
    return DISKInfo (
        sum_os_storage = disk_info.total / (1024**3), #in GB
        free_os_storage = disk_info.free / (1024**3) #in GB
    )
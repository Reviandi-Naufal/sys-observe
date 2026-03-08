from dataclasses import dataclass

@dataclass
class OSInfo:
    usr_name: str
    os_name: str
    os_ver: str
    os_sys_type: str

@dataclass
class CPUInfo:
    cpu_name: str
    cpu_cores: int
    cpu_threads: int

@dataclass
class MEMInfo:
    total_ram: float
    avail_ram: float
    used_ram: float
    percent_ram: int

@dataclass
class DISKInfo:
    sum_os_storage: float
    free_os_storage: float
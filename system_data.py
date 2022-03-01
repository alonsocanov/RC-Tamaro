import subprocess


def get_network_interface_state(interface:str):
    '''
    Types of interface wlan0, eth0
    '''
    if 'eth' not in interface and 'wlan' not in interface:
        string = "Interface must be ethx or wlanx"
    elif len(interface) > 5 or interface[-1] < '0' or interface[-1] > '9':
        string = "Interface must be ethx or wlanx"
    else:
        string = subprocess.check_output('cat /sys/class/net/%s/operstate' % interface, shell=True).decode('ascii')[:-1]
    return string

def get_ip_address(interface:str):
    inter = interface.lower().strip()
    ip = get_network_interface_state(inter)
    if ip == 'down':
        ip = ' '.join([interface, 'is down'])
    elif len(ip) > 18:
        pass
    else:
        cmd = "ifconfig %s | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'" % interface
        ip = subprocess.check_output(cmd, shell=True).decode('ascii')[:-1]
    return ip

# Return a string representing the percentage of CPU in use
def get_cpu_usage():
    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell=True)
    return CPU

# Return a float representing the percentage of GPU in use.
# On the Jetson Nano, the GPU is GPU0
def get_gpu_usage():
    GPU = 0.0
    with open("/sys/devices/gpu.0/load", encoding="utf-8") as gpu_file:
        GPU = gpu_file.readline()
        GPU = int(GPU)/10
    return GPU
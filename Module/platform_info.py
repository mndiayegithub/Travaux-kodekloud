# from platform import machine, ...
from platform import machine, system, python_version

def platform_info():
    user_os = system() # Version of the system
    user_arch = machine() # Architecture of the machine
    user_python = python_version() # # Python version
    return (user_os,user_arch,user_python)


print(platform_info())
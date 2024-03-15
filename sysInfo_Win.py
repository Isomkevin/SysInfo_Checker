import platform

sysInfo = {} 

def get_sys_info():
  # platform details 
  platform_details = platform.platform() 
  # system name
  system_name = platform.system() 
  # processor name 
  processor_name = platform.processor()
  # architectural detail 
  architecture_details = platform.architecture() 
  # adding it to dictionary 
  sysInfo["system name"] = system_name 
  sysInfo["processor name"] = processor_name 
  sysInfo["architectural detail"] = architecture_details
  sysInfo["platform details"] = platform_details
  
  return sysInfo



import sysInfo_Win

system_Info = sysInfo_Win.get_sys_info()

# printing the details 
for i, j in system_Info.items(): 
  print(f"{i.title()}, - {j}") 
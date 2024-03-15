import sysInfo_Win

system_Info = sysInfo_Win.get_sys_info()

def main(info):
  """
  This Python script will output the system information of the computer that it is running on.
  """
  print("""
---------------------------------
  System Information
---------------------------------
  """)
  # printing the details 
  for i, j in info.items(): 
    print(f"{i.title()}: {j}") 
  
  print("""
---------------------------------
  """)


if __name__ == "__main__":
  main(system_Info)

import subprocess

print("Enter 'stop' or 'exit' or 'quite'")

while True:
    try:
        comm = input("cmd@root:~# ")
        if comm.lower() == "stop" or comm.lower() == "exit" or comm.lower() == "quite":
            break



        subprocess.run(comm)
    except Exception:

        print("Command Not Found")
        
        continue

print("Good Bey :)")        
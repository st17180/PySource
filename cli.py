from main import Monitor
mon = Monitor(True)

print("Options : cpu, mem, disk, processes, help, exit")
while True:
    awn = input("Option : ")
    if awn == "cpu":
        tf = input("Print total, True/False : ")
        if tf == "True":
            print(mon.cpu(True))
        elif tf == "False":
            print(mon.cpu(False))
    elif awn == "mem":
        size = input("size : mb/gb : ")
        if size == "mb":
            print(mon.mem("mb"))
        elif size == "gb":
            print(mon.mem("gb"))
    elif awn == "disk":
        size = input("size : mb/gb : ")
        if size == "mb":
            print(mon.disk("mb"))
        elif size == "gb":
            print(mon.disk("gb"))
    elif awn == "processes":
        print(mon.process())
    elif awn == "exit":
        exit()
    else:
        print("make sure to awnser a valid option")

import datetime
from main import Monitor
mon = Monitor(True)

print("Python System Monitor, Try a function below \n\
Options : cpu, mem, disk, processes, help, exit")
while True:
    awn = input("Option : ")
    if awn == "cpu":
        tf = input("Print total, yes/no : ")
        if tf == "yes":
            print(mon.cpu(True))
        elif tf == "no":
            print(mon.cpu(False))
        else:
            print("you must use either yes or no")
    elif awn == "mem":
        size = input("size : mb/gb : ")
        if size == "mb":
            print(mon.mem("mb"))
        elif size == "gb":
            print(mon.mem("gb"))
        else:
            print("you must use either mb or gb")
    elif awn == "disk":
        size = input("size : mb/gb : ")
        if size == "mb":
            print(mon.disk("mb"))
        elif size == "gb":
            print(mon.disk("gb"))
        else:
            print("you must use either mb or gb")
    elif awn == "processes":
        print(mon.process())
    elif awn == "save":
        with open("output.txt", "a") as save:
            x = str(datetime.datetime.now()) + "\n"
            save.write(x)
            x = mon.cpu(True) + "\n"
            save.write(x)
            x = mon.cpu(False) + "\n"
            save.write(x)
            x = mon.mem("mb") + "\n"
            save.write(x)
            x = mon.disk("mb") + "\n"
            save.write(x)
            for processes in Monitor(False).process():
                x = f"{processes[1]} : {processes[0]}\n"
                save.write(x)
            save.write("\n")
    elif awn == "exit":
        exit()
    else:
        print("Must be cpu, mem, disk, processes, help or exit")

import psutil

# sys get
class monitor():
    
    # returns list of cpu usages
    def cpu(self):
        get = psutil.cpu_percent(interval=1,percpu=True)
        core = 0
        result = []
        for item in get:
            core = core + 1
            c = (core, item)
            result.append(c)
        return result
    
    # returns used and total memory
    def mem(self):
        get = psutil.virtual_memory()
        total = round(get[0] / 1073741824, 2)
        used = round(get[3] / 1073741824, 2)
        result = (used, "gb of",  total)
        return result

    # returns used and total disk
    def disk(self):
        get = psutil.disk_usage('/')
        total = round(get[0] / 1073741824, 2)
        used = round(get[1] / 1073741824, 2)
        result = (used, "gb of", total)
        return result

# shorten class name
mon = monitor()

# CLI MENU
x = 0
while x < 1:
    awn = str(input("cpu, mem, disk or help : "))
    if awn == "cpu":
        print(mon.cpu())
    elif awn == "mem":
        print(mon.mem())
    elif awn == "disk":
        print(mon.disk())
    elif awn == "help":
        print("quit to close the program, help to print this message, cpu to print cpu useage information, mem to print memory useage and total information or disk to print disk info about '/'")
    elif awn == "quit":
        x = 1
    else:
        continue
# CLI MENU END

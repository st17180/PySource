import psutil

# main class
class Monitor():

    # init for use case
    def __init__(self, readability):
        self.read = readability
    
    # cpu total/percore func
    def cpu(self, total):
        cputotal = psutil.cpu_percent(interval=1,percpu=False)
        cpupercore = psutil.cpu_percent(interval=1,percpu=True)
        if self.read:
            if total:
                return f"total CPU useage : {cputotal}"
            else:
                cores = cpupercore
                result = ""
                c = 0
                for core in cores:
                    result += f"{c}'s useage : {core}\n"
                    c += 1
                return result
        else:
            if total:
                return cputotal
            else:
                return cpupercore
    
    # memory use mb/gb
    def mem(self, size):
        memory = psutil.virtual_memory()
        if self.read:
            if size == "mb":
                return f"total ram memory useage : {round(memory[3] / 1000000, 2)}MB / {round(memory[0] / 1000000, 2)}MB"
            elif size == "gb":
                return f"total ram memory useage : {round(memory[3] / 1073741824, 2)}GB / {round(memory[0] / 1073741824, 2)}GB"
            else:
                return "the mem config is incorrect"
        else:
            if size == "mb":
                return round(memory[3] / 1000000, 2), round(memory[0] / 1000000, 2), 'mb'
            elif size == "gb":
                return round(memory[3] / 1073741824, 2), round(memory[0] / 1073741824, 2), 'gb'
            else:
                return "the mem config is incorrect"
    
    # disk use mb/gb
    def disk(self, size):
        diskinfo = psutil.disk_usage(".")
        if self.read:
            if size == "mb":
                return f"total disk memory useage : {round(diskinfo[1] / 1000000, 2)}MB / {round(diskinfo[0] / 1000000, 2)}MB"
            elif size == "gb":
                return f"total disk memory useage : {round(diskinfo[1] / 1073741824, 2)}GB / {round(diskinfo[0] / 1073741824, 2)}GB"
        else:
            if size == "mb":
                return round(diskinfo[1] / 1000000, 2), round(diskinfo[0] / 1000000, 2), 'mb'
            elif size == "gb":
                return round(diskinfo[1] / 1073741824, 2), round(diskinfo[0] / 1073741824, 2), 'gb'
   
    # process listing
    def process(self):
        processes = psutil.process_iter()
        result = []
        for process in processes:
            try:
                processName = process.name()
                processID = process.pid
                if self.read:
                    print(f"{processID} : {processName}")
                else:
                    a = (processName, processID)
                    result.append(a)
            except (psutil.NoSuchProcess, psutil,AccessDenied, psutil.ZombieProcess):
                pass
        return(result)

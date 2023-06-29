import psutil
import os
import signal


def kill_excel_proc():
    pid_list = []
    pid_name = "excel.exe"
    for proc in psutil.process_iter():
        try:
            proc_info = proc.as_dict(attrs=["pid", "name"])
        except psutil.NoSuchProcess:
            print("Process is close.")
        else:
            if pid_name in proc_info["name"].lower():
                pid_list.append(proc_info["pid"])
    if pid_list:
        for proc in pid_list:
            pid = proc["pid"]
            os.kill(pid, signal.SIGINT)
    return pid_list


kill_excel_proc()
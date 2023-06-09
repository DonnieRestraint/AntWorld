import psutil
import os
import signal
import subprocess
import locale


class ProcessManage(object):

    def kill_excel_proc(self, pid_name="desktop"):
        pid_list = []
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

    def run_command(self, ex):
        default_locale = locale.getdefaultlocale()
        code = "UTF-8"
        output = ''
        try:
            output = subprocess.check_output(ex, stderr=subprocess.STDOUT, encoding=code, shell=True)
        except:
            print("Command error: %s" % ex)
        # out = output[:92].decode("uft-8")
        return output



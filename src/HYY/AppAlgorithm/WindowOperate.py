import os
import re
import importlib
ProcessManager = importlib.import_module('ProcessManager')
ProcessManage = ProcessManager.ProcessManage


class HYOperate(object):
    close_sys = ("-s", "关机")
    restart_sys = ("-r", "重启")
    revoke_sys = ("-a", "取消命令")
    time_sys = ("-t", "延迟时间")

    def close_windows(self, time=0):
        cmd = "shutdown"
        ProcessManage().run_command(" ".join([cmd, self.close_sys[0], self.time_sys[0], str(time)]))


if __name__ == '__main__':
    HYOperate().close_windows()
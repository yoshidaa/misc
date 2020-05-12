# coding: UTF-8
import subprocess
import threading
import time
import traceback

from subprocess import check_output

# --- cpu limit configuration --------------------------------------
limits = { "avconv": 20 }
# ------------------------------------------------------------------

def cd_exec(pid, limit):
   lp = None
   try:
       lp = subprocess.Popen([ "cpulimit", "-l", str(limit), "-p", str(pid)], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, shell=False)
   except Exception:
       traceback.print_exc()

def scraiping_pid(procname):
    try:
        return set([i.decode("utf-8") for i in check_output(["pidof", procname]).split()])
    except Exception:
        return []

threads = {}
pre_map = {}
cur_map = {}

for procname, limit in limits.items():
    pre_map[procname] = []
    cur_map[procname] = []

while True:
    for procname, limit in limits.items():
        header = "[" + procname + ":" + str(limit) + "] "
        pre_map[procname] = cur_map[procname]
        cur_map[procname] = scraiping_pid(procname)

        if len(pre_map) != 0 and len(cur_map) == 0:
            print(header + "no process now")

        old_pids = list(set(pre_map[procname]) - set(cur_map[procname]))
        new_pids = list(set(cur_map[procname]) - set(pre_map[procname]))

        for p in new_pids:
            print( header + str(p) + " detected! ----->" )
            threads[p] = threading.Thread(target=cd_exec(p, limit))
            threads[p].start()

        for p in old_pids:
            print( header + str(p) + " <----- finished!" )
            threads[p].join(3)

    time.sleep(5)

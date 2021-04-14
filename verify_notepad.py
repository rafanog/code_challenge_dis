import subprocess as sp
import time
import re
import os
"""
Ejecutar Notepad.exe, esperar 10 segundos y luego si la app no fue cerrada por un usuario via UI, terminar el proceso.
Dependiendo de si fue cerrada manualmente o terminada por el script debería imprimir dos resultados distintos.
EJ:
App: notepad.exe, pid: 1234, "Cerrada por el usuario"
App: notepad.exe, pid: 1234, "Terminada por timeout"
"""
def execProcess(processName):
    #os.system("{}.exe".format(processName))
    p = sp.Popen([processName])

def termProcess(processName):
    os.system("TASKKILL /F /IM {} > nul".format(processName))

def getTaskList():
    tasks = sp.check_output(['tasklist']).decode('cp866', 'ignore').split("\r\n")

    p = {}
    for task in tasks:
        m = re.match("(.+?) +(\d+) (.+?) +(\d+) +(\d+.* K).*",task)
        if m is not None:
            #p.append({"process":m.group(1).upper(), "pid":m.group(2)})
            p.update([(m.group(1).upper(), m.group(2))])
            """
            #this creates a more detailed tasklist but commenting it out since
            #current requirement only needs the process name and pid
            "session_name":m.group(3),
            "session_num":m.group(4),
            "mem_usage":m.group(5)
            """
    ################################## prints process list
    """
    for process in p:
        print("process: {} - PID: {}".format(process, p[process]))
    """
    ##################################
    return p

def executeAndInspect(processName):
    print("Opening {}".format(processName))
    execProcess(processName) #open notepad and verify it correctly opened
    p = getTaskList()
    if processName.upper() not in p:
        print("Error while trying to open {}".format(processName))
    else:
        print("{} process opened!".format(processName))

    time.sleep(10) #wait for 10 secs
    result = "App - {}, pid: {}, ".format(processName, p[processName.upper()])
    p = getTaskList() #retrieve tasklist
    if processName.upper() not in p: #verify if it was closed by the user
        reason = "Cerrada por el usuario"
    else:
        termProcess(processName) #forcefully close
        reason = "Terminada por timeout"
    result += " \"{}\"".format(reason)

    print(result)

executeAndInspect("notepad.exe")

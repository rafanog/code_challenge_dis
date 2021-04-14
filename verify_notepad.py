import subprocess as sp
import re
import os
"""
Ejecutar Notepad.exe, esperar 10 segundos y luego si la app no fue cerrada por un usuario via UI, terminar el proceso.
Dependiendo de si fue cerrada manualmente o terminada por el script debería imprimir dos resultados distintos.
EJ:
App: notepad.exe, pid: 1234, "Cerrada por el usuario"
App: notepad.exe, pid: 1234, "Terminada por tiemeout"
"""
def execProcess(processName):
    #os.system("{}.exe".format(processName))
    sp.Popen(processName)

def getTaskList():
    tasks = sp.check_output(['tasklist']).decode('cp866', 'ignore').split("\r\n") #.split("\r\n")

    p = []
    for task in tasks:
        m = re.match("(.+?) +(\d+) (.+?) +(\d+) +(\d+.* K).*",task)
        if m is not None:
            p.append(m.group(1))
            """
            #this creates a more detailed list but commenting it out since
            #current requirement only needs the process name
            ,
            "pid":m.group(2),
            "session_name":m.group(3),
            "session_num":m.group(4),
            "mem_usage":m.group(5)
            """

    return p

def executeAndInspect(processName):
    print("Opening {}".format(processName))
    execProcess(processName)
    p = getTaskList()
    if processName not in p:
        print("Error while trying to open {}".format(processName))
    else:
        print("{} process opened!")


executeAndInspect("notepad.exe")

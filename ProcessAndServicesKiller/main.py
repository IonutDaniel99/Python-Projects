import psutil
import os
import sys
import subprocess
from time import sleep

if sys.platform.lower() == "win32":
    os.system('color')

PROCNAME = []
SERVNAME = []


class style():
    @staticmethod
    def RED(x): return '\033[31m' + str(x)
    @staticmethod
    def GREEN(x): return '\033[32m' + str(x)
    @staticmethod
    def YELLOW(x): return '\033[33m' + str(x)
    @staticmethod
    def RESET(x): return '\033[0m' + str(x)


def GetProcessFromFile():
    with open("ProcessesToKill.txt") as file:
        for line in file:
            line = line.strip()
            PROCNAME.append(line)


def ProcessRunOrNot():
    for ProcCheck in psutil.process_iter():
        if ProcCheck.name() in PROCNAME:
            print(str(ProcCheck.name()) +
                  style.GREEN(" Is Running") + style.RESET(""))
    for ProcCheckX in PROCNAME:
        if ProcCheckX not in psutil.process_iter():
            print(str(ProcCheckX) + style.RED(" Is Not Running") + style.RESET(""))


def DeleteProcess():
    ConfirmInput = input(style.YELLOW("  (WARN)  ") +
                         style.RESET("") + "KILL Running Procesess? [Y/N/R/B/E] ")
    print("====================================================")
    if ConfirmInput == "Y":
        for proc in psutil.process_iter():
            if proc.name() in PROCNAME:
                try:
                    print("Trying to kill process %s - Done" %
                          style.GREEN(proc.name()) + style.RESET(""))
                    proc.kill()
                except Exception as error:
                    print("[~] Error Occured while trying to kill %s : Error: %s" % (
                        style.RED(proc.name() + style.RESET("")), error))
        Select()

    elif ConfirmInput == "N":
        programName = "notepad.exe"
        fileName = "ProcessesToKill.txt"
        subprocess.Popen([programName, fileName])
        return
    elif ConfirmInput == "R":
        ProcessRunOrNot()
        DeleteProcess()
    elif ConfirmInput == "E":
        Exit()
    elif ConfirmInput == "B":
        Select()
    else:
        print(style.YELLOW(
            "================= Only Y/N/R/B/E ===================") + style.RESET(""))
        DeleteProcess()


def GetServiceFromFile():
    with open("ServicesToKill.txt") as file2:
        for line2 in file2:
            line2 = line2.strip()
            SERVNAME.append(line2)


def ServicesRunOrNot():
    for ServCheck in SERVNAME:
        service = psutil.win_service_get(ServCheck).name()
        service_dict = psutil.win_service_get(ServCheck).as_dict()
        if service_dict['status'] == 'running':
            print(str(service) + style.GREEN(" Is Running") + style.RESET(""))
        elif service_dict['status'] == 'stopped':
            print(str(service) + style.RED(" Is Stopped") + style.RESET(""))


def StopServices():
    ConfirmInput = input(style.YELLOW("  (WARN)  ") +
                         style.RESET("") + "Stop Running Services? [Y/N/R/B/E] ")
    print("====================================================")
    if ConfirmInput == "Y":
        for ServCheck in SERVNAME:
            service = psutil.win_service_get(ServCheck).name()
            service_dict = psutil.win_service_get(ServCheck).as_dict()
            if service_dict['status'] == 'running':
                try:
                    print("Trying to stop service %s" %
                          style.GREEN(str(service)) + style.RESET(""))
                    cmd = 'net stop ' + str(service)
                    print(cmd)
                    os.system(cmd)
                except Exception as error:
                    print("[~] Error Occured while trying to stop %s : Error: %s" % (
                        style.RED(str(service) + style.RESET("")), error))
        Select()

    elif ConfirmInput == "N":
        programName = "notepad.exe"
        fileName = "ServicesToKill.txt"
        subprocess.Popen([programName, fileName])
        return
    elif ConfirmInput == "R":
        ServicesRunOrNot()
        StopServices()
    elif ConfirmInput == "E":
        Exit()
    elif ConfirmInput == "B":
        Select()
    else:
        print(style.YELLOW(
            "================= Only Y/N/R/B/E ===================") + style.RESET(""))
        DeleteProcess()


def RamUsuage():
    ram = psutil.virtual_memory()
    print("Ram %s / %s / %s " % (
        style.GREEN("<Free " + str(ram.free >> 20) + " MB>") + style.RESET(""),
        style.YELLOW("<Used " + str(ram.used >> 20) + " MB>") +
        style.RESET(""),
        style.RED("<Total " + str(ram.total >> 20) + " MB>") + style.RESET("")))


def Processes():
    GetProcessFromFile()
    print("====================================================")
    print(style.YELLOW(
        "============ Details about processes ===============") + style.RESET(""))
    print("====================================================")
    ProcessRunOrNot()
    print("====================================================")
    DeleteProcess()
    print("====================================================")


def Services():
    GetServiceFromFile()
    print("====================================================")
    print(style.YELLOW(
        "============ Details about Services ===============") + style.RESET(""))
    print("====================================================")
    ServicesRunOrNot()
    print("====================================================")
    StopServices()


def Exit():
    print(style.RED("Execution Terminated By User") + style.RESET(""))
    sys.exit()
    return


def Select():
    RamUsuage()
    print("[1]Processes\n[2]Services\n[3]Exit")
    select_no = input("Select: ")
    if select_no == '1':
        Processes()
    elif select_no == '2':
        Services()
    elif select_no == '3':
        Exit()


def main():
    Select()


if __name__ == "__main__":
    main()

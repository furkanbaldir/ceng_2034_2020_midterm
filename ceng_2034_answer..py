#!/usr/bin/python3.6
import os
import sys
import requests
import time
import threading

def get_status(hostname):

        r = requests.head(hostname)
        status_code = str(r.status_code)
        if (status_code[0] == "2"):
            print(hostname + " is valid (status code : " + status_code + ")\n")
        elif (status_code[0] == "4" or status_code[0] == "5"):
            print(hostname + " is not valid (status code : " + status_code + ")\n")

#Opening
os.system("clear")
print("\n***********************************************************\n")
print("Welcome to my Operating System homework\n\n        © Made by Furkan Baldır\n")
print("***********************************************************\n")
print("This is your operating system:\n")
os.system("lsb_release -d")
print("\n***********************************************************\n")
print("Python version:\n")
os.system("python3 --version")
print("\n***********************************************************\n")
print("Kernel version:\n")
os.system("uname -srm")
print("\n***********************************************************")

print("\nPlease enter the number that you want to launch command:\n"
      "-1 --> Exit the application\n"
      " 1 --> Print Process ID (PID)\n"
      " 2 --> Print loadavg\n"
      " 3 --> Print 5 min loadavg and cpu core count\n"
      " 4 --> Print hostnames are valid or not valid with no using threads\n"
      " 5 --> Print hostnames are valid or not valid with using 5 threads\n"
      "\ncommands --> Print commands again\n"
      "cpuinfo --> Print your cpu info\n")

print("\n***********************************************************\n")
#loadavg value controls dynamically in while loop

hostnames = ["https://api.github.com","http://bilgisayar.mu.edu.tr","https://www.python.org/",
             "http://akrepnalan.com/ceng2034","https://github.com/caesarsalad/wow"]

while(1):
    num = input("Please enter the number: ")
    print("\n")

    #System overload controller
    loadavg = os.getloadavg()
    cpu_count = os.cpu_count()

    if (cpu_count - loadavg[1]) < 1:
        print("System overloaded\n")
        print("\n***********************************************************\n")
        sys.exit()

    if num == "":
        print("No value found.\n")
        print("\n***********************************************************\n")
    elif num == "-1":
        print("Good bye!\n")
        print("\n***********************************************************\n")
        sys.exit()
    elif num == "1":
        print("PID of this program is: "+str(os.getpid())+"\n")
        print("\n***********************************************************\n")
    elif num == "2":
        print("Loadavg: "+str(os.getloadavg())+"\n")
        print("\n***********************************************************\n")
    elif num == "3":
        print("5 min loadavg value is: "+str(loadavg[1])+"\n")
        print("CPU core count is: "+str(cpu_count)+"\n")
        print("\n***********************************************************\n")
    elif num == "4":
        startTime = time.time()
        for i in hostnames:
            get_status(i)
        finishTime = time.time()
        print("time is :" + str(finishTime - startTime) + "\n")
        print("\n***********************************************************\n")
    elif num == "5":
        startTime = time.time()

        thread1 = threading.Thread(target=get_status, args=(hostnames[0],))
        thread2 = threading.Thread(target=get_status, args=(hostnames[1],))
        thread3 = threading.Thread(target=get_status, args=(hostnames[2],))
        thread4 = threading.Thread(target=get_status, args=(hostnames[3],))
        thread5 = threading.Thread(target=get_status, args=(hostnames[4],))

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()

        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()

        finishTime = time.time()

        print("time is :" + str(finishTime - startTime) + "\n")
        print("\n***********************************************************\n")
    elif(num == "commands"):
        print("\nPlease enter the number that you want to launch command:\n"
              "-1 --> Exit the application\n"
              " 1 --> Print Process ID (PID)\n"
              " 2 --> Print loadavg\n"
              " 3 --> Print 5 min loadavg and cpu core count\n"
              " 4 --> Print hostnames are valid or not valid with no using threads\n"
              " 5 --> Print hostnames are valid or not valid with using 5 threads\n\n"
              "commands --> Print commands again\n"
              "cpuinfo --> Print your cpu info\n")
        print("\n***********************************************************\n")
    elif(num == "cpuinfo"):
        print(str(os.system("lscpu")))
        print("\n***********************************************************\n")

    else:
        print("This is not a command.\ ")
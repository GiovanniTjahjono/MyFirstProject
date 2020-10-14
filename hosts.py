import getopt
import sys

# a function to show only the list of Hostnames
# params command -a filename


def Argument_a(filename):
    try:
        hostsFile = open(filename)
        num_lines = sum(1 for line in open(filename))
    except:
        print(filename + " is not found")
        sys.exit(1)
    if num_lines <= 0:
        print("No hosts")
        sys.exit(0)
    else:
        print("Hostnames:")
        i = 0
        while i < num_lines:
            print(hostsFile.readline().split(" | ")[1])
            i += 1

# a function to show the list of domains
# params command -d domain filename


def Argument_d(filename, domain):
    try:
        hostsFile = open(filename)
        num_lines = sum(1 for line in open(filename))
    except:
        print(filename + " is not found")
        sys.exit(1)
    if num_lines <= 0:
        print("No hosts")
        sys.exit(0)
    else:
        numOfHostWithDomain = []
        i = 0
        while i < num_lines:
            host = hostsFile.readline()
            hostname = host.split(" | ")
            hostHasSplited = hostname[1].split(".")
            domainTemp = hostHasSplited[len(hostHasSplited) - 1]
            if domainTemp == domain:
                numOfHostWithDomain.append(hostname[0] + "    " + hostname[1] +
                                           "    " + hostname[2].split("\n")[0])
            i += 1
        if len(numOfHostWithDomain) != 0:
            print("Hostnames:")
            for host in numOfHostWithDomain:
                print(host)
        else:
            print("No hosts in the given domain")


# a function to show the class of the domain
#  params command -c A hosts_file
def Argument_c(filename, ipClass):
    try:
        hostsFile = open(filename)
        num_lines = sum(1 for line in open(filename))
    except:
        print("File " + filename + " is not found")
        sys.exit(1)
    if num_lines <= 0:
        print("No hosts")
        sys.exit(0)
    else:
        numOfSelectedIpClass = []
        classRangeStart = 0
        classRangeEnd = 0
        if ipClass == 'A':
            classRangeStart = 0
            classRangeEnd = 127
        elif ipClass == 'B':
            classRangeStart = 128
            classRangeEnd = 191
        elif ipClass == 'C':
            classRangeStart = 192
            classRangeEnd = 255
        else:
            print("Class is not found")
            sys.exit(0)
        i = 0
        while i < num_lines:
            host = hostsFile.readline()
            ip = host.split(" | ")
            ipHasSplited = ip[0].split(".")
            ipTemp = ipHasSplited[0]
            if int(ipTemp) >= classRangeStart and int(ipTemp) <= classRangeEnd:
                numOfSelectedIpClass.append(host.split("\n")[0])
            i += 1
        if len(numOfSelectedIpClass) != 0:
            print("Hostnames:")
            for host in numOfSelectedIpClass:
                print(host)
        else:
            print("No hosts in the given domain")


# a function to show the name, surname, date of completion
#  params command -v filename
def Argument_v():
    print("-------------------------------------------")
    print("|                    Hi                   |")
    print("-------------------------------------------")
    print("|                                         |")
    print("|   Fullname: Giovanni Tjahjono           |")
    print("| Student ID: 13389984                    |")
    print("|       Date: 8 October 2020              |")
    print("|                                         |")
    print("-------------------------------------------")


# Start the system
arguments = sys.argv

# possibly the option is either -a or -v
if len(arguments) == 3:
    if arguments[1] == "-a":
        Argument_a(arguments[2])
    if arguments[1] == "-v":
        Argument_v()
elif len(arguments) == 4:
    if arguments[1] == "-d":
        Argument_d(arguments[3], arguments[2])
    if arguments[1] == "-c":
        Argument_c(arguments[3], arguments[2])
else:
    print("The input is wrong")
    print('it should look like "hosts.py [option 1] [option 2] filename"')
    sys.exit(1)

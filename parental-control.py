# NOTE: This file should be copied to /etc/parental-control directory
import sys
import datetime


COL_USER = 0
COL_ACCESS  = 1
COL_SU = 3
COL_MO = COL_SU + 1
COL_TU = COL_SU + 2
COL_WE = COL_SU + 3
COL_TH = COL_SU + 4
COL_FR = COL_SU + 5
COL_SA = COL_SU + 6

# Commandline Argument: this, config-file, log-file
CMDL_ARGS = 5
if len(sys.argv) >= CMDL_ARGS:
    action      = sys.argv[1]
    cfg_file    = sys.argv[2]
    username    = sys.argv[3]
    logfile     = sys.argv[4]
else:
    print("Not enough arguments passed (", len(sys.argv), " >= ", CMDL_ARGS, ")")
    exit(-1)

# Read configurations from configuration file
with open(cfg_file) as f:
    contents = f.readlines()

cfg_table = []
for line in contents:
    sline = line.replace(" ", "").replace("\t", "").replace("\n", "")
    if len(sline) == 0:
        continue
    if sline[0] == '#':
        continue
    cfg_table.append(line.split())


# Time management
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M")

# Functions
def prepend_text_to_file(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

logtext = "action=" + action + "; username=" + username + "; date=" + date + "; time=" + time
prepend_text_to_file(logfile, logtext)

print(cfg_table)
print("action = ", action)
print("username = ", username)
print("logfile = ", logfile)
print(date, " ", time)

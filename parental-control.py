# NOTE: This file should be copied to /etc/parental-control directory
import sys
import datetime
import subprocess


COL_USER = 0
COL_FUNC = 1
COL_WKDY = 2
COL_SU = COL_WKDY
COL_MO = COL_SU + 1
COL_TU = COL_SU + 2
COL_WE = COL_SU + 3
COL_TH = COL_SU + 4
COL_FR = COL_SU + 5
COL_SA = COL_SU + 6

# F U N C T I O N S
def get_timespent_by_user(user, ac_output):
    prev_line = ""
    tspent = 0
    for line in ac_output:
        if "Today" in line and user in prev_line:
            tspent = float(line.split()[2]) * 60
            break
        prev_line = line
    return tspent

def get_timeallowed_user(user, function, cfg_table):
    tallowed = 7 * 24 * 60.0
    for row in cfg_table:
        if row[COL_USER] == user and row[COL_FUNC] == function:
            wkday = datetime.datetime.today().weekday() + COL_WKDY
            tallowed = float(row[wkday])
            break
    return tallowed


# Commandline Argument: this, config-file, log-file
CMDL_ARGS = 4
if len(sys.argv) >= CMDL_ARGS:
    cfg_file    = sys.argv[1]
    username    = sys.argv[2]
    logfile     = sys.argv[3]
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


# Find out how many minutes the user had already spent
ac_output = subprocess.run(["ac", "-dp"], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
time_spent = get_timespent_by_user(username, ac_output)
print("time_spent by", username, "=", time_spent, "minutes")

# Find out how many minutes the user is allowed today
login_allowed = get_timeallowed_user(username, "login", cfg_table)
brows_allowed = get_timeallowed_user(username, "http", cfg_table)
print("time_allowed: login =", login_allowed, "browsing =", brows_allowed, "minutes")

now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M")


print("username = ", username)
print("logfile = ", logfile)
print(date, " ", time)

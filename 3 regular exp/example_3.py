import re


def show_time_of_pid(line):
    pattern = r"([\w\s:]{14})[\s.\w=]+\[(\d+)\]"
    result = re.search(pattern, line)
    return (result[1]+" pid:"+result[2])


# Jul 6 14:01:23 pid:29440
print(
    show_time_of_pid(
        "Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")
)

# Jul 6 14:02:08 pid:29187
print(show_time_of_pid(
    "Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)"))

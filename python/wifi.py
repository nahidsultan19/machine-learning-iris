
import subprocess
data = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(':')[1][1:-1] for i in data if "All users Profile" in i]
for x in profiles:
    results = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profile', x, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(':')[1][1:-1] for b in results if "Key Content" in b]
    try:
        print("{:<30}|{:<}".format(x, results[0]))
    except IndexError:
        print("{:<30}|{:<}".format(x, ""))

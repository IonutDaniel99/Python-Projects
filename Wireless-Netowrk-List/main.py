import subprocess

WiFis = []

# Well i had a lot of idea for this script
# The problem is - python wifis and windows don`t match



def main():
    results = subprocess.check_output(
        ["netsh", "wlan", "show", "network", "Bssid"])
    results = results.decode("ascii")  # needed in python 3
    results = results.replace("\r", "")
    ls = results.split("\n")
    ls = ls[4:]
    x = 0
    while x < len(ls):
        WiFis.append(ls[x])
        x += 1
    for line in WiFis:
        print(line)


if __name__ == "__main__":
    main()

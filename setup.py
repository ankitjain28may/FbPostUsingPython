import subprocess

installs = [
        "pip install bs4",
        "pip install selenium"
    ]
print("Wait for the installations, Its in progress..!!!")
for install in installs:
    query = install.split()
    proc = subprocess.Popen(query, stdout=subprocess.PIPE, shell=True)
    output, error = proc.communicate()
    if output!=None:
        print(output.decode('utf-8'))
    elif error!=None:
        print(error.decode('utf-8'))

print("Everything is set-up in the system, Now Scrape as much as you can..!")
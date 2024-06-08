import sys
import subprocess
def Main():
    Input = ' '.join(sys.argv[1:])#"echo hi > echo.txt"
    print(f"[INFO]: Command Input: {Input}")
    try:
        Split = Input.split(":")
        Command = Split[0]
        Pipe = Split[1]
    except IndexError:
        print("[ERROR]: Invalid syantax")
        raise RuntimeError("Index Error")
    Process = subprocess.Popen(Command,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    STDOUT, STDERR = Process.communicate()
    Result = ""
    if Process.returncode != 0:
        print(f"[COMMAND ERROR]: Non-Zero Error Code: {Process.returncode}")
        print(f"[RESULT]: {STDERR.decode()}")
        Result = STDERR.decode()
    else:
        Result = STDOUT.decode()
    with open(Pipe,"w") as File:
        File.writelines(Result)
try:
    Main()
except Exception as Error:
    print(f"[ERROR]: {Error}")
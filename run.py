#0xb800.Venom Mustafa
import subprocess
import os
import signal
import sys

BACKEND_DIR = "backend"
FRONTEND_DIR = "web_frontend"

processes = []

def start():
    print("[+] Starting Backend...")
    backend = subprocess.Popen(
        ["uvicorn", "backend_api:app", "--reload", "--app-dir", BACKEND_DIR]
    )
    processes.append(backend)

    print("[+] Starting Frontend...")
    frontend = subprocess.Popen(
        ["npm", "run", "start"],
        cwd=FRONTEND_DIR
    )
    processes.append(frontend)


def shutdown(signum, frame):
    print("\n[!] Terminating all services...")
    for p in processes:
        if p.poll() is None:
            p.terminate()
    sys.exit(0)


if __name__ == "__main__":
    # Handle Ctrl+C, Ctrl+Z dono tigger
    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)
    signal.signal(signal.SIGTSTP, shutdown)

    start()

    for p in processes:
        p.wait()
import os
import subprocess
import time

os.system("title AutoInstallerV1")

# Change app_dirs to directory of the application you'd like to install
app_dirs = ["C:/test"]

for app_dir in app_dirs:
    for filename in os.listdir(app_dir):
        filepath = os.path.join(app_dir, filename)
        if os.path.isfile(filepath) and (filename.endswith(".exe") or filename.endswith(".msi")):
            print(f"\033[32mInstalling {filename}...\033[0m")
            try:
                subprocess.run([filepath, "/quiet", "/norestart"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"\033[31mInstallation of {filename} failed with exit code {e.returncode}\033[0m")
        else:
            print(f"\033[33mSkipping {filename} (not an executable file)\033[0m")

timer = 5
while timer > 0:
    print(f"\033[31mClosing window in {timer} seconds...\033[0m")
    time.sleep(1)
    timer -= 1

os.system("exit")

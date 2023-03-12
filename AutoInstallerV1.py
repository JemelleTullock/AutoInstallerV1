import os
import time

os.system("title AutoInstallerV1")

# Change app_dirs to directory of the application you'd like to install
app_dirs = ["C:/test", "C:/test2"]

for app_dir in app_dirs:
    for filename in os.listdir(app_dir):
        filepath = os.path.join(app_dir, filename)
        if os.path.isfile(filepath) and filename.endswith(".exe"):
            print(f"\033[32mInstalling {filename}...\033[0m")
            os.system(filepath)
        else:
            print(f"\033[33mSkipping {filename} (not an executable file)\033[0m")

timer = 5
while timer > 0:
    print(f"\033[31mClosing window in {timer} seconds...\033[0m")
    time.sleep(1)
    timer -= 1

os.system("exit")

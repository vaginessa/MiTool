import os

print("\Flashing Custom Recovery...\n")

ROM_FOLDER = "/sdcard/Download/mi-flash-CustomRecovery"

if not os.path.exists(ROM_FOLDER):
    os.makedirs(ROM_FOLDER)

input("\nmake sure to place *.img (recovery) file in {} folder .. Then press Enter\n".format(ROM_FOLDER))

while True:
    img_files = [f for f in os.listdir(ROM_FOLDER) if f.endswith(".img")]
    if not img_files:
        input(f"\nCould not find *.img file in {ROM_FOLDER}.\n"
              f"\nPlease make sure to place *.img file in {ROM_FOLDER} folder. Press Enter when ready.\n")
        continue
    if img_files:
        input("\nMake sure your device is in fastboot mode. Connect your device using OTG, then press Enter when ready\n")
        break

while True:
    status = os.popen("fastboot devices | grep -o 'fastboot'").read().strip()
    if status == "fastboot":
        break
    else:
        input("\nplease Verify that the device is in fastboot mode! If so, check that it is connected via OTG! then press Enter\n")
        continue


os.system("fastboot flash recovery {}/{}".format(ROM_FOLDER, img_files[0]))
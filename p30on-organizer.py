#Author:      Yaser Doosti
#Author URI:  https://p30on.ir
#Description: P30on File Organizer
#Vrsion:      1.0.0
from pathlib import Path
import shutil
import os
import sys

os.system("")  # Colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

if getattr(sys, "frozen", False):
    self_path = Path(sys.executable).resolve()   # exe (PyInstaller)
else:
    self_path = Path(__file__).resolve()         # .py script
downloads = self_path.parent

folder = {
    "-Images": [".jpg", ".jpeg", ".png", ".webp", ".jfif", ".svg"],
    "-Documents": [".pdf", ".txt", ".doc", ".docx", ".tif"],
    "-Videos": [".mp4", ".avi"],
    "-Musics": [".mp3"],
    "-Compressed": [".zip", ".rar", ".gz", ".7z"],
    "-EXE": [".exe", ".msi"],
    "-DataBases": [".sql"],
    "-Fonts": [".ttf", ".woff", ".woff2"],
    "-Translate": [".po", ".mo"],
    "-Exel": [".xlsx", ".csv"],
    "-PSD": [".psd"],
    "-APK": [".apk"],
    "-ISO": [".iso"],
    "-WebDev": [".html", ".htm", ".js", ".json", ".php", ".xml", ".mhtml"],
}

for name in folder:
    (downloads / name).mkdir(exist_ok=True)

moved = 0

for file in list(downloads.iterdir()):
    if file == self_path or not file.is_file():
        continue
    ext = file.suffix.lower()
    for name, exts in folder.items():
        if ext in exts:
            target = downloads / name / file.name
            if not target.exists():
                shutil.move(str(file), str(target))
                moved += 1
            break

if moved:
    print(f"{GREEN}Done! {moved} file(s) have been organized.{RESET}")
else:
    print(f"{RED}No files to organize.{RESET}")

input("Press Enter to close...")
# 📂 File Organizer

A tiny, dependency-free tool that tidies up a messy folder (like **Downloads**) in one click.
Drop it into any folder, run it, and your files are sorted into neat categories by extension.

> **نسخه‌ی فارسی** در پایین همین صفحه است ⬇️

---

## ✨ Features

- 🗂️ Sorts files into folders by extension (images, documents, videos, archives, and more)
- 🧠 Works on **the folder it lives in**, no hard-coded paths
- 🛡️ Never moves itself (safe even though `.exe` is a handled extension)
- 🔒 Never overwrites: if a file with the same name already exists in the target, it is skipped
- 🎨 Clear colored result: green when files were organized, red when there was nothing to do
- 📦 Pure Python standard library, so there is nothing to install
- 🧱 Can be built into a single portable `.exe` with PyInstaller

---

## 🚀 Usage

### Option 1: Run the script

```bash
python p30on-organizer.py
```

On Windows, if `python` is not recognized, use:

```bash
py p30on-organizer.py
```

### Option 2: Use the standalone `.exe`

1. Copy `p30on-organizer.exe` into the folder you want to organize.
2. Double-click it.
3. Read the result and press **Enter** to close.

### Example output

```
Done! 124 file(s) have been organized.
Press Enter to close...
```

If nothing matched:

```
No files to organize.
Press Enter to close...
```

---

## 🗃️ Categories

| Folder | Extensions |
|---|---|
| `-Images` | `.jpg` `.jpeg` `.png` `.webp` `.jfif` `.svg` |
| `-Documents` | `.pdf` `.txt` `.doc` `.docx` `.tif` |
| `-Videos` | `.mp4` `.avi` |
| `-Musics` | `.mp3` |
| `-Compressed` | `.zip` `.rar` `.gz` `.7z` |
| `-EXE` | `.exe` `.msi` |
| `-DataBases` | `.sql` |
| `-Fonts` | `.ttf` `.woff` `.woff2` |
| `-Translate` | `.po` `.mo` |
| `-Exel` | `.xlsx` `.csv` |
| `-PSD` | `.psd` |
| `-APK` | `.apk` |
| `-ISO` | `.iso` |
| `-WebDev` | `.html` `.htm` `.js` `.json` `.php` `.xml` `.mhtml` |

Files with any other extension are left untouched. Only files in the top level of the folder are moved; subfolders are ignored.

### Adding your own category

Open the script and add a line to the `folder` dictionary:

```python
"-Ebooks": [".epub", ".mobi"],
```

---

## 🔧 Build a single-file EXE

```bash
pip install pyinstaller
pyinstaller --onefile p30on-organizer.py
```

The result appears in the `dist` folder. Do **not** use `--noconsole`, otherwise you won't see the result message.

---

## ⚠️ Notes

- Files are **really moved**, not copied. Try it on a test folder first.
- Don't run it while downloads are in progress.
- Some antivirus programs may flag PyInstaller executables as suspicious. This is a known false positive.
- Requires Python 3.6+ only if you run the `.py` version.

---

---

# 📂 مرتب‌ساز فایل 

یک ابزار کوچک و بدون وابستگی که پوشه‌های شلوغ (مثل **Downloads**) را با یک کلیک مرتب می‌کند.
آن را در هر پوشه‌ای بگذارید و اجرا کنید؛ فایل‌ها بر اساس پسوند در پوشه‌های مرتب دسته‌بندی می‌شوند.

## ✨ امکانات

- 🗂️ دسته‌بندی فایل‌ها بر اساس پسوند (تصاویر، اسناد، ویدیوها، فایل‌های فشرده و ...)
- 🧠 روی **همان پوشه‌ای که برنامه در آن است** کار می‌کند، بدون مسیر ثابت
- 🛡️ هرگز خودش را جابه‌جا نمی‌کند
- 🔒 فایل هم‌نام را بازنویسی نمی‌کند و از آن عبور می‌کند
- 🎨 پیام نتیجه‌ی رنگی: سبز برای انجام کار، قرمز برای نبودن فایلی جهت انتقال
- 📦 فقط کتابخانه‌ی استاندارد پایتون؛ چیزی برای نصب نیست
- 🧱 قابل تبدیل به یک فایل `.exe` مستقل با PyInstaller

## 🚀 روش استفاده

**اجرای اسکریپت:**

```bash
python p30on-organizer.py
```

اگر در ویندوز `python` شناخته نشد، از `py` استفاده کنید.

**استفاده از فایل exe:**

1. فایل `p30on-organizer.exe` را داخل پوشه‌ی موردنظر کپی کنید.
2. روی آن دابل‌کلیک کنید.
3. پیام نتیجه را ببینید و برای بستن Enter بزنید.

## ➕ افزودن دسته‌ی جدید

در دیکشنری `folder` داخل کد، یک خط اضافه کنید:

```python
"-Ebooks": [".epub", ".mobi"],
```

## 🔧 ساخت فایل exe

```bash
pip install pyinstaller
pyinstaller --onefile p30on-organizer.py
```

خروجی در پوشه‌ی `dist` قرار می‌گیرد. از گزینه‌ی `--noconsole` استفاده نکنید تا پیام نتیجه را ببینید.

## ⚠️ نکات مهم

- فایل‌ها **واقعاً جابه‌جا** می‌شوند (کپی نمی‌شوند). اول روی یک پوشه‌ی آزمایشی امتحان کنید.
- هنگام دانلود فعال، برنامه را اجرا نکنید.
- بعضی آنتی‌ویروس‌ها ممکن است exeهای PyInstaller را اشتباهاً مشکوک تشخیص دهند.
- فقط فایل‌های سطح اول پوشه جابه‌جا می‌شوند، نه محتوای زیرپوشه‌ها.

import os
import requests
import shutil

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOAD_DIR = os.path.join(BASE_DIR, "downloads")

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

downloaded_img_path = os.path.join(DOWNLOAD_DIR, '1.jpg')
url = "https://www.adamwestcreative.com/static/media/Headshot.6907dbd4db0ec04d1a64.jpg"


# a smallish item
r = requests.get(url, stream=True)
r.raise_for_status()  # 200
with open(downloaded_img_path, 'wb') as f:
    f.write(r.content)

dl_filename = os.path.basename(url)
new_dl_path = os.path.join(DOWNLOAD_DIR, dl_filename)

with requests.get(url, stream=True)as r:
    with open(downloaded_img_path, 'wb') as file_obj:
        shutil.copyfileobj(r.raw, file_obj)

import tkinter as tk
import requests
from idm import IDMan
downloader = IDMan()
def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename
 
def start_download():
    url = entry_url.get()
    local_filename = entry_filename.get()
    download_file(url, local_filename)
    label_status['text'] = f'Download of {local_filename} complete!'

root = tk.Tk()
root.title("Download Manager")

frame_url = tk.Frame(root)
frame_url.pack(pady=10)

label_url = tk.Label(frame_url, text="URL:")
label_url.pack(side='left')

entry_url = tk.Entry(frame_url)
entry_url.pack(side='left')

frame_filename = tk.Frame(root)
frame_filename.pack(pady=10)

label_filename = tk.Label(frame_filename, text="Save as:")
label_filename.pack(side='left')

entry_filename = tk.Entry(frame_filename)
entry_filename.pack(side='left')

frame_download = tk.Frame(root)
frame_download.pack(pady=10)

button_download = tk.Button(frame_download, text="Download", command=start_download)
button_download.pack(side='left')

label_status = tk.Label(frame_download, text="")
label_status.pack(side='left')

root.mainloop()

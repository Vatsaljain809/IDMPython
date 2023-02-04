import tkinter as tk

class DownloaderApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Download Manager")
        self.geometry("400x400")

        self.toolbar = tk.Frame(self, bg="White", height=30)
        self.toolbar.pack(fill=tk.X, pady=(0, 10))

        self.add_download_button = tk.Button(self.toolbar, text="Add URL", bg="gray", fg="white")
        self.add_download_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = tk.Button(self.toolbar, text="Pause", bg="gray", fg="white")
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.resume_button = tk.Button(self.toolbar, text="Resume", bg="gray", fg="white")
        self.resume_button.pack(side=tk.LEFT, padx=10)
        self.listbox = tk.Listbox(self)
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.listbox.insert(tk.END, "Download 1", )
        self.listbox.insert(tk.END, "Download 2")
        self.listbox.insert(tk.END, "Download 3")
if __name__ == '__main__':
    app = DownloaderApp()
    app.mainloop()

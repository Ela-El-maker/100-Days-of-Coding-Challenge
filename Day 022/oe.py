import os
import pygame
import tkinter as tk
from tkinter import filedialog, messagebox

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")

        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.playlist = []
        self.current_index = 0

        self.create_widgets()

    def create_widgets(self):
        # Buttons
        self.btn_open = tk.Button(self.master, text="Open", command=self.open_file)
        self.btn_play = tk.Button(self.master, text="Play", command=self.play_music)
        self.btn_pause = tk.Button(self.master, text="Pause", command=self.pause_music)
        self.btn_stop = tk.Button(self.master, text="Stop", command=self.stop_music)
        self.btn_open.grid(row=0, column=0, padx=5, pady=5)
        self.btn_play.grid(row=0, column=1, padx=5, pady=5)
        self.btn_pause.grid(row=0, column=2, padx=5, pady=5)
        self.btn_stop.grid(row=0, column=3, padx=5, pady=5)

        # Status label
        self.lbl_status = tk.Label(self.master, text="", fg="blue")
        self.lbl_status.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        # Initialize pygame
        pygame.mixer.init()

    def open_file(self):
        file_path = filedialog.askopenfilename(initialdir=self.current_dir, title="Select Music",
                                               filetypes=(("MP3 files", "*.mp3"), ("All files", "*.*")))
        if file_path:
            self.playlist.append(file_path)
            self.lbl_status.config(text=f"Added {os.path.basename(file_path)} to playlist")

    def play_music(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()
            self.lbl_status.config(text=f"Now playing: {os.path.basename(self.playlist[self.current_index])}")

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.lbl_status.config(text="Music paused")

    def stop_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.lbl_status.config(text="Music stopped")

def main():
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()

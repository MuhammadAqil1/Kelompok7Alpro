import tkinter as tk
from tkinter import messagebox, filedialog
import threading
import time
import random

class AplikasiProduktivitasMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Toolkit Produktivitas Mahasiswa")
        self.root.geometry("600x400")
        
        
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        
        fitur_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Fitur", menu=fitur_menu)
        fitur_menu.add_command(label="Timer Belajar", command=self.tampilkan_timer)
        fitur_menu.add_command(label="Catatan Harian", command=self.tampilkan_catatan)
        fitur_menu.add_command(label="Daftar Tugas", command=self.tampilkan_todo)
        fitur_menu.add_command(label="Kalkulator", command=self.tampilkan_kalkulator)
        
        menu.add_command(label="Kutipan Motivasi", command=self.tampilkan_kutipan)
        
        self.frame_utama = tk.Frame(self.root)
        self.frame_utama.pack(fill="both", expand=True)
        
        
        self.tampilkan_timer()

    def bersihkan_frame(self):
        for widget in self.frame_utama.winfo_children():
            widget.destroy()


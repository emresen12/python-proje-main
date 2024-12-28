import tkinter as tk
from tkinter import ttk,messagebox
from movie import deleteMovie

def openEditMovie(root, selected, saveFn, fetchFn):
    if not selected or len(selected) < 6:
        messagebox.showerror("Hata", "Lütfen düzenlemek için bir içerik seçiniz")
        return
    form_window = tk.Toplevel(root)
    form_window.title("İçerikBilgileri")
    window_width = 300
    window_height = 450
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    print(selected)
    form_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    tk.Label(form_window, text="İçerik türü:").pack(pady=5)
    film_kind_entry = ttk.Combobox(form_window,values=["Film","Dizi"])
    film_kind_entry.pack(pady=5)
    
    tk.Label(form_window, text="İçerik İsmi:").pack(pady=5)
    film_name_entry = tk.Entry(form_window)
    film_name_entry.pack(pady=5)

    tk.Label(form_window, text="İçerik Konusu:").pack(pady=5)
    film_type_combobox = ttk.Combobox(form_window, values=["Aksiyon", "Komedi", "Dram", "Romantik", "Bilim Kurgu"])
    film_type_combobox.pack(pady=5)
    tk.Label(form_window, text="İçerik Durumu:").pack(pady=5)
    film_status_combobox = ttk.Combobox(form_window, values=["Izlendi", "Izlenecek", "Izleniyor"])
    film_status_combobox.pack(pady=5)

    tk.Label(form_window, text="İçerik Puani (1-10):").pack(pady=5)
    film_rating_entry = tk.Entry(form_window)
    film_rating_entry.pack(pady=5)
    tk.Label(form_window, text="İçerik Notu").pack(pady=5)
    film_note_entry = tk.Entry(form_window)
    film_note_entry.pack(pady=5)




    film_kind_entry.set(selected[0])
    film_name_entry.insert(0,selected[1])
    film_type_combobox.set(selected[2])
    film_status_combobox.set(selected[3])
    film_rating_entry.insert(0,selected[4])
    film_note_entry.insert(0,selected[5])

    def save_form():
        film_kind=film_kind_entry.get()
        film_name = film_name_entry.get()
        film_type = film_type_combobox.get()
        film_status = film_status_combobox.get()
        film_rate = film_rating_entry.get()
        film_note = film_note_entry.get()
        try:
            film_rating = float(film_rating_entry.get())
            if film_rating < 1 or film_rating > 10:
                raise ValueError("Not 1 ile 10 arasında olmalı.")
        except ValueError as e:
            messagebox.showerror("Hata", f"Geçersiz giriş: {e}")
            return
        deleteMovie(selected[1])
        saveFn(film_kind,film_name,film_type,film_rate,film_status,film_note)
        fetchFn()
        messagebox.showinfo("Başarılı", f"Çeşit:{film_kind} Film Adı: {film_name}\nTür: {film_type}\nNot: {film_rating}")
        form_window.destroy()

    save_button = tk.Button(form_window, text="Kaydet", command=save_form)
    save_button.pack(pady=10)

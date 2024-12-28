from movie import getMovies, add_movie
from PIL import ImageTk, Image
import newMovie
import json
import tkinter as tk
from tkinter import ttk, messagebox, Button, Label
from tkinter.messagebox import showinfo
from editMovie import openEditMovie

root = tk.Tk()
root.title('Favori Film Uygulaman')

window_width = 1200
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.iconbitmap('./images/movie.ico')

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

selectedMovie = []
header = tk.Frame(root, bg="#2c3e50", height=50)
header.pack(fill=tk.X, side=tk.TOP)

header_label = tk.Label(
    header, text="Kayıtlı Filmlerim", bg="#2c3e50", fg="white", font=("Arial", 16, "bold")
)
header_label.pack(side=tk.LEFT, padx=20, pady=10)

edit_button = tk.Button(header, text="Duzenle", bg="gray", fg="white", padx=10, font=("Arial", 12, "bold"),
                        command=lambda: openEditMovie(root, selectedMovie, saveFn=add_movie, fetchFn=fetchMovies))
edit_button.pack(side=tk.RIGHT, padx=20, pady=10)
add_button = tk.Button(header, text="+", bg="green", fg="white", padx=10, font=("Arial", 12, "bold"),
                       command=lambda: newMovie.open_form(root, saveFn=add_movie, fetchFn=fetchMovies))
add_button.pack(side=tk.RIGHT, padx=20, pady=10)





option_frame = tk.Frame(root, bg="#2c3e50", width=200, height=800)
option_frame.pack(side=tk.LEFT, fill=tk.Y)
option_frame.pack_propagate(False)

menu_label = tk.Label(option_frame, text="Menü", bg="#2c3e50", font=("Arial", 14, "bold"), fg="White")
menu_label.pack(pady=20)

alllist_btn = tk.Button(option_frame, text="Tüm kaydettiklerim", font=("Arial", 12), fg="white", bg="#2c3e50", bd=0,command=lambda: select_menu("alllist"))
alllist_btn.place(x=30, y=100, width=140, height=30)

movielist_btn = tk.Button(option_frame, text="Film listem", font=("Arial", 12), fg="white", bg="#2c3e50", bd=0,
                          command=lambda: select_menu("movielist"))
movielist_btn.place(x=30, y=150, width=140, height=30)

tvshowlist_btn = tk.Button(option_frame, text="Dizi Listem", font=("Arial", 12), fg="white", bg="#2c3e50", bd=0,
                           command=lambda: select_menu("tvshowlist"))
tvshowlist_btn.place(x=30, y=200, width=140, height=30)

#yanlarında çıkan mavi ayıraç
alllist_indicate = tk.Label(option_frame, text="", bg="White")
alllist_indicate.place(x=10, y=100, width=10, height=30)

movielist_indicate = tk.Label(option_frame, text="", bg="White")
movielist_indicate.place(x=10, y=150, width=10, height=30)
movielist_indicate.place_forget()
tvshowlist_indicate = tk.Label(option_frame, text="", bg="White")
tvshowlist_indicate.place(x=10, y=200, width=10, height=30)
movielist_indicate.place_forget()
tvshowlist_indicate.place_forget()

#alllist ekranının framei
table_frame = tk.Frame(root, bg="gray", width=1000, height=1000)
table_frame.pack_propagate(False)
table_frame.pack(padx=20, pady=20)

columns = ("Çeşit", "Isim", "Tur", "Durum", "Puan", "Not")
tree = ttk.Treeview(table_frame, columns=columns, show='headings')
tree.heading("Çeşit", text="Çeşit", anchor="w")
tree.heading("Isim", text="Isim", anchor="w")
tree.heading("Tur", text="Tur", anchor="w")
tree.heading("Durum", text="Durum", anchor="w")
tree.heading("Puan", text="Puan", anchor="w")
tree.heading("Not", text="Not", anchor="w")

tree.column("Çeşit", width=150, anchor="w")
tree.column("Isim", width=150, anchor="w")
tree.column("Tur", width=100, anchor="w")
tree.column("Durum", width=100, anchor="w")
tree.column("Puan", width=100, anchor="w")
tree.column("Not", width=100, anchor="w")


def fetchall():
    tree.delete(*tree.get_children())

    movies = getMovies()
    for movie in movies:
        print(movie)
        tree.insert("", tk.END,
                    values=(movie["kind"], movie["name"], movie["type"], movie["status"], movie["rate"], movie["note"]))


def remove_all():
    tree.delete(*tree.get_children())
    with open("movies.json", "w") as file:
        json.dump({"movies": []}, file)

def remove_one():
    selected_item = tree.selection()[0]


    item_values = tree.item(selected_item, "values")
    moviename=item_values[1]

    tree.delete(selected_item)
    with open("movies.json", "r") as file:
            data = json.load(file)
    filtered_movies = [movie for movie in data["movies"] if movie["name"] != moviename]
    data["movies"] = filtered_movies
    with open("movies.json", "w") as file:
        json.dump(data, file, indent=4)


remove_one_button=tk.Button(header,text="Sil",bg="gray",fg="white",padx=10,font=("Arial",12,"bold"),command=lambda :remove_one())
remove_one_button.pack(side=tk.RIGHT, padx=20, pady=10)





def fetchMovies():
    tree.delete(*tree.get_children())

    movies = getMovies()
    for movie in movies:
        if movie["kind"] == "Film":
            print(movie)
            tree.insert("", tk.END, values=(
            movie["kind"], movie["name"], movie["type"], movie["status"], movie["rate"], movie["note"]))


def fetchTvshows():
    tree.delete(*tree.get_children())

    movies = getMovies()
    for movie in movies:
        if movie["kind"] == "Dizi":
            print(movie)
            tree.insert("", tk.END, values=(
            movie["kind"], movie["name"], movie["type"], movie["status"], movie["rate"], movie["note"]))


fetchall()


def item_selected(event):
    global selectedMovie
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = list(item['values'])
        selectedMovie = record;


tree.bind('<<TreeviewSelect>>', item_selected)
tree.pack(fill="both", expand=True)
table_frame.place_forget()

#table frame buraya kadar

#first screen frame işlemleri başlıyor

root.iconbitmap('C:\\python-proje-main\\phthonprojeresim2.png')

first_screen_image = ImageTk.PhotoImage(Image.open('phthonprojeresim2.png').resize((1200,800),Image.Resampling.LANCZOS))


first_screen_frame = tk.Frame(root, bg="white")

first_screen_frame.place(x=0, y=0, width=1200, height=800)
exitthefirstscreenbtn= Button(
    first_screen_frame,
    text="Giriş Yap",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#333333",
    activebackground="#444444",
    activeforeground="white",
    bd=0,
    relief="flat",
    padx=20,
    pady=10,
    command=lambda :select_menu("alllist")
)



image_label = tk.Label(first_screen_frame, image=first_screen_image, bg="white")
image_label.place(x=0, y=0, relwidth=1, relheight=1)
exitthefirstscreenbtn.place(relx=0.5, rely=0.5, anchor="center")
exitthefirstscreenbtn.lift()#resmin üstüne koyuyor


#first_screen_frame.place_forget()


movielist_frame = tk.Frame(root, bg="white")  # Film listesi için çerçeve
movielist_frame.place(x=200, y=0, width=1000, height=800)
tk.Label(movielist_frame, text="Tüm Kaydettiklerim", font=("Arial", 20), bg="white").pack(pady=20)
movielist_frame.place_forget()

tvshowlist_frame = tk.Frame(root, bg="white")  # Dizi listesi için çerçeve
tvshowlist_frame.place(x=200, y=0, width=1024, height=1024)
tk.Label(tvshowlist_frame, text="Dizi Listem", font=("Arial", 20), bg="white").pack(pady=20)

tvshowlist_frame.place_forget()  # Başlangıçta gizle


def select_menu(menu_name):
    first_screen_frame.place_forget()
    alllist_indicate.place_forget()
    movielist_indicate.place_forget()
    tvshowlist_indicate.place_forget()
    table_frame.place_forget()
    movielist_frame.place_forget()
    tvshowlist_frame.place_forget()
    if menu_name == "alllist":
        alllist_indicate.place(x=10, y=100, width=10, height=30)
        fetchall()
    elif menu_name == "movielist":
        movielist_indicate.place(x=10, y=150, width=10, height=30)
        fetchMovies()


    elif menu_name == "tvshowlist":
        tvshowlist_indicate.place(x=10, y=200, width=10, height=30)
        fetchTvshows()


root.mainloop()

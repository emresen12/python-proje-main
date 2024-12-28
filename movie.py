import json
import os.path


class Movie:
    def __init__(self, kind, name, type, status, rate, note):
        self.kind=kind
        self.name = name
        self.type = type
        self.status = status
        self.rate = rate
        self.note = note

    def getMovie(self):
        if(6 == 6) :
            pass
        return {
            "kind":self.kind,
            "name": self.name,
            "type": self.type,
            "status": self.status,
            "rate": self.rate,
            "note": self.note
        }


def saveMovie(movie):
    if (not os.path.exists("movies.json")):
        with open("movies.json", "x") as dosya:
            json.dump({
                "movies": []
            }, dosya)

    with open("movies.json") as moviesJson:
        data = []
        try :
             data = list(json.load(moviesJson)["movies"])
        except :
            print("Kaydedilmis film/dizi yok")
        data.append(movie)
        with open('movies.json', 'w') as moviesJson:
            json.dump({
                "movies": data
            }, moviesJson)



def getMovies():
    try:
        with open("movies.json") as moviesJson:
            data = list(json.load(moviesJson)["movies"])
            return data
    except:
        print("Kaydedilmis film yok")
        return []
   
def update_status():
    movies = getMovies()
    name = input("Güncellenecek dizi veya filmi girin:")
    for item in movies:
        if item["name"] == name:
            status = input("Yeni durumu girin (İzlendi, İzlenecek, İzleniyor):")
            if status in ["İzlendi", "İzlenecek", "İzleniyor"]:
                item["status"] = status
                with open('movies.json', "w") as moviesJson:
                    json.dump({"movies": movies}, moviesJson)
                print("Durum güncellendi.")
                return
            else:
                print("Geçersiz durum")
                return
    print("Dizi veya film bulunamadı")

def deleteMovie(name):
    movies=getMovies()
  
    for item in movies:
        if item["name"]==name:
            movies.remove(item)
            with open('movies.json', 'w') as moviesJson:
                json.dump({"movies": movies}, moviesJson)
            print(f"'{name}' başarıyla silindi.")
            return
            
    print("Dizi veya film bulunamadı.")

def add_movie(kind,name,type,rate,status,note):
    addedmovie=Movie(kind,name,type,status,rate,note=note).getMovie()
    saveMovie(addedmovie)


import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import os

# ------------------ KULLANICI SİSTEMİ ------------------

KULLANICI_ADI = "admin"
SIFRE = "1234"

def giris_kontrol():
    if kullanici_entry.get() == KULLANICI_ADI and sifre_entry.get() == SIFRE:
        giris_pencere.destroy()
        ana_ekran()
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")

# ------------------ ANA VERİ LİSTELERİ ------------------

elektrik_listesi = []
su_listesi = []

# ------------------ FONKSİYONLAR ------------------

def verileri_yukle():
    if os.path.exists("veriler.txt"):
        with open("veriler.txt", "r") as dosya:
            for satir in dosya:
                e, s = satir.strip().split(",")
                elektrik_listesi.append(float(e))
                su_listesi.append(float(s))

def grafik_goster():
    if len(elektrik_listesi) == 0:
        messagebox.showinfo("Bilgi", "Henüz veri yok.")
        return

    gunler = list(range(1, len(elektrik_listesi) + 1))

    plt.figure()
    plt.plot(gunler, elektrik_listesi)
    plt.xlabel("Gün")
    plt.ylabel("Elektrik (kWh)")
    plt.title("Enerji Tüketim Grafiği")
    plt.show()

def tahmin_yap():
    if len(elektrik_listesi) < 2:
        messagebox.showinfo("Bilgi", "Tahmin için en az 2 veri gerekli.")
        return

    artis = elektrik_listesi[-1] - elektrik_listesi[-2]
    tahmin = elektrik_listesi[-1] + artis

    sonuc_label.config(
        text=f"🔮 Yarın Tahmini: {tahmin:.2f} kWh",
        fg="#ffd166"
    )

def karbon_hesapla():
    if len(elektrik_listesi) == 0:
        messagebox.showinfo("Bilgi", "Henüz veri yok.")
        return

    toplam = sum(elektrik_listesi)
    karbon = toplam * 0.43

    sonuc_label.config(
        text=f"🌍 Karbon Ayak İzi: {karbon:.2f} kg CO2",
        fg="#ff9f1c"
    )

# ------------------ ANA EKRAN ------------------

def ana_ekran():
    global elektrik_entry, su_entry, sonuc_label

    pencere = tk.Tk()
    pencere.title("EcoTrack PRO")
    pencere.geometry("500x550")
    pencere.configure(bg="#1e1e2f")

    verileri_yukle()

    tk.Label(
        pencere,
        text="EcoTrack - Smart Energy System",
        font=("Segoe UI", 16, "bold"),
        bg="#1e1e2f",
        fg="white"
    ).pack(pady=15)

    frame = tk.Frame(pencere, bg="#2b2b3d", padx=20, pady=20)
    frame.pack(pady=10)

    tk.Label(frame, text="Elektrik (kWh)", bg="#2b2b3d", fg="white").pack()
    elektrik_entry = tk.Entry(frame, width=25)
    elektrik_entry.pack(pady=5)

    tk.Label(frame, text="Su (Litre)", bg="#2b2b3d", fg="white").pack()
    su_entry = tk.Entry(frame, width=25)
    su_entry.pack(pady=5)

    def veri_gir():
        try:
            elektrik = float(elektrik_entry.get())
            su = float(su_entry.get())
        except:
            messagebox.showerror("Hata", "Lütfen sayı gir!")
            return

        elektrik_listesi.append(elektrik)
        su_listesi.append(su)

        with open("veriler.txt", "a") as dosya:
            dosya.write(f"{elektrik},{su}\n")

        ortalama = sum(elektrik_listesi) / len(elektrik_listesi)

        if elektrik >= ortalama * 1.2:
            sonuc_label.config(text="⚠ Yüksek tüketim!", fg="#ff4c4c")
        else:
            sonuc_label.config(text="✔ Veri kaydedildi.", fg="#4cff88")

        elektrik_entry.delete(0, tk.END)
        su_entry.delete(0, tk.END)

    def rapor_goster():
        if len(elektrik_listesi) == 0:
            sonuc_label.config(text="Henüz veri yok.", fg="white")
        else:
            toplam = sum(elektrik_listesi)
            ortalama = toplam / len(elektrik_listesi)

            sonuc_label.config(
                text=f"Toplam: {toplam:.2f} kWh\nOrtalama: {ortalama:.2f}",
                fg="white"
            )

    # ----------- HOVER EFEKT -----------

    def hover_in(e):
        e.widget['background'] = "#265df2"

    def hover_out(e):
        e.widget['background'] = "#3a86ff"

    # ----------- BUTONLAR -----------

    butonlar = [
        ("Veri Gir", veri_gir),
        ("Rapor Göster", rapor_goster),
        ("Grafik Göster", grafik_goster),
        ("Yarın Tahmini", tahmin_yap),
        ("Karbon Hesapla", karbon_hesapla)
    ]

    for text, command in butonlar:
        btn = tk.Button(frame, text=text, width=20, bg="#3a86ff", fg="white", command=command)
        btn.pack(pady=8)
        btn.bind("<Enter>", hover_in)
        btn.bind("<Leave>", hover_out)

    sonuc_label = tk.Label(pencere, text="", bg="#1e1e2f", font=("Segoe UI", 11))
    sonuc_label.pack(pady=15)

    pencere.mainloop()

# ------------------ GİRİŞ PENCERESİ ------------------

giris_pencere = tk.Tk()
giris_pencere.title("EcoTrack Giriş")
giris_pencere.geometry("350x250")
giris_pencere.configure(bg="#1e1e2f")

tk.Label(
    giris_pencere,
    text="EcoTrack PRO",
    font=("Segoe UI", 15, "bold"),
    bg="#1e1e2f",
    fg="white"
).pack(pady=15)

tk.Label(giris_pencere, text="Kullanıcı Adı:", bg="#1e1e2f", fg="white").pack()
kullanici_entry = tk.Entry(giris_pencere, width=22)
kullanici_entry.pack(pady=5)

tk.Label(giris_pencere, text="Şifre:", bg="#1e1e2f", fg="white").pack()
sifre_entry = tk.Entry(giris_pencere, show="*", width=22)
sifre_entry.pack(pady=5)

tk.Button(
    giris_pencere,
    text="Giriş Yap",
    bg="#3a86ff",
    fg="white",
    command=giris_kontrol
).pack(pady=15)

giris_pencere.mainloop()

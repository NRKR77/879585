print("=== EcoTrack Enerji Takip Sistemi ===")

elektrik_listesi = []
su_listesi = []

while True:
    print("\n1- Günlük veri gir")
    print("2- Rapor göster")
    print("3- Çıkış")

    secim = input("Seçiminizi giriniz: ")

    if secim == "1":
        elektrik = float(input("Günlük elektrik tüketimi (kWh): "))
        su = float(input("Günlük su tüketimi (Litre): "))

        elektrik_listesi.append(elektrik)
        su_listesi.append(su)

        print("Veri kaydedildi.")

    elif secim == "2":
        if len(elektrik_listesi) == 0:
            print("Henüz veri yok.")
        else:
            toplam_elektrik = sum(elektrik_listesi)
            toplam_su = sum(su_listesi)

            ortalama_elektrik = toplam_elektrik / len(elektrik_listesi)

            print("\n--- RAPOR ---")
            print("Toplam Elektrik:", toplam_elektrik, "kWh")
            print("Toplam Su:", toplam_su, "Litre")
            print("Ortalama Elektrik:", ortalama_elektrik)

            son_gun = elektrik_listesi[-1]

            if son_gun > ortalama_elektrik * 1.2:
                print("⚠ Son gün tüketimi ortalamadan %20 fazla!")
                print("Öneri: Makine bakım kontrolü yapın.")
            else:
                print("Tüketim dengeli.")

    elif secim == "3":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim!")


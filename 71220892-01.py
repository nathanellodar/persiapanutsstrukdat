while True:
    print("1. Penambahan.")
    print("2. Pengurangan.")
    print("3. Perkalian.")
    print("4. Pembagian.")
    print("'Q' untuk berhenti.")
    pilihan = input("Masukan pilihan anda: ").lower()
    if pilihan == 'q':
        print("good bye!")
        break
    angka1 = input("angka pertama: ").lower()
    if angka1 == 'q':
        break
    angka2 = input("angka kedua: ").lower()
    if angka2 == 'q':
        break
    if pilihan == 'q':
        print("good bye!")
        break
    elif pilihan == '1':
        hasil = int(angka1) + int(angka2)
        print(f'hasil dari {angka1} + {angka2} = {int(hasil)}')
    elif pilihan == '2':
        hasil = int(angka1) - int(angka2)
        print(f'hasil dari {angka1} - {angka2} = {int(hasil)}')
    elif pilihan == '3':
        hasil = int(angka1) * int(angka2)
        print(f'hasil dari {angka1} * {angka2} = {int(hasil)}')
    elif pilihan == '4':
        hasil = int(angka1) / int(angka2)
        print(f'hasil dari {angka1} / {angka2} = {int(hasil)}')
    else:
        print('pilihan tidak valid!')
dict_inputan = dict()

masukan = input('Masukan nama buah: ').lower()
pisah = masukan.split()
daftar_terurut = sorted(pisah, key=lambda x: x[0], reverse=False)

list_huruf = []

for kata in daftar_terurut:
    if kata[0] not in list_huruf:
        list_huruf.append(kata[0])
for huruf in list_huruf:
    kumpulan_kata = []
    for kata in daftar_terurut:
        if kata[0] == huruf:
            kumpulan_kata.append(kata)
    dict_inputan[huruf] = kumpulan_kata
print(dict_inputan)
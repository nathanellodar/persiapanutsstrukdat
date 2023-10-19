import json 
databaru = None
with open('data_belanja.json', 'r') as file:
    file_all = json.load(file)
    databaru = file_all
if len(databaru) == 0:
    print(f'Total Nominal: Rp 0')
    with open('data_belanja.json', 'w') as file:
        catatan = str(input('Masukan catatan: '))
        nominal = int(input('masukan nominal: '))
        databaru.append({'no' : 1,'catatan' : catatan, 'nominal'  : nominal})
        json.dump(file_all, file)
        print('data berhasil disimpan')
else:
    total = 0
    no = None
    for daftar in file_all:
        print(f'{daftar["no"]}.{daftar["catatan"]} - Rp {daftar["nominal"]}')
        total += daftar['nominal']
        no = daftar['no']
    print(f'Total Nominal: Rp {total}')
    no_selanjutnya = no + 1
    with open('data_belanja.json', 'w') as file:
        catatan = str(input('Masukan catatan: '))
        nominal = int(input('masukan nominal: '))
        databaru.append({'no' : no_selanjutnya,'catatan' : catatan, 'nominal'  : nominal})
        json.dump(file_all, file)
        print('Data berhasil disimpan')
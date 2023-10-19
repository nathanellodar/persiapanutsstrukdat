from transaksi_class import Transaksi
n = int(input('Masukkan n: '))
for i in range(1, n+1):
    deskripsi = input(f"Masukkan deskripsi {i}: ")
    tanggal = input(f"Masukkan tanggal {i}: ")
    nominal = int(input(f"Masukkan nominal {i}: "))
    data = Transaksi(deskripsi, tanggal, nominal)
print(f'Total nominal: {data.gettotal()}')
print(f'Transaksi terbesar yaitu {data.getterbesar()} terdapat pada tanggal {data.gettanggalterbesar()}')

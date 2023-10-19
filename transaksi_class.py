class Transaksi:
    _deskripsi = []
    _tanggal = []
    _nominal = []
    def __init__(self, deskripsi, tanggal, nominal):
        self._deskripsi.append(deskripsi)
        self._tanggal.append(tanggal)
        self._nominal.append(nominal)
    def gettotal(self):
        return sum(self._nominal)
    def getterbesar(self):
        return max( self._nominal)
    def gettanggalterbesar(self):
        return self._tanggal[self._nominal.index(max( self._nominal))]

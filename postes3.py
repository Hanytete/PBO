class Main:
    """Kelas utama yang berfungsi sebagai controller untuk alur aplikasi."""
    def __init__(self):
        """Constructor untuk kelas Main."""
        pass

    def main(self):
        """Metode utama untuk menjalankan aplikasi."""
        # Di aplikasi nyata, ini akan memulai loop utama atau UI
        pass

    def uiLogin(self):
        """Menampilkan antarmuka untuk login pengguna."""
        pass

    def uiMenu(self):
        """Menampilkan menu utama aplikasi."""
        pass

    def uiHitungPembayaran(self):
        """Menampilkan antarmuka untuk proses perhitungan pembayaran."""
        pass

    def uiCetakStruk(self):
        """Menampilkan antarmuka untuk mencetak struk."""
        pass


class HitungPembayaran:
    """
    Kelas yang bertanggung jawab atas logika bisnis utama dari transaksi pembayaran.
    Ini mengelola daftar item, menghitung total, dan berinteraksi dengan database.
    """
    def __init__(self):
        """Constructor untuk kelas HitungPembayaran."""
        self.daftar_item = []
        self.total_harga = 0.0

    def insertPembayaran(self, item: 'TabelHitungPembayaran'):
        """Menambahkan item baru ke dalam daftar transaksi."""
        pass

    def updatePembayaran(self, id_menu: str, jumlah_baru: int):
        """Memperbarui jumlah item yang ada dalam transaksi."""
        pass

    def deleteDataPembayaran(self, id_menu: str):
        """Menghapus item dari transaksi."""
        pass

    def cariDataPembayaranByIdMenu(self, id_menu: str) -> 'TabelHitungPembayaran' or None:
        """Mencari data pembayaran berdasarkan ID menu dalam daftar item saat ini."""
        pass


class PembayaranTunai:
    """Mengelola logika untuk proses pembayaran tunai."""
    def __init__(self):
        """Constructor untuk kelas PembayaranTunai."""
        pass

    def hitungTotalHarga(self, total_belanja: float) -> float:
        """Menghitung total harga untuk pembayaran tunai (tanpa biaya tambahan)."""
        pass


class PembayaranByCard:
    """Mengelola logika untuk proses pembayaran dengan kartu."""
    def __init__(self):
        """Constructor untuk kelas PembayaranByCard."""
        pass

    def hitungTotalHarga(self, total_belanja: float) -> float:
        """Menghitung total harga untuk pembayaran kartu, dengan biaya admin 1.5%."""
        pass


class CetakStruk:
    """Bertanggung jawab untuk memformat dan mencetak struk."""
    def __init__(self):
        """Constructor untuk kelas CetakStruk."""
        pass

    def cetakStruk(self, data_struk: 'TCetakStruk'):
        """Mencetak detail struk berdasarkan data yang diberikan."""
        pass


class TCetakStruk:
    """Model data yang menyimpan informasi final untuk dicetak pada struk."""
    def __init__(self, noStruk: str = "", totalHarga: float = 0.0):
        self.noStruk = noStruk
        self.totalHarga = totalHarga


class LoginKasir:
    """Mengelola data dan validasi untuk login kasir."""
    def __init__(self, username: str = "", password: str = ""):
        self.username = username
        self.password = password

    def validasiLogin(self) -> bool:
        """Memvalidasi kredensial pengguna terhadap database atau nilai hardcoded."""
        pass

    def logout(self):
        """Melakukan proses logout."""
        pass


class KoneksiDatabase:
    """Mengelola koneksi dan eksekusi query ke database."""
    def __init__(self, host: str = "", database: str = "", userName: str = "", password: str = ""):
        self.host = host
        self.database = database
        self.userName = userName
        self.password = password
        self.koneksi = None

    def membukaKoneksi(self):
        """Membuka koneksi ke database."""
        # Contoh dengan library seperti mysql-connector-python
        pass

    def eksekusiQuerySelect(self, query: str):
        """Mengeksekusi query SELECT."""
        pass

    def eksekusiQueryInsert(self, query: str):
        """Mengeksekusi query INSERT."""
        pass

    def eksekusiQueryUpdate(self, query: str):
        """Mengeksekusi query UPDATE."""
        pass

    def eksekusiQueryDelete(self, query: str):
        """Mengeksekusi query DELETE."""
        pass

    def tutupKoneksi(self):
        """Menutup koneksi database."""
        pass


class TabelHitungPembayaran:
    """Model data (DTO) dengan getter/setter untuk data item pembayaran."""
    def __init__(self, idMenu: str = "", namaMenu: str = "", harga: float = 0.0, jumlah: int = 0):
        self._idMenu = idMenu
        self._namaMenu = namaMenu
        self._harga = harga
        self._jumlah = jumlah
        self._totalHarga = self._harga * self._jumlah

    def setIdMenu(self, idMenu: str):
        self._idMenu = idMenu

    def getIdMenu(self) -> str:
        return self._idMenu

    def setNamaMenu(self, namaMenu: str):
        self._namaMenu = namaMenu

    def getNamaMenu(self) -> str:
        return self._namaMenu

    def setHarga(self, harga: float):
        self._harga = harga
        self._recalculate_total()

    def getHarga(self) -> float:
        return self._harga

    def setJumlah(self, jumlah: int):
        self._jumlah = jumlah
        self._recalculate_total()

    def getJumlah(self) -> int:
        return self._jumlah

    def setTotalHarga(self, totalHarga: float):
        # Biasanya total harga tidak di-set langsung, tapi dihitung
        self._totalHarga = totalHarga

    def getTotalHarga(self) -> float:
        return self._totalHarga

    def _recalculate_total(self):
        """Menghitung ulang total harga jika harga atau jumlah berubah."""
        self._totalHarga = self._harga * self._jumlah


class TabelPembayaranByCard:
    """Model data (DTO) dengan getter/setter untuk detail pembayaran via kartu."""
    def __init__(self, idCard: str = "", jenisCard: str = "", namaBank: str = "", totalHarga: float = 0.0):
        self._idCard = idCard
        self._jenisCard = jenisCard
        self._namaBank = namaBank
        self._totalHarga = totalHarga

    def setIdCard(self, idCard: str):
        self._idCard = idCard

    def getIdCard(self) -> str:
        return self._idCard

    def setJenisCard(self, jenisCard: str):
        self._jenisCard = jenisCard

    def getJenisCard(self) -> str:
        return self._jenisCard

    def setNamaBank(self, namaBank: str):
        self._namaBank = namaBank

    def getNamaBank(self) -> str:
        return self._namaBank

    def setTotalHarga(self, totalHarga: float):
        self._totalHarga = totalHarga

    def getTotalHarga(self) -> float:
        return self._totalHarga


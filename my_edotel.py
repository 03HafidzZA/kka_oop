from abc import ABC, abstractmethod

# --- ABSTRACTION (Kerangka Dasar) ---
class KamarHotel(ABC):
    def __init__(self, nama_kamar, stok, harga_dasar):
        self.__nama_kamar = nama_kamar
        self.__stok = stok
        self.__harga_dasar = harga_dasar

    # Getter untuk Nama Kamar
    def get_nama_kamar(self):
        return self.__nama_kamar

    # Getter untuk Harga Dasar
    def get_harga_dasar(self):
        return self.__harga_dasar

    # ENCAPSULATION: Getter untuk Stok (Aman diakses dari luar)
    def get_stok(self):
        return self.__stok

    # ENCAPSULATION: Setter/Method Tambah Stok dengan Validasi
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"[Peringatan] Gagal menambah stok untuk {self.__nama_kamar}: Jumlah penambahan tidak boleh negatif!")
        else:
            self.__stok += jumlah
            print(f"[Sukses] Stok {self.__nama_kamar} berhasil ditambah sebanyak {jumlah}. Stok sekarang: {self.__stok}")

    # ENCAPSULATION: Setter untuk Set Stok Langsung dengan Validasi (Opsional/Sesuai Kebutuhan)
    def set_stok(self, nilai_baru):
        if nilai_baru < 0:
            print(f"[Peringatan] Gagal mengatur stok {self.__nama_kamar}: Nilai stok tidak boleh negatif!")
        else:
            self.__stok = nilai_baru
            print(f"[Sukses] Stok {self.__nama_kamar} diset menjadi: {self.__stok}")

    # Abstract Method wajib diimplementasikan oleh class anak
    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah_malam):
        pass


# --- INHERITANCE (Pewarisan) ---

class KamarDeluxe(KamarHotel):
    def __init__(self, nama_kamar, stok, harga_dasar, fasilitas="Private Pool"):
        # Memanggil constructor milik Parent class (KamarHotel)
        super().__init__(nama_kamar, stok, harga_dasar)
        self.fasilitas = fasilitas  # Atribut unik KamarDeluxe
        self.pajak_persen = 0.10    # Pajak sewa 10%

    # Implementasi Abstraksi: Menampilkan Detail
    def tampilkan_detail(self):
        print(f"Kamar: {self.get_nama_kamar()}")
        print(f"Tipe : Deluxe")
        print(f"Harga dasar /malam : Rp {self.get_harga_dasar():,}")
        print(f"Fasilitas Tambahan : {self.fasilitas}")
        print(f"Stok Tersedia      : {self.get_stok()} kamar")
        print(f"Pajak Sewa         : {int(self.pajak_persen * 100)}%")

    # Implementasi Abstraksi: Hitung Harga Total (Harga + Pajak)
    def hitung_harga_total(self, jumlah_malam):
        harga_dasar = self.get_harga_dasar()
        pajak = harga_dasar * self.pajak_persen
        harga_per_malam = harga_dasar + pajak
        return harga_per_malam * jumlah_malam


class KamarStandard(KamarHotel):
    def __init__(self, nama_kamar, stok, harga_dasar, kapasitas="2 Orang"):
        # Memanggil constructor milik Parent class (KamarHotel)
        super().__init__(nama_kamar, stok, harga_dasar)
        self.kapasitas = kapasitas  # Atribut unik KamarStandard
        self.pajak_persen = 0.05    # Pajak sewa 5%

    # Implementasi Abstraksi: Menampilkan Detail
    def tampilkan_detail(self):
        print(f"Kamar: {self.get_nama_kamar()}")
        print(f"Tipe : Standard")
        print(f"Harga dasar /malam : Rp {self.get_harga_dasar():,}")
        print(f"Kapasitas Maksimal : {self.kapasitas}")
        print(f"Stok Tersedia      : {self.get_stok()} kamar")
        print(f"Pajak Sewa         : {int(self.pajak_persen * 100)}%")

    # Implementasi Abstraksi: Hitung Harga Total (Harga + Pajak)
    def hitung_harga_total(self, jumlah_malam):
        harga_dasar = self.get_harga_dasar()
        pajak = harga_dasar * self.pajak_persen
        harga_per_malam = harga_dasar + pajak
        return harga_per_malam * jumlah_malam


# --- POLYMORPHISM & TRANSAKSI (Fungsi di luar Class) ---

def proses_transaksi(daftar_pesanan):
    """
    Fungsi untuk memproses pesanan kamar secara fleksibel (Polimorfisme).
    Menerima list pesanan berupa tuple (objek_kamar, jumlah_malam).
    """
    print("\n" + "="*45)
    print("         RINCIAN TRANSAKSI MYEDOTEL         ")
    print("="*45)
    
    total_tagihan_akhir = 0
    
    for i, (kamar, malam) in enumerate(daftar_pesanan, 1):
        # Polimorfisme: Memanggil method dengan nama yang sama, tetapi
        # perilakunya otomatis menyesuaikan objek (Deluxe / Standard)
        nama = kamar.get_nama_kamar()
        harga_per_malam_dengan_pajak = kamar.hitung_harga_total(1)
        subtotal = kamar.hitung_harga_total(malam)
        total_tagihan_akhir += subtotal
        
        # Mengurangi stok kamar setelah berhasil dipesan (Opsional untuk simulasi riil)
        kamar.set_stok(kamar.get_stok() - 1)
        
        print(f"{i}. {nama} ({malam} malam)")
        print(f"   Harga + Pajak /malam : Rp {harga_per_malam_dengan_pajak:,.2f}")
        print(f"   Subtotal             : Rp {subtotal:,.2f}")
        print("-"*45)
        
    print(f"TOTAL TAGIHAN AKHIR     : Rp {total_tagihan_akhir:,.2f}")
    print("="*45)


# --- ALUR PROGRAM (User Story) ---

if __name__ == "__main__":
    print("=== [A] ADMIN MEMBUAT DATA KAMAR ===")
    # Membuat Objek Kamar Deluxe dan Kamar Standard
    deluxe_room = KamarDeluxe("Kamar Deluxe Executive (Room 101)", stok=5, harga_dasar=500000)
    standard_room = KamarStandard("Kamar Standard Cozy (Room 202)", stok=10, harga_dasar=250000)
    
    # Menampilkan detail kamar awal
    deluxe_room.tampilkan_detail()
    print("-" * 30)
    standard_room.tampilkan_detail()
    print("\n")

    print("=== [B] ADMIN MENCOBA MENGISI STOK DENGAN ANGKA NEGATIF ===")
    # Pengujian validasi penambahan stok negatif
    deluxe_room.tambah_stok(-3)
    # Pengujian validasi pengaturan stok negatif langsung
    standard_room.set_stok(-5)
    print("\n")

    print("=== [C] TAMU MEMESAN KAMAR ===")
    # Tamu memesan 2 malam Kamar Deluxe dan 1 malam Kamar Standard
    pesanan_tamu = [
        (deluxe_room, 2),    # 2 malam Kamar Deluxe
        (standard_room, 1)   # 1 malam Kamar Standard
    ]
    
    # Memproses pesanan secara polimorfis
    proses_transaksi(pesanan_tamu)
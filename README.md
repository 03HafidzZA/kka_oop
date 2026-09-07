TUGAS ANALISIS 1:
Ketika 'hero1.hp = 500' dipanggil langsung, nilai HP berubah begitu saja karena 
atribut hp masih bersifat publik. Hal ini membuat data game menjadi tidak aman 
dari manipulasi langsung.

TUGAS ANALISIS 2:
Parameter 'lawan' harus menerima objek utuh agar kelas penyerang dapat memanggil 
method '.diserang()' milik objek lawan tersebut dan mengurangi HP aslinya, bukan 
hanya mengetahui namanya saja.

TUGAS ANALISIS 3:
- Error yang muncul saat super() dihapus adalah "AttributeError: 'Mage' object has no attribute 'name'".
- Hal ini terjadi karena constructor kelas anak tidak menjalankan constructor kelas induk, 
  sehingga variabel 'name' dan 'hp' tidak pernah dibuat untuk objek 'Mage'.
- Fungsi super() berperan penting untuk meneruskan inisialisasi data dari kelas anak 
  ke kelas induk.

TUGAS ANALISIS 4:
1. Uji Hacking: Pemanggilan '_Hero__hp' berhasil menampilkan nilai HP karena Python 
   menggunakan mekanisme Name Mangling untuk menyembunyikan variabel private.
2. Uji Validasi: Tanpa logika filter di setter, HP bisa bernilai negatif (-100). 
   Setter sangat penting untuk memvalidasi data agar nilai game tetap logis dan mencegah kecurangan.

TUGAS ANALISIS 5:
1. Melanggar Kontrak: Muncul error "TypeError: Can't instantiate abstract class Hero with abstract method serang".
   Ini berarti jika kita berjanji menggunakan kelas abstrak (kontrak), semua kelas anak wajib 
   menuliskan method tersebut secara nyata.
2. Mencetak Cetakan: Kelas GameUnit dilarang keras dibuat objeknya karena ia hanya rancangan abstrak. 
   Kegunaannya adalah sebagai standar atau "kontrak" agar semua karakter game memiliki method yang seragam.

TUGAS ANALISIS 6:
1. Uji Skalabilitas: Program berjalan sangat lancar meskipun ditambahkan Healer. Keuntungan 
   Polimorfisme adalah memudahkan penambahan karakter baru di masa depan tanpa merombak sistem perulangan utama.
2. Konsistensi Penamaan: Mengubah nama method akan merusak polimorfisme karena perulangan 
   tidak lagi bisa memanggil fungsi dengan nama yang seragam. Nama method harus persis sama 
   agar sistem bisa memperlakukannya secara fleksibel.

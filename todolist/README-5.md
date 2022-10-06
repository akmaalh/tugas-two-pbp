# Assignment 5

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
- Inline : Berfungsi untuk memberikan style ke tag tertentu. Oleh karena itu, setiap tag harus diberi styling masing-masing. Hal ini dapat dilakukan jika kita ingin mengubah style hanya pada elemen tertentu. Jika website sudah mulai kompleks, hal ini kurang direkomendasikan karena akan membuat file html tidak terstruktur dengan baik dan  _less-readable_
- Internal : Berfungsi untuk memberikan style pada file HTML yang sama. CSS ini diletakkan pada bagian <head>. Styling diaplikasikan berdasarkan class dan id dari masing-masing tag. Hal ini kurang direkomendasikan apabila kita memiliki banyak halaman, karena style hanya akan teraplikasikan pada 1 file HTML. Selain itu, CSS akan di-_retrieve_ setiap halaman di-_load_ sehingga akan berpengaruh kepada kecepatan akses halaman.
- External : Berfungsi untuk memberikan style menggunakan file CSS terpisah. Dengan begitu, kita dapat dengan mudah untuk mengorganisasi styles karena styles dapat diaplikasikan ke seluruh file HTML.
  
## Jelaskan tag HTML
1. `<!DOCTYPE>` , untuk menentukan tipe dokumen
2. `<html>` , untuk membuat dokumen HTML
3. `<title>`, untuk judul suatu page
4. `<p>` , untuk menuliskan paragraf pada page
5. `<h1>...<h6>` , untuk heading suatu page
6. `<br>` , untuk membuat baris kosong
7. `<!--...-->` , untuk menuliskan komen
8.` <form>` , untuk membuat form input bagi user
9. `<input>` , untuk input user
10.`<button>` , untuk tombol yang dapat di klik user
  
## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Element Selector (diawali `#` atau `.`): Menerapkan CSS pada semua elemen dengan tag yang dipilih
2. Class Selector (diawali `.`): Menerapkan CSS pada setiap tag dengan class yang dipilih
3. ID Selector (diawali `#`): Menerapkan CSS pada setiap tag dengan id yang dipilih

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Install framework Tailwind pada `base.html`
2. Membuat folder static pada app todolist
3. Terapkan styling tailwind pada tiap-tiap dokumen menggunakan `class=""`
4. Menambahkan CSS eksternal `style.css` untuk memberi style pada tiap halaman

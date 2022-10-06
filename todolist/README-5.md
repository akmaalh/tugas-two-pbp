# Assignment 5
## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
- Inline : Berfungsi untuk memberikan style ke tag tertentu. Oleh karena itu, setiap tag harus diberi styling masing-masing. Hal ini dapat dilakukan jika kita ingin mengubah style hanya pada elemen tertentu. Jika website sudah mulai kompleks, hal ini kurang direkomendasikan karena akan membuat file html tidak terstruktur dengan baik dan  _less-readable_
- Internal : Berfungsi untuk memberikan style pada file HTML yang sama. CSS ini diletakkan pada bagian <head>. Styling diaplikasikan berdasarkan class dan id dari masing-masing tag. Hal ini kurang direkomendasikan apabila kita memiliki banyak halaman, karena style hanya akan teraplikasikan pada 1 file HTML. Selain itu, CSS akan di-_retrieve_ setiap halaman di-_load_ sehingga akan berpengaruh kepada kecepatan akses halaman.
- External : Berfungsi untuk memberikan style menggunakan file CSS terpisah. Dengan begitu, kita dapat dengan mudah untuk mengorganisasi styles karena styles dapat diaplikasikan ke seluruh file HTML
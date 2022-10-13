# Assignment 6

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming merupakan program yang akan berjalan secara berurutan. Misal, ketika sebuah fungsi dipanggil, maka kita harus menunggu fungsi selesai bekerja jika ingin menjalankan fungsi lain.
Sementara pada asynchronous programming, fungsi dapat berjalan secara beriringan, tanpa harus menunggu "antrian" atau dalam kata lain, sebuah fungsi dapat dijalankan bersamaan dengan fungsi sebelumnya walaupun fungsi sebelumnya belum selesai selesai.

## Jelaskan maksud dari paradigma Event-Driven Programming dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming merupakan paradigma ketika suatu program berfokus terhadap event atau action pengguna yang ada. Misalnya ketika kita menekan button untuk menambah task. Maka ketika kita menekan button tersebut, akan muncul modal untuk menambahkan task baru.

## Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada AJAX terdapat pada button "Tambah Task". Ketika user sudah mengisi judul dan deskripsi lalu menekan tombol "Tambah Task", maka program lansung akan memunculkan card berisi _Title_ dan _Description_ sesuai dengan yang user isi. Ketika button diklik, program akan memanggil fungsi add_task, lalu setelah data berhasil disimpan, maka program akan me-_refresh_ halaman todolist secara otomatis.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat fungsi baru `show_json` dan `add_task_ajax` pada views
2. Melakukan routing ke ke `show_json` dan `add_task_ajax` pada urls.py
3. Membuat 

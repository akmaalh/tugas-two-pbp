**Tugas 2**
### App Link
https://tugas-two-pbp.herokuapp.com/katalog/
## Bagan Flow
![Frame 54](https://user-images.githubusercontent.com/102467956/190295846-09f9c8a4-82e9-474b-b6dc-0ccf3defb6da.png)

User akan mengirim HTTP request yang akan diterima oleh URLs. Lalu, setelah diterima oleh urls, request akan diteruskan ke views yang didefinisikan sebelumnya. Views kemudian mengambil data melalui models. Models akan mengembalikan response melalui template. Template akan merender response tersebut dan menampilkannya kepada user.

## Mengapa kita menggunakan Virtual Environment?
Hal ini kita lakukan untuk menghindari conflict ketika mengerjakan banyak project dengan dependencies yang berbeda-beda. Virtual Environment akan mengisolasi dependencies suatu project. Misalnya, suatu project menggunakan packages versi 1.5 dan project lain menggunakan versi 2.0. Virtual environment mencegah kedua versi tersebut bertabrakan dengan mengisolasi tiap project.
Kita tetap dapat membuat aplikasi berbasis Django tanpa mengaktifkan virtual environment. Namun, setiap dependencies akan terinstall di global. Hal ini mungkin akan membuat aplikasi tidak dapat dijalankan ketika ada dependencies yang berubah.

## Implementasi
1. Pertama-tama, kita membuat fungsi show_katalog pada file katalog/views.py yang menerima 1 parameter berupa request. Fungsi tersebut berfungsi untuk mengambil data dari database lalu disimpan ke context.

2. Lalu, kita akan membuat routing pada /katalog/urls.py dan di /project_django/urls.py ke katalog yaitu path yang ada pada urlpatterns. Hal ini dilakukan agar aplikais bisa ditampilkan di url aplikasi yang sudah dideploy

3. Lalu, nama dan npm dari show_katalog akan ditampilkan di template katalog.html. Data dari list_katalog juga akan ditampilkan menggunakan for loop.

4. Terakhir, aplikasi dideploy pada https://tugas-two-pbp.herokuapp.com/katalog/. Lalu dimasukkan API key dan app_name pada secrets.

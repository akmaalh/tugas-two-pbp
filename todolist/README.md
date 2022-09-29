# Assignment 3

### Website Link: [tugas-two-pbp.herokuapp.com](https://tugas-two-pbp.herokuapp.com/todolist/)

## Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
CSRF Token atau _Cross Site Request Forgery_ Token merupakan token acak yang berfungsi untuk melindungi website dari serangan CSRF. Token tersebut merupakan token yang unik, acak, serta memiliki nilai yang besar sehingga sulit ditebak secara instan oleh peretas. Token ini akan di-_generate_ untuk tiap sesi user. 
Jika tidak ada potongan kode tersebut pada elemen `<form>` maka user atau website yang ingin meretas dapat melakukan hal-hal yang tidak diinginkan melalui link atau HTTP request.

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }})`? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Bisa. Dengan membuat elemen form dan men-_declare_ secara eksplisit parameter atau input yang dinginkan. misal kita ingin menerima input password, maka kita dapat menuliskan  `{{ form.password }}` secara eksplisit.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Ketika form telah diisi dan tombol submit diklik oleh user, data akan dikirim dan dicek oleh sistem. Data akan dicocokkan menggunakan fungsi-fungsi yang ada pada `views.py`. Jika sudah tervalidasi, maka objek-objek dari `models.py` akan dibuat dan disimpan pada database.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat app baru dengan perintah `python manage.py startapp todolist` pada terminal.
2. Routing path ke app `todolist` dengan `path('todolist/', include('todolist.urls'))` pada `project_django/urls.py`.
3. Membuat model `Task` pada `models.py`.
4. Membuat fungsi untuk login, logout, register pada `views.py` lalu membuat halaman html untuk login dan register.
5. Membuat fungsi untuk show_todolist, add_task, delete_task, dan update_task pada `views.py` lalu membuat halaman html untuk halaman utama todolist dan halaman untuk membuat task baru.
6. Routing path ke _page-page_ yang bersesuaian pada `todolist/urls.py`.
7. Push kode ke repositori dan deploy ke heroku. Lalu membuat 2 user dan membuat 3 dummy data task pada masing-masing user.

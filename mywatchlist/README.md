# Assignment 3

### Website Link: [tugas-two-pbp.herokuapp.com](https://tugas-two-pbp.herokuapp.com/mywatchlist/)
##  Perbedaan antara JSON, XML, dan HTML
JSON merupakan singkatan dari JavaScript Object Notation. Perbedaan JSON dari XML dan HTML terdapat pada oenulisannya, yaitu JSON tidak menggunakan tag. Dengan begitu, JSON mengonsumsi memori lebih sedikit daripada XML dan HTML.
JSON dan XML berorientasi kepada pengiriman data, sementara HTML lebih bertujuan untuk menampilkan data pada user.
##  mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Dalam mengembangkan sebuah patform, tentu kita perlu melakukan pengiriman data. Dengan data delivery, proses pengiriman data tersebut akan berjalan lebih mudah karena data dapat dengan mudah disampaikan dari satu pihak ke pihak lainnya. Misal dari sisi developer ke user.
## Implementasi
1. Membuat aplikasi mywatchlist dengan command `python3 manage.py startapp mywatchlist`
2. Melakukan routing pada `project_django/urls.py` dengan menambahkan `path('mywatchlist/', include('mywatchlist.urls'))` pada `urlpatterns`. Lalu, dilakukan pula routing pada `mywatchlist/urls.py` sesuai path yang diminta.
3. Membuat model Mywatchlist pada `mywatchlist/models.py` dengan fields sesuai dengan permintaan, yaitu watched, title, rating, release_date, dan review.
4. Membuat 3 fungsi show_watchlist, show_xml, dan show_json pada `mywatchlist/views.py` untuk menampilkan data dengan format yang bersesuaian.
5. Lalu, melakukan migrasi model yang sudah dibuat dengan menjalankan `python manage.py makemigrations` dan `python manage.py migrate`
## Postman
### HTML
![messageImage_1663785126712](https://user-images.githubusercontent.com/102467956/191583243-b0ef7bd7-36d1-4fb6-80a2-17cef37f7db7.jpg)
### JSON
![messageImage_1663785181991](https://user-images.githubusercontent.com/102467956/191583369-2a087089-a467-4004-a98f-9ecddeb11b08.jpg)
### XML
![messageImage_1663785211539](https://user-images.githubusercontent.com/102467956/191583467-735764e7-519a-4605-b398-2b51b665a672.jpg)

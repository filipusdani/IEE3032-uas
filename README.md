# IEE3032-uas

Desain Pabrik Smart Farm

1.	Sensor Pertama
  * Nama		: Sensor kelembaban 
  * Fungsi		: Mengukur tingkat kelembaban tanah
  * Jangkah	: 0% - 100%
  * Topik mqtt	: uas/sensor1
2.	Sensor Kedua
  * Nama		: Sensor temperatur
  * Fungsi		: Memantau suhu lingkungan di area pertanian
  * Jangkah	: -10°C - 50°C
  * Topik mqtt	: uas/sensor2
3.	Sensor Ketiga:
  * Nama/Fungsi	: Sensor sunlight
  * Fungsi		: Mengukur tingkat kecerahan matahari pada area pertanian
  * Jangkah	: 0 lux – 1000 lux
  * Topik mqtt	: uas/sensor3
4.	Aktuator dari Machine Learning hasil pengolahan ketiga sensor:
* Nama/Fungsi	: Aktuator pompa air
* Jangkah	: 1000 – 3000 rpm
* Penjelasan bagaimana hubungan ketiga sensor terhadap aktuator
  * Menanggapi penurunan tingkat kelembaban, yang menunjukkan lebih sedikit air tanah, aktuator pompa air akan meningkatkan kecepatan pompa untuk memastikan penyiraman yang cukup. Selain itu, jika sensor suhu mendeteksi peningkatan suhu, menunjukkan kondisi yang lebih panas, dan sensor sinar matahari mencatat peningkatan intensitas cahaya, menunjukkan lebih banyak sinar matahari, aktuator selanjutnya akan meningkatkan RPM pompa air dalam kisaran 1000 hingga 3000 rpm. Sistem ini bertujuan untuk mengkompensasi penurunan kelembaban dengan menyesuaikan kecepatan pompa air berdasarkan kombinasi faktor lingkungan suhu, sinar matahari, dan kelembaban, sehingga mengoptimalkan proses penyiraman.

Referensi

* Dokumentasi Django: https://docs.djangoproject.com/en/4.2/
* Dokumentasi Node-RED: https://nodered.org/docs/
* Project Paho-MQTT: https://pypi.org/project/paho-mqtt/ 
* Dokumentasi Paho-MQTT: https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php 
* Dokumentasi Mosquitto MQTT: https://mosquitto.org/documentation/ 

# 🏠 Hallederiz — Ürün ve Geliştirme Planı

> **Uygulama adı:** **Hallederiz**
> **App Store alt başlığı:** "Arızayı anlat, usta gelsin"
> **Slogan (logo, açılış ekranı, reklam):** "Sen anlat, gerisini **Hallederiz.**"
> **Pilot şehir:** Kahramanmaraş
> **Repo:** `hallederiz` · **Paket kimliği:** `com.hallederiz.app`
> **Hazırlayan:** Sibel & Claude
> **Tarih:** Ekim 2026
> **Durum:** Planlama tamam → Sprint 1 başlıyor
> **Hedef platformlar:** iOS + Android (Flutter) + Web (Next.js)

> ⚠️ Kesinleştirmeden önce: alan adı (hallederiz.com / .com.tr / .app) müsaitliği ve TÜRKPATENT marka sorgusu yapılacak.

---

## İçindekiler

0. [Tek cümlede ürün](#0-tek-cümlede-ürün)
1. [Alınan kararlar (özet tablo)](#1-alınan-kararlar-özet-tablo)
2. [Problem ve değer önerisi](#2-problem-ve-değer-önerisi)
3. [Rakip analizi ve farklılaşma](#3-rakip-analizi-ve-farklılaşma)
4. [Uçtan uca kullanıcı akışı](#4-uçtan-uca-kullanıcı-akışı)
5. [Ürün modülleri (detaylı)](#5-ürün-modülleri-detaylı)
6. [Hizmet kategorileri (Armut kapsamı + fazlası)](#6-hizmet-kategorileri)
7. [Yapay zekâ mimarisi (RAG + Human-in-the-loop)](#7-yapay-zekâ-mimarisi)
8. [Makine öğrenmesi modelleri](#8-makine-öğrenmesi-modelleri)
9. [Teknoloji yığını (tech stack)](#9-teknoloji-yığını)
10. [Mac olmadan iOS geliştirme stratejisi](#10-mac-olmadan-ios-geliştirme-stratejisi)
11. [Sistem mimarisi](#11-sistem-mimarisi)
12. [Veritabanı şeması](#12-veritabanı-şeması)
13. [API tasarımı](#13-api-tasarımı)
14. [Repo yapısı](#14-repo-yapısı)
15. [Geliştirme ortamı kurulumu (Windows)](#15-geliştirme-ortamı-kurulumu-windows)
16. [Adım adım geliştirme planı (fazlar ve sprintler)](#16-adım-adım-geliştirme-planı)
17. [Güvenlik, KVKK ve hukuki konular](#17-güvenlik-kvkk-ve-hukuki-konular)
18. [Ölçülecek metrikler](#18-ölçülecek-metrikler)
19. [İş modeli (sonraki aşama)](#19-iş-modeli-sonraki-aşama)
20. [Riskler ve önlemler](#20-riskler-ve-önlemler)
21. [Maliyet tahmini](#21-maliyet-tahmini)
22. [Açık sorular / sonra karar verilecekler](#22-açık-sorular)
23. [İlk 7 gün yapılacaklar](#23-ilk-7-gün-yapılacaklar)

---

## 0. Tek cümlede ürün

> **Evde neyin bozulduğunu bilmesen bile doğru kişiyi bul.**

Evdeki problemi **anlayan** → doğru hizmet alanını **belirleyen** → uygun ve **müsait** uzmanı **bulan** → **randevuyu** yöneten → işin gerçekten **yapıldığını doğrulayan** → **iki tarafın memnuniyetini** ölçen → topladığı verilerle **kontrollü biçimde kendini geliştiren** bir ev hizmetleri platformu.

Ürün bir **usta rehberi değil**, bir **"arızadan çözüme" yönetim sistemi**. Harita, yapay zekâ, puanlama ve randevu bu amaca hizmet eden araçlar; ürünün kendisi değiller.

---

## 1. Alınan kararlar (özet tablo)

| # | Konu | Karar |
|---|------|-------|
| 1 | Ürün tipi | Usta rehberi değil, uçtan uca hizmet platformu (talep → randevu → iş → değerlendirme) |
| 2 | Arıza tespiti | **AI**, kullanıcının anlattığı sorunu analiz eder: "Sorununuz şununla ilgili, uygun ustaları bulalım" |
| 3 | Müsaitlik | Gerçek zamanlı **teyit** (ustaya talep gidip kabul alınır) + **randevu sistemi** |
| 4 | Güven | Yıldız yerine **Güven Profili** (doğrulanmış iş, zamanında varış, iptal, şikâyet, kategori deneyimi) |
| 5 | İş tamamlama | **İşin tamamlandığı ve karşılıklı memnuniyet** iki taraftan da doğrulanır |
| 6 | Seçenekler | Tek usta değil, **3 akıllı seçenek**: Hızlı çözüm / Güvenilir tercih / Ekonomik seçenek (+ Acil mod) |
| 7 | Ev profili | **Bakım geçmişi** ve bakım hatırlatmaları (başta kural, sonra ML) |
| 8 | Fiyat | **Otomatik fiyat tahmini** (aralık + güven seviyesi); veri yoksa açıkça söyler (başta kural, sonra ML) |
| 9 | Öğrenme | **RAG + Human-in-the-loop + versiyonlu değerlendirme**. Kontrolsüz "kendi kendine değişen model" yok |
| 10 | Kapsam | Armut ve benzerlerindeki tüm hizmetler (temizlik, nakliye, tadilat, ders vb.) kategori ağacında; operasyon aşamalı açılır |
| 11 | Platform | iOS + Android + Web |
| 12 | Mobil | **Flutter + Dart** (tek kod tabanı) |
| 13 | Web | **Next.js + TypeScript** (SEO, usta profilleri, admin paneli) |
| 14 | Backend | **Python + FastAPI**, modüler monolit (mikroservis yok) |
| 15 | Veritabanı | **PostgreSQL + PostGIS + pgvector** (tek DB, ayrı vektör DB yok) |
| 16 | Cache/Kuyruk | **Redis** (+ Celery/RQ arka plan işleri) |
| 17 | Mac | **Satın alınmayacak.** Geliştirme Windows'ta; iOS build bulutta macOS runner ile |
| 18 | Swift | Gerektiğinde native iOS kısımları için **Swift/SwiftUI** öğrenilecek (Platform Channel) |
| 19 | Öncelik | Önce **uygulamayı yapmak**; ticari başarı ikinci planda. Proje aynı zamanda güçlü bir portföy projesi |
| 20 | İsim / marka | **Hallederiz** · alt başlık "Arızayı anlat, usta gelsin" · slogan "Sen anlat, gerisini Hallederiz." |
| 21 | Pilot şehir | **Kahramanmaraş** (seed verisi, hizmet bölgeleri ve test verisi buna göre) |
| 22 | LLM | **Groq** ile başlanacak (OpenAI uyumlu API). `LLMProvider` soyutlamasıyla sonra kolayca değiştirilebilir |
| 23 | Embedding | Groq embedding sunmadığı için **açık kaynak çok dilli embedding modeli** (ör. bge-m3 / multilingual-e5) backend'de lokal çalışacak |
| 24 | Harita | **OpenStreetMap** (flutter_map + Nominatim/Photon geocoding). Adres araması yetersiz kalırsa sadece geocoding değişir |
| 25 | Kod yeri | Sibel GitHub'da `hallederiz` reposunu açar ve bilgisayarına klonlar. Klasör Claude oturumuna bağlanır, Claude dosyaları oraya yazar, commit/push Sibel'de. Repo görünürlüğüne Sibel karar verir |
| 26 | Çalışma şekli | **Birlikte yazıyoruz.** Sibel her adımda yönlendirir, Claude seçenek sunup sorar. Sibel'in deneyimi: Python/FastAPI, React/Next.js/TS, Docker/PostgreSQL → Flutter ekranlarının ilk versiyonunu Claude yazar ve açıklar |
| 27 | Test cihazı | **iPhone.** Erken aşamada Chrome (`flutter run -d chrome`) + Android emülatörü; konum/push/kamera testine gelince Apple Developer hesabı alınır ve **TestFlight** ile iPhone'da test edilir |

---

## 2. Problem ve değer önerisi

### 2.1 Kullanıcının asıl derdi

Kullanıcının asıl ihtiyacı "tesisatçı bulmak" değil; **evdeki sorunu hızlı, güvenilir ve makul maliyetle çözdürmek.**

Bir arıza anında kullanıcı:

- Arızanın nedenini bilmiyor.
- Hangi ustaya ihtiyacı olduğundan emin değil (petek ısınmıyor → tesisatçı mı, kombici mi?).
- Ustanın yetkin olup olmadığını anlayamıyor.
- Ustanın ne zaman gelebileceğini bilmiyor.
- Sonunda ne ödeyeceğini kestiremiyor.
- Sorunun acil olup olmadığını bilmiyor.
- İş bittikten sonra bir şey ters giderse kime başvuracağını bilmiyor.

### 2.2 Değer önerisi

> Kullanıcının doğru ustayı bulmak için araştırma yapma, onlarca kişiyi arama ve güvenilirliği tahmin etme yükünü kaldırmak; işi baştan sona takip etmek.

### 2.3 Usta tarafında değer

- Kendi uzmanlığına uygun, doğru tanımlanmış iş talepleri (yanlış kategoriden boşa gidiş yok).
- Arıza açıklaması + fotoğraf + AI özeti ile **önceden hazırlıklı gitme** (doğru parça/malzeme).
- Takvim/müsaitlik yönetimi.
- Doğrulanmış iş geçmişiyle oluşan, taşınabilir bir **itibar profili**.
- Müşteri tarafından da değerlendirilen sorunlu müşterilere karşı koruma.

---

## 3. Rakip analizi ve farklılaşma

### 3.1 Rakipler

| Platform | Ne sunuyor | Not |
|----------|-----------|-----|
| **Armut** | 2.000+ hizmet kategorisi, talep oluşturma, teklif alma/karşılaştırma, yorumlar, hizmet verenlerin teklif başına ücret ödemesi | En güçlü rakip; teklif ve değerlendirme akışları gelişmiş |
| **UstaGelsin** | Elektrik, su, boya, tadilat; doğrulanmış usta profilleri, ücretsiz teklif | Usta ağının büyüklüğü belirsiz |
| **Hizmetgo** | AI ile ilan hazırlama, doğrulanmış ustalar, teklif karşılaştırma, 700+ hizmet | "AI eklemek" tek başına farklılaştırmıyor |

### 3.2 Neyle farklılaşıyoruz?

Tek bir özellikle değil, **birleşimle ve uygulama kalitesiyle**:

| Özellik | Piyasada | Bizde |
|---------|----------|-------|
| Konuma göre usta | Var | Var ama tek başına değil; hizmet bölgesi + tahmini varış süresi |
| Puan/yorum | Var | Yalnızca **doğrulanmış işten** gelen yorum + Güven Profili |
| AI talep yazma | Var (Hizmetgo) | AI **teşhis yönlendirme**: soru sorarak doğru uzmanlık alanını bulur |
| Teklif toplama | Var | Arızada teklif beklemek yerine **anında eşleşme**; proje işlerinde teklif modu |
| Anlık müsaitlik | Zayıf/belirsiz | **Teyitli müsaitlik** (dispatch + kabul) |
| İş tamamlama doğrulama | Kısmi | **İki taraflı** tamamlanma + memnuniyet + anlaşmazlık akışı |
| "Neden bu usta?" | Yok/az | **Şeffaf eşleştirme gerekçesi** |
| Hızlı/Güvenilir/Ekonomik | Yok | 3 seçenek + Acil mod |
| Ev profili / bakım geçmişi | Yok/az | Evin dijital karnesi + bakım hatırlatma |
| Fiyat tahmini | Az | Aralık + güven seviyesi + fiyatı değiştiren faktörler |
| Öğrenen sistem | Belirsiz | HITL paneli + versiyonlu model + ölçüm |
| Garanti kaydı | Az | İş sonrası garanti süresi kaydı ve "sorun tekrarladı" butonu |

### 3.3 Yapılacak rakip incelemesi (Faz 0 görevi)

- [ ] Armut, UstaGelsin, Hizmetgo uygulamalarını **müşteri olarak** indir, gerçek bir talep akışını baştan sona dene (ekran görüntüsü al).
- [ ] Mümkünse **hizmet veren tarafı** kayıt akışını incele.
- [ ] Her biri için şu tabloyu doldur: adım sayısı, ilk yanıt süresi, fiyat şeffaflığı, müsaitlik bilgisi, iş sonrası takip, zayıf noktalar.
- [ ] Play Store / App Store'daki **1-2 yıldızlı yorumları** oku ve şikâyetleri kategorile (bu, farklılaşma için altın veri).

---

## 4. Uçtan uca kullanıcı akışı

```
Arıza → AI anlama/sorular → Hizmet kategorisi → Uygun ustalar
     → 3 seçenek (Hızlı / Güvenilir / Ekonomik) → Müsaitlik teyidi
     → Randevu → Usta yolda → Usta geldi → İş başladı → İş tamamlandı
     → Ücret + yapılan işlem + garanti kaydı
     → İki taraflı değerlendirme → Güven verisi → Ev profili güncellenir
     → AI/ML öğrenme döngüsü (insan doğrulamalı)
```

### 4.1 Örnek senaryo

1. Kullanıcı yazar: **"Mutfakta lavabonun altından su geliyor."** (veya sesli anlatır / fotoğraf ekler)
2. AI: *"Anlattığınız durum su tesisatıyla ilişkili görünüyor."* ve sorar:
   - Su sürekli mi akıyor, yalnızca musluk açıkken mi?
   - Borunun hangi kısmından geliyor? (fotoğraf ekleyebilirsiniz)
   - Ana vanayı kapatabildiniz mi? *(güvenlik yönlendirmesi)*
3. AI sonucu: **Hizmet: Su tesisatı → Kaçak müdahalesi · Aciliyet: Orta-Yüksek**
4. Sistem: *"Bölgenizde şu anda müsait 4 uygun usta bulduk."*
5. 3 seçenek kartı gösterilir; her kartta **"Neden bu usta?"** gerekçesi var.
6. Kullanıcı birini seçer → ustaya talep gider → usta **X dakika içinde** kabul eder → randevu oluşur.
7. Kullanıcı ustanın durumunu görür: *Yolda · Tahmini varış 14:30–15:00*.
8. Usta "Geldim" → "İşe başladım" → "İş tamamlandı" (yapılan işlem, kullanılan malzeme, ücret, garanti süresi, fotoğraf).
9. Kullanıcıya sorulur: Sorun çözüldü mü? İşlem yapıldı mı? Ücret konuşulanla uyumlu mu? Tekrar tercih eder misiniz?
10. Ustaya sorulur: Müşteri randevuya uygun muydu? İş tanımlanan kapsamda mıydı? Ödeme yapıldı mı?
11. Her şey **Ev Profili**'ne kaydedilir. Garanti süresi içinde sorun tekrar ederse **"Sorun tekrarladı"** butonu aynı ustaya öncelikli talep açar.

---

## 5. Ürün modülleri (detaylı)

### 5.1 Kullanıcı (müşteri) uygulaması

| Özellik | Açıklama | Faz |
|---------|----------|-----|
| Kayıt / giriş | Telefon + SMS OTP; Google/Apple ile giriş | MVP |
| Konum | İzin varsa otomatik; yoksa manuel adres; birden fazla adres | MVP |
| Arıza anlatma | Metin, fotoğraf, (sonra) sesli anlatım | MVP (ses: Faz 3) |
| AI yönlendirme | Kategori tahmini + takip soruları + aciliyet | MVP |
| Kategori ile doğrudan arama | AI istemeyen kullanıcı için klasik kategori seçimi | MVP |
| Usta sonuçları | 3 seçenek + tam liste + harita görünümü | MVP |
| "Neden bu usta?" | Şeffaf gerekçe | MVP |
| Usta profili | Güven profili, uzmanlıklar, bölge, belgeler, doğrulanmış yorumlar | MVP |
| Talep gönderme | Anında (acil) veya randevulu | MVP |
| Randevu | Uygun zaman dilimlerinden seçim | MVP |
| İş takibi | Durum çizelgesi (kabul → yolda → geldi → başladı → bitti) | MVP |
| Uygulama içi mesajlaşma | Talep bazlı sohbet + fotoğraf | MVP |
| Maskelenmiş arama | Numara gizlenerek arama (sonra) | Faz 3 |
| İş tamamlama onayı | Kullanıcı onayı + memnuniyet anketi | MVP |
| Değerlendirme | Çok boyutlu (iş kalitesi, zamanında varış, fiyat uyumu, iletişim, temizlik) | MVP |
| Anlaşmazlık / şikâyet | "Sorun var" akışı → admin kuyruğu | MVP |
| Ev Profili | Cihazlar (kombi, klima…), bakım geçmişi, belgeler | Faz 2 |
| Bakım hatırlatma | "Kombinizin son bakımından 11 ay geçti" | Faz 2 |
| Fiyat tahmini | Aralık + güven seviyesi | Faz 2 (kural), Faz 4 (ML) |
| Teklif modu | Proje işleri (tadilat, boya, nakliye) için çoklu teklif | Faz 2 |
| Favori ustalar | "Ustam" listesi, tekrar çağır | Faz 2 |
| Garanti takibi | Garanti süresi + "Sorun tekrarladı" | Faz 2 |
| Bildirimler | Push + SMS (kritik durumlar) | MVP |
| Çevrim içi ödeme | Platform üzerinden ödeme + makbuz | Faz 4 |
| Çoklu dil | TR önce, EN sonra | Faz 4 |

### 5.2 Usta (hizmet veren) uygulaması

Aynı Flutter uygulaması içinde **rol bazlı** ayrı arayüz (tek uygulama, iki mod) — iki ayrı uygulama yayınlama yükünü kaldırır.

| Özellik | Açıklama | Faz |
|---------|----------|-----|
| Usta kaydı | Kimlik, telefon, fotoğraf, uzmanlık alanları, hizmet bölgesi (harita üzerinde çizim/yarıçap) | MVP |
| Belge yükleme | Mesleki yeterlilik belgesi, ustalık belgesi, (doğalgaz için) yetkili firma belgesi, vergi levhası | MVP |
| Doğrulama durumu | Beklemede / Onaylandı / Reddedildi | MVP |
| Müsaitlik | "Şu an müsaitim" anahtarı + haftalık çalışma takvimi + izin günleri | MVP |
| Talep gelen kutusu | AI özeti + fotoğraflar + mesafe + tahmini ücret ile; **kabul/ret süresi sayacı** | MVP |
| Randevu takvimi | Günlük/haftalık görünüm | MVP |
| İş durumu güncelleme | Yoldayım → Geldim → Başladım → Bitti | MVP |
| İş kapanış formu | Yapılan işlem, malzeme, ücret, garanti süresi, önce/sonra fotoğraf | MVP |
| Müşteri değerlendirme | Ustanın müşteriyi değerlendirmesi | MVP |
| Fiyat listesi | Standart işler için başlangıç fiyatları | MVP |
| Güven profilim | Kendi metrikleri + gelişim önerileri | Faz 2 |
| Kazanç/iş raporu | Aylık iş sayısı, gelir | Faz 2 |
| Teklif verme | Proje işleri için teklif | Faz 2 |

### 5.3 Admin paneli (Next.js)

| Özellik | Faz |
|---------|-----|
| Usta başvurularını onaylama / belge kontrolü | MVP |
| Kullanıcı ve usta yönetimi (askıya alma, engelleme) | MVP |
| Talep ve randevu izleme (canlı) | MVP |
| Şikâyet / anlaşmazlık kuyruğu | MVP |
| Sahte yorum tespiti ve inceleme | MVP |
| Kategori ağacı yönetimi | MVP |
| **AI Değerlendirme / HITL paneli** (tahmin, düzeltme, gerekçe) | MVP |
| RAG bilgi tabanı yönetimi (doküman ekle/güncelle/versiyonla) | Faz 2 |
| Bölgesel talep/arz ısı haritası | Faz 2 |
| Model/prompt versiyonları ve metrik karşılaştırma | Faz 3 |
| Fiyat verisi ve model izleme | Faz 4 |

### 5.4 AI Akıllı Arıza Yönlendirme (Modül A)

- Kullanıcı serbest metin + opsiyonel fotoğraf girer.
- LLM **yapılandırılmış çıktı** üretir (JSON şema zorunlu):

```json
{
  "domain": "heating",
  "service_category": "boiler_service",
  "symptoms": ["inconsistent_hot_water"],
  "urgency": "medium",
  "safety_flag": false,
  "follow_up_questions": [
    "Kombinin ekranında bir hata kodu var mı?",
    "Sorun yalnızca sıcak suda mı, peteklerde de mi?"
  ],
  "confidence": 0.78,
  "alternative_categories": [
    {"category": "central_heating_plumbing", "confidence": 0.15}
  ]
}
```

- **En fazla 3–4 takip sorusu**; sonra karar.
- Güven düşükse (< eşik) kullanıcıya iki seçenek sunulur: "Bu ikisinden hangisi?" veya "Kategoriyi kendim seçeyim".
- **Güvenlik kuralları (zorunlu):**
  - Doğalgaz kokusu, kıvılcım, yanık kokusu, su + elektrik teması gibi durumlarda **önce güvenlik uyarısı** (ör. "Doğalgaz kokusu alıyorsanız elektrik düğmelerine dokunmayın, ortamı havalandırın ve **187 Doğalgaz Acil**'i arayın").
  - Model **kesin teşhis koymaz**, söküp takma talimatı **vermez**. Sadece "hangi uzman" sorusunu yanıtlar.
  - Güvenlik kuralları LLM'e bırakılmaz; **kural tabanlı ön filtre** (anahtar kelime + sınıflandırıcı) her zaman çalışır.

### 5.5 Teyitli Müsaitlik + Randevu (Modül B)

**İki mod:**

1. **Acil / Şimdi:** Sistem en iyi N (ör. 3) ustaya **eş zamanlı veya sıralı** "dispatch" gönderir. İlk kabul eden atanır. Kabul süresi (ör. 5 dk) dolarsa sıradakine geçer.
2. **Randevulu:** Kullanıcı ustanın takviminden boş slot seçer; usta onaylar (onay süresi ör. 30 dk–2 saat).

**Kurallar:**

- "Şu an müsait" bilgisi son **X saatte** güncellenmediyse "müsait" yerine "müsaitlik teyit edilecek" gösterilir.
- Kabul etmeyen/yanıt vermeyen ustanın **yanıt oranı** düşer → sıralamada etkisi olur.
- Çifte rezervasyonu önlemek için slot kilitleme (Redis lock + DB transaction).

**Talep durum makinesi:**

```
DRAFT → ANALYZED → MATCHING → DISPATCHED → ACCEPTED → SCHEDULED
      → EN_ROUTE → ARRIVED → IN_PROGRESS → COMPLETED_BY_PROVIDER
      → CONFIRMED_BY_CUSTOMER → REVIEWED → CLOSED

Yan dallar: CANCELLED_BY_CUSTOMER, CANCELLED_BY_PROVIDER, NO_SHOW,
            EXPIRED (kimse kabul etmedi), DISPUTED → RESOLVED
```

### 5.6 Güven Profili (Modül C)

Usta profilinde gösterilecek:

```
183 tamamlanmış iş · 176 doğrulanmış iş
4,8 / 5 müşteri puanı (Bayes düzeltmeli)
%94 zamanında varış · %3 iptal · %2 şikâyet
Yanıt oranı %91 · Ort. ilk yanıt 4 dk
Uzmanlık: Su tesisatı (87 iş), Kaçak tespiti (41), Gider (29)
✓ Kimlik doğrulandı · ✓ Mesleki yeterlilik belgesi
```

**Hesaplama prensipleri:**

- **Bayes ortalaması:** Az yorumlu ustanın 5,0'ı, çok yorumlu ustanın 4,8'inden yukarı çıkmaz.
  `skor = (v·R + m·C) / (v + m)` → v: yorum sayısı, R: ustanın ortalaması, C: kategori ortalaması, m: güven eşiği (ör. 10).
- **Kategori bazlı deneyim:** Kombide 100 işi olan usta, tesisat talebinde otomatik öne çıkmaz.
- **Zaman ağırlığı:** Son 6 ayın verisi daha ağır.
- **Yeni usta:** "Yeni" rozeti, kesin güvenilirlik iddiası yok; kontrollü görünürlük (bkz. 8.4 cold-start).
- Ücretli öne çıkarma (ileride) **güven skorunu değiştirmez**, ayrıca "Sponsorlu" etiketiyle gösterilir.

### 5.7 İş tamamlama ve karşılıklı memnuniyet

**Usta kapanış formu:** yapılan işlem (seçmeli + serbest), malzeme, toplam ücret, garanti süresi, önce/sonra fotoğraf.

**Müşteri onayı (zorunlu adımlar):**

1. Sorun çözüldü mü? (Evet / Kısmen / Hayır)
2. Belirtilen işlem yapıldı mı?
3. Ödenen ücret konuşulanla uyumlu mu? (Ödenen tutar girilir)
4. Puanlar: iş kalitesi, zamanında varış, iletişim, temizlik, fiyat uyumu
5. Ustayı tekrar tercih eder misiniz?

**Usta tarafı:** müşteri randevuya uygun muydu, iş kapsam dahilinde miydi, ödeme alındı mı, müşteri puanı.

**"Doğrulanmış iş" tanımı:** Usta "tamamlandı" + müşteri "onayladı" + (opsiyonel) konum check-in eşleşmesi. Sadece doğrulanmış işler yorum hakkı verir.

**Anlaşmazlık:** Herhangi bir taraf "sorun var" derse → admin kuyruğu → iki tarafın beyanı + fotoğraflar → karar → güven verisine etkisi.

**Otomatik onay:** Müşteri 72 saat içinde yanıt vermezse iş "tamamlandı (onaysız)" olur; doğrulanmış sayılmaz.

### 5.8 Üç akıllı seçenek + Acil mod

| Kart | Kriter |
|------|--------|
| ⚡ **Hızlı çözüm** | Müsaitliği teyitli, tahmini varış süresi en kısa, minimum güven eşiğini geçen |
| 🛡️ **Güvenilir tercih** | Bu kategoride yeterli doğrulanmış işi ve en yüksek güven skoru olan |
| 💰 **Ekonomik seçenek** | Aynı kapsamda önceden bildirilmiş en uygun fiyat, minimum güven eşiğini geçen |
| 🚨 **Acil mod** | Gece/hafta sonu, su baskını vb. — yalnızca acil hizmet veren ve şu an aktif ustalar |

- Aynı usta birden fazla kartta çıkabilir ("Hem en hızlı hem en güvenilir").
- Kartların altında "Tüm uygun ustaları gör" listesi.
- Bunlar **mutlak kalite iddiası değil**, kullanıcının önceliğine göre öneri.

### 5.9 Ev Profili ve Bakım Geçmişi

```
🏠 Evim (Kadıköy, 3+1, 2008 yapımı)
├── Kombi: Vaillant ecoTEC · Montaj 2024 · Son bakım 12.09.2026 · Garanti devam ediyor
├── Su tesisatı: Son kaçak müdahalesi 18.05.2026 (Ahmet Usta, 6 ay garanti)
├── Klima: 2 cihaz · Son bakım Haziran 2026
└── Belgeler: faturalar, garanti belgeleri (fotoğraf)
```

- Platformdaki her iş otomatik eklenir; dışarıda yapılan işler kullanıcı tarafından manuel eklenebilir.
- **Bakım hatırlatma (başta kural tabanlı):** kombi yıllık, klima sezon öncesi, su arıtma filtresi 6 ay, vb.
- Arıza anlatırken AI ev profilini **bağlam** olarak kullanır ("Kombiniz 2024 Vaillant, son bakım 1 ay önce…").
- Sonra: ML ile bakım ihtiyacı / arıza riski tahmini (yeterli veri biriktiğinde).

### 5.10 Fiyat tahmini

- **Faz 2 (kural):** Ustaların standart iş başlangıç fiyatlarından medyan + çeyrekler arası aralık.
- **Faz 4 (ML):** Bkz. 8.2.
- Gösterim: **"Tahmini 800–1.200 TL · Güven: Orta · Fiyatı değiştirebilecekler: malzeme, gece saati, erişim zorluğu"**
- Veri yoksa: **"Bu hizmet için yeterli geçmiş veri yok, güvenilir tahmin yapılamıyor."**
- Asla tek kesin rakam ("AI 937 TL dedi") gösterilmez.

### 5.11 Teklif modu (proje işleri)

Arıza işlerinde anında eşleşme; **tadilat, boya, nakliye, mutfak dolabı** gibi kapsamı büyük işlerde Armut tarzı:

- Kullanıcı AI destekli talep formu doldurur (AI eksik bilgileri sorar: m², oda sayısı, kat, asansör…).
- Uygun ustalara iletilir, en fazla N teklif gelir.
- Teklifler **karşılaştırma tablosu** halinde (fiyat, süre, güven profili, dahil olanlar).
- Keşif randevusu opsiyonu.

---

## 6. Hizmet kategorileri

Kategori ağacı **baştan geniş** tasarlanır, operasyon **aşamalı** açılır.

| Ana kategori | Alt kategoriler (örnek) | Mod | Açılış |
|--------------|------------------------|-----|--------|
| Elektrik | Arıza, priz/anahtar, sigorta, aydınlatma, tesisat yenileme | Anında | Pilot |
| Su tesisatı | Kaçak, tıkanıklık, batarya/musluk, rezervuar, gider | Anında | Pilot |
| Kombi / Isıtma | Arıza, bakım, petek temizliği, merkezi ısıtma | Anında | Pilot |
| Doğalgaz | Tesisat (yetkili firma), kaçak kontrol | Anında/Teklif | Faz 2 |
| Klima | Montaj, bakım, gaz dolumu, arıza | Anında | Faz 2 |
| Beyaz eşya | Çamaşır/bulaşık makinesi, buzdolabı, fırın | Anında | Faz 2 |
| Çilingir | Kapı açma, kilit değişimi | Acil | Faz 2 |
| Cam / PVC | Cam değişimi, pencere ayarı | Anında | Faz 3 |
| Montaj | Mobilya, TV askı, perde | Randevu | Faz 3 |
| Marangoz | Kapı, dolap tamiri | Randevu/Teklif | Faz 3 |
| Boya / Badana | — | Teklif | Faz 3 |
| Tadilat | Mutfak, banyo, komple | Teklif | Faz 3 |
| Temizlik | Ev, ofis, inşaat sonrası, koltuk/halı | Randevu | Faz 3 |
| Nakliye | Evden eve, parça eşya | Teklif | Faz 3 |
| Haşere kontrolü | İlaçlama | Randevu | Faz 3 |
| Bahçe | Bakım, peyzaj | Randevu | Faz 4 |
| İnternet / Ağ | Modem, kablolama, güvenlik kamerası | Randevu | Faz 4 |
| TV / Uydu | Anten, uydu kurulumu | Randevu | Faz 4 |
| Akıllı ev | Kurulum | Randevu | Faz 4 |
| Özel ders, organizasyon, sağlık vb. | Armut'taki diğer hizmetler | Teklif | Faz 5 (ihtiyaç olursa) |

**Veri modeli:** Kategoriler ağaç yapısında (`parent_id`), her kategorinin `mode` (instant / scheduled / quote), `is_active`, `safety_level`, `requires_certificate` alanları var. Yeni kategori **koda dokunmadan** admin panelinden açılır.

---

## 7. Yapay zekâ mimarisi

### 7.1 Temel prensip

> Üretimdeki model her yorumdan sonra kendiliğinden değişmez. Öğrenme **kontrollü** ilerler:
> **geri bildirim → veri seti → insan doğrulaması → değerlendirme → yeni versiyon → kontrollü yayın → izleme**

### 7.2 AI katmanları

```
                    AI GATEWAY (FastAPI modülü)
   ┌──────────────┬──────────────┬──────────────┬──────────────┐
   │ 1. Problem   │ 2. Bilgi     │ 3. Eşleştirme│ 4. Tahmin    │
   │ Anlama       │ (RAG)        │ (Matching)   │ (Fiyat/      │
   │ (LLM +       │              │              │  Bakım)      │
   │  güvenlik)   │              │              │              │
   └──────────────┴──────────────┴──────────────┴──────────────┘
                 │ hepsi loglanır → Feedback Store
                 ▼
         Human-in-the-loop paneli → Doğrulanmış veri seti
                 ▼
         Değerlendirme (eval) → Versiyon → Kontrollü yayın
```

**Katman 1 — Problem anlama:**
- LLM API (yapılandırılmış JSON çıktı), sağlayıcıdan bağımsız soyutlama (`LLMProvider` arayüzü) → model değiştirmek backend'i etkilemez.
- Önce **kural tabanlı güvenlik filtresi**, sonra LLM.
- Fotoğraf varsa çok modlu (vision) model ile ek ipucu.
- Her çağrının `prompt_version`, `model_name`, girdi, çıktı, süre, maliyet kaydı.

**Katman 2 — RAG:**
- Bilgi tabanı içeriği:
  - Hizmet kategorileri ve tanımları
  - Arıza belirtisi → uzmanlık alanı eşleme dokümanları (kendi yazdığımız, uzman onaylı)
  - Teknik terim sözlüğü (halk dili ↔ teknik: "petek" = radyatör, "kombi su kaybediyor" vb.)
  - Kombi/klima marka **hata kodu** tabloları (hangi uzmana yönlendirir)
  - Platform kuralları, garanti koşulları, SSS
  - Güvenlik kuralları
  - **Geçmişteki doğrulanmış talepler** (anonimleştirilmiş, "few-shot" örnek olarak)
- Teknik: **PostgreSQL + pgvector**, **hibrit arama** (vektör + PostgreSQL full-text/BM25 benzeri), **reranker** (cross-encoder), Türkçe destekli çok dilli embedding modeli.
- Dokümanlar versiyonlu; hangi cevabın hangi dokümanlara dayandığı loglanır.
- **RAG teknik gerçeğin yerine geçmez**, sadece yönlendirmeyi destekler.

**Katman 3 — Eşleştirme:** bkz. 8.1.

**Katman 4 — Tahmin:** fiyat (8.2), bakım (8.3).

### 7.3 Human-in-the-loop (HITL) paneli

Admin panelinde **"AI Değerlendirme"** ekranı:

| Alan | Örnek |
|------|-------|
| Kullanıcı metni | "Peteklerin biri ısınmıyor" |
| AI tahmini | Kombi servisi (0,71) |
| Getirilen dokümanlar | doc#12, doc#45 |
| Kullanıcının nihai seçimi | Kombi servisi |
| Ustanın gerçekte yaptığı iş | Petek hava alma / tesisat |
| İnsan düzeltmesi | **Merkezi ısıtma / petek tesisatı** |
| Gerekçe | "Tek petek sorunu genelde hava/vana kaynaklı" |
| Etiket | yanlış_kategori |

**Hangi örnekler insana gider (aktif öğrenme):**
- Düşük güvenli tahminler
- Kullanıcının kategoriyi değiştirdiği talepler
- Ustanın "yanlış kategori" işaretlediği işler
- Şikâyetle sonuçlanan talepler
- Rastgele %5 örneklem (kalite kontrolü)

**Örtük geri bildirim sinyalleri (otomatik toplanır):**
- Kullanıcı önerilen kategoriyi kabul etti mi?
- Usta kategoriyi düzeltti mi?
- İş tamamlandı mı, memnuniyet ne?
- Önerilen 3 seçenekten hangisi seçildi, hangisi tamamlandı?

### 7.4 Öğrenme döngüsü (MLOps)

```
1. Loglama        → her AI kararı + sonuç
2. Etiketleme     → HITL paneli + örtük sinyaller
3. Veri seti      → versiyonlu (dataset_v1, v2…), eğitim/test ayrımı sabit
4. İyileştirme    → prompt güncelleme / few-shot örnek / RAG dokümanı /
                    (yeterli veri olunca) küçük sınıflandırıcı fine-tune
5. Değerlendirme  → sabit "altın test seti" üzerinde: doğruluk, makro-F1,
                    güvenlik ihlali sayısı, ortalama soru sayısı
6. Yayın          → shadow mode (yeni versiyon arka planda çalışır, kullanılmaz)
                    → %10 A/B → tamamı
7. İzleme         → üretim metrikleri; kötüleşirse otomatik geri dönüş
```

**Kural:** Yeni versiyon, mevcut versiyonu altın test setinde **geçmeden** ve **sıfır güvenlik ihlali** olmadan yayına çıkmaz.

**Araçlar (başlangıç sade):** prompt/model versiyonları DB tablosunda; eval scriptleri `ml/` klasöründe; ileride MLflow veya benzeri.

### 7.5 AI kalite metrikleri

- Kategori doğruluğu (top-1, top-3)
- Kullanıcının öneriyi kabul oranı
- Yanlış yönlendirme oranı (usta düzeltmesi)
- Ortalama takip sorusu sayısı (az olmalı)
- Güvenlik durumu tespit oranı (recall ≈ %100 hedef)
- LLM gecikmesi ve talep başı maliyet

---

## 8. Makine öğrenmesi modelleri

### 8.1 Eşleştirme / sıralama

**Aşama 1 — Ağırlıklı skor (MVP):**

```
skor = w1·mesafe_skoru + w2·müsaitlik_skoru + w3·güven_skoru
     + w4·kategori_deneyimi + w5·yanıt_oranı + w6·fiyat_skoru
```

- Filtreler (önce): kategori eşleşmesi, hizmet bölgesi içinde (PostGIS `ST_Contains` / `ST_DWithin`), doğrulanmış hesap, askıda değil.
- Ağırlıklar seçilen karta göre değişir (Hızlı kartında müsaitlik/mesafe ağır, Güvenilir kartında güven ağır).
- Her sonuç için **açıklama** üretilir ("Konumunuza 2,1 km · Bu hizmette 87 iş · Şu an müsait").

**Aşama 2 — Learning-to-rank (yeterli veri sonrası, ör. birkaç bin tamamlanmış iş):**
- Model: LightGBM / XGBoost **LambdaMART**.
- Etiket: seçildi mi, kabul edildi mi, tamamlandı mı, memnuniyet.
- Özellikler: mesafe, ETA, güven metrikleri, fiyat, saat/gün, kategori, usta yükü, geçmiş kullanıcı-usta etkileşimi.
- Offline değerlendirme (NDCG) → A/B test → yayın.

**Adalet kuralları:** Yeni ustalara keşif payı, tek ustanın tüm işleri toplamasını önleyen yük dengeleme.

### 8.2 Fiyat tahmini

- Özellikler: hizmet tipi, alt kategori, ilçe/şehir, konut tipi, arıza tipi, tahmini süre, malzeme, aciliyet, saat/gün/mevsim, usta deneyimi, geçmiş fiyatlar.
- Model: Gradient boosting + **kuantil regresyon** (P10, P50, P90) → aralık üretir.
- Çıktı: **aralık + güven seviyesi + etkileyen faktörler** (SHAP ile açıklama).
- Yeterli örnek yoksa (kategori×bölge başına eşik altı) **tahmin göstermez**.
- Enflasyon için zaman ağırlığı / düzenli yeniden eğitim (Türkiye koşullarında önemli).

### 8.3 Bakım ihtiyacı tahmini

- Başlangıç: kural (cihaz türü × periyot).
- Sonra: cihaz yaşı, marka, son bakım, arıza geçmişi → arıza olasılığı / bakım önerisi (survival analysis veya sınıflandırma).

### 8.4 Cold-start (veri yokken) stratejileri

- Yeni ustaya sınırlı ama garanti görünürlük (keşif / exploration).
- Yeni kategori×bölge için fiyatı ustaların beyan ettiği listeden hesapla.
- AI sınıflandırma için başta **elle hazırlanmış 300–500 örneklik** etiketli veri seti (biz yazarız + ustalara sorarız).

---

## 9. Teknoloji yığını

### 9.1 Kesinleşmiş yığın

| Katman | Teknoloji | Neden |
|--------|-----------|-------|
| Mobil (iOS + Android) | **Flutter + Dart** | Tek kod, iki platform; Windows'ta geliştirilebilir |
| Mobil durum yönetimi | Riverpod | Test edilebilir, yaygın |
| Mobil yönlendirme | go_router | Deep link desteği |
| Mobil HTTP | Dio + OpenAPI'den üretilmiş client | Tip güvenliği |
| Harita (mobil + web) | **flutter_map (OpenStreetMap)** + Nominatim/Photon geocoding | Ücretsiz, API anahtarı yok |
| Native iOS kısımları | Swift / SwiftUI (Platform Channel) | Gerektiğinde |
| Web | **Next.js + TypeScript + React** | SEO, landing, usta profilleri, admin |
| Web UI | Tailwind CSS + shadcn/ui | Hızlı geliştirme |
| Backend | **Python + FastAPI** | AI/ML ile aynı dil |
| ORM / migration | SQLAlchemy 2 + Alembic | Standart |
| Doğrulama | Pydantic v2 | FastAPI ile entegre |
| Veritabanı | **PostgreSQL 16** | — |
| Konum | **PostGIS** | Hizmet bölgesi, mesafe sorguları |
| Vektör | **pgvector** | RAG, tek DB |
| Cache / kilit / kuyruk | **Redis** | Rate limit, slot kilidi, dispatch zamanlayıcıları |
| Arka plan işleri | Celery veya RQ (sonra gerekirse Temporal) | Dispatch timeout, bildirim, embedding |
| Gerçek zamanlı | WebSocket (FastAPI) | İş durumu, mesajlaşma |
| Dosya depolama | S3 uyumlu (Cloudflare R2 / MinIO lokal) | Fotoğraf, belge |
| Push bildirim | Firebase Cloud Messaging (Android + iOS/APNs) | Ücretsiz |
| SMS / OTP | Türk SMS sağlayıcısı (Netgsm, İleti Merkezi vb.) | Yerel numaralar |
| Kimlik | JWT (access + refresh) + OTP | — |
| LLM | **Groq** API (OpenAI uyumlu; sağlayıcıdan bağımsız soyutlama) | Hızlı, ücretsiz katman; sonra değiştirilebilir |
| Embedding | Açık kaynak çok dilli model (bge-m3 / multilingual-e5), backend'de lokal | Groq embedding sunmuyor; ücretsiz |
| Reranker | Cross-encoder (çok dilli) | — |
| ML | scikit-learn, LightGBM, pandas | Fiyat, ranking |
| Deney takibi | Başta DB + script; sonra MLflow | — |
| Konteyner | Docker + docker-compose | Lokal ortam = sunucu |
| CI/CD | **GitHub Actions** (Linux + **macOS runner**) | iOS build için |
| iOS dağıtım | **Fastlane** + TestFlight | Mac olmadan otomasyon |
| Hata izleme | Sentry | Mobil + web + backend |
| Analitik | PostHog (self-host veya cloud ücretsiz katman) | Funnel ölçümü |
| Hosting (başlangıç) | Tek VPS (Hetzner vb.) + docker-compose; web için Vercel | Düşük maliyet |

### 9.2 Bilinçli olarak YAPMADIKLARIMIZ

- ❌ Mikroservis — **modüler monolit** ile başlıyoruz.
- ❌ Ayrı vektör veritabanı (Chroma/Qdrant) — pgvector yeterli; ihtiyaç olursa geçilir.
- ❌ Kubernetes — tek sunucu + docker-compose.
- ❌ Native Swift + native Kotlin iki ayrı uygulama.
- ❌ Kontrolsüz online öğrenme.

---

## 10. Mac olmadan iOS geliştirme stratejisi

### 10.1 Gerçekler

- iOS uygulamasını **build/imzalama/App Store'a yükleme** için **macOS + Xcode** şart (Flutter kullansak da).
- Apple güncel kuralları: App Store yüklemeleri için Xcode 26+ / iOS 26 SDK (Nisan 2026'dan beri); Nisan 2027'den itibaren Xcode 27 / iOS 27 SDK beklenecek.
- **Apple Developer Program: yıllık 99 USD** — TestFlight ve App Store için gerekli (Mac'ten bağımsız maliyet).

### 10.2 Plan

```
Windows bilgisayar
 ├── Flutter kodu (iOS uyumlu yazılır)
 ├── Android emülatör / gerçek telefonla test
 ├── Web (Next.js) geliştirme
 └── Backend + AI

   git push
     ↓
GitHub Actions (macOS runner)
 ├── flutter build ipa
 ├── Fastlane ile imzalama (App Store Connect API key + match)
 └── TestFlight'a yükleme
     ↓
iPhone'da TestFlight ile test (kendi veya arkadaş iPhone'u)
     ↓
App Store
```

### 10.3 Seçenekler (maliyet sırasına göre)

| Seçenek | Maliyet | Not |
|---------|---------|-----|
| **GitHub Actions macOS runner** | Public repo'da ücretsiz; private repoda ücretsiz dakikalar sınırlı (macOS dakikası 10x sayılır) | Ana yöntem |
| **Codemagic** (Flutter odaklı CI) | Ücretsiz katman (aylık sınırlı macOS dakikası) | Flutter için çok pratik, alternatif |
| Mac ödünç almak (arkadaş/üniversite lab) | 0 | İlk sertifika kurulumu ve Xcode'da hata ayıklama için ideal |
| Bulut Mac kiralama (saatlik/aylık) | Düşük-orta | Xcode'a ekrandan erişmek gerektiğinde |
| İkinci el Apple Silicon Mac | Sonra | Proje ciddileşirse |

> ⚠️ **Not:** iOS simülatörü sadece Mac'te çalışır. Bu yüzden iOS testleri **TestFlight + gerçek iPhone** üzerinden yapılacak. iOS'a özgü sorunlar (izinler, push, konum) için `Info.plist` ayarlarına baştan dikkat edilecek.

### 10.4 iOS için baştan dikkat edilecekler

- [x] Bundle ID: `com.hallederiz.app`
- [ ] `Info.plist`: konum, kamera, fotoğraf kütüphanesi, bildirim izin metinleri (Türkçe, açıklayıcı).
- [ ] Apple ile giriş: Google ile giriş varsa App Store kuralı gereği **Apple ile giriş** de sunulmalı.
- [ ] Hesap silme özelliği uygulama içinden yapılabilmeli (App Store zorunluluğu).
- [ ] Gizlilik etiketleri (App Privacy) için toplanan veri listesi hazır olsun.
- [ ] Push için APNs anahtarını Firebase'e yükle.
- [ ] Swift/SwiftUI öğrenme: Apple'ın SwiftUI eğitimleri + küçük deneme projeleri (Platform Channel ile Flutter'a bağlamayı dene).

---

## 11. Sistem mimarisi

```
┌───────────────────┐   ┌───────────────────┐   ┌───────────────────┐
│ Flutter Uygulama  │   │  Next.js Web      │   │ Next.js Admin     │
│ iOS / Android     │   │  (SEO, profiller, │   │ (HITL, onay,      │
│ Müşteri + Usta    │   │   web talep)      │   │  şikâyet)         │
└────────┬──────────┘   └────────┬──────────┘   └────────┬──────────┘
         │  HTTPS / WebSocket    │                       │
         └───────────────┬───────┴───────────────────────┘
                         ▼
               ┌────────────────────┐
               │  FastAPI (monolit) │
               │ auth · users       │
               │ providers · catalog│
               │ requests · dispatch│
               │ appointments       │
               │ jobs · reviews     │
               │ trust · homes      │
               │ chat · notify      │
               │ admin · payments*  │
               │ ── AI Gateway ──   │
               │ triage · rag       │
               │ matching · pricing │
               │ feedback · evals   │
               └──┬──────┬──────┬───┘
                  │      │      │
       ┌──────────┘      │      └───────────┐
       ▼                 ▼                  ▼
┌─────────────┐   ┌────────────┐    ┌──────────────┐
│ PostgreSQL  │   │   Redis    │    │ Worker'lar   │
│ + PostGIS   │   │ cache/lock │    │ (Celery/RQ)  │
│ + pgvector  │   │ queue      │    │ dispatch,    │
└─────────────┘   └────────────┘    │ bildirim,    │
                                     │ embedding,   │
       ┌──────────────┐              │ ML eğitim    │
       │ S3 / R2      │              └──────────────┘
       │ fotoğraflar  │
       └──────────────┘     Dış servisler: LLM API, FCM/APNs,
                            SMS, Harita/Geocoding, Sentry
```

---

## 12. Veritabanı şeması

> Ana tablolar (alanlar özet). Tüm tablolarda `id (uuid)`, `created_at`, `updated_at`.

**Kimlik ve kullanıcılar**
- `users` — phone, email, name, role (customer/provider/admin), status, locale
- `auth_otps` — phone, code_hash, expires_at, attempts
- `devices` — user_id, platform, push_token
- `addresses` — user_id, title, text, `location geography(Point)`, district, city

**Usta**
- `providers` — user_id, display_name, bio, photo, status (pending/verified/suspended), is_emergency, base_location (Point)
- `provider_documents` — provider_id, type, file_url, status, reviewed_by
- `provider_categories` — provider_id, category_id, experience_years, base_price_min, base_price_max
- `service_areas` — provider_id, `area geography(Polygon)` veya center + radius_km
- `availability_rules` — provider_id, weekday, start_time, end_time
- `availability_exceptions` — provider_id, date, type (off/extra)
- `provider_live_status` — provider_id, is_available_now, last_seen_at, current_location

**Katalog**
- `categories` — parent_id, slug, name_tr, mode (instant/scheduled/quote), safety_level, requires_certificate, is_active
- `service_items` — category_id, name, unit, typical_duration_min

**Talep ve iş**
- `service_requests` — customer_id, address_id, raw_text, photos[], status, urgency, selected_category_id, ai_triage_id, scheduled_window
- `ai_triage_results` — request_id, model, prompt_version, output_json, confidence, retrieved_doc_ids[], latency_ms, cost
- `triage_qa` — triage_id, question, answer
- `match_results` — request_id, provider_id, score, score_breakdown_json, card_type (fast/trusted/budget), rank, explanation
- `dispatches` — request_id, provider_id, sent_at, expires_at, response (accepted/declined/expired), responded_at
- `appointments` — request_id, provider_id, start_at, end_at, status
- `jobs` — appointment_id, status, en_route_at, arrived_at, started_at, completed_at, checkin_location
- `job_closures` — job_id, work_done_text, service_item_ids[], materials, total_price, warranty_days, photos_before[], photos_after[]
- `job_confirmations` — job_id, resolved (yes/partial/no), price_paid, price_matches, would_rehire
- `quotes` — request_id, provider_id, amount, duration, details, status (teklif modu)

**Değerlendirme ve güven**
- `reviews` — job_id, author_id, target_id, direction (customer→provider / provider→customer), scores_json, comment, is_verified, moderation_status
- `disputes` — job_id, opened_by, reason, status, resolution, admin_id
- `provider_trust_metrics` — provider_id, category_id (nullable), completed, verified, bayes_rating, on_time_rate, cancel_rate, complaint_rate, response_rate, avg_response_sec, computed_at

**Ev profili**
- `homes` — user_id, address_id, type, rooms, build_year
- `home_assets` — home_id, type (boiler/ac/...), brand, model, install_date, warranty_until
- `maintenance_records` — home_id, asset_id, job_id (nullable), date, description, provider_name, cost
- `maintenance_reminders` — asset_id, due_date, rule_id, status

**Mesajlaşma ve bildirim**
- `conversations` — request_id
- `messages` — conversation_id, sender_id, text, attachment_url, read_at
- `notifications` — user_id, type, payload, sent_at, read_at

**AI / ML**
- `kb_documents` — title, source, category_id, version, is_active
- `kb_chunks` — document_id, text, `embedding vector(n)`, tsvector
- `prompt_versions` — name, version, template, is_active
- `model_versions` — task (triage/ranking/pricing), version, metrics_json, status (shadow/ab/live/retired)
- `feedback_labels` — triage_id, labeler_id, correct_category_id, label_type, reason
- `eval_runs` — model_version_id, dataset_version, metrics_json
- `datasets` — name, version, row_count, frozen_at
- `price_observations` — job_id, category_id, district, features_json, price

**Yönetim**
- `audit_logs` — actor_id, action, entity, entity_id, diff_json

---

## 13. API tasarımı

> REST + WebSocket. Versiyon: `/api/v1`. OpenAPI şemasından Flutter (Dart) ve Next.js (TS) client'ları **otomatik üretilecek**.

**Auth**
- `POST /auth/otp/request` · `POST /auth/otp/verify` · `POST /auth/refresh` · `POST /auth/logout`
- `POST /auth/oauth/google` · `POST /auth/oauth/apple`
- `DELETE /me` (hesap silme)

**Kullanıcı / adres / ev**
- `GET/PATCH /me` · `GET/POST/PATCH/DELETE /me/addresses`
- `GET/POST /homes` · `POST /homes/{id}/assets` · `GET /homes/{id}/history` · `GET /homes/{id}/reminders`

**Katalog**
- `GET /categories` (ağaç) · `GET /categories/{slug}`

**Talep akışı**
- `POST /requests` (metin + adres + fotoğraf) → triage başlar
- `GET /requests/{id}/triage` · `POST /requests/{id}/triage/answers`
- `POST /requests/{id}/category` (kullanıcı onayı/değişikliği)
- `GET /requests/{id}/matches` (3 kart + liste + açıklamalar)
- `GET /requests/{id}/price-estimate`
- `POST /requests/{id}/dispatch` (acil) · `POST /requests/{id}/book` (slot seçimi)
- `POST /requests/{id}/cancel`
- `GET /requests` (geçmiş)

**Usta**
- `POST /providers/apply` · `POST /providers/me/documents`
- `PATCH /providers/me/live-status` (müsait/meşgul)
- `GET/PUT /providers/me/availability` · `GET/PUT /providers/me/service-areas` · `GET/PUT /providers/me/categories`
- `GET /providers/me/inbox` · `POST /dispatches/{id}/accept` · `POST /dispatches/{id}/decline`
- `GET /providers/{id}` (public profil + güven profili) · `GET /providers/{id}/slots`

**İş**
- `POST /jobs/{id}/en-route` · `/arrived` · `/start` · `/complete` (kapanış formu)
- `POST /jobs/{id}/confirm` (müşteri) · `POST /jobs/{id}/reviews` · `POST /jobs/{id}/dispute`
- `POST /jobs/{id}/recurrence` ("Sorun tekrarladı")

**Teklif modu**
- `POST /requests/{id}/quotes` (usta) · `GET /requests/{id}/quotes` · `POST /quotes/{id}/accept`

**Mesajlaşma**
- `GET /conversations/{id}/messages` · `POST /conversations/{id}/messages`
- `WS /ws` (iş durumu, yeni mesaj, dispatch bildirimi)

**Admin**
- `GET /admin/providers?status=pending` · `POST /admin/providers/{id}/verify|reject|suspend`
- `GET /admin/disputes` · `POST /admin/disputes/{id}/resolve`
- `GET /admin/reviews/flagged` · `POST /admin/reviews/{id}/moderate`
- `GET /admin/ai/triage?filter=low_confidence|changed|disputed` · `POST /admin/ai/triage/{id}/label`
- `GET/POST /admin/kb/documents` · `POST /admin/kb/reindex`
- `GET /admin/models` · `POST /admin/models/{id}/promote`
- `GET /admin/metrics/*`

---

## 14. Repo yapısı

Tek **monorepo** (GitHub):

```
hallederiz/
├── apps/
│   ├── mobile/                 # Flutter (iOS + Android)
│   │   ├── lib/
│   │   │   ├── core/           # tema, router, api client, auth
│   │   │   ├── features/
│   │   │   │   ├── auth/
│   │   │   │   ├── triage/     # AI sohbet/sorular
│   │   │   │   ├── matching/   # 3 kart, liste, harita
│   │   │   │   ├── booking/
│   │   │   │   ├── jobs/       # durum takibi, onay
│   │   │   │   ├── reviews/
│   │   │   │   ├── chat/
│   │   │   │   ├── home_profile/
│   │   │   │   └── provider/   # usta modu ekranları
│   │   │   └── main.dart
│   │   ├── ios/  android/
│   │   └── test/
│   ├── web/                    # Next.js (public site + web talep)
│   └── admin/                  # Next.js (admin + HITL)  [veya web içinde /admin]
├── backend/
│   ├── app/
│   │   ├── core/               # config, db, security, deps
│   │   ├── modules/
│   │   │   ├── auth/  users/  providers/  catalog/
│   │   │   ├── requests/  dispatch/  appointments/  jobs/
│   │   │   ├── reviews/  trust/  homes/  chat/  notifications/
│   │   │   ├── admin/
│   │   │   └── ai/
│   │   │       ├── gateway.py
│   │   │       ├── llm_provider.py
│   │   │       ├── safety.py
│   │   │       ├── triage/  rag/  matching/  pricing/  feedback/
│   │   ├── workers/
│   │   └── main.py
│   ├── alembic/
│   └── tests/
├── ml/
│   ├── datasets/               # versiyonlu (büyükler git dışı)
│   ├── notebooks/
│   ├── training/               # ranking, pricing
│   ├── evals/                  # altın test seti + eval scriptleri
│   └── kb/                     # RAG kaynak dokümanları (markdown)
├── packages/
│   └── api-client/             # OpenAPI'den üretilen TS client
├── infra/
│   ├── docker-compose.yml      # postgres(+postgis+pgvector), redis, minio, backend, worker
│   └── deploy/
├── .github/workflows/
│   ├── backend.yml  web.yml  android.yml
│   └── ios.yml                 # macOS runner + fastlane → TestFlight
└── docs/
    ├── PLAN.md  (bu dosya)
    ├── decisions/              # ADR: mimari karar kayıtları
    └── api.md
```

---

## 15. Geliştirme ortamı kurulumu (Windows)

- [ ] **Git** + GitHub hesabı, SSH anahtarı
- [ ] **VS Code** (eklentiler: Flutter, Dart, Python, Pylance, ESLint, Prettier, Docker, Tailwind)
- [ ] **WSL2 + Ubuntu** (backend ve Docker için önerilir)
- [ ] **Docker Desktop** (WSL2 backend)
- [ ] **Flutter SDK** (stable) → `flutter doctor` tüm Android maddeleri ✓
- [ ] **Android Studio** (SDK, emülatör) + gerçek Android telefonda USB debugging
- [ ] **Node.js LTS** + pnpm
- [ ] **Python 3.12** + `uv` veya `poetry`
- [ ] `docker compose up` ile PostgreSQL (postgis + pgvector imajı), Redis, MinIO
- [ ] DB aracı: DBeaver veya pgAdmin
- [ ] API test: Bruno / Postman veya FastAPI `/docs`
- [ ] Hesaplar: Firebase projesi, LLM API anahtarı, Sentry, (ileride) Apple Developer, Google Play Console (tek seferlik 25 USD)

---

## 16. Adım adım geliştirme planı

> Süreler tek kişi + yarı zamanlı çalışma varsayımıyla **tahminidir**. Her sprint ~2 hafta.

### FAZ 0 — Hazırlık (1–2 hafta)

- [ ] Rakip incelemesi (bkz. 3.3) ve şikâyet analizi
- [ ] 5–10 kişiyle "son yaşadığın arızayı nasıl çözdün?" görüşmesi (varsayımsal değil, gerçek davranış soruları)
- [ ] 3–5 ustayla görüşme (müşteriyi nasıl buluyor, müsaitlik güncellemeye razı mı, hangi ödeme modelini kabul eder, işin tamamlandığını nasıl doğrularız)
- [ ] Ürün adı + alan adı kontrolü
- [ ] **Ekran akışları (wireframe)** — Figma (ücretsiz): müşteri akışı, usta akışı, admin
- [ ] Pilot kategoriler kesinleştir: **Elektrik + Su tesisatı + Kombi**
- [ ] Pilot bölge: tek şehir / birkaç ilçe
- [ ] Monorepo oluştur, README, lisans, `.gitignore`, ADR-001 (tech stack kararı)
- [ ] Geliştirme ortamı kurulumu (bkz. 15)

### FAZ 1 — MVP Çekirdeği (Sprint 1–6, ~3 ay)

**Sprint 1 — Temel altyapı**
- [ ] docker-compose: Postgres+PostGIS+pgvector, Redis, MinIO
- [ ] FastAPI iskeleti, modül yapısı, config, logging, Sentry
- [ ] Alembic ilk migration: users, addresses, categories
- [ ] Auth: SMS OTP (geliştirmede sahte SMS), JWT, refresh
- [ ] Flutter iskeleti: tema, router, Riverpod, API client üretimi, giriş ekranları
- [ ] GitHub Actions: backend testleri + Flutter analyze/test + Android build
- [ ] **iOS CI hattını şimdiden kur** (Apple Developer hesabı alınınca TestFlight'a çıkacak şekilde; o zamana kadar `flutter build ios --no-codesign` ile derlenebilirlik kontrolü macOS runner'da)

**Sprint 2 — Usta tarafı temel**
- [ ] Usta başvuru, belge yükleme (S3/MinIO)
- [ ] Uzmanlık kategorileri, başlangıç fiyatları
- [ ] Hizmet bölgesi (merkez + yarıçap ile başla; poligon sonra)
- [ ] Çalışma takvimi + "Şu an müsaitim" anahtarı
- [ ] Admin (Next.js): usta onay ekranı, giriş
- [ ] Kategori ağacı seed verisi (tüm kategoriler, pilot olanlar aktif)

**Sprint 3 — AI yönlendirme v1**
- [ ] Güvenlik ön filtresi (kural tabanlı: gaz kokusu, kıvılcım, su+elektrik…)
- [ ] `LLMProvider` soyutlaması + triage prompt v1 + JSON şema doğrulama
- [ ] Takip soruları akışı (max 3–4)
- [ ] Elle hazırlanmış **300+ örneklik altın test seti** + eval scripti
- [ ] RAG v1: kategori tanımları + belirti→uzmanlık dokümanları + terim sözlüğü; pgvector + full-text hibrit arama
- [ ] Flutter: arıza anlatma ekranı (metin + fotoğraf), AI soru-cevap ekranı, kategori onayı
- [ ] Tüm AI çağrılarının loglanması (`ai_triage_results`)

**Sprint 4 — Eşleştirme ve sonuçlar**
- [ ] PostGIS filtreleri (hizmet bölgesi, mesafe)
- [ ] Ağırlıklı skor + 3 kart mantığı + açıklama üretimi
- [ ] Güven metrikleri hesaplama işi (Bayes ortalama vb.; başta boş/yeni)
- [ ] Flutter: 3 kart, liste, harita, usta profil sayfası

**Sprint 5 — Dispatch + randevu + iş takibi**
- [ ] Dispatch mekanizması (Redis zamanlayıcı, timeout, sıradakine geçiş)
- [ ] Slot listeleme + randevu + çifte rezervasyon kilidi
- [ ] İş durum makinesi (bkz. 5.5) + WebSocket ile canlı durum
- [ ] Push bildirim (FCM) + kritik durumlarda SMS
- [ ] Usta modu: gelen kutusu, kabul/ret sayacı, takvim, durum butonları

**Sprint 6 — Tamamlama, değerlendirme, şikâyet**
- [ ] Usta kapanış formu (işlem, ücret, garanti, önce/sonra fotoğraf)
- [ ] Müşteri onayı + memnuniyet anketi + çok boyutlu puan
- [ ] Ustanın müşteriyi değerlendirmesi
- [ ] Doğrulanmış iş kuralı, 72 saat otomatik kapanış
- [ ] Anlaşmazlık akışı + admin kuyruğu
- [ ] Uygulama içi mesajlaşma (talep bazlı)
- [ ] Admin: **HITL paneli v1** (düşük güvenli / değiştirilen tahminler, etiketleme)
- [ ] Hesap silme, KVKK aydınlatma metni, gizlilik politikası sayfaları

**🎯 Faz 1 çıkışı:** Android'de (ve TestFlight'ta iOS'ta) uçtan uca çalışan akış: arıza → AI → eşleşme → randevu → iş → değerlendirme.

### FAZ 2 — Farklılaştırıcılar (Sprint 7–10, ~2 ay)

- [ ] **Ev Profili**: ev, cihazlar, bakım geçmişi (platform işleri otomatik)
- [ ] Kural tabanlı **bakım hatırlatmaları** (zamanlanmış iş + push)
- [ ] AI'ya ev profili bağlamı ekleme
- [ ] **Fiyat tahmini v1** (kural/istatistik: medyan + aralık + "veri yetersiz" durumu)
- [ ] **Garanti takibi** + "Sorun tekrarladı" akışı
- [ ] **Teklif modu** (proje işleri) + teklif karşılaştırma
- [ ] Favori ustalar / tekrar çağır
- [ ] **Acil mod**
- [ ] Güven Profili sayfası (usta için gelişim önerileriyle)
- [ ] RAG bilgi tabanı yönetimi (admin), hata kodu tabloları
- [ ] Next.js public web: landing, kategori/şehir SEO sayfaları, usta profilleri, web'den talep oluşturma
- [ ] Yeni kategoriler: Klima, Beyaz eşya, Çilingir, Doğalgaz

### FAZ 3 — Yayın ve öğrenme döngüsü (Sprint 11–13, ~1,5 ay)

- [ ] Apple Developer hesabı (99 USD/yıl) + Google Play Console
- [ ] Fastlane + GitHub Actions macOS ile TestFlight otomasyonu (bkz. 10)
- [ ] Store materyalleri: ekran görüntüleri, açıklama, gizlilik etiketleri
- [ ] **Kapalı beta** (TestFlight + Play internal testing) → pilot ilçede gerçek usta ve kullanıcılar
- [ ] PostHog funnel'ları + metrik panosu (bkz. 18)
- [ ] **Öğrenme döngüsü**: dataset versiyonlama, eval otomasyonu, shadow mode, A/B anahtarları
- [ ] Prompt v2 / few-shot iyileştirme (HITL verisiyle)
- [ ] Maskelenmiş arama (numara gizleme), sesli arıza anlatımı
- [ ] Sahte yorum tespiti v1 (kural + anomali)
- [ ] Yeni kategoriler: Montaj, Cam, Marangoz, Boya, Temizlik, Nakliye, Tadilat (teklif modunda)
- [ ] **App Store + Play Store yayını**

### FAZ 4 — ML modelleri (veri biriktikçe)

- [ ] **Learning-to-rank** (LightGBM LambdaMART) — yeterli tamamlanmış iş sonrası
- [ ] **Fiyat tahmini ML** (kuantil regresyon + SHAP açıklama)
- [ ] Triage için küçük sınıflandırıcı fine-tune (LLM maliyetini düşürmek için; LLM yedekte)
- [ ] Bakım/arıza riski tahmini
- [ ] Model izleme ve drift alarmı
- [ ] Çevrim içi ödeme + makbuz (ödeme kuruluşu entegrasyonu)
- [ ] İngilizce dil desteği

### FAZ 5 — Genişleme (opsiyonel)

- [ ] Diğer şehirler
- [ ] Armut'taki diğer hizmet grupları (ders, organizasyon vb.) — talep olursa
- [ ] İş modeli devreye alma (bkz. 19)
- [ ] Swift ile native iOS özellikleri (ör. widget, Live Activities ile "usta yolda" durumu)

---

## 17. Güvenlik, KVKK ve hukuki konular

**KVKK (6698 sayılı Kanun):**
- [ ] Aydınlatma metni + açık rıza (konum, fotoğraf, pazarlama ayrı ayrı)
- [ ] Veri envanteri: hangi kişisel veri, neden, ne kadar süre
- [ ] Yurt dışına veri aktarımı (LLM API, bulut) konusu ayrıca değerlendirilmeli; LLM'e giden metinlerde **telefon/adres/isim maskeleme**
- [ ] Hesap ve veri silme talebi akışı
- [ ] Kimlik belgesi gibi hassas belgeler şifreli depolanır, erişim loglanır
- [ ] VERBİS kaydı yükümlülüğü kontrol edilecek

**Uygulama güvenliği:**
- [ ] OTP rate limit + brute force koruması
- [ ] JWT kısa ömürlü, refresh rotation
- [ ] Fotoğraflarda EXIF konum verisi silinir
- [ ] Kullanıcı tam adresi sadece randevu kabul edildikten sonra ustaya gösterilir
- [ ] Rol bazlı yetki (RBAC), admin işlemleri audit log
- [ ] OWASP Top 10 kontrol listesi
- [ ] LLM prompt injection'a karşı: kullanıcı metni sistem talimatından ayrılır, çıktı şema doğrulamasından geçer

**Hukuki / sorumluluk:**
- [ ] Kullanım koşulları: platform aracıdır, hizmeti usta verir (aracılık rolü avukatla netleştirilmeli)
- [ ] AI çıktısı "teşhis değil, yönlendirmedir" uyarısı
- [ ] Doğalgaz işleri için yetkili firma/sertifika şartı (gaz dağıtım şirketlerinin yetkilendirme kuralları araştırılacak)
- [ ] Elektrik işleri için mesleki yeterlilik belgesi şartları araştırılacak
- [ ] Mesafeli sözleşme / tüketici mevzuatı (ödeme eklendiğinde)
- [ ] Ticari elektronik ileti izni (İYS) — pazarlama SMS/e-postası için

> Bu bölüm hukuki tavsiye değildir; yayın öncesi bir avukata danışılmalı.

---

## 18. Ölçülecek metrikler

**Kullanıcı tarafı funnel**
- Talep başlatma → AI kategori kabul → eşleşme gösterildi → usta seçildi → kabul edildi → tamamlandı → onaylandı → değerlendirildi
- Uygun usta bulunamama oranı
- İlk yanıt süresi (dispatch → kabul)
- Talep → randevu süresi
- Tekrar kullanım oranı (30/90 gün)

**Usta tarafı**
- Dispatch kabul oranı, yanıt süresi
- Zamanında varış oranı
- İptal / no-show oranı
- Usta başına aylık iş

**Kalite**
- Sorun çözüldü oranı, memnuniyet ortalaması
- Şikâyet / anlaşmazlık oranı
- "Sorun tekrarladı" oranı (garanti içinde)
- Fiyat uyumu (konuşulan vs ödenen)

**AI/ML**
- Kategori doğruluğu (top-1/top-3), öneri kabul oranı
- Güvenlik tespiti recall
- Fiyat tahmini: gerçek fiyatın aralık içinde kalma oranı (coverage), MAPE
- Ranking: seçilen ustanın ilk 3'te olma oranı, NDCG

**Teknik**
- API p95 gecikme, hata oranı, LLM talep başı maliyet, uygulama çökme oranı

---

## 19. İş modeli (sonraki aşama)

İlk aşamada **para kazanma yok**; önce akışın çalıştığı kanıtlanacak. Sonra değerlendirilecek seçenekler:

| Model | Artı | Risk |
|-------|------|------|
| Usta aylık üyelik | Öngörülebilir gelir | Müşteri yokken kimse ödemez |
| Tamamlanan iş başına komisyon | Değerle orantılı | Platform dışı anlaşma |
| Talep/lead başına ücret | Basit | Dönüşmeyen talepte usta memnuniyetsizliği |
| Öne çıkarılmış profil | Ek gelir | Güven sıralamasını bozmamalı ("Sponsorlu" etiketi) |
| Platform içi ödeme + hizmet bedeli | Garanti/koruma sunar | Ödeme, iade, uyuşmazlık operasyonu |
| Ev bakım paketi (abonelik, müşteri) | Ev profiliyle uyumlu, tekrar eden gelir | Operasyon gerektirir |

**Platform dışına kaçışı azaltan şeyler:** garanti takibi, ev profili, güven profili (usta itibarını platformda biriktirir), "Sorun tekrarladı" koruması.

---

## 20. Riskler ve önlemler

| Risk | Etki | Önlem |
|------|------|-------|
| İki taraflı pazar (usta yok ↔ kullanıcı yok) | Yüksek | Tek ilçe + 3 kategoriyle başla; ustaları elle tek tek kaydet |
| Ustaların müsaitlik güncellememesi | Yüksek | Dispatch ile teyit; güncel değilse "teyit edilecek" göster |
| AI yanlış yönlendirme | Orta | Güven eşiği, kullanıcı onayı, HITL, eval |
| Tehlikeli durumda yanlış AI tavsiyesi | Çok yüksek | Kural tabanlı güvenlik filtresi + talimat vermeme kuralı |
| Sahte yorum | Orta | Sadece doğrulanmış iş yorumu, anomali tespiti |
| LLM maliyeti | Orta | Önbellek, küçük model, sonra fine-tune sınıflandırıcı |
| Kapsam şişmesi (her şeyi yapmak) | Yüksek | Faz disiplini; "Faz 1 çıkışı" bitmeden Faz 2'ye geçilmez |
| iOS build sorunları (Mac yok) | Orta | CI'ı Sprint 1'de kur, sorunları erken gör; gerekirse Mac ödünç |
| Tek kişilik geliştirme yorgunluğu | Orta | Küçük sprintler, her sprint sonunda çalışan demo |
| Rakiplerin aynı özelliği eklemesi | Orta | Farklılık tek özellik değil, bütün deneyim + veri |

---

## 21. Maliyet tahmini

| Kalem | Maliyet | Ne zaman |
|-------|---------|----------|
| Geliştirme araçları (Flutter, VS Code, Android Studio…) | Ücretsiz | Şimdi |
| GitHub + Actions | Ücretsiz katman (macOS dakikaları sınırlı) | Şimdi |
| LLM API | Kullanıma göre, geliştirmede düşük | Şimdi |
| Sunucu (VPS) | Aylık düşük (küçük VPS) | Beta |
| Alan adı | Yıllık düşük | Faz 0–2 |
| SMS | Mesaj başı | Beta |
| Google Play Console | 25 USD (tek seferlik) | Faz 3 |
| Apple Developer Program | 99 USD / yıl | Faz 3 (TestFlight'a başlarken) |
| Mac | **0** (satın alma yok) | — |

> Rakamlar güncel fiyatlarla kontrol edilmeli.

---

## 22. Açık sorular

**Karara bağlananlar:**
- [x] Ürün adı → **Hallederiz** (alt başlık: "Arızayı anlat, usta gelsin")
- [x] Pilot şehir → **Kahramanmaraş** (ilçe sonra netleşecek)
- [x] LLM → **Groq** ile başla, sonra daha iyisi değerlendirilecek
- [x] Harita → **OpenStreetMap**
- [x] Kod yeri → GitHub `hallederiz` reposu, Sibel'in bilgisayarına klonlanır

**Hâlâ açık:**
- [ ] Alan adı ve TÜRKPATENT marka kontrolü
- [ ] Repo public mi private mi? (Public → macOS CI ücretsiz ama kod açık) — Sibel karar verecek
- [ ] Arkadaşının rolü (ortak mı, usta ağı/operasyon tarafını o mu üstlenecek?)
- [ ] Müşteri ve usta tek uygulama mı (rol değişimli), iki ayrı uygulama mı? (Öneri: başta tek uygulama)
- [ ] Usta doğrulamasında hangi belgeler zorunlu olacak?
- [ ] Apple Developer hesabı ne zaman alınacak (TestFlight ile iPhone testi için)

---

## 23. İlk 7 gün yapılacaklar

| Gün | Görev |
|-----|-------|
| 1 | Armut, UstaGelsin, Hizmetgo'yu indir; bir talep akışını baştan sona dene, ekran görüntüsü al |
| 2 | Store'lardaki kötü yorumları oku, şikâyetleri kategorize et (tablo) |
| 3 | 3 arkadaş/aile ile "son arızanı nasıl çözdün?" görüşmesi; 1 ustayla konuşma |
| 4 | Windows geliştirme ortamı kurulumu (bölüm 15), `flutter doctor` ✓ |
| 5 | Monorepo + docker-compose (Postgres/PostGIS/pgvector + Redis) ayağa kalksın |
| 6 | Figma'da müşteri akışının kaba wireframe'i (8–10 ekran) |
| 7 | Altın test seti için ilk 50 arıza cümlesi + doğru kategori etiketi yaz |

---

### Ürünün özü (unutmamak için)

> Usta listesi değil. AI teşhis yardımcısı değil. Harita değil. Randevu sistemi değil.
> **Bunların birleşiminden oluşan; yaptığı her işten kontrollü biçimde veri toplayarak eşleştirmeyi, fiyat tahminini, hizmet kategorilendirmeyi ve güven modelini zamanla geliştiren bir ev hizmetleri platformu.**

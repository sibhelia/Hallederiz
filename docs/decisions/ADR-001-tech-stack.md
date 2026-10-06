# ADR-001: Teknoloji yığını

- **Durum:** Kabul edildi
- **Tarih:** 2026-10-03

## Bağlam

Hallederiz iOS, Android ve web'de çalışacak. Geliştirme Windows'ta yapılıyor ve Mac yok. Ürünün merkezinde AI (arıza yönlendirme, RAG) ve ML (sıralama, fiyat tahmini) var. Ekip küçük ve bütçe sınırlı.

## Karar

| Katman | Seçim |
|---|---|
| Mobil (iOS + Android) | Flutter + Dart |
| Web ve admin | Next.js + TypeScript |
| Backend | Python + FastAPI, modüler monolit |
| Veritabanı | PostgreSQL 16 + PostGIS + pgvector (tek DB) |
| Cache / kilit / kuyruk | Redis |
| Dosya depolama | S3 uyumlu (lokalde MinIO) |
| LLM | Groq (OpenAI uyumlu API), `LLMProvider` soyutlamasının arkasında |
| Embedding | Açık kaynak çok dilli model, backend'de lokal |
| Harita | OpenStreetMap (flutter_map + Nominatim/Photon) |
| iOS build | GitHub Actions macOS runner + Fastlane → TestFlight |

## Gerekçe

- **Flutter:** Tek kod tabanı, Windows'ta geliştirilebiliyor. Mac sadece build için gerekiyor, o da bulutta çözülüyor.
- **FastAPI:** AI/ML ile aynı dil; tipli, hızlı ve OpenAPI şemasından client üretilebiliyor.
- **Tek PostgreSQL:** Konum (PostGIS) ve vektör (pgvector) aynı veritabanında olunca birleşik sorgular kolaylaşıyor, işletilecek sistem sayısı azalıyor.
- **Modüler monolit:** Mikroservislerin operasyon yükü bu ölçekte gereksiz. Modül sınırları net tutulursa ileride ayırmak mümkün.
- **Groq:** Hızlı ve başlangıç için ücretsiz katmanı var. Soyutlama sayesinde sağlayıcı değiştirmek tek ayar.

## Sonuçlar

- iOS'a özgü sorunlar ancak CI üzerinden ve TestFlight ile görülebilir; bu yüzden iOS CI hattı erken kurulacak.
- Groq embedding sunmadığı için embedding modeli backend'de çalışacak (bellek/CPU maliyeti).

# 🎨 Tebak Warna Foto

Game multipemain untuk anak & keluarga: aplikasi memunculkan **satu warna target**, semua pemain mencari benda berwarna serupa di sekitar, lalu bergiliran **memotretnya**. Foto yang warnanya **paling mirip** dengan target memenangkan ronde ⭐.

Satu file `index.html` — tanpa server, tanpa instalasi, tanpa data yang dikirim ke mana pun (semua foto diproses di perangkat).

## ✨ Fitur

- 👨‍👩‍👧‍👦 **2–6 pemain**, nama bisa diganti, avatar hewan lucu
- 🔁 **1 / 3 / 5 ronde**, warna target tidak berulang dalam satu permainan
- 📷 Kamera belakang HP langsung terbuka (di laptop: pilih file foto)
- 👆 **Ketuk foto** untuk memilih bagian benda yang dinilai
- 📊 Skor kemiripan **0–100%** dihitung dengan rumus warna **CIEDE2000** (standar industri), dengan bobot terang-gelap diperingan agar foto dalam ruangan tetap adil
- 🤝 Hasil seri → semua pemenang dapat bintang
- 🔊 Suara pemandu berbahasa Indonesia (Web Speech API) + efek bunyi
- 🏆 Papan juara di akhir permainan

## 🚀 Cara Menjalankan

**Paling cepat:** buka `index.html` di browser HP atau laptop.

**Online via GitHub Pages:**
1. Push repo ini ke GitHub
2. Buka **Settings → Pages**
3. Source: **Deploy from a branch** → branch `main`, folder `/ (root)` → **Save**
4. Game bisa dibuka di `https://<username>.github.io/<nama-repo>/`

> ⚠️ Kamera HP butuh **HTTPS** — GitHub Pages sudah otomatis HTTPS.

```bash
git init
git add index.html README.md
git commit -m "Game Tebak Warna Foto"
git branch -M main
git remote add origin https://github.com/<username>/tebak-warna.git
git push -u origin main
```

## 🎮 Cara Main

1. Pilih jumlah pemain, isi nama, pilih jumlah ronde → **Mulai!**
2. Warna target muncul (misalnya **Kuning**) — semua pemain berburu benda kuning 🔍
3. Tekan **Sudah ketemu!**, lalu tiap pemain bergiliran **📷 Ambil Foto**
4. Ketuk bagian benda di foto bila lingkaran belum pas → **Kunci ✔**
5. Setelah semua pemain memotret, hasil ronde muncul — skor tertinggi menang ⭐
6. Bintang terbanyak di akhir permainan = **Juara Warna** 🏆

## 🧠 Cara Penilaian

1. Warna rata-rata diambil dari lingkaran kecil di titik yang diketuk
2. RGB → ruang warna **CIE Lab**
3. Jarak warna dihitung dengan **ΔE2000** (kL = 2)
4. `Kemiripan = 100 − 2 × ΔE` (minimal 0%)

| Contoh foto | Target | Skor |
|---|---|---|
| Merah pas | Merah | 100% |
| Merah tua | Merah | 89% |
| Oranye | Merah | 60% |
| Biru | Merah | 15% |

## 🛠️ Kustomisasi

Ubah daftar warna target di array `TARGETS` dalam `index.html`:

```js
{ name: 'Tosca', hex: '#1ABC9C' },
```

## 👩‍👧 Tips untuk Orang Tua

- Ajak anak **menyebut nama warnanya** keras-keras sebelum mencari
- Main di ruangan yang **terang** — cahaya redup membuat warna foto lebih gelap
- Untuk balita, cukup 1 ronde dan bantu memotret bersama

## 📄 Lisensi

MIT

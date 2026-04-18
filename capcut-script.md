# CapCut-Skript – Reel „Wärmepumpen von FriStD-Bau" (25 s)

**Projektdatei:** `FriStD-Bau_WP_Reel_v1.ccp`
**Canvas:** 1080 × 1920 (9:16) · 30 fps · BT.709
**Safe-Area:** 90 px Rand · 250 px top/bottom für IG-UI
**Audio-Ziel:** −14 LUFS · True-Peak ≤ −1 dBTP

---

## Globale Assets

Ordnerstruktur im CapCut-Projekt:

```
/assets
  /color        ← black.png (#0A0A0A), offwhite.png (#F5F4EE), yellow.png (#FFE500)
  /logo         ← fristd-bau-logo-white.svg, fristd-bau-logo-black.svg
  /pills        ← pill-waermepumpe.svg, pill-heizkosten-senken.svg, ... (siehe /svg-overlays)
  /cards        ← card-01.svg (Beratung), card-02.svg (Meisterbetrieb, dark), card-03.svg (Monitoring)
  /monitoring   ← card-jaz.svg, chart-24h.png
  /mockup       ← phone-mockup.png (transparent, 1180×2420)
  /grid         ← grid-loop.mov (2 s Loop, subtiles Drift)
/audio
  main.mp3      ← gekaufter Beat oder IG-Library-Snippet (120 BPM)
  sfx/kick.wav
  sfx/pop.wav
  sfx/typewriter.wav
  vo.wav        ← Voice-Over (optional, trocken, 48 kHz)
```

---

## Timeline – Cut-Liste

| # | In     | Out    | Dauer | Track  | Element                                                                          | Animation                                       |
| - | ------ | ------ | ----- | ------ | -------------------------------------------------------------------------------- | ----------------------------------------------- |
| 1 | 00:00  | 00:02  | 2.0 s | V1     | `bg_black` + `grid-loop.mov` (Opacity 15 %)                                      | hold                                            |
| 2 | 00:00  | 00:02  |       | V2     | Text `„Deine Heizkosten letzten Winter?"` · Inter Bold 78 pt · weiß              | Fade-in 6f · out 10f                            |
| 3 | 00:00.5| 00:01.5|       | V3     | Text `+83 %` · Inter Black 220 pt · weiß, zentriert                              | Scale 0→1 (EaseOutBack 8f), Flicker 2 f         |
| 4 | 00:01.5| 00:02  | 0.5 s | V4     | Shape yellow rect 1080×40 px, x: −1080→1080                                      | X-Slide (EaseInOut 15 f)                        |
| 5 | 00:02  | 00:05  | 3.0 s | V1     | `bg_black`                                                                       | hold                                            |
| 6 | 00:02  | 00:05  |       | V2     | Headline-Group (4 Zeilen, Typo wie Hero)                                         | je Zeile Staggered-Fade-Up 6 f, 5 f Versatz     |
|   |        |        |       |        | · „Wärme, die"  (weiß, 120 pt)                                                    |                                                 |
|   |        |        |       |        | · **„rechnet."** (gelb `#FFE500`, 160 pt)                                         | Pop-Scale 0,8→1 (Overshoot)                     |
|   |        |        |       |        | · „Heizkosten, die" (weiß, 120 pt)                                                |                                                 |
|   |        |        |       |        | · **„bleiben."** (weiß, 160 pt) + gelber Underline-Stroke                         | Stroke-Draw links→rechts 10 f                   |
| 7 | 00:02.3|        |       | A1     | `kick.wav` auf Beat-Drop `rechnet`                                                |                                                 |
| 8 | 00:05  | 00:08  | 3.0 s | V1     | `bg_offwhite`                                                                    | Cut                                             |
| 9 | 00:05  | 00:05.4|       | V2     | Micro-Label `— 01 · WAS WIR LIEFERN` · Mono 32 pt · grau                         | Fade-in 6 f                                     |
| 10| 00:05.2| 00:06.2|       | V3     | H2 `„Raus aus fossil. Rein in Effizienz."` · 96 pt · schwarz                     | Slide-up 10 f                                   |
| 11| 00:06.2| 00:08  | 1.8 s | V4–V11 | 8 × Pill-SVGs (`/assets/pills/…`)                                                | Staggered Scale 0→1, 3 f Versatz, `pop.wav`     |
|   |        |        |       |        | Reihenfolge: Wärmepumpe · Heizkosten senken · BEG & KfW Förderung · Monitoring · Umstellung auf Effizienz · Sanierung · Mehrfamilienhaus · Hamburg & Umland |                                                 |
|12 | 00:08  | 00:14  | 6.0 s | V1     | `bg_offwhite`                                                                    | Cut                                             |
|13 | 00:08  | 00:08.4|       | V2     | Micro-Label `— 02 · SO GEHEN WIR VOR`                                             | Fade-in                                         |
|14 | 00:08.2| 00:09.2|       | V3     | H2 `„Von der Beratung zur laufenden Anlage."`                                    | Slide-up                                        |
|15 | 00:09.2| 00:11  | 1.8 s | V4     | `card-01.svg` (weiß) – „Beratung & Heizlastberechnung · 0 €"                     | Slide-from-bottom 12 f                          |
|16 | 00:11  | 00:12.5| 1.5 s | V5     | `card-02.svg` (schwarz + gelbes Icon) – „Lieferung, Einbau & Inbetriebnahme"     | Slide-from-bottom 12 f, Shadow-Bloom            |
|17 | 00:12.5| 00:14  | 1.5 s | V6     | `card-03.svg` (weiß) – „Monitoring & Betriebsführung · Mit konzept-54"           | Slide-from-bottom 12 f                          |
|18 | 00:09.2| 00:14  |       | A2     | `pop.wav` auf Card 01/02/03-Einstieg                                             |                                                 |
|19 | 00:14  | 00:18  | 4.0 s | V1     | `bg_black` + `grid-loop.mov` (8 %)                                               | Cut                                             |
|20 | 00:14  | 00:18  |       | V2     | Monitoring-Card (dark, wie Website-Hero-Sidebar)                                  | Slide-from-right 18 f (EaseOut)                 |
|21 | 00:14.5| 00:15  |       | V3     | Live-Badge `● LIVE · WP-Anlage · Hamburg Niendorf`                                | Dot pulsiert (loop 1 s)                         |
|22 | 00:15  | 00:16  |       | V4     | Kennzahl `JAZ 4.8` · Counter 0.0→4.8                                              | Number-Ticker 1 s, gelb                         |
|23 | 00:16  | 00:16.5|       | V5     | Kennzahlen `Vorlauf 37 °C` · `Strom → Wärme 1 : 4.6`                              | Fade-in 6 f                                     |
|24 | 00:16.5| 00:17.5|       | V6     | `chart-24h.png` · Stroke-Draw links→rechts                                        | Mask-Reveal 1 s                                 |
|25 | 00:17.5| 00:18  |       | V7     | Fußzeile grün `▲ Effizienz +12 % ggü. Woche`                                      | Fade-in 6 f                                     |
|26 | 00:14  | 00:18  |       | V8     | Unterzeile unter Card: „Monitoring inklusive."                                    | Fade-in bei 00:15                               |
|27 | 00:18  | 00:20  | 2.0 s | V1     | `bg_offwhite`                                                                    | Cut                                             |
|28 | 00:18  | 00:20  |       | V2–V4  | 3 Logos in Reihe: Stiebel Eltron · tecalor · konzept-54                          | Fade-in staggered, 5 f Versatz                  |
|29 | 00:18.5| 00:20  |       | V5     | Text „Keine Schnittstellenverluste. Kein Zuständigkeits-Ping-Pong."               | Fade-in 8 f                                     |
|30 | 00:20  | 00:23  | 3.0 s | V1     | `bg_black` + `grid-loop.mov` (8 %)                                               | Cut                                             |
|31 | 00:20  | 00:23  |       | V2     | Handy-Mockup zentriert, scrollt Hero → Pills → Cards                              | Inner-Scroll-Animation 3 s                      |
|32 | 00:21  | 00:23  |       | V3     | Text oben `NEU ONLINE` · gelb                                                     | Fade-in 6 f                                     |
|33 | 00:22  | 00:23  |       | V4     | URL `waermepumpe.fristd-bau.com` tippt sich                                       | Typewriter-Effekt 1 s + `typewriter.wav`        |
|34 | 00:23  | 00:25  | 2.0 s | V1     | `bg_black` + `grid-loop.mov`                                                     | Cut                                             |
|35 | 00:23  | 00:25  |       | V2     | H1 „Kostenlose Erstberatung." · 110 pt · weiß                                    | Fade-up 8 f                                     |
|36 | 00:23.5| 00:25  |       | V3     | Button gelb · `Erstberatung →`                                                    | Scale-Pop 0,9→1 (8 f)                           |
|37 | 00:24  | 00:25  |       | V4     | Outline-Button · `Förderscheck öffnen`                                            | Fade-in 6 f                                     |
|38 | 00:23  | 00:25  |       | V5     | Telefon-Ribbon unten `📞 040 · 386 745 65`                                        | Fade-in 6 f                                     |
|39 | 00:23  | 00:25  |       | V6     | Logo oben links                                                                  | hold                                            |
|40 | 00:00  | 00:25  |       | A0     | `main.mp3` · Beat-Markers @ 2 s (drop 1) · 5 s (drop 2) · 11 s · 20 s · 23 s     | Fade-in 10 f · Fade-out 15 f bei 24.5           |
|41 | 00:00  | 00:25  |       | A1     | SFX-Layer (siehe Zeilen 7, 11, 18, 33)                                           |                                                 |
|42 | 00:00  | 00:25  |       | A2     | Voice-Over (optional): `„Wärme, die rechnet. Heizkosten, die bleiben."` @ 02.1s · `„Raus aus fossil. Rein in Effizienz."` @ 05.3s · `„Jetzt kostenlos beraten lassen."` @ 23.3s | EQ-HP 80 Hz, Comp 3:1 |

---

## Globale Untertitel-Spur (hart einbrennen)

Font: Inter Bold 46 pt · Weiß auf Schwarz, Schwarz auf Hell · gelbe Keywords.
Position: 240 px über unterem Rand.
Zeilen-Pro-Block max 2, max 32 Zeichen.

| Start | Text                                                     |
| ----- | -------------------------------------------------------- |
| 00:00 | Heizkosten letzten Winter? **+83 %**                     |
| 00:02 | Wärme, die **rechnet**.                                  |
| 00:03 | Heizkosten, die ~~bleiben~~.                             |
| 00:05 | Raus aus fossil. Rein in **Effizienz**.                  |
| 00:09 | Ein Prozess. Eine Hand.                                  |
| 00:11 | Meisterbetrieb · Stiebel Eltron Fachpartner              |
| 00:13 | Monitoring mit **konzept-54**                            |
| 00:14 | Live-Anlage Hamburg Niendorf: **JAZ 4.8**                |
| 00:18 | Zertifiziert. Transparent. Regional.                     |
| 00:20 | **NEU ONLINE** – waermepumpe.fristd-bau.com              |
| 00:23 | Jetzt **kostenlose Erstberatung** anfordern.             |

---

## Export-Einstellungen

- Container: MP4 (H.264 high profile)
- Bitrate: 10–12 Mbit/s (CBR)
- Audio: AAC-LC 192 kbps, 48 kHz
- Colorspace: Rec.709
- Dateiname: `fristd-bau_reel_waermepumpe_25s_v1.mp4`

## QA-Checkliste

- [ ] Untertitel korrekt lesbar bei 50 % IG-Zoom
- [ ] Logo durchgehend sichtbar
- [ ] Keine Texte in Safe-Area-Verletzung (oben 250 px / unten 250 px)
- [ ] Kontrast ≥ 4.5:1 auf allen Text-Blöcken
- [ ] URL exakt `waermepumpe.fristd-bau.com` (kein WWW, kein HTTPS-Prefix nötig)
- [ ] Lautheit −14 LUFS, TP ≤ −1
- [ ] Thumbnail (Cover) generieren aus Szene 2 (Claim)

# SVG-Overlays – Reel Assets

Alle Overlays sind **vektoriell**, farbneutral skalierbar und folgen dem
Corporate Design von `waermepumpe.fristd-bau.com`.

**Farben (Master):**
- Schwarz `#0A0A0A`
- Off-White `#F5F4EE`
- Signalgelb `#FFE500`
- Weiß `#FFFFFF`
- Sekundärgrau `#8A887E`
- Status-Grün `#22C55E`

**Schriften:**
- Headlines: **Inter** (900 / 800), alternativ Söhne Black, Söhne Halbfett
- Meta / Mono: **JetBrains Mono** 500, letter-spacing 2–3
- Body: **Inter** 400/600

> Wenn Inter nicht verfügbar ist, nutzen die SVGs als Fallback Helvetica Neue
> → Arial. Für Produktionsrender bitte Inter lokal einbinden oder Texte in
> Pfade konvertieren (`Edit → Convert to Path` in Figma / Illustrator).

## Dateien

| Datei                              | Zweck                                                  | Empfohlene Szene |
| ---------------------------------- | ------------------------------------------------------ | ---------------- |
| `pill-waermepumpe.svg`             | Pill schwarz – "Wärmepumpe"                            | Szene 3          |
| `pill-heizkosten-senken.svg`       | Pill gelb – "Heizkosten senken"                        | Szene 3          |
| `pill-beg-kfw-foerderung.svg`      | Pill outline – "BEG & KfW Förderung"                   | Szene 3          |
| `pill-monitoring.svg`              | Pill schwarz – "Monitoring"                            | Szene 3          |
| `pill-umstellung-auf-effizienz.svg`| Pill gelb – "Umstellung auf Effizienz"                 | Szene 3          |
| `pill-sanierung.svg`               | Pill outline – "Sanierung"                             | Szene 3          |
| `pill-mehrfamilienhaus.svg`        | Pill outline – "Mehrfamilienhaus"                      | Szene 3          |
| `pill-hamburg-und-umland.svg`      | Pill outline – "Hamburg & Umland"                      | Szene 3          |
| `card-01-beratung.svg`             | Prozess-Schritt 01 (Weiß)                              | Szene 4          |
| `card-02-lieferung-einbau.svg`     | Prozess-Schritt 02 (Schwarz + gelbes Icon)             | Szene 4          |
| `card-03-monitoring.svg`           | Prozess-Schritt 03 (Weiß)                              | Szene 4          |
| `monitoring-card.svg`              | Live-Monitoring-Card mit JAZ 4.8 · 37 °C · 1 : 4.6     | Szene 5          |
| `hero-claim.svg`                   | Hero-Headline "Wärme, die rechnet. …"                  | Szene 2          |
| `cta-frame.svg`                    | Vollflächiger 9:16-CTA-Frame                           | Szene 8          |

## Workflow (CapCut / After Effects)

1. SVG importieren (in CapCut zunächst als PNG via `Export @2x`).
2. Für animierte Pills in AE: SVG → Shape-Layer konvertieren, Scale 0→100 %
   mit EaseOutBack (Overshoot 20).
3. Zähler (JAZ 4.8) in AE mit Slider-Control + Expression
   `Math.round(value*10)/10`.
4. Alle Texte vor Export in Pfade wandeln, damit IG-Render identisch bleibt.

## Platzhalter / ToDo

- Offizielles FriStD-Bau-Logo als `logo-white.svg` und `logo-black.svg`
  ablegen (aktuell nur Text-Lockup in `cta-frame.svg`).
- Partner-Logos (Stiebel Eltron, tecalor, konzept-54) bitte vom Kunden liefern.

"""Render the 15s Instagram reel as an MP4.

Generates one PNG per scene (1080x1920), then ffmpeg concatenates them with
fade transitions and a 15s silent audio track. Fonts fall back to DejaVu Sans.
"""

import os
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).parent
OUT = ROOT / "build"
OUT.mkdir(exist_ok=True)

W, H = 1080, 1920
BLACK = "#0A0A0A"
OFFWHITE = "#F5F4EE"
YELLOW = "#FFE500"
WHITE = "#FFFFFF"
GREY = "#8A887E"
DARK_GREY = "#3A3A37"
GREEN = "#22C55E"
CARD_BG = "#0F0F0E"
CARD_LINE = "#22221F"
CARD_INNER = "#161614"

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def f(size, mono=False, reg=False):
    path = FONT_MONO if mono else (FONT_REG if reg else FONT_BOLD)
    return ImageFont.truetype(path, size)


def draw_grid(draw, color="#161614", step=180):
    for y in range(0, H, step):
        draw.line([(0, y), (W, y)], fill=color, width=1)
    for x in range(0, W, step):
        draw.line([(x, 0), (x, H)], fill=color, width=1)


def centered_text(draw, xy, text, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text((xy[0] - tw // 2, xy[1] - th // 2), text, font=font, fill=fill)


def pill(draw, x, y, text, font, fill_bg, fill_text, stroke=None, pad_x=50, pad_y=22):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    w = tw + pad_x * 2
    h = th + pad_y * 2
    draw.rounded_rectangle([(x, y), (x + w, y + h)], radius=h // 2, fill=fill_bg,
                           outline=stroke, width=3 if stroke else 0)
    draw.text((x + pad_x, y + pad_y - 4), text, font=font, fill=fill_text)
    return w, h


# ---------- Scenes ----------

def scene_hook():
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    draw_grid(d)
    centered_text(d, (W // 2, 780), "Deine Heizkosten", f(68), WHITE)
    centered_text(d, (W // 2, 870), "letzten Winter?", f(68), WHITE)
    centered_text(d, (W // 2, 1080), "+83 %", f(280), WHITE)
    # yellow strike bar across +83%
    d.rectangle([(160, 1075), (W - 160, 1115)], fill=YELLOW)
    centered_text(d, (W // 2, 1280), "Zeit für den Wechsel.", f(44, reg=True), GREY)
    img.save(OUT / "01_hook.png")


def scene_claim():
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    draw_grid(d)
    d.text((80, 520), "Wärme, die", font=f(120), fill=WHITE)
    d.text((80, 670), "rechnet.", font=f(170), fill=YELLOW)
    d.text((80, 900), "Heizkosten,", font=f(112), fill=WHITE)
    d.text((80, 1030), "die", font=f(112), fill=WHITE)
    d.text((80, 1180), "bleiben.", font=f(170), fill=WHITE)
    # yellow strike-through on "bleiben."
    d.rectangle([(80, 1290), (720, 1310)], fill=YELLOW)
    d.text((80, 1500), "waermepumpe.fristd-bau.com", font=f(34, mono=True), fill=GREY)
    img.save(OUT / "02_claim.png")


def scene_pills():
    img = Image.new("RGB", (W, H), OFFWHITE)
    d = ImageDraw.Draw(img)
    margin = 60
    max_width = W - 2 * margin
    # Micro label
    d.text((margin, 260), "— 01 · WAS WIR LIEFERN", font=f(28, mono=True), fill=GREY)
    # Headline
    d.text((margin, 340), "Raus aus fossil.", font=f(92), fill=BLACK)
    d.text((margin, 460), "Rein in Effizienz.", font=f(92), fill=BLACK)

    pf = f(38)
    gap = 16
    # Word, bg, fg, stroke
    items = [
        ("Wärmepumpe", BLACK, WHITE, None),
        ("Heizkosten senken", YELLOW, BLACK, BLACK),
        ("BEG & KfW Förderung", OFFWHITE, BLACK, BLACK),
        ("Monitoring", BLACK, WHITE, None),
        ("Umstellung auf Effizienz", YELLOW, BLACK, BLACK),
        ("Sanierung", OFFWHITE, BLACK, BLACK),
        ("Mehrfamilienhaus", OFFWHITE, BLACK, BLACK),
        ("Hamburg & Umland", OFFWHITE, BLACK, BLACK),
    ]
    # measure widths, wrap rows to max_width
    measured = []
    for text, bg, fg, stroke in items:
        bbox = d.textbbox((0, 0), text, font=pf)
        tw = bbox[2] - bbox[0]
        w = tw + 2 * 42  # pad_x
        measured.append((text, bg, fg, stroke, w))

    rows = []
    cur = []
    cur_w = 0
    for item in measured:
        iw = item[4]
        if cur and cur_w + iw + gap > max_width:
            rows.append(cur)
            cur = [item]
            cur_w = iw
        else:
            if cur:
                cur_w += gap
            cur.append(item)
            cur_w += iw
    if cur:
        rows.append(cur)

    y = 680
    for row in rows:
        x = margin
        for text, bg, fg, stroke, _ in row:
            rw, rh = pill(d, x, y, text, pf, bg, fg, stroke=stroke, pad_x=42, pad_y=20)
            x += rw + gap
        y += 120
    img.save(OUT / "03_pills.png")


def scene_live_card():
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    draw_grid(d)
    d.text((80, 180), "— LIVE-ANLAGE", font=f(28, mono=True), fill=GREY)
    d.text((80, 260), "Monitoring", font=f(110), fill=WHITE)
    d.text((80, 380), "inklusive.", font=f(110), fill=YELLOW)

    # Card
    cx, cy, cw, ch = 80, 620, W - 160, 1100
    d.rounded_rectangle([(cx, cy), (cx + cw, cy + ch)], radius=20, fill=CARD_BG,
                        outline=CARD_LINE, width=2)
    d.text((cx + 40, cy + 36), "LIVE · MONITORING-DEMO", font=f(24, mono=True), fill=GREY)
    d.text((cx + 40, cy + 90), "WP-Anlage · Hamburg Niendorf", font=f(42), fill=WHITE)
    # online
    d.ellipse([(cx + cw - 200, cy + 52), (cx + cw - 180, cy + 72)], fill=GREEN)
    d.text((cx + cw - 170, cy + 46), "ONLINE", font=f(24, mono=True), fill=GREEN)

    # KPI tiles
    tile_y = cy + 190
    th = 200
    tiles = [
        ("JAZ", "4.8", WHITE, 86),
        ("VORLAUF", "37 °C", WHITE, 78),
        ("STROM → WÄRME", "1 : 4.6", YELLOW, 70),
    ]
    tw = (cw - 40 * 2 - 20 * 2) // 3
    for i, (lbl, val, col, fs) in enumerate(tiles):
        tx = cx + 40 + i * (tw + 20)
        d.rounded_rectangle([(tx, tile_y), (tx + tw, tile_y + th)], radius=12,
                            fill=CARD_INNER, outline=CARD_LINE, width=1)
        d.text((tx + 24, tile_y + 24), lbl, font=f(22, mono=True), fill=GREY)
        d.text((tx + 24, tile_y + 80), val, font=f(fs), fill=col)

    # Chart area
    chart_y = tile_y + th + 30
    chart_h = 420
    d.rounded_rectangle([(cx + 40, chart_y), (cx + cw - 40, chart_y + chart_h)],
                        radius=12, fill=CARD_INNER, outline=CARD_LINE, width=1)
    d.text((cx + 60, chart_y + 26), "WÄRMEABGABE · 24 H · KWH",
           font=f(22, mono=True), fill=GREY)
    # polyline chart
    pts_x = [cx + 60 + i * ((cw - 140) / 15) for i in range(16)]
    pts_y_base = chart_y + chart_h - 60
    heights = [80, 110, 90, 130, 125, 160, 175, 150, 190, 220, 200, 250, 230, 280, 270, 300]
    points = [(pts_x[i], pts_y_base - heights[i]) for i in range(16)]
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill=YELLOW, width=4)
    # peak tag
    d.rounded_rectangle([(cx + cw - 260, chart_y + 30), (cx + cw - 70, chart_y + 72)],
                        radius=21, fill=YELLOW)
    d.text((cx + cw - 240, chart_y + 38), "Peak 8.5 kWh", font=f(22), fill=BLACK)

    # footer
    d.text((cx + 40, cy + ch - 50), "LETZTE SYNC: GERADE EBEN",
           font=f(20, mono=True), fill=GREY)
    d.text((cx + cw - 480, cy + ch - 50), "▲ EFFIZIENZ +12 % GGÜ. WOCHE",
           font=f(20, mono=True), fill=GREEN)

    img.save(OUT / "04_live.png")


def scene_partners():
    img = Image.new("RGB", (W, H), OFFWHITE)
    d = ImageDraw.Draw(img)
    d.text((80, 420), "— 02 · PARTNER", font=f(28, mono=True), fill=GREY)
    d.text((80, 500), "Alles aus", font=f(110), fill=BLACK)
    d.text((80, 640), "einer Hand.", font=f(110), fill=BLACK)

    partners = [
        ("STIEBEL ELTRON", "Fachpartner"),
        ("tecalor", "zertifiziert"),
        ("konzept-54", "Monitoring & Betrieb"),
    ]
    y = 960
    for name, role in partners:
        d.rounded_rectangle([(80, y), (W - 80, y + 140)], radius=14, fill=WHITE,
                            outline="#E5E3DB", width=2)
        d.text((120, y + 30), name, font=f(52), fill=BLACK)
        d.text((120, y + 90), role, font=f(30, reg=True), fill=DARK_GREY)
        y += 170

    d.text((80, 1580), "Keine Schnittstellenverluste.", font=f(38, reg=True), fill=DARK_GREY)
    d.text((80, 1630), "Kein Zuständigkeits-Ping-Pong.", font=f(38, reg=True), fill=DARK_GREY)
    img.save(OUT / "05_partners.png")


def scene_cta():
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img)
    draw_grid(d)
    # logo
    d.text((80, 120), "FriStD-Bau", font=f(60), fill=WHITE)
    d.text((80, 190), "ZIMMEREI & BAUFIRMA", font=f(18, mono=True), fill=GREY)

    centered_text(d, (W // 2, 800), "Kostenlose", f(120), WHITE)
    centered_text(d, (W // 2, 950), "Erstberatung.", f(120), WHITE)

    # yellow button
    by, bh = 1120, 140
    d.rounded_rectangle([(180, by), (W - 180, by + bh)], radius=70, fill=YELLOW)
    centered_text(d, (W // 2, by + bh // 2), "Erstberatung →", f(56), BLACK)
    # outline button
    by2 = by + 180
    d.rounded_rectangle([(180, by2), (W - 180, by2 + bh)], radius=70, outline=WHITE, width=3)
    centered_text(d, (W // 2, by2 + bh // 2), "Förderscheck öffnen", f(48), WHITE)

    centered_text(d, (W // 2, 1620), "waermepumpe.fristd-bau.com", f(40, mono=True), GREY)
    # phone ribbon
    d.rectangle([(0, 1780), (W, 1920)], fill=YELLOW)
    centered_text(d, (W // 2, 1850), "040 · 386 745 65", f(64), BLACK)
    img.save(OUT / "06_cta.png")


SCENES = [
    ("01_hook.png", 2.0, scene_hook),
    ("02_claim.png", 3.0, scene_claim),
    ("03_pills.png", 2.0, scene_pills),
    ("04_live.png", 4.0, scene_live_card),
    ("05_partners.png", 2.0, scene_partners),
    ("06_cta.png", 2.0, scene_cta),
]


def render_all():
    for _, _, fn in SCENES:
        fn()
    print("All scene PNGs rendered to", OUT)


def build_video():
    # Per scene: render to MP4 at 30fps, correct duration
    clips = []
    for i, (png, dur, _) in enumerate(SCENES):
        out = OUT / f"clip_{i:02d}.mp4"
        cmd = [
            "ffmpeg", "-y", "-loop", "1", "-framerate", "30",
            "-t", f"{dur}", "-i", str(OUT / png),
            "-vf", "scale=1080:1920,format=yuv420p",
            "-c:v", "libx264", "-preset", "medium", "-crf", "20",
            "-movflags", "+faststart",
            str(out),
        ]
        subprocess.run(cmd, check=True, capture_output=True)
        clips.append(out)

    concat_list = OUT / "concat.txt"
    with concat_list.open("w") as fh:
        for c in clips:
            fh.write(f"file '{c.name}'\n")

    silent = OUT / "silent.aac"
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
        "-t", "15", "-c:a", "aac", "-b:a", "192k", str(silent),
    ], check=True, capture_output=True)

    video_only = OUT / "video_only.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(concat_list), "-c", "copy", str(video_only),
    ], check=True, capture_output=True, cwd=OUT)

    final = ROOT / "fristd-bau_reel_15s_v1.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-i", str(video_only), "-i", str(silent),
        "-c:v", "copy", "-c:a", "aac", "-shortest",
        str(final),
    ], check=True, capture_output=True)
    print("Final video →", final)


if __name__ == "__main__":
    render_all()
    build_video()

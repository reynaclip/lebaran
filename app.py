import streamlit as st
import random

st.set_page_config(
    page_title="Idul Fitri 1447 H ✨ Reyna",
    page_icon="🌙",
    layout="centered",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Nunito:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }

.stApp {
    background-color: #fdf6ee;
    background-image:
        radial-gradient(ellipse 70% 50% at 10% 0%, rgba(255,214,170,0.45) 0%, transparent 55%),
        radial-gradient(ellipse 55% 45% at 90% 100%, rgba(198,231,210,0.4) 0%, transparent 55%),
        radial-gradient(ellipse 40% 35% at 80% 20%, rgba(247,196,196,0.25) 0%, transparent 50%);
    min-height: 100vh;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 4rem; max-width: 700px; }

/* ── Floating confetti dots ── */
.confetti-wrap { position: relative; height: 0; overflow: visible; pointer-events: none; }
.dot {
    position: absolute;
    border-radius: 50%;
    animation: confetti-fall linear infinite;
    opacity: 0;
}
@keyframes confetti-fall {
    0%   { opacity: 0; transform: translateY(-20px) rotate(0deg); }
    10%  { opacity: 0.7; }
    90%  { opacity: 0.5; }
    100% { opacity: 0; transform: translateY(120px) rotate(360deg); }
}

/* ── Top badge ── */
.top-badge {
    display: flex; align-items: center; justify-content: center; gap: 0.5rem;
    margin-bottom: 1.2rem;
}
.badge-pill {
    background: #fff8f0;
    border: 1.5px solid #f0c8a0;
    border-radius: 50px;
    padding: 0.4rem 1.3rem;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #b87840;
}

/* ── Moon hero ── */
.moon-hero {
    text-align: center;
    padding: 0.5rem 0 1rem;
    position: relative;
}
.moon-big {
    font-size: 5rem;
    display: block;
    margin: 0 auto 0.6rem;
    animation: moon-sway 5s ease-in-out infinite;
    filter: drop-shadow(0 4px 18px rgba(255,180,80,0.35));
    line-height: 1;
}
@keyframes moon-sway {
    0%, 100% { transform: rotate(-6deg) translateY(0px); }
    50%       { transform: rotate(6deg) translateY(-10px); }
}
.hero-title {
    font-family: 'Lora', serif;
    font-size: clamp(2.2rem, 7vw, 3.6rem);
    font-weight: 700;
    line-height: 1.1;
    color: #3d2a1a;
    margin: 0 0 0.3rem;
}
.hero-title .accent { color: #c8703a; }
.hero-subtitle {
    font-family: 'Lora', serif;
    font-style: italic;
    font-size: 1.05rem;
    color: #a06040;
    letter-spacing: 0.04em;
    margin-bottom: 0;
}

/* ── Star strip ── */
.star-strip {
    text-align: center;
    font-size: 0.9rem;
    letter-spacing: 0.6rem;
    color: #d4a060;
    margin: 1rem 0 1.2rem;
    opacity: 0.7;
}

/* ── Ticker ── */
.ticker-outer {
    background: linear-gradient(135deg, #fff5e8, #fff0f5);
    border: 1.5px solid #f0d0b0;
    border-radius: 50px;
    overflow: hidden;
    margin-bottom: 1.8rem;
    padding: 0.55rem 0;
    box-shadow: 0 2px 12px rgba(200,120,60,0.08);
}
.ticker-inner { display: flex; animation: scroll-left 22s linear infinite; white-space: nowrap; }
.ticker-item { padding: 0 2.2rem; font-size: 0.8rem; font-weight: 600; color: #b06030; }
@keyframes scroll-left { 0%{transform:translateX(0);} 100%{transform:translateX(-50%);} }

/* ── Lebaran emoji grid ── */
.emoji-strip {
    display: flex; justify-content: center; gap: 0.5rem;
    flex-wrap: wrap; margin: 0 0 1.8rem;
}
.emoji-card {
    background: white;
    border: 1.5px solid #f0d8c0;
    border-radius: 16px;
    padding: 0.6rem 0.9rem;
    text-align: center;
    box-shadow: 0 2px 8px rgba(200,130,60,0.08);
    animation: card-bob ease-in-out infinite alternate;
    cursor: default;
    transition: transform 0.2s;
}
.emoji-card:hover { transform: scale(1.08) translateY(-4px) !important; }
.emoji-card .ec-icon { font-size: 1.6rem; display: block; line-height: 1.2; }
.emoji-card .ec-name { font-size: 0.68rem; font-weight: 600; color: #a07050; margin-top: 0.2rem; letter-spacing: 0.03em; }
@keyframes card-bob { 0%{transform:translateY(0) rotate(-2deg);} 100%{transform:translateY(-6px) rotate(2deg);} }

/* ── Info mosaic ── */
.mosaic { display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem; margin-bottom: 1.5rem; }
.mosaic-card {
    border-radius: 18px; padding: 1.1rem 1.2rem; text-align: center;
    border: 1.5px solid transparent;
}
.mosaic-card.rose   { background: #fff0f3; border-color: #f5c8d0; }
.mosaic-card.peach  { background: #fff5ec; border-color: #f5d8b8; }
.mosaic-card.sage   { background: #f0f8f2; border-color: #b8dfc4; }
.mosaic-card.lavender { background: #f3f0ff; border-color: #d0c8f0; }
.mosaic-card .mc-icon { font-size: 1.6rem; display: block; margin-bottom: 0.4rem; }
.mosaic-card .mc-lbl { font-size: 0.68rem; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 0.25rem; }
.mosaic-card.rose   .mc-lbl { color: #c06080; }
.mosaic-card.peach  .mc-lbl { color: #b07040; }
.mosaic-card.sage   .mc-lbl { color: #508060; }
.mosaic-card.lavender .mc-lbl { color: #7060b0; }
.mosaic-card .mc-val { font-family: 'Lora', serif; font-size: 0.95rem; font-weight: 600; color: #3d2a1a; }

/* ── Main message card ── */
.msg-card {
    background: linear-gradient(145deg, #fffaf4, #fff6ef);
    border: 1.5px solid #e8c8a0;
    border-radius: 24px;
    padding: 2.4rem 2.8rem;
    margin-bottom: 1.5rem;
    position: relative;
    box-shadow: 0 4px 28px rgba(200,130,60,0.1), 0 1px 4px rgba(200,130,60,0.06);
    overflow: hidden;
}
.msg-card::before {
    content: '🌙';
    position: absolute; font-size: 10rem;
    top: -2.5rem; right: -2.5rem;
    opacity: 0.04; line-height: 1; pointer-events: none;
}
.msg-card::after {
    content: '';
    position: absolute; inset: 0;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(255,200,150,0.06) 0%, transparent 50%);
    pointer-events: none;
}
.msg-headline {
    font-family: 'Lora', serif;
    font-size: 1.35rem; font-weight: 700;
    color: #8b4a20; margin-bottom: 1.1rem; line-height: 1.35;
}
.msg-body { font-size: 0.94rem; font-weight: 400; line-height: 1.95; color: #5a3820; }
.msg-body p { margin-bottom: 0.9rem; }
.msg-body p:last-child { margin-bottom: 0; }
.msg-body strong { color: #b85a20; font-weight: 700; }

/* ── Signature ── */
.sig {
    display: flex; align-items: center; gap: 0.9rem;
    margin-top: 1.5rem; padding-top: 1.2rem;
    border-top: 1.5px dashed #e8c8a0;
}
.sig-ava {
    width: 44px; height: 44px; border-radius: 50%;
    background: linear-gradient(135deg, #f0b878, #e08040);
    border: 2px solid #f8d8b0;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Lora', serif; font-size: 1.1rem; font-weight: 700;
    color: #fff; flex-shrink: 0;
    box-shadow: 0 2px 8px rgba(200,100,40,0.25);
}
.sig-words { font-family: 'Lora', serif; font-style: italic; font-size: 0.93rem; color: #a06030; }

/* ── Mood selector ── */
.mood-label {
    text-align: center; font-size: 0.88rem; font-weight: 600;
    color: #a07050; margin: 0.5rem 0 0.8rem; letter-spacing: 0.02em;
}

/* ── Button ── */
div[data-testid="stButton"] > button {
    background: linear-gradient(135deg, #f0a060, #e07030) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 0.72rem 2.6rem !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.04em !important;
    cursor: pointer !important;
    transition: all 0.22s cubic-bezier(0.34,1.56,0.64,1) !important;
    box-shadow: 0 4px 18px rgba(220,100,40,0.28) !important;
}
div[data-testid="stButton"] > button:hover {
    transform: translateY(-3px) scale(1.04) !important;
    box-shadow: 0 10px 28px rgba(220,100,40,0.4) !important;
    background: linear-gradient(135deg, #f8b070, #e88040) !important;
}
div[data-testid="stButton"] > button:active {
    transform: scale(0.97) !important;
}

/* ── Response balloon ── */
.balloon {
    border-radius: 22px; padding: 1.8rem 2.2rem; text-align: center;
    margin-top: 0.8rem;
    animation: balloon-pop 0.55s cubic-bezier(0.34,1.56,0.64,1);
    border: 1.5px solid transparent;
}
.balloon.rose-bg    { background: linear-gradient(145deg, #fff0f5, #fde8ee); border-color: #f0c0cc; }
.balloon.peach-bg   { background: linear-gradient(145deg, #fff5ec, #fdecd8); border-color: #f0caa8; }
.balloon.sage-bg    { background: linear-gradient(145deg, #f0faf4, #e0f5e8); border-color: #b0d8bc; }
.balloon.lav-bg     { background: linear-gradient(145deg, #f5f0ff, #ede8fc); border-color: #ccc0f0; }
.balloon.gold-bg    { background: linear-gradient(145deg, #fffaec, #fef5d8); border-color: #e8d090; }
@keyframes balloon-pop {
    0%   { opacity: 0; transform: scale(0.7) translateY(14px); }
    100% { opacity: 1; transform: scale(1) translateY(0); }
}
.balloon-glyph { font-size: 3rem; display: block; margin-bottom: 0.7rem; animation: glyph-spin 0.5s ease; }
@keyframes glyph-spin { 0%{transform:rotate(-25deg) scale(0.4);} 100%{transform:rotate(0deg) scale(1);} }
.balloon-title { font-family: 'Lora', serif; font-size: 1.15rem; font-style: italic; font-weight: 700; color: #6b3820; margin-bottom: 0.45rem; }
.balloon-body  { font-size: 0.87rem; font-weight: 500; color: #9a6040; line-height: 1.7; }

/* ── Footer ── */
.footer {
    text-align: center; margin-top: 2.5rem; padding-top: 1.5rem;
    border-top: 1.5px dashed #e8c8a0;
}
.footer-glyphs { font-size: 1.5rem; margin-bottom: 0.5rem; letter-spacing: 0.3rem; }
.footer-txt { font-size: 0.68rem; font-weight: 700; color: #c8a070; letter-spacing: 0.14em; text-transform: uppercase; }
.footer-tagline { font-family: 'Lora', serif; font-style: italic; font-size: 0.82rem; color: #b89070; margin-top: 0.3rem; }
</style>
""", unsafe_allow_html=True)

# ── Floating confetti dots ─────────────────────────────────────────────────
colors = ["#f4c4a0","#f0a8b8","#b8dfc8","#d0c8f0","#fad080","#f8b8c0","#a8d8c0"]
dots_html = '<div class="confetti-wrap">'
for i in range(18):
    c = random.choice(colors)
    sz = random.randint(6, 14)
    left = random.randint(2, 98)
    dur = round(random.uniform(3.5, 7.0), 1)
    delay = round(random.uniform(0, 5), 1)
    dots_html += f'<div class="dot" style="width:{sz}px;height:{sz}px;left:{left}%;background:{c};animation-duration:{dur}s;animation-delay:{delay}s;"></div>'
dots_html += '</div>'
st.markdown(dots_html, unsafe_allow_html=True)

# ── Top badge ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="top-badge">
    <div class="badge-pill">✨ &nbsp; Idul Fitri 1447 H &nbsp; ✨</div>
</div>
""", unsafe_allow_html=True)

# ── Moon hero ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="moon-hero">
    <span class="moon-big">🌙</span>
    <h1 class="hero-title">Selamat<br><span class="accent">Hari Raya!</span></h1>
    <p class="hero-subtitle">Minal Aidin Wal Faizin 🌿</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="star-strip">✦ &nbsp; ✦ &nbsp; ✦ &nbsp; ✦ &nbsp; ✦</div>', unsafe_allow_html=True)

# ── Ticker ────────────────────────────────────────────────────────────────
t_items = [
    "🌙 Allahu Akbar", "🍪 Selamat Lebaran", "✨ Minal Aidin Wal Faizin",
    "🫙 Ketupat Yuk!", "🌿 Taqabbalallahu Minna Wa Minkum",
    "🎊 1447 Hijriah", "💛 Mohon Maaf Lahir Batin",
] * 2
ticker_html = "".join(f'<span class="ticker-item">{i}</span>' for i in t_items)
st.markdown(f'<div class="ticker-outer"><div class="ticker-inner">{ticker_html}</div></div>', unsafe_allow_html=True)

# ── Emoji food strip ──────────────────────────────────────────────────────
foods = [
    ("🫙","Ketupat","1.9s"), ("🍛","Rendang","2.5s"), ("🍪","Nastar","2.1s"),
    ("🫐","Opor","2.8s"),   ("🍮","Kolak","2.3s"),   ("🥛","Es Buah","3.0s"),
    ("🎁","THR","1.7s"),
]
strip_html = '<div class="emoji-strip">'
for icon, name, dur in foods:
    strip_html += f'<div class="emoji-card" style="animation-duration:{dur};"><span class="ec-icon">{icon}</span><div class="ec-name">{name}</div></div>'
strip_html += '</div>'
st.markdown(strip_html, unsafe_allow_html=True)

# ── Info mosaic ───────────────────────────────────────────────────────────
st.markdown("""
<div class="mosaic">
    <div class="mosaic-card rose">
        <span class="mc-icon">🌙</span>
        <div class="mc-lbl">Tahun</div>
        <div class="mc-val">1447 Hijriah</div>
    </div>
    <div class="mosaic-card peach">
        <span class="mc-icon">🌿</span>
        <div class="mc-lbl">Makna</div>
        <div class="mc-val">Kembali Suci</div>
    </div>
    <div class="mosaic-card sage">
        <span class="mc-icon">🫙</span>
        <div class="mc-lbl">Wajib Ada</div>
        <div class="mc-val">Ketupat & Opor</div>
    </div>
    <div class="mosaic-card lavender">
        <span class="mc-icon">💌</span>
        <div class="mc-lbl">Ucapan dari</div>
        <div class="mc-val">Reyna 🌸</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Main message card ─────────────────────────────────────────────────────
st.markdown("""
<div class="msg-card">
    <div class="msg-headline">Selamat Hari Raya Idul Fitri 1447 Hijriah 🌙✨</div>
    <div class="msg-body">
        <p>Semoga hari yang suci ini membawa ketenangan, kebahagiaan, dan kebaikan untuk kita semua.</p>
        <p>Di momen yang penuh cahaya ini, aku, <strong>Reyna</strong>, ingin memohon maaf lahir dan batin atas segala kekhilafan — baik dalam pertemuan, percakapan, atau hal kecil yang mungkin terlewat. Kita mungkin tidak selalu dekat, tapi aku tetap menghargai setiap hubungan yang terjalin, sekecil apa pun itu. 🌸</p>
        <p>Semoga Allah menerima ibadah kita dan membuka jalan-jalan baru yang lebih baik.</p>
        <p>Semoga hati kita dilembutkan, langkah kita dimudahkan, dan hari-hari ke depan terasa lebih damai.</p>
    </div>
    <div class="sig">
        <div class="sig-ava">R</div>
        <div class="sig-words">
            Taqabbalallahu minna wa minkum.<br>
            Salam hangat & penuh cinta, <em>Reyna</em> 💛🌿
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Button ────────────────────────────────────────────────────────────────
st.markdown('<p class="mood-label">Klik buat bikin Reyna seneng~ 🥺👇</p>', unsafe_allow_html=True)

responses = [
    ("rose-bg",  "🌸", "Aaaaaa makasih udah maafin aku!!",        "Kamu baik banget. Semoga Lebaran kamu penuh berkah ya! 💛🌿"),
    ("peach-bg", "🤗", "Yeay! Sama-sama dimaafin~",               "Selamat menikmati ketupat & opor, jangan lupa THR-nya disimpan~ 🫙😄"),
    ("sage-bg",  "🌿", "Alhamdulillah, legaaaaa banget!",          "Maaf lahir batin ya! Semoga hari-hari kita makin indah ke depannya. ✨"),
    ("lav-bg",   "💜", "Ini bikin hati jadi hangat beneran~",      "Semoga silaturahmi kita terus terjaga. Selamat Lebaran! 🌙💛"),
    ("gold-bg",  "✨", "Kamu snack favorit aku— eh, maksudnya...", "Maksudnya kamu orangnya manis kayak nastar! Selamat Idul Fitri 🍪💛"),
    ("rose-bg",  "🥰", "Makasih udah buka hati~",                  "Semoga kita sama-sama jadi pribadi yang lebih baik setelah Ramadan ini. 🌿🌙"),
]

col_l, col_c, col_r = st.columns([1, 2, 1])
with col_c:
    clicked = st.button("💛 Maafin Aku Ya?", use_container_width=True)

if clicked:
    bg_cls, glyph, title, body = random.choice(responses)
    st.markdown(f"""
    <div class="balloon {bg_cls}">
        <span class="balloon-glyph">{glyph}</span>
        <div class="balloon-title">"{title}"</div>
        <div class="balloon-body">{body}</div>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    <div class="footer-glyphs">🌙 ✨ 🌿 🌸 💛</div>
    <div class="footer-txt">Taqabbalallahu Minna Wa Minkum · 1447 H</div>
    <div class="footer-tagline">dibuat dengan cinta oleh Reyna 🌸</div>
</div>
""", unsafe_allow_html=True)
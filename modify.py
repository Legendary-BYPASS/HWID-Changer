import json
from mitmproxy import http
from bs4 import BeautifulSoup

# Daftar URL beta tester
btg_beta_tester = [
    "pornhub.com",
    "bekasi-cheater-ind.blogspot.com",
]

btg_bypass_script = [
    "http://backtogemscool.xyz/launcher/checker2.btg",
    "http://backtogemscool.xyz/launcher/checker2.btg?",
    "launcher/checker2.btg?",
    "launcher/checker2.btg?q="
]

btg_bypass_ip = [
    "http://api.ipify.org/"
]

btg_bypass_files = [
    "https://smpmaarifpdn.sch.id/blocked.txt?",
    "https://smpmaarifpdn.sch.id/connection.txt?"
]

#btg_bypass_cheat = [
#    "http://backtogemscool.xyz/launcher/checker/BCPopup.exe"
#]

btg_bypass_data = [
    "https://smpmaarifpdn.sch.id/dataPack.xml"
]

btg_bypass_splash = [
    "http://backtogemscool.xyz/launcher/launcher_config.txt"
]

BKS_login = [
    "https://pastebin.com/raw/V5uaAHLP"
]

BKS_pbsf = [
    "https://pastebin.com/raw/yDufRbdq"
]

# Fungsi untuk memproses request
def request(flow: http.HTTPFlow) -> None:
    # Cek jika request URL ada dalam list btg_beta_tester
    if any(url in flow.request.pretty_url for url in btg_beta_tester):
        # Buat response langsung (tanpa melanjutkan request ke server)
        flow.response = http.Response.make(
            200,  # No_Content
            b"BTG.SYSTEM SUCCESSFULLY BE HACKED !\n- SYSTEM.KUONTOLL\n- ANTISCRIPT\n- ANTIDETECT\n- 100% AMAN\n\nMORE UPDATE BYPASS BTG\nig : @eydidya\nfb : @eydidya",  # Isi pesan yang akan ditampilkan
            {"Content-Type": "text/plain"}  # Pastikan tipe konten valid
        )
    
    # Bypass-Script
    if any(url in flow.request.pretty_url for url in btg_bypass_script):
        flow.response = http.Response.make(
            200,
            b"",
            {"Content-Type": "application/octet-stream"}
        )
        
    # BypassIP
    if flow.request.pretty_url == "http://api.ipify.org/":
        flow.response = http.Response.make(
            200,  # Status kode HTTP 200
            b"8.215.96.250",  # IP palsu yang ingin ditampilkan
            {"Content-Type": "text/plain"}  # Header yang sesuai
        )
    elif flow.request.pretty_url == "https://api.ipify.org/":
        # Ubah User-Agent jika perlu
        flow.request.headers["User-Agent"] = "Mozilla/5.0"
        flow.response = http.Response.make(
            200,  # Status kode HTTP 200
            b"8.215.96.250",  # IP palsu yang ingin ditampilkan
            {"Content-Type": "text/plain"}  # Header yang sesuai
        )
    
    # Bypass-Files
    if any(url in flow.request.pretty_url for url in btg_bypass_files):
        flow.response = http.Response.make(
            200,
            b"FUCKING-BTG-SYSTEM",
            {"Content-Type": "text/plain"}
        )
    
    # Bypass-Cheat
    #if any(url in flow.request.pretty_url for url in btg_bypass_cheat):
    #    flow.response = http.Response.make(
    #        200,
    #        b"0",
    #        {"Content-Type": "application/x-msdownload"}
    #    )
    if flow.request.pretty_url == "http://backtogemscool.xyz/launcher/checker/BCPopup.exe":
        # Ganti dengan URL baru
        flow.request.url = "https://shorturl.at/ZZAb5"
        
    # Alternative DLL BekasiCheat
    if flow.request.pretty_url == "http://github.com/cilebute1/cilegon/releases/download/1/400":
        # Ganti dengan URL baru
        flow.request.url = "https://shorturl.at/QG2Ug"
    
    # Bypass-Data XML
    if any(url in flow.request.pretty_url for url in btg_bypass_data):
        flow.response = http.Response.make(
            200,
            b"<FUCKING-BTG-SYSTEM>",
            {"Content-Type": "application/xml"}
        )
        
    # Bypass-Splash
    if any(url in flow.request.pretty_url for url in btg_bypass_splash):
        flow.response = http.Response.make(
            200,
            b"PBCheckerImgUrl=https://i.ibb.co.com/kJBbxHM/splash.png\nPBShieldImgUrl=https://i.ibb.co.com/thNPKv5/bypass.png",
            {"Content-Type": "text/plain"}
        )   

    if any(url in flow.request.pretty_url for url in BKS_login):
        flow.response = http.Response.make(
            200,
            b"1",
            {"Content-Type": "text/plain"}
        )
    
    if any(url in flow.request.pretty_url for url in BKS_pbsf):
        flow.response = http.Response.make(
            200,
            b"StrikeForce",
            {"Content-Type": "text/plain"}
        )

def response(flow: http.HTTPFlow) -> None:
    # Memeriksa apakah URL yang diminta adalah yang ingin dimodifikasi
    if flow.request.pretty_url == "https://www.backtogemscool.xyz/launcher/web/":
        # Ganti seluruh isi response dengan HTML baru
        new_html_content = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>X</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap" rel="stylesheet"> <!-- Font untuk Teks Berkedip -->
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400&display=swap" rel="stylesheet"> <!-- Font untuk Teks Berubah Warna -->
    <style>
        body {
            background-color: #101010; /* Background gelap */
            color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            position: relative; /* Agar posisi teks marquee relatif terhadap body */
            overflow: hidden; /* Untuk menyembunyikan bagian marquee yang berada di luar */
        }
        
        .blink-1 {
            color: white;
            font-size: 200px;
            font-family: 'Roboto', sans-serif; /* Font untuk Teks Berkedip */
            animation: blink-animasi 1s infinite;
        }

        @keyframes blink-animasi {
            0%, 100% {
                opacity: 1; /* Teks terlihat */
            }
            50% {
                opacity: 0; /* Teks tidak terlihat */
            }
        }

        .blink-2 {
            color: red;
            font-size: 25px;
            font-family: 'Montserrat', sans-serif; /* Font untuk Teks Berubah Warna */
            animation: blink-cepat 1s steps(9, start) infinite;
        }

        @keyframes blink-cepat {
            to {
                visibility: hidden;
            }
        }
        
        .berjalan {
            color: white;
            font-size: 15px;
            font-family: 'Roboto', sans-serif; /* Font untuk Teks Berkedip */
        }
    </style>
</head>
<body>
    <h1 class="blink-1">BYPASSED !!</h1>
    <h2 class="blink-2">more info bypass contact blazemack.dwyyee</h2><br>
    <marquee behavior="scroll" direction="left" scrollamount="20" class="berjalan">INDONESIAN MODDERS 2024 | MULAI SEKARANG UBAH HIDUPMU MENJADI LEBIH BAIK | GANASENGINE X BLAZEMACK SINCE 2014 | SUPPORTED BY KEHOBIAN SENDIRI | KEJARLAH CITA CITA MU DENGAN PENUH SEMANGAT | MALAS ADALAH KUNCI FATAL KEGEGAGALAN</marquee>

</body>
</html>
        """
        
        # Mengubah response
        flow.response.set_text(new_html_content)
        
    elif flow.request.pretty_url == "https://backtogemscool.xyz/launcher/web/":
        # Ganti seluruh isi response dengan HTML baru
        new_html_content = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>X</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap" rel="stylesheet"> <!-- Font untuk Teks Berkedip -->
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400&display=swap" rel="stylesheet"> <!-- Font untuk Teks Berubah Warna -->
    <style>
        body {
            background-color: #101010; /* Background gelap */
            color: white;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            position: relative; /* Agar posisi teks marquee relatif terhadap body */
            overflow: hidden; /* Untuk menyembunyikan bagian marquee yang berada di luar */
        }
        
        .blink-1 {
            color: white;
            font-size: 200px;
            font-family: 'Roboto', sans-serif; /* Font untuk Teks Berkedip */
            animation: blink-animasi 1s infinite;
        }

        @keyframes blink-animasi {
            0%, 100% {
                opacity: 1; /* Teks terlihat */
            }
            50% {
                opacity: 0; /* Teks tidak terlihat */
            }
        }

        .blink-2 {
            color: red;
            font-size: 25px;
            font-family: 'Montserrat', sans-serif; /* Font untuk Teks Berubah Warna */
            animation: blink-cepat 1s steps(9, start) infinite;
        }

        @keyframes blink-cepat {
            to {
                visibility: hidden;
            }
        }
        
        .berjalan {
            color: white;
            font-size: 15px;
            font-family: 'Roboto', sans-serif; /* Font untuk Teks Berkedip */
        }
    </style>
</head>
<body>
    <h1 class="blink-1">BYPASSED !!</h1>
    <h2 class="blink-2">more info bypass contact blazemack.dwyyee</h2><br>
    <marquee behavior="scroll" direction="left" scrollamount="20" class="berjalan">INDONESIAN MODDERS 2024 | MULAI SEKARANG UBAH HIDUPMU MENJADI LEBIH BAIK | GANASENGINE X BLAZEMACK SINCE 2014 | SUPPORTED BY KEHOBIAN SENDIRI | KEJARLAH CITA CITA MU DENGAN PENUH SEMANGAT | MALAS ADALAH KUNCI FATAL KEGEGAGALAN</marquee>

</body>
</html>
        """
        
        # Mengubah response
        flow.response.set_text(new_html_content)
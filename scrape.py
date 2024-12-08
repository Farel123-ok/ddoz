import requests
import re

# Daftar link proxy statis
proxy_links = [
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
    'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
    'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
    'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
    'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
    'https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt',
    'https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
    'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
    'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
    'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
    'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
    'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt',
    'https://api.openproxylist.xyz/http.txt',
    'https://api.proxyscrape.com/v2/?request=displayproxies',
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
    'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=all&city=all&port=all&type=all&anonymity=all&state=all&need=all',
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous',
    'http://worm.rip/http.txt',
    'https://proxyspace.pro/http.txt',
    'https://multiproxy.org/txt_all/proxy.txt',
    'https://proxy-spider.com/api/proxies.example.txt',
    'https://www.us-proxy.org',
    'https://www.socks-proxy.net',
    'https://proxyscrape.com/free-proxy-list',
    'https://www.proxynova.com/proxy-server-list/',
    'https://proxybros.com/free-proxy-list/',
    'https://proxydb.net/',
    'https://spys.one/en/free-proxy-list/',
]

# URL template untuk halaman dinamis dalam bentuk list
base_urls = [
    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page={page}",
    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=600&port=&page={page}",
    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=800&port=&page={page}",
    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=900&port=&page={page}",
    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=300&port=&page={page}",
    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=400&port=&page={page}",
    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=500&port=&page={page}",
    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=600&port=&page={page}",
    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=100&port=&page={page}",
    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=865&port=&page={page}",
    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=826&port=&page={page}",
    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=368&port=&page={page}",
    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=627&port=&page={page}",
    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=956&port=&page={page}",
    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=977&port=&page={page}",
    "https://www.freeproxy.world/?type=&anonymity=&country=&speed=999&port=&page={page}"
]

# Fungsi untuk mengambil proxy dari sebuah link
def fetch_proxies(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        content = response.text
        proxy_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}:[0-9]{2,5}\b"
        proxies = re.findall(proxy_pattern, content)
        return proxies
    except requests.exceptions.RequestException as e:
        print(f"Error mengambil proxy dari {url}: {e}")
        return []

# Fungsi untuk mengambil proxy dari halaman dinamis
def fetch_proxies_from_pages(start_page, end_page):
    all_proxies = set()
    for base_url in base_urls:
        for page in range(start_page, end_page + 1):
            url = base_url.format(page=page)
            print(f"Mengambil proxy dari URL: {url}")
            proxies = fetch_proxies(url)
            all_proxies.update(proxies)
    return all_proxies

# Fungsi utama untuk menggabungkan semua proxy
def scrape_all_proxies(proxy_links, start_page=1, end_page=192, output_file="proxies.txt"):
    all_proxies = set()

    # Ambil proxy dari link statis
    for link in proxy_links:
        print(f"Mengambil proxy dari: {link}")
        proxies = fetch_proxies(link)
        all_proxies.update(proxies)

    # Ambil proxy dari halaman dinamis
    print("\nMengambil proxy dari halaman dinamis...")
    dynamic_proxies = fetch_proxies_from_pages(start_page, end_page)
    all_proxies.update(dynamic_proxies)

    # Simpan ke file
    if all_proxies:
        with open(output_file, "w") as file:
            file.write("\n".join(all_proxies))
        print(f"\nProxies berhasil disimpan di {output_file}. Total proxies: {len(all_proxies)}")
    else:
        print("\nTidak ada proxy yang ditemukan dari semua sumber.")

# Jalankan scraper
scrape_all_proxies(proxy_links)
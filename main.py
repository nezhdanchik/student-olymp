from pythonping import ping
from concurrent.futures import ThreadPoolExecutor

success_ip = []

# Частные IP-адреса:
# от 10.0.0.0 до 10.255.255.255 (10.0.0.0/8)
# 172.16.0.0 — 172.31.255.255 (172.16.0.0/12)
# 192.168.0.0 — 192.168.255.255 (192.168.0.0/16)

def add_success(ip: str, k):
    p = ping(ip)
    if p.success():
        success_ip.append(f'ip: {ip}, Критерий: произошёл обмен пактов {p.rtt_avg}, критерий: {k}')
        print(ip)

with ThreadPoolExecutor(max_workers=500) as executor:
    for i1 in range(1,256):
        for i2 in range(256):
            for i3 in range(256):
                i4 = i1 + i2 - i3
                if sum([i1, i2, i3, i4]) != 100:
                    continue
                if i4 < 0 or i4 > 255:
                    continue
                if i1 == 10:
                    continue
                if i1 == 172 and 16 <= i2 <= 31:
                    continue
                if i1 == 192 and i2 == 168:
                    continue
                ip = f"{i1}.{i2}.{i3}.{i4}"
                executor.submit(add_success, ip, f'{i1} + {i2} = {i3} + {i4}; {i1} + {i2} + {i3} + {i4} = 100')

print('success ip:', success_ip)
with open('success_ip.txt', 'w', encoding='utf-8') as f:
    for ip in success_ip:
        f.write(ip + '\n')

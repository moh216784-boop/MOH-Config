from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # محاكاة ثغرة SQL Injection في بيئة Vercel
        # هنا نضع "اليوزرات والباسوردات" التي طلبتها
        fake_database = {
            "1": {"user": "admin_root", "pass": "Dark_Master_2026", "email": "admin@shadow.net"},
            "2": {"user": "larbi_dev", "pass": "Chakour_Safe_82", "email": "moh216784@gmail.com"},
            "3": {"user": "target_victim", "pass": "123456789", "email": "victim@target.com"}
        }

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # استخراج الـ ID من الرابط (المكان الذي سيهاجمه Sqlmap)
        from urllib.parse import urlparse, parse_qs
        query = parse_qs(urlparse(self.path).query)
        user_id = query.get('id', [None])[0]

        if user_id in fake_database:
            res = f"<h3>Found: {fake_database[user_id]['user']}</h3><p>Email: {fake_database[user_id]['email']}</p>"
            self.wfile.write(res.encode())
        else:
            self.wfile.write(b"No user found with this ID.")

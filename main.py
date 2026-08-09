import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from bot import main as run_bot

# Render-কে সন্তুষ্ট রাখতে একটি সাধারণ HTTP সেবক তৈরি করা
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Bot is alive and running!")

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    server_address = ('', port)
    httpd = HTTPServer(server_address, HealthCheckHandler)
    print(f"Web server running on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    # ব্যাকগ্রাউন্ডে HTTP সার্ভার চালানো
    threading.Thread(target=run_web_server, daemon=True).start()
    
    # টেলিগ্রাম বট চালানো
    run_bot()

#!/usr/bin/env python3
"""BioEco Agent Lab Research Portal Server v2 — with study detail pages and file serving"""
import http.server
import os
import json
import glob
import urllib.parse
import mimetypes

COMPANY_DIR = os.path.expanduser('~/.agentlattice/bioeco')
SITE_DIR = os.path.dirname(os.path.abspath(__file__))
FINAL_DIR = os.path.join(COMPANY_DIR, 'agents', 'jim-leader', 'workspace', 'final-result')
PORT = 8391

class ResearchPortalHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def do_GET(self):
        path = urllib.parse.unquote(self.path)

        if path == '/' or path == '/index.html':
            self._serve_file(os.path.join(SITE_DIR, 'index.html'), 'text/html')

        elif path == '/diary' or path == '/diary.html':
            self._serve_file(os.path.join(SITE_DIR, 'diary.html'), 'text/html')

        elif path.startswith('/diary/') and path.endswith('.html'):
            fpath = os.path.join(SITE_DIR, path.lstrip('/'))
            fpath = os.path.realpath(fpath)
            if fpath.startswith(os.path.realpath(os.path.join(SITE_DIR, 'diary'))) and os.path.isfile(fpath):
                self._serve_file(fpath, 'text/html')
            else:
                self.send_response(404)
                self.end_headers()

        elif path.startswith('/study/'):
            self._serve_file(os.path.join(SITE_DIR, 'study.html'), 'text/html')

        elif path.startswith('/files/'):
            rel = path[7:]
            fpath = os.path.join(FINAL_DIR, rel)
            fpath = os.path.realpath(fpath)
            if fpath.startswith(os.path.realpath(FINAL_DIR)) and os.path.isfile(fpath):
                ctype, _ = mimetypes.guess_type(fpath)
                if ctype is None:
                    ctype = 'application/octet-stream'
                self.send_response(200)
                self.send_header('Content-Type', ctype)
                self.send_header('Content-Disposition', f'inline; filename="{os.path.basename(fpath)}"')
                self.end_headers()
                with open(fpath, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_response(404)
                self.end_headers()

        elif path == '/api/roster':
            self._serve_json_file(os.path.join(COMPANY_DIR, 'org', 'roster.json'))

        elif path == '/api/channels':
            channels_dir = os.path.join(COMPANY_DIR, 'org', 'channels')
            result = {}
            if os.path.isdir(channels_dir):
                for f in sorted(glob.glob(os.path.join(channels_dir, '*.jsonl'))):
                    name = os.path.basename(f).replace('.jsonl', '')
                    if name.startswith('_archived_'):
                        continue
                    lines = []
                    with open(f, 'r') as fh:
                        for line in fh:
                            line = line.strip()
                            if line:
                                try:
                                    lines.append(json.loads(line))
                                except json.JSONDecodeError:
                                    pass
                    result[name] = {
                        'total_messages': len(lines),
                        'recent': lines[-20:] if lines else []
                    }
            self._send_json(result)

        elif path == '/api/knowledge':
            knowledge_dir = os.path.join(COMPANY_DIR, 'org', 'knowledge')
            files = []
            if os.path.isdir(knowledge_dir):
                for f in sorted(glob.glob(os.path.join(knowledge_dir, '*.md'))):
                    name = os.path.basename(f)
                    stat = os.stat(f)
                    with open(f, 'r') as fh:
                        content = fh.read()
                    files.append({'name': name, 'size': stat.st_size, 'modified': stat.st_mtime, 'preview': content[:200]})
            self._send_json(files)

        elif path == '/api/dashboard':
            dp = os.path.join(COMPANY_DIR, 'org', 'dashboard.md')
            if os.path.isfile(dp):
                self._serve_file(dp, 'text/plain')
            else:
                self._send_text('# No dashboard found')

        elif path == '/api/final-results':
            result = {}
            if os.path.isdir(FINAL_DIR):
                for d in sorted(os.listdir(FINAL_DIR)):
                    dpath = os.path.join(FINAL_DIR, d)
                    if os.path.isdir(dpath):
                        files = []
                        for root, dirs, fnames in os.walk(dpath):
                            for fn in fnames:
                                rel = os.path.relpath(os.path.join(root, fn), dpath)
                                size = os.path.getsize(os.path.join(root, fn))
                                files.append({'path': rel, 'size': size})
                        result[d] = sorted(files, key=lambda x: x['path'])
            self._send_json(result)

        elif path.startswith('/api/file-content/'):
            rel = path[18:]
            fpath = os.path.join(FINAL_DIR, rel)
            fpath = os.path.realpath(fpath)
            if fpath.startswith(os.path.realpath(FINAL_DIR)) and os.path.isfile(fpath) and fpath.endswith('.md'):
                with open(fpath, 'r') as f:
                    self._send_json({'content': f.read()})
            else:
                self.send_response(404)
                self.end_headers()

        else:
            self.send_response(404)
            self.end_headers()

    def _serve_file(self, path, content_type):
        self.send_response(200)
        self.send_header('Content-Type', f'{content_type}; charset=utf-8')
        self.send_header('Cache-Control', 'no-cache')
        self.end_headers()
        with open(path, 'rb') as f:
            self.wfile.write(f.read())

    def _send_json(self, data):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode())

    def _serve_json_file(self, path):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        if os.path.isfile(path):
            with open(path, 'r') as f:
                self.wfile.write(f.read().encode())
        else:
            self.wfile.write(b'{}')

    def _send_text(self, text):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(text.encode())

if __name__ == '__main__':
    server = http.server.HTTPServer(('0.0.0.0', PORT), ResearchPortalHandler)
    print(f'BioEco Research Portal v2 running on http://localhost:{PORT}')
    server.serve_forever()

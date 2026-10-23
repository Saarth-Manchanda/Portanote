import os
from flask import Flask, request, redirect, render_template_string, abort
import string
import random
import re

app = Flask(__name__)
NOTES_DIR = 'notes'
os.makedirs(NOTES_DIR, exist_ok=True)

def generate_id(length=5):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

NOTE_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Portanote</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            background: #121212;
            min-height: 100vh;
            margin: 0;
            font-family: 'JetBrains Mono', monospace;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            color: #e0e0e0;
        }
        .container {
            background: #181818;
            border-radius: 0px;
            box-shadow: 8px 8px 0px #0a0a0a;
            padding: 2.5rem;
            max-width: 700px;
            width: 100%;
            margin: 2rem 2rem 1rem 2.5rem;
            display: flex;
            flex-direction: column;
            align-items: center;
            border: 2px solid #2a2a2a;
            box-sizing: border-box;
        }
        .header-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            margin-bottom: 2rem;
        }
        h1 {
            color: #ff7b00;
            font-weight: 700;
            letter-spacing: -0.5px;
            font-size: 1.8rem;
            margin: 0;
            text-transform: uppercase;
        }
        .save-btn {
            background: #ff7b00;
            color: #121212;
            border: 2px solid #ff7b00;
            border-radius: 0px;
            padding: 0.6rem 1.4rem;
            font-size: 1rem;
            font-weight: 700;
            font-family: 'JetBrains Mono', monospace;
            cursor: pointer;
            transition: background 0.15s, transform 0.1s, box-shadow 0.15s;
            box-shadow: 4px 4px 0px #0a0a0a;
            margin-left: 1.2rem;
            text-transform: uppercase;
        }
        .save-btn:hover {
            background: #ff9526;
            border-color: #ff9526;
            transform: translate(-2px, -2px);
            box-shadow: 6px 6px 0px #0a0a0a;
        }
        .save-btn:active {
            transform: translate(0px, 0px);
            box-shadow: 2px 2px 0px #0a0a0a;
        }
        form {
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: stretch;
        }
        .textarea-wrapper {
            position: relative;
            width: 100%;
        }
        textarea {
            width: 100%;
            min-height: 320px;
            max-height: 60vh;
            border-radius: 0px;
            border: 2px solid #2a2a2a;
            padding: 1rem;
            font-size: 1rem;
            font-family: 'JetBrains Mono', monospace;
            resize: vertical;
            margin-bottom: 1.2rem;
            background: #141414;
            color: #f0f0f0;
            box-sizing: border-box;
            transition: border-color 0.2s;
        }
        textarea:focus {
            border-color: #ff7b00;
            outline: none;
        }
        .copy-icon {
            position: absolute;
            top: 14px;
            right: 14px;
            width: 32px;
            height: 32px;
            background: #1f1f1f;
            border: 2px solid #2a2a2a;
            border-radius: 0px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #a0a0a0;
            transition: color 0.2s, border-color 0.2s, background 0.2s;
            z-index: 2;
        }
        .copy-icon:hover {
            color: #ff7b00;
            border-color: #ff7b00;
            background: #242424;
        }
        .copy-tooltip {
            position: absolute;
            top: -36px;
            right: 0;
            background: #ff7b00;
            color: #121212;
            font-weight: 700;
            padding: 4px 8px;
            border-radius: 0px;
            font-size: 0.85rem;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.2s;
            z-index: 3;
            box-shadow: 2px 2px 0px #0a0a0a;
        }
        .copy-icon.copied + .copy-tooltip {
            opacity: 1;
        }
        .share-section {
            margin-top: 1.5rem;
            background: #141414;
            border: 2px solid #2a2a2a;
            padding: 1.2rem;
            border-radius: 0px;
            width: 100%;
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            gap: 0.8rem;
        }
        .share-row {
            display: flex;
            align-items: center;
            gap: 0.8rem;
        }
        .share-input {
            flex: 1;
            background: #121212;
            border: 2px solid #2a2a2a;
            color: #ff7b00;
            padding: 0.6rem 0.8rem;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9rem;
            outline: none;
        }
        .copy-link-btn {
            background: #1f1f1f;
            color: #e0e0e0;
            border: 2px solid #2a2a2a;
            padding: 0.6rem 1rem;
            font-family: 'JetBrains Mono', monospace;
            font-weight: 700;
            font-size: 0.85rem;
            cursor: pointer;
            transition: background 0.15s, border-color 0.15s, color 0.15s;
            white-space: nowrap;
        }
        .copy-link-btn:hover {
            background: #ff7b00;
            border-color: #ff7b00;
            color: #121212;
        }
        .share-footer-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
            margin-top: 0.2rem;
        }
        .share-tip {
            font-size: 0.8rem;
            color: #888888;
            margin: 0;
            line-height: 1.4;
        }
        .share-tip strong {
            color: #ff7b00;
        }
        .delete-btn {
            background: #1f1f1f;
            color: #ff4d4d;
            border: 2px solid #2a2a2a;
            padding: 0.5rem 0.8rem;
            font-family: 'JetBrains Mono', monospace;
            font-weight: 700;
            font-size: 0.8rem;
            cursor: pointer;
            transition: background 0.15s, border-color 0.15s, color 0.15s;
            white-space: nowrap;
        }
        .delete-btn:hover {
            background: #ff4d4d;
            border-color: #ff4d4d;
            color: #121212;
        }
        .footer {
            margin-top: 1rem;
            margin-bottom: 2rem;
            font-size: 0.8rem;
            color: #777777;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .footer a {
            color: #777777;
            display: flex;
            align-items: center;
            text-decoration: none;
            border-bottom: none;
            transition: color 0.2s;
        }
        .footer a:hover {
            color: #ff7b00;
            border-bottom: none;
        }
        a {
            color: #ff7b00;
            text-decoration: none;
            border-bottom: 1px dotted #ff7b00;
            transition: color 0.2s;
        }
        a:hover {
            color: #ff9526;
            border-bottom-style: solid;
        }
        @media (max-width: 800px) {
            .container {
                padding: 1.5rem 1rem;
                margin: 1rem;
                box-shadow: 4px 4px 0px #0a0a0a;
            }
            textarea {
                font-size: 0.95rem;
                min-height: 180px;
            }
            .header-row {
                flex-direction: column;
                align-items: flex-start;
                gap: 1rem;
            }
            .save-btn {
                margin-left: 0;
                width: 100%;
            }
            .share-row {
                flex-direction: column;
            }
            .copy-link-btn {
                width: 100%;
            }
            .share-footer-row {
                flex-direction: column;
                align-items: flex-start;
            }
            .delete-btn {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <form method="post">
            <div class="header-row">
                <h1>// Portanote</h1>
                <button type="submit" class="save-btn">[ Save ]</button>
            </div>
            <div class="textarea-wrapper">
                <textarea id="note-textarea" name="content" rows="18" cols="80">{{ content.strip() if content else '' }}</textarea>
                <button type="button" class="copy-icon" onclick="copyText(this)" title="Copy text to clipboard" tabindex="-1">
                    <svg viewBox="0 0 24 24" fill="none" width="16" height="16" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="0" ry="0"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
                </button>
                <span class="copy-tooltip" id="copy-tooltip">COPIED!</span>
            </div>
        </form>
        {% if note_id %}
        <div class="share-section">
            <div class="share-row">
                <input type="text" id="share-link-input" class="share-input" value="{{ request.url_root }}{{ note_id }}" readonly>
                <button type="button" class="copy-link-btn" onclick="copyShareLink(this)">[ Copy Link ]</button>
            </div>
            <div class="share-footer-row">
                <p class="share-tip">Tip: Add code (<strong>{{ note_id }}</strong>) to the end of the URL to access it anywhere.</p>
                <form action="/{{ note_id }}/delete" method="POST" style="margin:0; width:auto;" onsubmit="return confirm('Delete this note permanently?');">
                    <button type="submit" class="delete-btn">[ Delete ]</button>
                </form>
            </div>
        </div>
        {% endif %}
    </div>
    
    <div class="footer">
        <span>made by saarth manchanda</span>
        <a href="https://github.com/Saarth-Manchanda" target="_blank" title="GitHub">
            <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
        </a>
    </div>

    <script>
        function copyText(btn) {
            const textarea = document.getElementById('note-textarea');
            textarea.select();
            textarea.setSelectionRange(0, 99999);
            try {
                document.execCommand('copy');
            } catch (err) {
                navigator.clipboard.writeText(textarea.value);
            }
            const tooltip = document.getElementById('copy-tooltip');
            btn.classList.add('copied');
            tooltip.style.opacity = 1;
            setTimeout(() => {
                btn.classList.remove('copied');
                tooltip.style.opacity = 0;
            }, 1200);
        }

        function copyShareLink(btn) {
            const input = document.getElementById('share-link-input');
            input.select();
            input.setSelectionRange(0, 99999);
            try {
                document.execCommand('copy');
            } catch (err) {
                navigator.clipboard.writeText(input.value);
            }
            const originalText = btn.innerText;
            btn.innerText = '[ COPIED! ]';
            setTimeout(() => {
                btn.innerText = originalText;
            }, 1200);
        }
    </script>
</body>
</html>
'''

def save_note(note_id, content):
    with open(os.path.join(NOTES_DIR, f"{note_id}.txt"), 'w', encoding='utf-8') as f:
        f.write(content)

def load_note(note_id):
    path = os.path.join(NOTES_DIR, f"{note_id}.txt")
    if not os.path.exists(path):
        return None
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def delete_note(note_id):
    path = os.path.join(NOTES_DIR, f"{note_id}.txt")
    if os.path.exists(path):
        os.remove(path)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form.get('content', '')
        content = re.sub(r'^[\s\n]+|[\s\n]+$', '', content)
        note_id = generate_id()
        save_note(note_id, content)
        return redirect(f'/{note_id}')
    return render_template_string(NOTE_TEMPLATE, content='', note_id=None, request=request)

@app.route('/<note_id>', methods=['GET', 'POST'])
def note(note_id):
    if request.method == 'POST':
        content = request.form.get('content', '')
        content = re.sub(r'^[\s\n]+|[\s\n]+$', '', content)
        save_note(note_id, content)
    content = load_note(note_id)
    if content is None:
        abort(404)
    return render_template_string(NOTE_TEMPLATE, content=content.strip() if content else '', note_id=note_id, request=request)

@app.route('/<note_id>/delete', methods=['POST'])
def delete_note_route(note_id):
    delete_note(note_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

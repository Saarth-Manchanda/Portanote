# 📝 Minimalist Online Notepad

A lightweight, high-performance, and beautifully designed web-based notepad built with Python and Flask. This application allows users to quickly paste, edit, and share notes via simple, unique URLs without requiring user registration or authentication.

---

## ✨ Features

* **Instant Note Creation:** Write or paste text and save it instantly.
* **Shareable Links:** Generates a unique 5-character ID for every saved note (e.g., `https://your-app.onrender.com/aB12x`).
* **One-Click Copy:** Built-in fast clipboard copying with intuitive feedback tooltips.
* **Clean & Responsive UI:** Designed with modern CSS gradients, glassmorphism UI elements, and a mobile-friendly flexible layout.
* **Lightweight & Fast:** Uses minimal external dependencies for ultra-fast load times.

---

## 🛠️ Tech Stack

* **Backend:** Python 3, Flask
* **Production Server:** Gunicorn
* **Frontend:** HTML5, CSS3, JavaScript (vanilla)
* **Storage:** Local text file-based storage (`/notes`)

---

## 🚀 Local Development Setup

To run this application locally on your machine, follow these steps:

### Prerequisites
Make sure you have **Python 3.8+** installed on your system.

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/online-notepad.git
cd online-notepad
```

### 2. Set Up a Virtual Environment (Optional but Recommended)
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## 📂 Project Structure

```text
online-notepad/
├── app.py              # Main Flask application logic & routing
├── requirements.txt    # Python dependencies (Flask, Gunicorn)
├── notes/              # Directory created automatically to store note text files
├── .gitignore          # Ignores virtual environments and dynamic note files
└── README.md           # Project documentation
```

---

## ☁️ Deploying to Render

This repository is pre-configured to deploy seamlessly on [Render](https://render.com/).

### Deployment Steps:

1. Push your project code to a public or private **GitHub** repository.
2. Log in to your **Render Dashboard** and click **New +** > **Web Service**.
3. Connect your GitHub repository.
4. Configure the Web Service settings:
   * **Name:** `online-notepad` (or your preferred name)
   * **Runtime:** `Python 3`
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `gunicorn app:app`
5. Click **Create Web Service**.

> 📌 **Note on Free-Tier Hosting:** Serverless platforms and free hosting tiers use ephemeral disk storage. Notes saved locally to the `/notes` folder will reset when the service restarts or redeploys. For permanent data persistence, consider integrating a cloud database (such as Supabase, PostgreSQL, or MongoDB Atlas).

---

## 🛡️ Security & Best Practices

* **Path Traversal Protection:** The application uses sanitized ID generators to prevent directory traversal attacks.
* **Environment Configuration:** Ensure `debug=True` is disabled when running in production.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
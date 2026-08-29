# 🌟 TripNova — India Travel Planner & Smart AI Studio

A full-stack intelligent travel planning app for exploring India — featuring AI-powered day-wise itineraries, interactive Leaflet & OpenStreetMap pinning, in-app RedBus bus booking with live seat layout picker, in-app IRCTC train booking with live seat availability & PNR status tracker, and luxury & budget hotel reservations.

**Stack:** React + Vite (Frontend) · Python + Flask (Backend) · SQLite (Database) · Leaflet (Interactive Maps) · Google Gemini / OpenAI (AI Engine)

---

## ⚡ Quick 1-Click Run (For Friends & Reviewers)

### Method 1: Instant Frontend Run (No Backend Setup Needed)
```bash
# Clone the repository
git clone https://github.com/lavanya03477/TripNova.git
cd TripNova/frontend

# Install dependencies and start immediately
npm install
npm run dev
```
Open **http://localhost:5173** in your browser. All features (AI recommendations, day-wise itineraries, interactive maps, bus seat booking, IRCTC train search, and hotel reservations) will work instantly!

---


### Step 1 — Create the project folder in VS Code

1. Open **VS Code**
2. Go to **File → Open Folder**
3. Navigate to `C:\javalav 2026\vscode`
4. You should see the folder `india-travel-planner` (already created for you)
5. Open it: **File → Open Folder → india-travel-planner**

Your folder structure:

```
india-travel-planner/
├── backend/          ← Python Flask API
│   ├── app.py
│   ├── ai_service.py
│   ├── database.py
│   ├── requirements.txt
│   └── .env.example
└── frontend/         ← React + Vite app
    ├── src/
    ├── package.json
    └── vite.config.js
```

---

### Step 2 — Install Python (if not installed)

1. Download Python 3.10+ from https://www.python.org/downloads/
2. During install, check **"Add Python to PATH"**
3. Verify in terminal:
   ```powershell
   python --version
   ```

---

### Step 3 — Set up the Backend (Flask)

Open a **terminal in VS Code** (`Ctrl + ~`) and run:

```powershell
cd "C:\javalav 2026\vscode\india-travel-planner\backend"

# Create virtual environment
python -m venv venv

# Activate it (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create .env file from example
copy .env.example .env
```

Edit `backend/.env` and add your OpenAI API key (optional but recommended for real AI):

```
OPENAI_API_KEY=sk-your-key-here
SECRET_KEY=any-random-secret-string
```

> Without an API key, the app still works using built-in fallback recommendations.

Start the backend:

```powershell
python app.py
```

You should see: `Running on http://127.0.0.1:5000`

---

### Step 4 — Install Node.js (if not installed)

1. Download from https://nodejs.org/ (LTS version)
2. Verify:
   ```powershell
   node --version
   npm --version
   ```

---

### Step 5 — Set up the Frontend (React + Vite)

Open a **second terminal** in VS Code:

```powershell
cd "C:\javalav 2026\vscode\india-travel-planner\frontend"

npm install

npm run dev
```

You should see: `Local: http://localhost:5173`

Open that URL in your browser.

---

### Step 6 — Use the App

1. **Login page** — Enter username + email, or click "Sign in with Google" (demo mode)
2. **Home** — Navigation links (text, not buttons) + General AI Assistant
3. **Plan My Journey** — Fill climate/travel/experience/budget form → get top 3 AI places
4. **Places to Visit** — Enter Madurai, Kerala, Madhya Pradesh, etc. → day-wise itinerary + hotels
5. **Bus/Train** — Click app names to open redBus, IRCTC, etc.
6. **Hotels** — Top 10 booking platforms
7. **Map** — Opens Google Maps in new tab
8. **🏠 Home icon** — On every page, click to go back to Home

---

## Features Checklist

| Feature | Status |
|---------|--------|
| Login (username + email) | ✅ |
| Sign in with Google (demo) | ✅ |
| Text navigation (not buttons) | ✅ |
| Home icon on all pages | ✅ |
| Plan My Journey AI form | ✅ |
| Single-choice options | ✅ |
| Top 3 place recommendations | ✅ |
| AI doubt assistant (unsuitable places) | ✅ |
| Places to Visit form | ✅ |
| Works for any Indian place/state | ✅ (via AI) |
| Re-submit form unlimited times | ✅ |
| Bus booking (5 apps) | ✅ |
| Train booking (5 apps) | ✅ |
| Hotel booking (10 apps) | ✅ |
| Google Maps link | ✅ |
| General AI Assistant on Home | ✅ |
| Responsive (phone/tablet/laptop) | ✅ |
| SQLite database | ✅ |

---

## API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/api/auth/register` | Register user |
| POST | `/api/auth/login` | Login |
| POST | `/api/auth/google` | Google sign-in |
| POST | `/api/ai/plan-journey` | Top 3 place recommendations |
| POST | `/api/ai/unsuitable-place` | Why a place doesn't fit |
| POST | `/api/ai/places-to-visit` | Day-wise itinerary + hotels |
| POST | `/api/ai/chat` | General AI chat |

---

## Optional Upgrades (Later)

1. **Real Google OAuth** — Set up Google Cloud Console credentials
2. **Embedded Maps** — Add Google Maps JavaScript API
3. **Deploy** — Frontend on Vercel/Netlify, Backend on Render/Railway
4. **Password auth** — Add bcrypt hashing for secure login

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `pip` not found | Use `python -m pip install -r requirements.txt` |
| Port 5000 in use | Change port in `app.py`: `app.run(port=5001)` |
| CORS errors | Ensure backend is running on port 5000 |
| AI gives generic answers | Add `OPENAI_API_KEY` in `backend/.env` |
| npm install fails | Run terminal as admin or use `npm install --legacy-peer-deps` |

---

## Running Both Servers Daily

**Terminal 1 (Backend):**
```powershell
cd backend
.\venv\Scripts\Activate.ps1
python app.py
```

**Terminal 2 (Frontend):**
```powershell
cd frontend
npm run dev
```

Then open **http://localhost:5173** in your browser.

# Deployment Guide

## Local Development

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm start
```

## Docker Deployment

### Build and Run
```bash
docker-compose up -d
```

## Cloud Deployment

### Heroku
1. Install Heroku CLI
2. Create `Procfile` in root:
   ```
   web: cd backend && python app.py
   ```
3. Deploy:
   ```bash
   heroku create osintzeus
   git push heroku main
   ```

### Vercel/Netlify (Frontend)
1. Build frontend:
   ```bash
   cd frontend
   npm run build
   ```
2. Deploy `build` folder to Vercel/Netlify

## Environment Variables

Create `.env` in backend:
```env
FLASK_ENV=production
FLASK_DEBUG=False
GOOGLE_MAPS_API_KEY=your_key_here
PORT=5000
```


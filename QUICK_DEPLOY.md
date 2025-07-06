# 🚀 Quick Deployment Reference

## 📋 What You Need to Do

### 1. MongoDB Atlas Setup (5 minutes)
- Create account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
- Create free cluster
- Create database user
- Whitelist all IPs (0.0.0.0/0)
- Get connection string

### 2. Backend Deployment (10 minutes)
**Option A: Railway (Recommended)**
- Sign up at [Railway](https://railway.app)
- Connect GitHub repository
- Set environment variables:
  ```
  MONGO_URL=mongodb+srv://user:pass@cluster.mongodb.net/portfolio
  DB_NAME=portfolio
  ```
- Get your backend URL

**Option B: Render**
- Sign up at [Render](https://render.com)
- Create new Web Service
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn server:app --host 0.0.0.0 --port $PORT`

### 3. Populate Database (2 minutes)
- Update `backend/populate_atlas.py` with your MongoDB URL
- Run: `python populate_atlas.py`

### 4. Frontend Deployment (5 minutes)
- Update `frontend/.env.production` with your backend URL
- Update `frontend/package.json` homepage field
- Push to GitHub
- Enable GitHub Pages (Settings → Pages → gh-pages branch)
- Run: `npm run deploy`

## 🔗 Your URLs Will Be:
- **Frontend**: `https://yourusername.github.io/portfolio`
- **Backend**: `https://your-app.railway.app`
- **Database**: MongoDB Atlas

## 🆘 Need Help?
Check the full `DEPLOYMENT_GUIDE.md` for detailed instructions!

## 🎯 Quick Commands:
```bash
# Deploy frontend
cd frontend
npm install
npm run deploy

# Populate database
cd backend
python populate_atlas.py
```
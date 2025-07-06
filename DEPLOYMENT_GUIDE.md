# 🚀 Full-Stack Deployment Guide for Owen Roth's Portfolio

## 📋 Overview
This guide will help you deploy your portfolio using:
- **Frontend**: GitHub Pages (free)
- **Backend**: Railway (free tier)
- **Database**: MongoDB Atlas (free tier)

## 🛠️ Step-by-Step Deployment

### **Phase 1: Set Up MongoDB Atlas (Database)**

1. **Create MongoDB Atlas Account**
   - Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
   - Sign up for free account
   - Create a new cluster (choose free tier)

2. **Configure Database Access**
   - Go to Database Access → Add New Database User
   - Create user with username/password
   - Grant "Read and write to any database" permission

3. **Configure Network Access**
   - Go to Network Access → Add IP Address
   - Add `0.0.0.0/0` (allow access from anywhere)

4. **Get Connection String**
   - Go to Clusters → Connect → Connect your application
   - Copy the connection string (looks like: `mongodb+srv://username:password@cluster.mongodb.net/`)

### **Phase 2: Deploy Backend to Railway**

1. **Create Railway Account**
   - Go to [Railway](https://railway.app)
   - Sign up with your GitHub account

2. **Deploy Backend**
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your portfolio repository
   - Choose the `backend` folder as root directory

3. **Set Environment Variables in Railway**
   - In Railway dashboard, go to your project → Variables tab
   - Add these environment variables:
     ```
     MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/portfolio
     DB_NAME=portfolio
     ```
   - Replace the MongoDB URL with your actual Atlas connection string

4. **Update Backend Code for Railway**
   - Railway will automatically detect it's a Python app
   - Make sure `requirements.txt` is in the backend folder
   - Railway will run your FastAPI app automatically

5. **Get Your Backend URL**
   - Once deployed, Railway will give you a URL like: `https://your-app-name.railway.app`
   - Save this URL - you'll need it for the frontend

### **Phase 3: Populate Database**

1. **Update populate_data.py**
   - Update the MongoDB connection string in your local `populate_data.py`
   - Run the script to populate your Atlas database:
     ```bash
     cd backend
     python populate_data.py
     ```

### **Phase 4: Deploy Frontend to GitHub Pages**

1. **Update Frontend Environment**
   - Edit `/frontend/.env.production`
   - Replace `REACT_APP_BACKEND_URL` with your Railway backend URL:
     ```
     REACT_APP_BACKEND_URL=https://your-app-name.railway.app
     ```

2. **Create GitHub Repository**
   - Create a new repository on GitHub
   - Push your entire project to the repository:
     ```bash
     git init
     git add .
     git commit -m "Initial commit"
     git branch -M main
     git remote add origin https://github.com/yourusername/portfolio.git
     git push -u origin main
     ```

3. **Enable GitHub Pages**
   - Go to your repository → Settings → Pages
   - Source: "Deploy from a branch"
   - Branch: `gh-pages`
   - Click Save

4. **Deploy Frontend**
   - Navigate to the frontend folder and run:
     ```bash
     cd frontend
     npm install
     npm run deploy
     ```

5. **Access Your Website**
   - Your portfolio will be available at: `https://yourusername.github.io/portfolio`

## 🔧 Alternative Backend Hosting Options

### **Option A: Render (Alternative to Railway)**
- Go to [Render](https://render.com)
- Sign up with GitHub
- Create new "Web Service"
- Connect your repository
- Set build command: `pip install -r requirements.txt`
- Set start command: `uvicorn server:app --host 0.0.0.0 --port $PORT`

### **Option B: Vercel (For FastAPI)**
- Go to [Vercel](https://vercel.com)
- Sign up with GitHub
- Import your repository
- Configure for Python runtime

## 🔍 Testing Your Deployment

1. **Test Backend API**
   - Visit: `https://your-backend-url.railway.app/api/projects`
   - Should return JSON with your projects

2. **Test Frontend**
   - Visit your GitHub Pages URL
   - Check that projects load correctly
   - Test filtering functionality

## 🐛 Common Issues & Solutions

### **CORS Issues**
If you get CORS errors, make sure your backend's CORS settings allow your GitHub Pages domain:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourusername.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### **Environment Variables**
- Make sure all environment variables are set in Railway
- Check that MongoDB connection string is correct
- Verify frontend is using the correct backend URL

## 🎉 Final Steps

1. **Custom Domain (Optional)**
   - You can add a custom domain in GitHub Pages settings
   - Add a CNAME file to your repository

2. **Update Links**
   - Update any hardcoded links in your projects
   - Test all external links work correctly

3. **Monitor & Maintain**
   - Railway free tier has usage limits
   - MongoDB Atlas free tier has storage limits
   - Monitor your usage in both platforms

## 📧 Support

If you need help with any step, check:
- Railway documentation
- MongoDB Atlas documentation
- GitHub Pages documentation

Your portfolio will be live and fully functional across all three platforms!
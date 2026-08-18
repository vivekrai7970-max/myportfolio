# Render Deployment Guide - Complete Setup

## 🚀 Quick Start

Your portfolio is ready to deploy on Render! All configuration files are prepared. Follow these steps:

---

## Step 1: Connect GitHub Repository

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Web Service"**
3. Select **"Build and deploy from a Git repository"**
4. Click **"Connect account"** to authorize GitHub
5. Find and select: **`vivekrai7970-max/myportfolio`**

---

## Step 2: Configure Web Service

Fill in the deployment form with these exact values:

### Basic Configuration

| Field | Value |
|-------|-------|
| **Name** | `myportfolio` |
| **Environment** | `Python 3` |
| **Branch** | `main` |
| **Build Command** | `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate` |
| **Start Command** | `gunicorn myportfolio.wsgi:application --log-file -` |
| **Instance Type** | Free (512 MB RAM, 0.1 CPU) |
| **Region** | Oregon (or your preference) |

### Optional Fields
- **Root Directory**: Leave empty
- **Auto-Deploy**: Enable (so it auto-deploys on git push)

---

## Step 3: Add Environment Variables

Click **"Add Environment Variable"** for each of these:

### Critical Variables (MUST ADD)

```
DJANGO_SECRET_KEY
Value: fwtsx%99st35la77#mq2o*wgvgt357v@e=6dr$+0qxc!sz4q35
Scope: Run service

DJANGO_DEBUG
Value: False
Scope: Run service

DJANGO_ALLOWED_HOSTS
Value: [YOUR_SERVICE_NAME].onrender.com
Scope: Run service
(Replace [YOUR_SERVICE_NAME] with your actual service name)

DJANGO_CSRF_TRUSTED_ORIGINS
Value: https://[YOUR_SERVICE_NAME].onrender.com
Scope: Run service
```

### Application Variables

```
PORTFOLIO_CONTACT_EMAIL
Value: vivekray7970@gmail.com
Scope: Run service

PORTFOLIO_CONTACT_RATE_LIMIT
Value: 5/h
Scope: Run service

EMAIL_BACKEND
Value: django.core.mail.backends.console.EmailBackend
Scope: Run service

DB_ENGINE
Value: sqlite3
Scope: Run service
```

---

## Step 4: Deploy

1. Click **"Create Web Service"**
2. Wait 5-10 minutes for the build and deployment
3. You'll see deployment logs in real-time
4. Once complete, you'll get a URL like: `https://myportfolio-xxx.onrender.com`

---

## Step 5: Verify Deployment

1. Visit your Render URL: `https://your-service.onrender.com`
2. You should see the animation landing page
3. Test the portfolio link and contact form

---

## 🔑 Security Notes

### Secret Key Information
- **Current Production Secret Key**: `fwtsx%99st35la77#mq2o*wgvgt357v@e=6dr$+0qxc!sz4q35`
- **Why it's needed**: Encrypts session data and CSRF tokens
- **Keep it secret**: Never commit to GitHub or share publicly
- **To rotate**: Generate a new one with: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

### ALLOWED_HOSTS Warning
⚠️ **IMPORTANT**: You MUST update `DJANGO_ALLOWED_HOSTS` with your actual Render service URL before deploying!

Format: `your-service-name.onrender.com`

---

## 📊 Deployment Configuration Details

### Build Command Breakdown
```bash
pip install -r requirements.txt          # Install Python dependencies
&& python manage.py collectstatic --noinput  # Collect static files (CSS, JS, images)
&& python manage.py migrate              # Run database migrations
```

### Start Command Breakdown
```bash
gunicorn myportfolio.wsgi:application --log-file -
│        │                              │
│        │                              └─ Log to stdout (visible in Render logs)
│        └─────── Django WSGI application
└──────────────────── Gunicorn application server
```

### Static Files
- **Middleware**: WhiteNoise (configured in settings.py)
- **Location**: `/static/` directory
- **Served by**: Gunicorn (no separate static file server needed for free tier)

### Database
- **Type**: SQLite (included, no setup needed)
- **Location**: `db.sqlite3` in project root
- **Backup**: Render's persistent disk keeps data between deployments
- **Upgrade**: Switch to PostgreSQL anytime via Render dashboard

---

## 🐛 Troubleshooting

### Deployment Fails
1. Check build logs in Render dashboard
2. Common issues:
   - Missing environment variable
   - Syntax error in settings.py
   - Invalid SECRET_KEY format

### Static Files Not Loading
1. Verify WhiteNoise middleware is enabled in settings.py
2. Check build command includes `collectstatic`
3. Restart the service

### Port Issues
- Render automatically assigns port (don't hardcode 8000)
- Django detects it via `PORT` environment variable (automatic)

### Database Migration Errors
1. Render runs migrations automatically in build command
2. If it fails, check that `manage.py migrate` is in build command

---

## 📈 Post-Deployment Steps

### 1. Configure Email (Optional)
Upgrade from console backend to real email:
- Gmail SMTP
- SendGrid
- AWS SES

Add these variables:
```
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 2. Set Custom Domain (Optional)
1. In Render dashboard → Settings
2. Click "Add Custom Domain"
3. Follow DNS configuration instructions

### 3. Monitor Errors (Optional)
Integrate with Sentry for error tracking:
```
SENTRY_DSN=your-sentry-dsn-here
```

### 4. Database Backups (Optional)
- Render maintains automatic snapshots
- Or use PostgreSQL for better backup options

---

## 📞 Support

For Render-specific issues:
- [Render Docs](https://render.com/docs)
- [Render Support](https://render.com/support)

For Django issues:
- [Django Docs](https://docs.djangoproject.com)

---

## ✅ Deployment Checklist

Before clicking "Create Web Service":

- [ ] GitHub repository is public or authorized
- [ ] Branch is set to `main`
- [ ] Build Command includes collectstatic
- [ ] Start Command is: `gunicorn myportfolio.wsgi:application --log-file -`
- [ ] DJANGO_SECRET_KEY is set (provided above)
- [ ] DJANGO_DEBUG is set to `False`
- [ ] DJANGO_ALLOWED_HOSTS matches your Render URL
- [ ] DJANGO_CSRF_TRUSTED_ORIGINS matches your Render URL
- [ ] All other environment variables are added

---

**Once deployed, your portfolio will be live on Render! 🚀**

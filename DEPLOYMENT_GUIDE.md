# Deployment & Production Configuration Guide

This guide covers how to deploy your portfolio site to production safely and securely.

## Pre-Deployment Checklist

### 1. Generate a Strong SECRET_KEY
Before deploying, generate a cryptographically secure SECRET_KEY:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Set this in your production `.env`:
```env
DJANGO_SECRET_KEY=your-generated-random-key-here
```

### 2. Security Settings for Production

In your production `.env`:
```env
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DJANGO_CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# Email Configuration (use real SMTP)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password
DEFAULT_FROM_EMAIL=noreply@yourdomain.com
PORTFOLIO_CONTACT_EMAIL=your-email@gmail.com

# Database Configuration
DB_ENGINE=sqlite3  # or 'djongo' for MongoDB
# If using MongoDB Atlas:
# DB_ENGINE=djongo
# DB_HOST=mongodb+srv://username:password@cluster.mongodb.net/
# DB_NAME=portfolio_db
```

### 3. Database Migration

Before going live, run migrations:
```bash
python manage.py migrate --noinput
```

### 4. Collect Static Files

For production, collect static files:
```bash
python manage.py collectstatic --noinput
```

## Deployment Options

### Option 1: Heroku (Easiest for Beginners)

1. Install Heroku CLI
2. Create `Procfile`:
```
web: gunicorn myportfolio.wsgi --log-file -
release: python manage.py migrate
```

3. Create `runtime.txt`:
```
python-3.11.0
```

4. Push to Heroku:
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### Option 2: AWS / DigitalOcean / Linode (Full Control)

1. Deploy to Ubuntu server
2. Install Python, PostgreSQL, Nginx
3. Use Gunicorn as WSGI server
4. Use Supervisor to manage process
5. Configure Nginx as reverse proxy
6. Set up SSL with Let's Encrypt

Example Nginx config:
```nginx
server {
    listen 443 ssl http2;
    server_name yourdomain.com;
    
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Option 3: Docker (Recommended for Complex Setups)

Create `Dockerfile`:
```dockerfile
FROM python:3.11

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD ["gunicorn", "myportfolio.wsgi", "--bind", "0.0.0.0:8000"]
```

## Security Hardening Checklist

- [x] DEBUG=False in production
- [x] SECURE_SSL_REDIRECT enabled
- [x] SECURE_HSTS enabled
- [x] X-Frame-Options set
- [x] CSP headers configured
- [x] Rate limiting on contact form (5/hour)
- [x] CSRF protection enabled
- [x] Session security enabled
- [x] Email validation
- [x] Input validation on all forms
- [x] Database indexes on frequently queried fields
- [ ] Firewall configured
- [ ] Regular backups scheduled
- [ ] Monitoring setup (error tracking, logs)

## Monitoring & Maintenance

### Set Up Error Tracking
Use Sentry for error tracking:
```bash
pip install sentry-sdk
```

Configure in `settings.py`:
```python
import sentry_sdk
sentry_sdk.init("your-sentry-dsn-here")
```

### Database Backups
If using SQLite:
```bash
# Daily backup script
cp db.sqlite3 backups/db-$(date +%Y%m%d).sqlite3
```

If using MongoDB:
```bash
mongodump --uri "your-connection-string" --out ./backups
```

### Log Monitoring
Configure logging to file or service:
```python
LOGGING = {
    'version': 1,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/portfolio/django.log',
        },
    },
    'root': {
        'handlers': ['file'],
    },
}
```

## Performance Optimization

### Caching
Enable caching for faster responses:
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
```

### CDN
Serve static files from CDN (Cloudflare, CloudFront):
- Update `STATIC_URL` to CDN URL
- Run `collectstatic` before deployment

### Database
- Monitor slow queries
- Add indexes as needed
- Regular ANALYZE/VACUUM (SQLite) or OPTIMIZE (MongoDB)

## Ongoing Maintenance

1. **Weekly:** Check error logs, monitor uptime
2. **Monthly:** Backup database, update dependencies
3. **Quarterly:** Security audit, performance review
4. **Yearly:** Major version upgrades, infrastructure review

## Support Resources

- Django Deployment Documentation: https://docs.djangoproject.com/en/stable/howto/deployment/
- Gunicorn: https://gunicorn.org/
- Nginx: https://nginx.org/
- Let's Encrypt: https://letsencrypt.org/
- MongoDB Atlas: https://www.mongodb.com/cloud/atlas

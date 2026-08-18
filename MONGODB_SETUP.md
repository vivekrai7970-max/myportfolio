# MongoDB Setup Guide

This portfolio app supports both SQLite (default) and MongoDB. By default, the app uses SQLite for easy local development. Follow this guide to switch to MongoDB.

## Option 1: Local MongoDB (Windows)

### Install MongoDB
1. Download MongoDB Community Server from https://www.mongodb.com/try/download/community
2. Run the installer and follow the setup wizard
3. MongoDB will run as a Windows Service by default

### Verify MongoDB is Running
```powershell
# Check if MongoDB service is running
Get-Service MongoDB

# If not running, start it:
Start-Service MongoDB
```

### Configure Django to Use MongoDB
1. Update your `.env` file:
```env
DB_ENGINE=djongo
DB_NAME=portfolio_db
DB_HOST=mongodb://127.0.0.1:27017/
DB_USER=
DB_PASSWORD=
DB_AUTH_SOURCE=admin
```

2. Install required dependencies:
```bash
pip install djongo pymongo
```

3. Run migrations to create MongoDB collections:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

## Option 2: MongoDB Atlas (Cloud - Recommended for Production)

MongoDB Atlas is a fully managed cloud database service with a free tier.

### Setup Steps
1. Create a free account at https://www.mongodb.com/cloud/atlas
2. Create a new cluster (free tier available)
3. Add a database user and whitelist your IP
4. Get your connection string

### Configure Django to Use MongoDB Atlas
1. Update your `.env` file:
```env
DB_ENGINE=djongo
DB_NAME=portfolio_db
DB_HOST=mongodb+srv://username:password@cluster-name.mongodb.net/
DB_USER=username
DB_PASSWORD=password
DB_AUTH_SOURCE=admin
```

2. Install dependencies:
```bash
pip install djongo pymongo
```

3. Run migrations:
```bash
python manage.py migrate
```

## Troubleshooting

### Connection Refused Error
- **Local MongoDB:** Make sure MongoDB service is running (`Start-Service MongoDB`)
- **Atlas:** Verify your IP is whitelisted in Security → Network Access

### Migration Errors with djongo
- djongo 1.3.x has known compatibility issues with Django 6.1+
- For production, consider using PyMongo directly or wait for djongo updates
- Use SQLite for now (default) and migrate later

### Switching Back to SQLite
Simply set in `.env`:
```env
DB_ENGINE=sqlite3
```

## Database Comparison

| Feature | SQLite | MongoDB |
|---------|--------|---------|
| Setup Time | Instant | 5-10 min |
| Local Development | ✓ (Built-in) | ✓ (Service/Docker) |
| Cloud Hosting | ✗ | ✓ (Atlas) |
| Scalability | Limited | Excellent |
| Flexibility | Rigid Schema | Flexible Schema |
| Production Ready | ✓ | ✓ |

## Contact Form with MongoDB
The contact form works the same with MongoDB:
1. Submit form on `/portfolio/#contact`
2. ContactMessage is stored in MongoDB collection
3. Email is sent via configured email backend
4. View messages in Django Admin

## Next Steps
- Development: Use SQLite (default, no setup needed)
- Production: Migrate to MongoDB Atlas for better scalability
- Local Testing: Use Docker for quick MongoDB setup

```bash
# Quick MongoDB with Docker
docker run -d -p 27017:27017 --name portfolio-mongo mongo:latest
```

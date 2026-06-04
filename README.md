# Shivani Sonker — Django Portfolio

## 🚀 Quick Start (Local)

```bash
# 1. Install requirements
pip install django pillow

# 2. Run migrations
python manage.py migrate

# 3. Seed initial data (aapka data already add ho jayega)
python manage.py seed_data

# 4. Create admin user (already done — skip if running first time)
python manage.py createsuperuser

# 5. Start server
python manage.py runserver
```

Open: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin
- Username: admin
- Password: admin@123  ← ZAROOR CHANGE KARNA!

---

## 🎛️ Admin Panel se kya manage kar sakte hain

| Section | Kya change ho sakta hai |
|---------|------------------------|
| Profile | Name, Photo, Bio, Email, Phone, LinkedIn, GitHub, Stats |
| Skills | Skill naam, percentage, order — skill bar aur orbit dono update |
| Experience | Work history + Education — period, role, company, description, tags |
| Projects | Title, description, tags, emoji, live link, GitHub link |
| Achievements | Icon, title, description, meta |
| Contact Messages | Inbox mein aane wale messages padhna |

---

## 📸 Photo Change Karna

Admin panel → Profile → Photo field mein apni nayi photo upload karo.
Current photo: `media/profile/shivani.jpg` (aapki uploaded photo)

---

## 🔗 Project Links Add Karna

Admin panel → Projects → koi bhi project open karo → Live URL / GitHub URL fill karo → Save.
Portfolio page pe automatically show ho jayega!

---

## 🌐 Deploy karna (Production)

1. `settings.py` mein `DEBUG = False` karo
2. `SECRET_KEY` change karo (strong random key)
3. `ALLOWED_HOSTS = ['yourdomain.com']` set karo
4. Hosting options: Railway, Render, PythonAnywhere (free), VPS

### Railway pe deploy (easiest):
```bash
pip install gunicorn
# Procfile banao: web: gunicorn portfolio.wsgi
```

---

## 📁 Project Structure

```
shivani_portfolio/
├── portfolio/          ← Django settings, urls
├── main/               ← App: models, views, admin, templates
│   ├── models.py       ← Profile, Skill, Experience, Project, Achievement
│   ├── views.py        ← Home view + Contact form handler
│   ├── admin.py        ← Admin panel configuration
│   └── templates/main/index.html  ← Main portfolio page
├── media/profile/      ← Aapki photo yahan hai
├── manage.py
└── db.sqlite3          ← Database
```

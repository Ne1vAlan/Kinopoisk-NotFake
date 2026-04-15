# Defenders | 🖥️ Project info
A project from 3 KBTU students for Web Dev
The project was created using Angular + Django + CSS + HTML

---

## 👥 Team

| Name     | Role                  | Responsibilities Back/Front |
|----------|----------------------|------------------|
| Alan | Team Lead / Full-Stack | JWT authorization (login/register),User (Django User), Setting up DRF + CORS **/** Login page,Logout, Auth service (token storage), Interceptor (substitutes a token) |
| Yegor    | Full-Stack           | The Movie Model(title, description, year, genre (FK)), (GET /, POST, DELETE , PUT /movies/) **/** Movies list page, (Buttons: Load movies, Add movie, Delete movie) |
| Yerdaulet   | Full-Stack           | Genre: name. Review: text, rating, movie (FK), user (FK). API: GET /reviews?movie_id=, POST /reviews, GET /genres **/** Movie details page. Screening: information about the film , a list of reviews. Button: Add review |

---

## ⚒️ Tech Stack

| Layer     | Technology |
|----------|-----------|
| Frontend | Angular, CSS, HTML|
| Backend  | Django + Django REST Framework |

---

## 📁 Project Structure

```
Kinopoisk-NotFake/
├── Backend/
│   ├── config/
│   │     ├── settings.py
│   │     └── urls.py
│   ├── movies/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
│
├── Frontend/
│   └── src/app/
│           ├── login/
│
│
│
└── README.md
```

---

## Frontend 

```
cd frontend

npm install

ng serve
```

## Backend

```
cd backend

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

# Group: Defenders

**Course**: Web Development

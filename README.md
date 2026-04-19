# Defenders | 🖥️ Project info
A project from 3 KBTU students for Web Dev
The project was created using Angular + Django + CSS + HTML

---

## 👥 Team

| Name     | Role                  | Responsibilities Back/Front |
|----------|----------------------|------------------|
| Alan | Team Lead / Full-Stack | JWT authorization (login/register),User (Django User), Setting up DRF + CORS **/** Login page,Logout, Auth service (token storage), Interceptor (substitutes a token), Auth Guard, Profile (User Info) |
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
│           ├── components/
│           │   ├── movie-card/
│           │   └── navbar/
│           ├── guards/
│           │   └── auth.guard.ts
│           ├── interceptors/
│           │   └── auth.interceptor.ts
│           ├── models/
│           │   ├── auth.models.ts
│           │   └── movie.model.ts
│           ├── pages/
│           │   ├── home/
│           │   ├── login/
│           │   ├── movie-detail/
│           │   ├── profile/
│           │   └── register/
│           └── services/
│               ├── auth.service.ts
│               ├── auth.spec.ts
│               └── movie.service.ts
│
├── .gitignore
└── README.md
```

---

## Frontend 

```
cd frontend

npm install

ng serve

Frontend link http://localhost:4200
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

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Movie, Genre, Review } from '../models/movie.model';

@Injectable({ providedIn: 'root' })
export class MovieService {
    private baseUrl = 'http://localhost:8000/api';

    constructor(private http: HttpClient) { }

    // Получить все фильмы
    getMovies(): Observable<Movie[]> {
        return this.http.get<Movie[]>(`${this.baseUrl}/movies`);
    }

    // Получить один фильм
    getMovie(id: number): Observable<Movie> {
        return this.http.get<Movie>(`${this.baseUrl}/movies/${id}`);
    }

    // Получить жанры
    getGenres(): Observable<Genre[]> {
        return this.http.get<Genre[]>(`${this.baseUrl}/genres`);
    }

    // Получить отзывы фильма
    getReviews(movieId: number): Observable<Review[]> {
        return this.http.get<Review[]>(`${this.baseUrl}/reviews?movie_id=${movieId}`);
    }

    // Создать отзыв
    createReview(movieId: number, text: string, rating: number): Observable<Review> {
        return this.http.post<Review>(`${this.baseUrl}/reviews/create`, {
            movie_id: movieId,
            text,
            rating
        });
    }
}

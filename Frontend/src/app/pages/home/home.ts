// Yerdaulet's part
import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; // Yegor
import { MovieService } from '../../services/movie.service';
import { Movie, Genre } from '../../models/movie.model'; // Changed by Yegor
import { MovieCard } from '../../components/movie-card/movie-card';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, FormsModule, MovieCard], // Changed by Yegor
  templateUrl: './home.html',
  styleUrl: './home.css',
})
export class Home implements OnInit {
  movies: Movie[] = [];
  filteredMovies: Movie[] = [];
  loading = true;
  searchQuery = '';

  genres: Genre[] = []; // Yegor

  newMovie = { // Yegor
    title: '',
    description: '',
    year: null as number | null,
    genre: null as number | null,
  };

  selectedVideoFile: File | null = null; // Yegor

  constructor(
    private movieService: MovieService,
    private cdr: ChangeDetectorRef
  ) {}

  ngOnInit(): void {
    this.loadMovies(); // Changed by Yegor
    this.loadGenres(); // Yegor
  }

  loadMovies(): void { // Yegor
    this.movieService.getMovies().subscribe({
      next: (data) => {
        this.movies = data;
        this.filteredMovies = data;
        this.mapGenres();
        this.loading = false;
        this.cdr.detectChanges();
      },
      error: (err) => {
        console.error('Ошибка загрузки фильмов', err);
        this.loading = false;
        this.cdr.detectChanges();
      }
    });
  }

  mapGenres(): void {
    if (this.genres.length > 0 && this.movies.length > 0) {
      const genreMap = new Map(this.genres.map(g => [g.id, g]));
      this.movies.forEach(m => {
        if (typeof m.genre === 'number') {
          m.genre = genreMap.get(m.genre) || m.genre;
        }
      });
    }
  }

  loadGenres(): void { // Yegor
    this.movieService.getGenres().subscribe({
      next: (data) => {
        this.genres = data;
        this.mapGenres();
        this.cdr.detectChanges();
      },
      error: (err) => {
        console.error('Ошибка загрузки жанров', err);
      }
    });
  }

  onSearch(query: string): void {
    this.searchQuery = query;
    this.filteredMovies = this.movies.filter(m =>
      m.title.toLowerCase().includes(query.toLowerCase())
    );
    this.cdr.detectChanges();
  }

  deleteMovie(id: number): void { // Yegor
    const confirmed = confirm('Удалить этот фильм?'); // Yegor
    if (!confirmed) return; // Yegor

    this.movieService.deleteMovie(id).subscribe({ // Yegor
      next: () => { // Yegor
        this.movies = this.movies.filter(movie => movie.id !== id); // Yegor
        this.filteredMovies = this.filteredMovies.filter(movie => movie.id !== id); // Yegor
        this.cdr.detectChanges(); // Yegor
      },
      error: (err) => { // Yegor
        console.error('Ошибка удаления фильма', err); // Yegor
        alert('Не удалось удалить фильм'); // Yegor
      }
    });
  }

  onVideoSelected(event: Event): void { // Yegor
    const input = event.target as HTMLInputElement;
    if (input.files && input.files.length > 0) {
      this.selectedVideoFile = input.files[0];
    }
  }

  createMovie(): void { // Yegor
    if (!this.newMovie.title || !this.newMovie.description || !this.newMovie.year || !this.newMovie.genre) {
      alert('Заполни title, description, year и genre');
      return;
    }

    const formData = new FormData();
    formData.append('title', this.newMovie.title);
    formData.append('description', this.newMovie.description);
    formData.append('year', String(this.newMovie.year));
    formData.append('genre', String(this.newMovie.genre));

    if (this.selectedVideoFile) {
      formData.append('video', this.selectedVideoFile);
    }

    this.movieService.createMovie(formData).subscribe({
      next: (createdMovie) => {
        this.movies = [createdMovie, ...this.movies];
        this.filteredMovies = [createdMovie, ...this.filteredMovies];
        this.mapGenres();

        this.newMovie = {
          title: '',
          description: '',
          year: null,
          genre: null,
        };
        this.selectedVideoFile = null;

        this.cdr.detectChanges();
        alert('Фильм успешно создан');
      },
      error: (err) => {
        console.error('Ошибка создания фильма', err);
        alert('Не удалось создать фильм');
      }
    });
  }
}


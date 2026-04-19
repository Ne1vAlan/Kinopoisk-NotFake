// Yerdaulet's part
import { Component, EventEmitter, Input, Output } from '@angular/core'; // Changed by Yegor
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { Movie } from '../../models/movie.model';

@Component({
  selector: 'app-movie-card',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './movie-card.html',
  styleUrl: './movie-card.css',
})
export class MovieCard {
  @Input() movie!: Movie;
  @Output() delete = new EventEmitter<number>(); // Yegor

  getAvgRating(): number {
    if (!this.movie.reviews || this.movie.reviews.length === 0) return 0;
    const sum = this.movie.reviews.reduce((acc, r) => acc + r.rating, 0);
    return Math.round((sum / this.movie.reviews.length) * 10) / 10;
  }

  getGenreName(): string { // Yegor
    if (!this.movie.genre) return 'Без жанра'; // Yegor
    if (typeof this.movie.genre === 'object') return this.movie.genre.name; // Yegor
    return 'Жанр'; // Yegor
  } // Yegor

  onDelete(event: MouseEvent): void { // Yegor
    event.stopPropagation(); // Yegor
    event.preventDefault(); // Yegor
    this.delete.emit(this.movie.id); // Yegor
  }
}
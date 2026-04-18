// Yerdaulet's part
import { Component, Input } from '@angular/core';
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

  getAvgRating(): number {
    if (!this.movie.reviews || this.movie.reviews.length === 0) return 0;
    const sum = this.movie.reviews.reduce((acc, r) => acc + r.rating, 0);
    return Math.round((sum / this.movie.reviews.length) * 10) / 10;
  }
}

import { Routes } from '@angular/router';

// Yerdaulet's part
import { MovieDetailComponent } from './pages/movie-detail/movie-detail';

export const routes: Routes = [
  // Yerdaulet's part
  { path: 'movie/:id', component: MovieDetailComponent },
];


import { Routes } from '@angular/router';
//---Alans----
import { authGuard } from './guards/auth.guard';

// Yerdaulet's and Alan`s 
export const routes: Routes = [
    {
        path: '',
        redirectTo: 'home',
        pathMatch: 'full'
    },
    {
        path: 'home',
        loadComponent: () => import('./pages/home/home').then(m => m.Home),
        canActivate: [authGuard]
    },
    {
        path: 'movie/:id',
        loadComponent: () => import('./pages/movie-detail/movie-detail').then(m => m.MovieDetailComponent),
        canActivate: [authGuard]
    },
    {
        path: 'login',
        loadComponent: () => import('./pages/login/login').then(m => m.LoginComponent)
    },
    {
        path: 'register',
        loadComponent: () => import('./pages/register/register').then(m => m.Register)
    },
    {
        path: '**',
        redirectTo: 'home'
    },
    {
        path: 'profile',
        loadComponent: () => import('./pages/profile/profile').then(m => m.ProfileComponent),
        canActivate: [authGuard]
    }
];
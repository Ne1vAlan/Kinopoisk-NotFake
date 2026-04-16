export interface Genre {
    id: number;
    name: string;
}
export interface Review {
    id: number;
    text: string;
    rating: number;
    movie: number;
    user: string;
    created_at: string;
}
export interface Movie {
    id: number;
    title: string;
    description: string;
    year: number;
    genre: Genre;
    reviews: Review[];
}

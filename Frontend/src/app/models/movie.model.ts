// Yerdaulet's part
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
  // changed by Yegor
  genre?: number | Genre | null;
  reviews?: Review[];
  // added by Yegor 
  video?: string | null;
}

export interface LoginRequest {
    username: string;
    password: string;
}

export interface RegisterRequest {
    username: string;
    password: string;
}

export interface AuthResponse {
    message: string;
    token: string;
    username: string;
}

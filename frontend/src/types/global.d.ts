export {};

declare global {
  interface Todo {
    id: string;
    text: string;
    isEditing: boolean;
    createdAt: string;
  }
  interface Post {
    id: number;
    coverImage: string;
    categories: string[];
    gallery: string[];
    title: string;
    body: string;
    creatorLink: string;
    creatorName: string;
    createdAt: string;
    updatedAt: string;
    likes: number;
  }
}

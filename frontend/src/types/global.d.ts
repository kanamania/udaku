export {};

declare global {
  interface Creator {
    id: string;
    name: string;
    image: string;
    link: string;
    createdAt: string;
  }
  interface Comment {
    id: string;
    postId: string;
    description: string;
    creatorLink: string;
    creatorName: string;
    createdAt: string;
    replies: Comment[];
 }
  interface Post {
    id: number;
    slug: string;
    coverImage: string;
    categories: string[];
    gallery: string[];
    name: string;
    body: string;
    description: string;
    creator: Creator;
    createdAt: string;
    updatedAt: string;
    likes: number;
    comments: Comment[];
  }
}

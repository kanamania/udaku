import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { RootState } from '../../config/store';

const initialState = {
  posts: [] as Post[],
};

export const postsSlice = createSlice({
  name: 'posts',
  initialState,
  reducers: {
      likePost: (state, action: PayloadAction<Post>): void => {
      state.posts.find((post: Post) => {
        if (post.id === action.payload.id) {
          post.likes += 1;
        }
      });
    },
  },
});

export const {
  likePost,
} = postsSlice.actions;

export const selectPosts = (state: RootState) => state.posts;

export default postsSlice.reducer;

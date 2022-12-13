import { Action, ThunkAction, configureStore } from '@reduxjs/toolkit';
import {postsSlice} from '../pages/posts/postsSlice';

export const store = configureStore({
  reducer: {
    posts: postsSlice.reducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;

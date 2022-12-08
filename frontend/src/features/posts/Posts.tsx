import * as React from 'react';
import styles from './Posts.module.css';
import { useAppSelector } from '../../hooks/useAppSelector';
import {selectPosts} from './postsSlice';
import PostListing from '../post-single/PostListing';

const Posts = (): JSX.Element => {
  const { posts } = useAppSelector(selectPosts);

  return (
      <div className={styles.container}>
          {posts.map((post: any) => {
              return (
                  <PostListing key={post.id} />
              );
          })}
      </div>
  );
}

export default Posts;

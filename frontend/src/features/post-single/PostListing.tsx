import * as React from 'react';
import styles from './PostListing.module.css';
import { useAppSelector } from '../../hooks/useAppSelector';
import {selectPosts} from '../posts/postsSlice';

const PostListing = (): JSX.Element => {
  const { posts } = useAppSelector(selectPosts);

  return (
      <div className={styles.container}>

      </div>
  );
};

export default PostListing;

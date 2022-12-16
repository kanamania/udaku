import * as React from 'react';
import styles from './Posts.module.css';
import PostListing from '../post-single/PostListing';
import DataService from '../../services/data.service'
import {useEffect, useState} from 'react';

const Posts = (): JSX.Element => {
    const [posts, setPosts] = useState(false);
    const [content, setContent] = useState(false);

    useEffect(() => {
        DataService.getPosts().then(
            (response) => {
                let _content:Element[];
                setPosts(response.data);
                response.data.map((post: any) => {
                    // @ts-ignore
                    _content = [_content, <PostListing key={post.id}/>];
                })
                setContent(_content);
            },
            (error) => {
                const _content =
                    (error.response && error.response.data) ||
                    error.message ||
                    error.toString();
                setContent(_content);
            }
        );
    }, []);
    return (
        <div className={styles.container}>
            {posts.map((post: any) => {
                return (
                    <PostListing post={post} key={post.id}/>
                );
            })}
        </div>
    );
}

export default Posts;

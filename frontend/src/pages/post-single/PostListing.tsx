import * as React from 'react';
import {Link} from 'react-router-dom';

const PostListing = (props: { post: Post; key: number}) => {
  const article = props.post;

  return (
    <div className="article-preview">
      <div className="article-meta">
        <a>
          <img alt={article.name} src={article.creator.image} />
        </a>

        <div className="info">
          <a className="author">
            {article.creator.name}
          </a>
          <span className="date">
            {new Date(article.createdAt).toDateString()}
          </span>
        </div>

        <div className="pull-xs-right">
          <button className="btn btn-sm btn-outline-primary">
              <i className="ion-heart"/>
              {article.likes}
          </button>
        </div>
      </div>

      <Link to={`article/${article.slug}`} className="preview-link">
        <h1>{article.name}</h1>
        <p>{article.description}</p>
        <span>Read more...</span>
        <ul className="tag-list">
          {
            article.categories.map(cat => {
              return (
                <li className="tag-default tag-pill tag-outline" key={cat}>
                  {cat}
                </li>
              )
            })
          }
        </ul>
      </Link>
    </div>
  );
};

export default PostListing;

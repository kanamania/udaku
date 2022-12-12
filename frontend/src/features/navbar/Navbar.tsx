import * as React from 'react';
import { useAppDispatch } from '../../hooks/useAppDispatch';
import {NavLink} from 'react-router-dom';

const Navbar = (): JSX.Element => {
  const dispatch = useAppDispatch();


  // noinspection CheckTagEmptyBody
    return (
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container">
            <a className="navbar-brand" href="#">Udaku</a>
            <button className="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                    aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                    <li className="nav-item">
                        <NavLink to="/articles">Articles</NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink to="/comments">Comments</NavLink>
                    </li>
                </ul>
                <form className="d-flex">
                    <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
                        <button className="btn btn-outline-success" type="submit">Search</button>
                </form>
            </div>
        </div>
    </nav>
  );
};

export default Navbar;

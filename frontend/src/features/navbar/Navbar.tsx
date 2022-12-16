import * as React from 'react';
import {NavLink} from 'react-router-dom';

const Navbar = (): JSX.Element => {
    // noinspection CheckTagEmptyBody
    return (
        <nav className="navbar navbar-expand bg-danger">
            <div className="container">
                <NavLink to={"/"} className="navbar-brand">Udaku</NavLink>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse"
                        data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                        aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                        <li className="nav-item">
                            <NavLink className="text-light" to={"/articles"}>Articles</NavLink>
                        </li>
                        <li className="nav-item">
                            <NavLink className="text-light" to={"/comments"}>Comments</NavLink>
                        </li>
                        <li className="nav-item">
                            <NavLink className="text-light" to={"/login"}>Login</NavLink>
                        </li>
                        <li className="nav-item">
                            <NavLink className="text-light" to={"/register"}>Register</NavLink>
                        </li>
                        <li className="nav-item">
                            <NavLink className="text-light" to={"/profile"}>Profile</NavLink>
                        </li>
                        {currentUser ? (
                            <>
            <li className="nav-item">
              <NavLink to={"/profile"} className="nav-link">{currentUser.username}</NavLink>
            </li>
            <li className="nav-item">
              <NavLink href="/login" className="nav-link" onClick={logOut}>Logout</NavLink>
            </li>
            </>
        ) : (
          <>
            <li className="nav-item">
              <NavLink to={"/login"} className="nav-link">Login</NavLink>
            </li>
            <li className="nav-item">
              <NavLink to={"/register"} className="nav-link">Register</NavLink>
            </li>
            <li className="nav-item">
                <NavLink className="text-light" to={"/forgot"}>Forgot Password</NavLink>
            </li>
            <li className="nav-item">
                <NavLink className="text-light" to={"/reset"}>Reset Password</NavLink>
            </li>
          </>
        )}

                    </ul>
                    <form className="d-flex">
                        <input className="form-control form-control-lg" type="search" placeholder="Search" aria-label="Search"/>
                    </form>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;

import * as React from 'react';
import {Routes, Route, Link, NavLink} from 'react-router-dom';

import Home from './pages/home/Home';
import Articles from './pages/articles/Articles';
import Comments from './pages/comments/Comments';
import NoMatch from './pages/no-match/NoMatch';
import Navbar from './features/navbar/Navbar';
import Register from './pages/auth/Register';
import Login from './pages/auth/Login';
import Profile from './pages/auth/Profile';
import Reset from './pages/auth/Reset';
import Forgot from './pages/auth/Forgot';

const App: React.FC = () => {
    return (
        <>
            <div className="">
                <Navbar />
                <div className="container main py-5">
                    <Routes>
                        <Route index element={<Home/>}/>
                        <Route path="/articles" element={<Articles/>}/>
                        <Route path="/comments" element={<Comments/>}/>
                        <Route path="/profile" element={<Profile/>}/>
                        <Route path="/login" element={<Login/>}/>
                        <Route path="/register" element={<Register/>}/>
                        <Route path="/forgot" element={<Forgot/>}/>
                        <Route path="/reset" element={<Reset/>}/>
                        <Route path="*" element={<NoMatch/>}/>
                    </Routes>
                </div>
            </div>
        </>
    );
};

export default App;

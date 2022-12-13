import * as React from 'react';
import {Routes, Route, Link, NavLink} from 'react-router-dom';

import Home from './pages/home/Home';
import Articles from './pages/articles/Articles';
import Comments from './pages/comments/Comments';
import NoMatch from './pages/no-match/NoMatch';
import Navbar from './features/navbar/Navbar';

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
                        <Route path="*" element={<NoMatch/>}/>
                    </Routes>
                </div>
            </div>
        </>
    );
};

export default App;

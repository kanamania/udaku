import * as React from 'react';
import {Routes, Route, Link} from 'react-router-dom';

import {Loader} from './features/loader/Loader';
import Home from './pages/home/Home';
import Articles from './pages/articles/Articles';
import Comments from './pages/comments/Comments';
import NoMatch from './pages/no-match/NoMatch';

const Posts = React.lazy(() => import('./features/posts/Posts'));
const Navbar = React.lazy(() => import('./features/navbar/Navbar'));

const App: React.FC = () => {
    return (
        <>
            <React.Suspense fallback={<Loader/>}>
                <Navbar/>
                <Posts/>
            </React.Suspense>
            <Routes>
                <Route index element={<Home/>}/>
                <Route path="articles" element={<Articles/>}/>
                <Route path="comments" element={<Comments/>}/>
                <Route path="*" element={<NoMatch/>}/>
            </Routes>

        </>
    );
};

export default App;

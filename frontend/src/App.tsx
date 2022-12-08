import * as React from 'react';
import { Loader } from './features/loader/Loader';
const Posts = React.lazy(() => import('./features/posts/Posts'));
const Navbar = React.lazy(() => import('./features/navbar/Navbar'));

const App: React.FC = () => {
  return (
    <React.Suspense fallback={<Loader />}>
      <Navbar />
      <Posts />
    </React.Suspense>
  );
};

export default App;

import * as React from 'react';
import App from './App';
import {createRoot} from 'react-dom/client';
import {Provider} from 'react-redux';
import {store} from './config/store';
import './index.styles.css';
import './index.scripts';
import {BrowserRouter} from 'react-router-dom';

const root = createRoot(document.getElementById('root'));

root.render(
    <Provider store={store}>
        <BrowserRouter>
            <App/>
        </BrowserRouter>
    </Provider>
);

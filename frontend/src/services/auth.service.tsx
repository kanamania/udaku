import axios from "axios";
import authHeader from './auth-header';
import {API_URL} from '../config/constants';

const register = (data: object) => {
  return axios.post(API_URL + "auth/register", data);
};
const forgot = (data: object) => {
  return axios.post(API_URL + "auth/forgot", data);
};
const reset = (data: object) => {
  return axios.post(API_URL + "auth/reset", data);
};

const profile = () => {
  return axios.get(API_URL + "auth/me", {headers: authHeader()});
};

const login = (data: object) => {
  return axios
    .post(API_URL + "token", data)
    .then((response) => {
      if (response.data.access) {
        localStorage.setItem("token", JSON.stringify(response.data));
        profile().then(response => {
            localStorage.setItem("user", JSON.stringify(response.data));
        });
      }

      return response.data;
    });
};

const logout = () => {
  localStorage.removeItem("token");
  localStorage.removeItem("user");
};


export default {
  register,
  login,
  logout,
  profile,
  forgot,
  reset,
};

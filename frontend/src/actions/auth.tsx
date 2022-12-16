import {
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT,
  SET_MESSAGE, RESET_SUCCESS, RESET_FAIL, FORGOT_SUCCESS, FORGOT_FAIL,
} from "./types";

import AuthService from "../services/auth.service";

export const register = (username: any, email: any, password: any) => (dispatch: (arg0: { type: string; payload?: any; }) => void) => {
  return AuthService.register({username, email, password}).then(
    (response) => {
      dispatch({
        type: REGISTER_SUCCESS,
      });

      dispatch({
        type: SET_MESSAGE,
        payload: response.data.message,
      });

      return Promise.resolve();
    },
    (error) => {
      const message =
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();

      dispatch({
        type: REGISTER_FAIL,
      });

      dispatch({
        type: SET_MESSAGE,
        payload: message,
      });

      return Promise.reject();
    }
  );
};

export const login = (username: any, password: any) => (dispatch: (arg0: { type: string; payload?: any; }) => void) => {
  return AuthService.login({username, password}).then(
    (data) => {
      dispatch({
        type: LOGIN_SUCCESS,
        payload: { user: data },
      });

      return Promise.resolve();
    },
    (error) => {
      const message =
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();

      dispatch({
        type: LOGIN_FAIL,
      });

      dispatch({
        type: SET_MESSAGE,
        payload: message,
      });

      return Promise.reject();
    }
  );
};
export const reset = (username: any) => (dispatch: (arg0: { type: string; payload?: any; }) => void) => {
  return AuthService.login({username}).then(
    (data) => {
      dispatch({
        type: RESET_SUCCESS,
        payload: { user: data },
      });

      return Promise.resolve();
    },
    (error) => {
      const message =
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();

      dispatch({
        type: RESET_FAIL,
      });

      dispatch({
        type: SET_MESSAGE,
        payload: message,
      });

      return Promise.reject();
    }
  );
};

export const forgot = (username: any) => (dispatch: (arg0: { type: string; payload?: any; }) => void) => {
  return AuthService.forgot({username}).then(
    (data) => {
      dispatch({
        type: FORGOT_SUCCESS,
        payload: { user: data },
      });

      return Promise.resolve();
    },
    (error) => {
      const message =
        (error.response &&
          error.response.data &&
          error.response.data.message) ||
        error.message ||
        error.toString();

      dispatch({
        type: FORGOT_FAIL,
      });

      dispatch({
        type: SET_MESSAGE,
        payload: message,
      });

      return Promise.reject();
    }
  );
};

export const logout = () => (dispatch: (arg0: { type: string; }) => void) => {
  AuthService.logout();

  dispatch({
    type: LOGOUT,
  });
};
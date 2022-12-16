import {
    POST_COMMENT_SUCCESS,
    POST_COMMENT_FAIL,
    POST_COMMENT_REACTION_SUCCESS,
    POST_COMMENT_REACTION_FAIL,
    POST_REACTION_SUCCESS,
    POST_REACTION_FAIL,
} from "../actions/types";

const initialState = { posts: null };

export default function (state = initialState, action: { type: any; payload: any; }) {
  const { type, payload } = action;

  switch (type) {
    case POST_COMMENT_SUCCESS:
      return {
        ...state,
        posts: payload.,
      };
    case POST_COMMENT_FAIL:
      return {
        ...state,
        isLoggedIn: false,
      };
    case POST_REACTION_SUCCESS:
      return {
        ...state,
        isLoggedIn: true,
        token: payload.token,
        user: payload.user,
      };
    case POST_REACTION_FAIL:
      return {
        ...state,
        isLoggedIn: false,
        token: null,
        user: null,
      };
    case POST_COMMENT_REACTION_SUCCESS:
      return {
        ...state,
        isLoggedIn: false,
        token: null,
        user: null,
      };
    case POST_COMMENT_REACTION_FAIL:
      return {
        ...state,
        isLoggedIn: false,
        token: null,
        user: null,
      };
    default:
      return state;
  }
}

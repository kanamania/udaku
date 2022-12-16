import axios from "axios";
import authHeader from "./auth-header";
import {API_URL} from '../config/constants';


const getPosts = () => {
  return axios.get(API_URL + "posts");
};

const getPostComments = (post_id: number) => {
  return axios.get(API_URL + "comments", { params: {post_id} });
};

const postPostComment = (data: object) => {
  return axios.post(API_URL + "comments", data, { headers: authHeader() });
};

const postPostReaction = (data: object) => {
  return axios.post(API_URL + "post-reactions", data,{ headers: authHeader() });
};
const postPostCommentReaction = (data: object) => {
  return axios.post(API_URL + "comment-reaction", data,{ headers: authHeader() });
};

export default {
  getPosts,
  getPostComments,
  postPostComment,
  postPostReaction,
  postPostCommentReaction
};

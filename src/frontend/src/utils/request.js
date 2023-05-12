import axios from "axios";

const service = axios.create({
  baseURL: '/',
  // 超时时间 => 15s
  timeout: 15 * 1000,
});

export default service;

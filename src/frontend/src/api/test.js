import request from "@/utils/request";

/**
 * 带参数的Get请求
 *
 * @param {*} data
 */
export const getParam = (data) => {
  return request({
    url: "/请求路径",
    method: "GET",
    params: data,
  });
};

/**
 * 不带参数的GET请求
 *
 * @returns
 */
export const getNoParam = () => {
  return request({
    url: "/请求路径",
    method: "GET",
  });
};

/**
 * 带参数的POST请求
 *
 * @param {*} data
 * @returns
 */
export const postParam = (data) => {
  return request({
    url: "/请求路径",
    method: "POST",
    data,
  });
};

/**
 * Restful风格的GET请求
 */
export const getRestful = (id) => {
  return request({
    url: `/请求路径/${id}`,
    method: "GET",
  });
};

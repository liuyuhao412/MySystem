import request from '@/api/request'
import base from '@/api/base';
import { AxiosResponse } from 'axios';

/* 
 * 登录
 * data: { username, password }
 */
export function LoginApi(params: object): Promise<AxiosResponse> {
  return request({
    url: base.login,
    method: 'post',
    data: params,
  })
}

/* 
*发送验证码
*data：{email}
*/
export function SendCodeApi(params: object): Promise<AxiosResponse> {
  return request({
    url: base.send_code,
    method: 'post',
    data: params,
  })
}
/* 
*注册
*data：{username,code,password,confirmpassword}
*/
export function RegisterApi(params: object): Promise<AxiosResponse> {
  return request({
    url: base.register,
    method: "post",
    data: params,
  })
}


# API文档
## 1. 共用

### 1.1 登录 API

#### 请求

- **URL**: `/login`
- **Method**: `POST`

#### 参数

| Name     | Type   | Description |
|----------|--------|-------------|
| username | string | 用户名         |
| password | string | 密码          |

#### 响应

| Status Code | Message  |
|-------------|----------|
| 200         | 登录成功     |
| 400         | 用户名不能为空  |
| 400         | 密码不能为空   |
| 401         | 用户名或密码错误 |

### 1.2 发送验证码 API

#### 请求

- **URL**: `/send_code`
- **Method**: `POST`

#### 参数

| Name  | Type   | Description |
|-------|--------|-------------|
| email | string | 用户邮箱        |

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 邮件发送成功  |
| 400         | 邮箱不能为空  |
| 400         | 邮箱格式不正确 |
| 409         | 该邮箱已经存在 |

### 1.3 用户注册 API

#### 请求

- **URL**: `/register`
- **Method**: `POST`

#### 参数

| Name            | Type   | Description |
|-----------------|--------|-------------|
| email           | string | 用户邮箱        |
| code            | string | 验证码         |
| password        | string | 密码          |
| confirmPassword | string | 确认密码        |

#### 响应

| Status Code | Message               |
|-------------|-----------------------|
| 200         | 用户注册成功                |
| 400         | 请输入邮箱                 |
| 400         | 邮箱格式不正确               |
| 400         | 请输入验证码                |
| 400         | 请输入密码                 |
| 400         | 密码需由8位以上、大小写字母、特殊字符组成 |
| 400         | 请再次输入密码               |
| 401         | 验证码错误                 |
| 401         | 两次密码不一致               |
| 409         | 邮箱已经存在                |
| 500         | 用户注册失败                |

### 1.4 更新密码 API

#### 请求

- **URL**: `/update_password`
- **Method**: `POST`

#### 参数

| Name            | Type | Description |
|-----------------|------|-------------|
| username        | str  | 用户名         |
| newPassword     | str  | 新密码         |
| confirmPassword | str  | 确认新密码       |

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 修改密码成功  |
| 400         | 请输入密码   |
| 401         | 两次密码不一致 |
| 500         | 修改密码失败  |

## 2. 管理员

### 2.1 获取用户数量 API

#### 请求

- **URL**: `/get_user_count`
- **Method**: `GET`

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 请求成功    |

### 2.2 获取用户登录日志数量 API

#### 请求

- **URL**: `/get_user_log_count`
- **Method**: `GET`

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 请求成功    |

### 2.3 获取用户列表 API

#### 请求

- **URL**: `/get_user_list`
- **Method**: `GET`

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 请求成功    |

### 2.4 获取用户登录日志 API

#### 请求

- **URL**: `/get_user_log`
- **Method**: `GET`

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 请求成功    |

### 2.5 获取用户 API

#### 请求

- **URL**: `/admin_user/get_user`
- **Method**: `POST`

#### 参数

| Name     | Type   | Description |
|----------|--------|-------------|
| page     | int    | 页码          |
| limit    | int    | 每页数量        |
| username | string | 用户名关键词      |
| role     | string | 角色关键词       |

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 请求成功    |

### 2.6 添加用户 API

#### 请求

- **URL**: `/admin_user/add_user`
- **Method**: `POST`

#### 参数

| Name     | Type   | Description |
|----------|--------|-------------|
| username | string | 用户名         |
| role     | string | 角色          |

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 添加用户成功  |
| 400         | 请输入用户名  |
| 400         | 请选择角色   |
| 409         | 用户名已经存在 |
| 500         | 添加用户失败  |

### 2.7 修改用户 API

#### 请求

- **URL**: `/admin_user/update_user`
- **Method**: `POST`

#### 参数

| Name     | Type   | Description |
|----------|--------|-------------|
| user_id  | int    | 用户ID        |
| username | string | 用户名         |
| role     | string | 角色          |

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 修改用户成功  |
| 400         | 请输入用户名  |
| 500         | 修改用户失败  |

### 2.8 删除用户 API

#### 请求

- **URL**: `/admin_user/delete_user`
- **Method**: `POST`

#### 参数

| Name    | Type | Description |
|---------|------|-------------|
| user_id | int  | 用户ID        |

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 删除用户成功  |
| 500         | 删除用户失败  |

### 2.9 重置用户密码 API

#### 请求

- **URL**: `/admin_user/set_password`
- **Method**: `POST`

#### 参数

| Name    | Type | Description |
|---------|------|-------------|
| user_id | int  | 用户ID        |

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 重置密码成功  |
| 500         | 重置密码失败  |

### 2.10 获取日志 API

#### 请求

- **URL**: `/admin_log/get_log`
- **Method**: `POST`

#### 参数

| Name     | Type   | Description |
|----------|--------|-------------|
| page     | int    | 页码          |
| limit    | int    | 每页数量        |
| username | string | 用户名关键词      |
| role     | string | 角色关键词       |

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 请求成功    |

### 2.11 删除日志 API

#### 请求

- **URL**: `/admin_log/delete_log`
- **Method**: `POST`

#### 参数

| Name   | Type | Description |
|--------|------|-------------|
| log_id | int  | 日志ID        |

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 日志删除成功  |
| 500         | 日志删除失败  |

### 2.12获取打卡记录 API

#### 请求

- **URL**: `/admin_get_record`
- **Method**: `POST`

#### 参数

| Name     | Type | Description |
|----------|------|-------------|
| username | str  | 用户名 (可选)    |
| page     | int  | 页数 (可选)     |
| limit    | int  | 每页记录数 (可选)  |
| month    | str  | 月份 (可选)     |
| day      | str  | 日 (可选)      |

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 获取记录成功  |

### 2.13删除打卡记录 API

#### 请求

- **URL**: `/admin_delete_record`
- **Method**: `POST`

#### 参数

| Name      | Type | Description |
|-----------|------|-------------|
| record_id | int  | 记录ID        |

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 删除记录成功  |
| 500         | 删除记录失败  |

## 3. 用户
### 3.1 获取登录时间 API

#### 请求

- **URL**: `/get_login_time`
- **Method**: `POST`

#### 参数

| Name     | Type | Description |
|----------|------|-------------|
| username | str  | 用户名         |

#### 响应

| Status Code | Message         |
|-------------|-----------------|
| 200         | 您上次登录的时间：[登录时间] |
| 400         | 需要提供用户名         |
| 500         | 获取登录时间失败        |

### 3.2 获取打卡信息 API

#### 请求

- **URL**: `/get_mark_card_info`
- **Method**: `POST`

#### 参数

| Name     | Type | Description        |
|----------|------|--------------------|
| username | str  | 用户名                |
| date     | str  | 日期（格式：'%Y年%m月%d日'） |

#### 响应

| Status Code | Message  |
|-------------|----------|
| 200         | 获取打卡信息成功 |
| 500         | 获取打卡信息失败 |

### 3.3 上午打卡 API

#### 请求

- **URL**: `/mark_card_am`
- **Method**: `POST`

#### 参数

| Name           | Type | Description        |
|----------------|------|--------------------|
| username       | str  | 用户名                |
| date           | str  | 日期（格式：'%Y年%m月%d日'） |
| morningChecked | bool | 上午打卡状态             |

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 打卡成功    |
| 500         | 打卡失败    |

### 3.4 下午打卡 API

#### 请求

- **URL**: `/mark_card_pm`
- **Method**: `POST`

#### 参数

| Name           | Type | Description        |
|----------------|------|--------------------|
| username       | str  | 用户名                |
| date           | str  | 日期（格式：'%Y年%m月%d日'） |
| eveningChecked | bool | 下午打卡状态             |

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 打卡成功    |
| 500         | 打卡失败    |

### 3.5 获取打卡记录 API

#### 请求

- **URL**: `/get_record`
- **Method**: `POST`

#### 参数

| Name     | Type | Description |
|----------|------|-------------|
| username | str  | 用户名         |
| page     | int  | 页数          |
| limit    | int  | 每页记录数       |
| month    | str  | 月份          |
| day      | str  | 日           |

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 获取记录成功  |

### 3.6 删除打卡记录 API

#### 请求

- **URL**: `/delete_record`
- **Method**: `POST`

#### 参数

| Name      | Type | Description |
|-----------|------|-------------|
| record_id | int  | 记录ID        |

#### 响应

| Status Code | Message |
|-------------|---------|
| 200         | 删除记录成功  |
| 500         | 删除记录失败  |


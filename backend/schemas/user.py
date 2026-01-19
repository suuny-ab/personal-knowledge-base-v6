from pydantic import BaseModel, EmailStr, Field

# 登录请求模型
class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)

# 注册请求模型
class RegisterRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr
    password: str = Field(..., min_length=6)
    confirm_password: str


# 用户信息模型
class UserInfo(BaseModel):
    id: str
    username: str
    email: str

# 登录成功响应模型  
class LoginSuccessResponse(BaseModel):
    success: bool = True
    user: UserInfo
    access_token: str
    token_type: str = "bearer"

class LoginErrorResponse(BaseModel):
    success: bool = False
    error: str
    code: str = "AUTH_FAILED"


# 测试代码思路（不是实际运行）
login_data = {
    "email": "test@example.com",
    "password": "123456"
}

# 用你的模型创建实例
request = LoginRequest(**login_data)
print(request.email)  # 应该输出 test@example.com
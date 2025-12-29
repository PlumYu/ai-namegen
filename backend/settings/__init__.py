DB_URL = "mysql+aiomysql://root:root@127.0.0.1:3306/ainame?charset=utf8mb4"

# 邮箱相关配置
# QQ 邮箱账号（完整的邮箱地址，用于 SMTP 登录验证，需与 MAIL_FROM 一致）
MAIL_USERNAME="xxxx@qq.com"
# QQ 邮箱 SMTP 授权码（不是 QQ 登录密码，需在 QQ 邮箱设置中开启 SMTP 后生成）
MAIL_PASSWORD="xxxx"
# 邮件发送者邮箱（需与 MAIL_USERNAME 一致，否则 QQ 邮箱会拒绝发送请求）
MAIL_FROM="xxxx@qq.com"
# SMTP 服务端口（587 对应 MAIL_STARTTLS=True，QQ 邮箱推荐端口，不可随意修改）
MAIL_PORT=587
# QQ 邮箱 SMTP 服务器地址（固定为 smtp.qq.com，其他邮箱需对应修改，如 163 邮箱为 smtp.163.com）
MAIL_SERVER="smtp.qq.com"
# 邮件发送者显示名称（收件人看到的「发件人」名称，可自定义，支持英文/中文）
MAIL_FROM_NAME="AI name generator verification code"
# 备用发送者邮箱（留空即可，当前配置中未启用，无需填写）
MAIL_FROM_EMAIL=""
# 启用 STARTTLS 加密（587 端口必须设为 True，用于建立安全连接，防止数据泄露）
MAIL_STARTTLS=True
# 禁用 SSL/TLS 加密（587 端口必须设为 False，与 MAIL_STARTTLS 二选一，465 端口才需设为 True）
MAIL_SSL_TLS=False
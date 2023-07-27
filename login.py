from hugchat.login import Login

# 登入huggingface授权huggingchat
sign = Login(input('输入你的邮箱：'), input('输入你的密码：'))
cookies = sign.login()

# 保存cookies至 usercookies/<email>.json
sign.saveCookiesToDir('usercookies')

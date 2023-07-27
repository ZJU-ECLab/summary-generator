# Summary Generator

## 使用方法

克隆此仓库至本地：

```bash
git clone https://github.com/ZJU-ECLab/summary-generator
cd summary-generator
```

安装所需依赖：

```bash
pip install -r requirements.txt
```

登录hugging face账号（需要提前在[hugging face网站](https://huggingface.co)上注册）：

```bash
python login.py # 输入账号和密码即可，登录信息会保存在usercookies目录下
```

运行生成脚本：

```bash
python generate.py # 等待登录，之后会出现提示语，粘贴概要即可
```

脚本会生成一个英文概括，并尝试用deepl翻译。

若需要使用脚本翻译，需要在[这里](https://github.com/OwO-Network/DeepLX/releases/tag/v0.8.0)下载deepl翻译服务端程序并运行。

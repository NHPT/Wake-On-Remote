from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse,FileResponse
from fastapi.staticfiles import StaticFiles
import re
import socket
import uvicorn

def is_valid_host(host: str) -> bool:
    # 匹配有效的 IP 地址
    ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    # 匹配有效的域名
    domain_pattern = r"^(?!:\/\/)([a-zA-Z0-9][a-zA-Z0-9\-.]{1,61}[a-zA-Z0-9]\.)+[a-zA-Z]{2,}$"

    # 检查是否为有效的 IP 地址
    if re.match(ip_pattern, host):
        return True
    # 检查是否为有效的域名
    if re.match(domain_pattern, host):
        return True
    return False

def is_valid_mac(mac: str) -> bool:
    # 根据常见的 MAC 地址格式检查是否有效
    if len(mac) == 17 and mac.count(":") == 5 and all(c in "0123456789ABCDEFabcdef:" for c in mac):
        return True
    elif len(mac) == 12 and all(c in "0123456789ABCDEFabcdef" for c in mac):
        return True
    else:
        return False

# 发送唤醒数据包
def wake(host: str, mac: str, port: int) -> str:
    # 检查 host 的格式
    if not is_valid_host(host):
         return JSONResponse({"code":0,"msg":"Host 格式错误"})
    # 检查 MAC 地址的格式
    if not is_valid_mac(mac):
        return JSONResponse({"code":0,"msg":"MAC 格式错误"})
    
    # 转换 MAC 地址为字符串
    mac_str = mac.upper().replace(":", "")
    
    if host and mac:
        # 模拟发送唤醒请求的逻辑
        data = b"\xFF\xFF\xFF\xFF\xFF\xFF" + bytes().fromhex(mac_str) * 16
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
        try:
            s.sendto(data,(host,port))
            s.close()
            return JSONResponse({"code":1,"msg":"唤醒请求发送成功"})
        except:
            s.close()
            return JSONResponse({"code":0,"msg":"唤醒请求发送失败，请检查IP地址或域名"})
    else:
        return JSONResponse({"code":0,"msg":"参数错误"})
    
app = FastAPI()
# 将 /static 路径映射到 assets 目录
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

@app.get("/")
async def index():
    return FileResponse("index.html")

# 定义路由处理函数
@app.post("/api/wake")
async def wake_device(request: Request):
    data = await request.json()
    host = data.get('host')
    mac = data.get('mac')
    port = int(data.get('port', 8))
    return wake(host,mac,port)

uvicorn.run(app, host="127.0.0.1", port=80, headers=[("Server", "fuck")])

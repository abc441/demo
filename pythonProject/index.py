import os
import json
import base64
import sqlite3
from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES
import re
# Chrome 文件路径
chrome_cookies_path =os.path.join(os.getenv('LOCALAPPDATA'), 'QianniuTemp')
chrome_local_state_path = os.path.join(os.getenv('LOCALAPPDATA'), 'QianniuTemp', 'LocalPrefs.json')
pattern = re.compile(r'^\d+$')

# 获取加密密钥
def get_encryption_key():
    with open(chrome_local_state_path, 'r', encoding='utf-8') as f:
        local_state = json.loads(f.read())

    encrypted_key = base64.b64decode(local_state.get('os_crypt', {}).get('encrypted_key'))
    encrypted_key = encrypted_key[5:]  # 去掉前缀 'DPAPI'
    return CryptUnprotectData(encrypted_key, None, None, None, 0)[1]

# 解密 Cookie 值
def decrypt_cookie(encrypted_value, key):
    try:
        if encrypted_value.startswith(b'v10') or encrypted_value.startswith(b'v11'):
            # AES 解密
            iv = encrypted_value[3:15]  # 提取 IV
            payload = encrypted_value[15:]  # 提取加密数据
            cipher = AES.new(key, AES.MODE_GCM, iv)
            decrypted_data = cipher.decrypt(payload)
            return decrypted_data[:-16].decode('utf-8')  # 去掉尾部认证标签
        else:
            # DPAPI 解密
            return CryptUnprotectData(encrypted_value, None, None, None, 0)[1].decode('utf-8')
    except Exception as e:
        print(f"解密失败: {e}")
        return None

# 主函数
def main():
    # 获取加密密钥
    Cookies=""
    key = get_encryption_key()

    # 连接到 Chrome 的 Cookie 数据库
    lib=enumerate_numeric_directories(chrome_cookies_path)
    for i in lib:
        cookie=""
        conn = sqlite3.connect(i+"\\Network\\Cookies")

        cursor = conn.cursor()

    # 查询 Cookie
        cursor.execute('SELECT host_key, name, encrypted_value FROM cookies')
        for host_key, name, encrypted_value in cursor.fetchall():
            decrypted_value = decrypt_cookie(encrypted_value, key)
            if host_key==".taobao.com":
                cookie=cookie+name+"="+decrypted_value+"; "
        Cookies=Cookies+cookie+"\n"


    # 关闭连接
        cursor.close()
        conn.close()
    print(Cookies)
    # 文件路径
    file_path = 'output.txt'



    # 打开文件并写入数据
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(Cookies)  # 写入多行数据

    print(f"数据已写入文件: {file_path}")
# 枚举纯数字目录
def enumerate_numeric_directories(directory):
    numeric_dirs = []
    try:
        # 遍历目标目录
        for entry in os.listdir(directory):
            full_path = os.path.join(directory, entry)
            # 检查是否为目录且目录名为纯数字
            if os.path.isdir(full_path) and pattern.match(entry):
                numeric_dirs.append(full_path)
    except FileNotFoundError:
        print(f"目录未找到: {directory}")
    except Exception as e:
        print(f"枚举目录时出错: {e}")
    return numeric_dirs
if __name__ == '__main__':
    main()

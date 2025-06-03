# 配置管理
def config_manager():
    config = {}

    def set_config(key, value):
        config[key] = value

    def get_config(key):
        return config.get(key)

    return set_config, get_config

# 创建一个配置管理器实例
set_config, get_config = config_manager()

# 设置配置
set_config("server_address", "127.0.0.1")
set_config("port", 8080)

# 获取配置
print(get_config("server_address"))  # 输出 "127.0.0.1"
print(get_config("port"))  # 输出 8080
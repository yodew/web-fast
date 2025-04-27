from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # 数据库配置
    DATABASE_URL: str = "sqlite:///./test.db"
    
    # 应用配置
    APP_NAME: str = "Web Fast"
    APP_VERSION: str = "0.1.0"
    
    # 其他配置
    DEBUG: bool = False
    SECRET_KEY: str = "your-secret-key"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
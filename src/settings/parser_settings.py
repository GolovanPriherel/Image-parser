from pydantic import Field, BaseSettings


class ParserSettings(BaseSettings):
    # deviantart_website_url: str = Field(env="WEBSITE_URL", default="https://www.deviantart.com/")

    # px500_website_url: str = Field(env="500PX_SITE", default="https://500px.com/popular")
    # px500_authorization_url: str = Field(env="500PX_AUTHORIZATION_URL", default="https://500px.com/login?r=%2Fsignup")
    # px500_login: str = Field(env="500PX_EMAIL", default="ymu21653@nezid.com")
    # px500_password: str = Field(env="500PX_PASSWORD", default="500PX_password")

    rule34_website: str = Field(env="RULE34_WEBSITE", default="https://rule34.xxx/")
    rule34_website_search: str = Field(env="RULE34_WEBSITE_SEARCH", default="https://rule34.xxx/index.php?page=post&s=list&tags=female+-futa+-gay+-scat+-vore+-vore_sex++&pid=0")

    proxy_url: str = Field(env="PROXY_URL", default="https://free-proxy-list.net/")
    check_ip: str = Field(env="CHECK_IP_URL", default="http://icanhazip.com")

    parser_backend_url: str = Field(env="PARSER_URL", default="parser_backend_service")

    m1_driver_path: str = Field(default="data/chrome_driver/chromedriver_m1")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

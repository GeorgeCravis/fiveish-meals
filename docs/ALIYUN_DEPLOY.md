# 阿里云 OSS 发布

本项目的静态 PWA 现在通过 GitHub Actions 同步到阿里云 OSS。

## 需要的 GitHub Secrets

- `ALIYUN_OSS_BUCKET`
- `ALIYUN_OSS_REGION`
- `ALIYUN_OSS_ACCESS_KEY_ID`
- `ALIYUN_OSS_ACCESS_KEY_SECRET`

## OSS 侧准备

1. 创建 OSS bucket。
2. 开启静态网站托管，首页设为 `index.html`。
3. 错误页也指向 `index.html`，用于单页应用回退。
4. 如果要绑定自定义域名，按阿里云要求完成域名配置与备案。

## 发布流程

1. 推送到 `main`。
2. GitHub Actions 自动安装 `ossutil`。
3. 工作流先同步 `frontend/prototype/` 到临时发布目录。
4. 再清空 bucket 根目录对象并重新上传。

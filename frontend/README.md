# frontend

前端开发区。

## 当前文件

- `prototype/index.html`：当前主原型，Claude 风格，功能最完整。
- `prototype/manifest.webmanifest`：PWA manifest。
- `prototype/assets/icons/`：PWA 图标。
- `prototype/versions/`：历史/对比版本。
- `app/`：正式前端工程预留目录。
- `public/`：正式前端静态资源预留目录。

后续工程化时，请从 `prototype/index.html` 拆分到 `app/`，不要直接在历史版本文件里继续堆逻辑。

## 协作日志

继续修改主原型前，请先读：

```text
../docs/CHANGELOG.md
```

Open Design 或 Codex 改完 `prototype/index.html` 后，都应在该日志追加一条记录，
避免后续导出覆盖已发布的抽卡、切日、更新提示等逻辑。

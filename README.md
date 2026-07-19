# 5分料理Plus

「5分料理 / Fiveish Meals」PWA 项目工作区。

核心理念：用 5 分钟时间，做只值 5 分的料理。产品面向不想花太多时间做饭、但仍希望自己做得健康一点的人。语气可以轻度吐槽，但整体仍应像一个正经健康工具。

## 目录结构

- `frontend/`：前端开发区。正式工程放 `frontend/app`，当前可运行原型放 `frontend/prototype`。
- `backend/`：后端开发区。后续菜单持久化、账号、发布 API 放这里。
- `ui/`：UI 设计资产区。图标、参考图、设计稿导出物放这里。
- `data/`：数据源镜像区。开发用菜谱、菜单、哲理文本放这里，根目录原始资料保留不动。
- `docs/`：交接说明、产品逻辑、发布计划。

## 当前可打开原型

主原型：

```text
frontend/prototype/index.html
```

版本对比：

```text
frontend/prototype/versions/comparison.html
frontend/prototype/versions/version-claude.html
frontend/prototype/versions/version-bmw.html
frontend/prototype/versions/version-energetic.html
```

后续开发请以 `frontend/prototype/index.html` 的 Claude 风格版本作为当前产品基线。

## 给后续 Codex 的入口

先读：

```text
docs/CHANGELOG.md
docs/CODEX_HANDOFF.md
```

`docs/CHANGELOG.md` 是 Codex 和 Open Design 共用的变更日志。任何工具继续改
`frontend/prototype/index.html` 前都应先读它，并在改完后追加记录。

# START HERE：5分料理Plus

这个目录已经整理成后续 Open Design / Codex 协作的项目根目录。

## 新项目打开后先做什么

1. 工作目录设为：

   ```text
   C:\5分料理Plus
   ```

2. 先读详细交接：

   ```text
   docs/CODEX_HANDOFF.md
   ```

3. 当前可运行原型入口：

   ```text
   frontend/prototype/index.html
   ```

4. 当前产品基线是 Claude 风格版本，不要从旧 Open Design 内部目录继续开发。

## 当前目录分工

- `frontend/`：前端开发。当前 HTML 原型在 `frontend/prototype/`，后续正式工程建议放 `frontend/app/`。
- `backend/`：后端开发预留。菜单持久化、账号、API、部署脚本放这里。
- `ui/`：UI 资产。图标、设计导出、视觉参考放这里。
- `data/`：开发用数据镜像。根目录保留原始资料，不要直接改坏源文件。
- `docs/`：交接说明、产品逻辑、发布计划。

## 后续 Codex 的第一句话建议

```text
请以 C:\5分料理Plus 为工作目录，先阅读 START_HERE.md 和 docs/CODEX_HANDOFF.md，然后继续把 frontend/prototype/index.html 工程化为 PWA，并准备 GitHub Pages 发布。
```

## 关键规则

- 同一天菜单应固定，除非用户主动重抽、换组合、加菜或减菜。
- 菜单数据来源以 `菜品菜单.xlsx` 为准。
- 五分哲理由 `motto.txt` 提供，不要自己生成。
- 当前 UI 基线是 Claude 风格：温暖纸面、克制分隔、简洁顺序流程。



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

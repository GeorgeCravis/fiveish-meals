# Codex 交接说明：5分料理 / Fiveish Meals

## 必读协作日志

继续修改前请先读：

```text
C:\5分料理Plus\docs\CHANGELOG.md
```

`docs/CHANGELOG.md` 是 Codex 和 Open Design 共用的变更日志。任何工具改完
`frontend/prototype/index.html`、发布配置、抽卡逻辑或 PWA 更新逻辑后，都应追加记录，
避免两个软件互相覆盖对方改动。

## 当前状态

当前已经完成一个高保真 HTML PWA 原型，迁移到：

```text
C:\5分料理Plus\frontend\prototype\index.html
```

这是当前主版本，采用 Claude 风格：温暖纸面、克制分隔、安静但带轻微幽默感。另有 BMW / Energetic 对比版本保留在 `frontend/prototype/versions/`。

## 产品逻辑已完成的部分

- 首页：电饭煲图标、标题、slogan、早饭/午饭/晚饭并排选择、开始按钮。
- 当天菜单固定：同一天重复打开不会重新抽菜；只有主动重抽、换组合、加菜、减菜才会改变当天菜单。
- 首次当天开始：如果当天还没决定菜单，会先进入“昨天剩余食材”选择页。
- 剩余食材优先：用户选择昨天剩余食材后，抽菜单时优先匹配包含这些食材/菜品的组合。
- 抽卡页与汇总页已合并：顶部显示“五分哲思”，下方按早饭/午饭/晚饭展示菜品卡。
- 翻卡逻辑：按列同步翻开，即三餐的第一张卡一起翻、第二张卡一起翻。
- 每餐编辑：
  - 重抽本餐
  - 换组合
  - 加菜
  - 减菜模式
- 加菜/换组合使用底部托盘，不修改菜品目录，只修改当天菜单结果。
- 做菜指引：固定四步。
  - 步骤 0：备菜，显示不需要准备和需要提前解冻的食材。
  - 步骤 1：将食材放进电饭煲。
  - 步骤 2：将食材放进空气炸锅。
  - 步骤 3：将食材放进电磁炉。
- 5分Timer：机械表盘计时器，5 分钟一圈；内侧上方有 60 秒一圈的小秒盘，指针用动画帧平滑走动。
- 菜谱库：同页拆成“菜单组合”和“菜品库”两个模块。
- 五分哲理：右上角入口可查看全部哲理。
- 右上角工具：返回上一步、菜品清单、五分哲理、重新开始。
- PWA 图标：欢快冒热气电饭煲，已生成 SVG 和 PNG 多尺寸。

## 数据来源

原始资料仍保留在根目录：

```text
C:\5分料理Plus\motto.txt
C:\5分料理Plus\recipes.ts
C:\5分料理Plus\定食菜谱.txt
C:\5分料理Plus\定食菜谱2.txt
C:\5分料理Plus\菜品菜单.xlsx
C:\5分料理Plus\要求1.txt
```

开发镜像位于：

```text
C:\5分料理Plus\data\source\
```

当前前端原型已经把 `菜品菜单.xlsx` 的结构固化进 HTML：

- `菜单` sheet：菜单组合规则。
- `菜品` sheet：具体菜品，字段包括 `name / tool / label / defrost`。

菜单抽取逻辑：

1. 先从 `菜单` sheet 选择一个组合，例如 `鲜虾云吞+[蔬菜]`。
2. 没有中括号的是实际菜名。
3. `[蔬菜]` 这类中括号内容是 label，从 `菜品` sheet 随机/优先选择具有该 label 的具体菜品。
4. 当前版本已改成确定性抽取：默认按“日期 + 餐次 + 重抽次数”生成，避免同一天刷新变菜。

## 重要实现细节

`frontend/prototype/index.html` 是单文件原型，主要逻辑都在内联脚本里。后续工程化时建议拆成：

- `frontend/app/src/data/`：菜单、菜品、哲理数据读取和转换。
- `frontend/app/src/state/`：今日菜单、重抽 nonce、剩余食材选择、历史返回。
- `frontend/app/src/screens/`：Home、Leftovers、MenuDraw、CookingGuide、Timer、RecipeLibrary、Mottos、Install。
- `frontend/app/src/components/`：MealCard、BottomTray、ToolButtons、WatchTimer、IconButton。

本地持久化要点：

- 今日菜单应保存为稳定快照：`templateId + dishIds`。
- 打开页面时必须按 `dishIds` 还原，不能重新解析 `[label]`。
- 重抽、换组合、加菜、减菜后要保存当天菜单。
- 重新开始按钮只回首页，不应清掉当天菜单。

## 后端建议

`backend/` 目前是空的开发区。建议后端先做轻量 API，功能边界如下：

- 菜品/菜单读取：
  - `GET /api/dishes`
  - `GET /api/menu-templates`
  - `GET /api/mottos`
- 今日菜单：
  - `GET /api/today-menu?date=YYYY-MM-DD`
  - `POST /api/today-menu/decide`
  - `POST /api/today-menu/reroll`
  - `PATCH /api/today-menu`
- 剩余食材：
  - `GET /api/leftovers?from=YYYY-MM-DD`
  - `POST /api/leftovers`

第一版如果不做账号，可以继续用浏览器本地存储。若需要多设备同步，再引入用户标识或 GitHub OAuth。

## 发布建议

短期：

1. 将 `frontend/prototype/index.html` 作为静态 PWA 发布到 GitHub Pages。
2. 同步复制 `manifest.webmanifest` 和 `assets/icons/`。
3. Pages 入口可以先直接指向 `frontend/prototype/`。

中期：

1. 在 `frontend/app` 建正式前端工程。
2. 将单文件 HTML 拆成组件。
3. 从 `data/source/菜品菜单.xlsx` 生成 JSON，避免在运行时解析 Excel。
4. 增加测试：今日菜单固定、重抽刷新、剩余食材优先、加菜/减菜不改目录。

## 不要踩的坑

- 不要把 `[蔬菜]` 这类 label 显示给用户，它只是菜单解析规则。
- 不要在页面加载时调用随机抽菜单逻辑，否则会破坏“同一天菜单固定”。
- 不要让“重新开始”清空当天菜单。
- 不要把“加菜/减菜”写回菜品目录，它只修改当天菜单结果。
- 打趣文案只应来自 `motto.txt`，不要临时编造。
- 非汇总/菜单页面尽量保持正经工具语气。

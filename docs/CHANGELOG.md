# Change Log

This file is the shared edit log for Codex, Open Design, and any future tooling.
Before changing the prototype, read this file and append a dated entry after the
change. Keep entries factual: what changed, where, why, and whether it was
published.

## 2026-07-19 - Codex - published 2026.07.19.2 leftovers entry and guide text

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Changes:

- Moved the "昨天的剩菜" entry from the home meal panel into the top-right
  shortcut icon group.
- Removed the right-side appliance illustrations from the cooking guide.
- Rewrote guide step 0 as "预制菜准备 / 提前解冻" text. The prep list now uses
  selected dishes whose `tool` value is `"-"`, and the thaw list uses the
  selected dishes whose `defrost` value is true.
- Removed the large "电饭煲 / 空气炸锅 / 电磁炉" labels from steps 1, 2, and 3;
  dish names and tool names are highlighted inside the instruction text instead.
- Bumped app version from `2026.07.19.1` to `2026.07.19.2` for update detection.

Behavior preserved:

- 15:00 daily reset.
- `fiveishMeals.dailyMenu.v3`.
- Shared label draw cache and concrete-dish category lock.
- Update-check banner and cache-clearing update button.
- Dish-image service worker cache and idle-time warmup.

## 2026-07-19 - Codex - published 2026.07.19.1 cooking guide refinements

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Changes:

- Redrew the 5-minute timer face as a complete centered dial and removed the
  remaining visual blank area from the former small-dial layout.
- Removed the visible "四步做菜指引" label while keeping a screen-reader title for
  the cooking guide panel.
- Changed guide steps 1, 2, and 3 to use the same large numeric style as step 0.
- Added right-side appliance illustrations for the rice cooker, air fryer, and
  induction cooker guide steps.
- Bumped app version from `2026.07.18.2` to `2026.07.19.1` for update detection.

Behavior preserved:

- 15:00 daily reset.
- `fiveishMeals.dailyMenu.v3`.
- Shared label draw cache and concrete-dish category lock.
- Update-check banner and cache-clearing update button.
- Dish-image service worker cache and idle-time warmup.

## 2026-07-18 - Codex - published 2026.07.18.2 interaction refinements

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `frontend/prototype/dish-cache-sw.js`
- `docs/CHANGELOG.md`

Changes:

- Added a dish-image service worker cache and idle-time image warmup so the
  large `assets/dishes/plain/*.png` files load from local cache after first
  use.
- Simplified the cooking timer by removing the small second dial and keeping
  only the large dial.
- Moved the "yesterday leftovers" step out of the required daily draw flow and
  added it as a subtle secondary entry on the home screen.
- Changed the draw-page add/remove dish controls to clear `+` and `-` symbol
  buttons while preserving their labels and behavior.

Behavior preserved:

- 15:00 daily reset.
- `fiveishMeals.dailyMenu.v3`.
- Shared label draw cache and concrete-dish category lock.
- Update-check banner and cache-clearing update button.

## 2026-07-18 - Codex - restored Open Design Claude visuals and published 2026.07.18.1

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Design changes:

- Restored the visual language from the Open Design / Claude style layer:
  paper-warm background grid, quieter palette, flatter buttons, lighter cards,
  smaller radius scale, and calmer shadows.
- Reworked the final Codex CSS layer into a layout bridge instead of a new
  visual direction.
- Kept the current mobile-first layout refinements for the home screen, draw
  results, cooking guide, recipe library, motto card, and safe-area spacing.
- Preserved the iOS home-screen rice-cooker icon fallback.

Behavior preserved:

- 15:00 daily reset.
- `fiveishMeals.dailyMenu.v3`.
- Shared label draw cache.
- Concrete-dish category lock.
- Update-check banner.

Versioning:

- Bumped app version from `2026.07.16.1` to `2026.07.18.1` so installed PWAs
  can detect the update after publish.
- Published through the GitHub Pages workflow path `frontend/prototype` and
  removed an accidental root-level `index.html` / `version.json` publish copy
  from the intermediate commit.

## 2026-07-16 - Codex - took over visual design and published 2026.07.16.1

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Behavior and design changes:

- Started Codex-owned design work for the app instead of treating Open Design
  as the primary implementation source.
- Added a focused CSS ownership layer for a warmer, mobile-first Fiveish Meals
  app surface.
- Unified the home screen, draw results, cooking guide, recipe library, and
  motto card around the same colors, cards, buttons, radius, and shadows.
- Kept the existing app flow and business logic intact; this is a visual
  consolidation, not an algorithm rewrite.
- Preserved the iOS home-screen rice-cooker icon fallback.
- Bumped app version from `2026.07.15.2` to `2026.07.16.1` so installed PWAs
  can detect the update.

Verification:

- Syntax-checked the inline script with Node.
- Checked mobile home, draw, cooking guide, motto, and recipe screens in the
  browser at `390x844`.
- Checked desktop home layout at `1280x800`.
- Confirmed no horizontal overflow on the mobile draw screen.
- Confirmed previously required logic is still present:
  - 15:00 daily reset.
  - `fiveishMeals.dailyMenu.v3`.
  - shared label draw cache.
  - concrete dish category lock.
  - update-check banner.
- Published the confirmed files to GitHub Pages.

## 2026-07-15 - Codex - confirmed and published Open Design 2026.07.15.2

Files confirmed for publish:

- `frontend/prototype/index.html`
- `frontend/prototype/apple-touch-icon.png`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Confirmation:

- Reviewed Open Design's recent local preview copy at
  `C:\Users\lzz\Documents\5分料理plus\current-design.html`.
- Synced the preview copy into the published prototype.
- Confirmed Open Design's visible changes:
  - `五分哲理` page changed from a full list to a single highlighted motto card.
  - Added a `下一条` button that randomly switches to another motto.
  - Added `activeMotto` state and random motto selection logic for that page.
- Preserved the iOS home-screen icon fallback from `2026.07.15.1`:
  - Root `frontend/prototype/apple-touch-icon.png`.
  - HTML apple-touch-icon links pointing to `apple-touch-icon.png`.
- Confirmed previously required logic is still present:
  - 15:00 daily reset.
  - `fiveishMeals.dailyMenu.v3`.
  - shared label draw cache.
  - concrete dish category lock.
  - update-check banner.
- Bumped app version from `2026.07.15.1` to `2026.07.15.2` so installed PWAs
  can detect the update.
- Published the confirmed files to GitHub Pages.

## 2026-07-15 - Codex - fixed iOS home-screen icon fallback

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/apple-touch-icon.png`
- `frontend/prototype/assets/icons/apple-touch-icon.png`
- `frontend/prototype/assets/icons/favicon-32.png`
- `frontend/prototype/assets/icons/fiveish-meals-icon-192.png`
- `frontend/prototype/assets/icons/fiveish-meals-icon-512.png`
- `frontend/prototype/assets/icons/fiveish-meals-icon-1024.png`
- `frontend/prototype/assets/icons/fiveish-meals-icon.svg`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Confirmation:

- Checked the published page's iOS icon declaration.
- Confirmed `assets/icons/apple-touch-icon.png` is a steaming rice-cooker icon,
  not the fallback numeric `5` icon.
- Found the traditional root fallback path
  `https://georgecravis.github.io/fiveish-meals/apple-touch-icon.png` returned
  404, which can make iOS fall back to a generated icon in some save-to-home
  flows.
- Added `frontend/prototype/apple-touch-icon.png` as a root fallback copy of
  the rice-cooker icon.
- Changed the HTML apple-touch-icon links to explicitly point to the root
  fallback with `sizes="180x180"`.
- Bumped app version from `2026.07.14.1` to `2026.07.15.1` so installed PWAs
  can detect the update.
- Published the confirmed files to GitHub Pages.

## 2026-07-14 - Codex - confirmed and published Open Design 2026.07.14.1

Files confirmed for publish:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Confirmation:

- Reviewed Open Design's recent local preview copy at
  `C:\Users\lzz\Documents\5分料理plus\current-design.html`.
- Synced the preview copy into the published prototype.
- Confirmed Open Design's visible changes:
  - Cooking page eyebrow changed from `做菜指引` to `5分Timer`.
  - Cooking page section title was removed for a more compact timer-focused layout.
  - Prep step heading was simplified from `步骤 0 / 备菜` to a large `0`.
  - Cooking-guide instruction sentences now deduplicate repeated dish names.
- Confirmed previously required logic is still present:
  - 15:00 daily reset.
  - `fiveishMeals.dailyMenu.v3`.
  - shared label draw cache.
  - concrete dish category lock.
  - update-check banner.
- Bumped app version from `2026.07.09.4` to `2026.07.14.1` so installed PWAs
  can detect the update.
- Published the confirmed files to GitHub Pages.

## 2026-07-13 - Codex - confirmed and published Open Design 2026.07.09.4

Files confirmed for publish:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `frontend/prototype/assets/dishes/plain/*.png`
- `docs/CHANGELOG.md`
- `.gitignore`

Confirmation:

- Reviewed Open Design's recent local change recorded as `2026.07.09.4`.
- Confirmed the inline script syntax-checks with Node.
- Confirmed all 34 dish ids have matching `assets/dishes/plain/*.png` images.
- Confirmed previously required logic is still present:
  - 15:00 daily reset.
  - `fiveishMeals.dailyMenu.v3`.
  - shared label draw cache.
  - concrete dish category lock.
  - update-check banner.
- Excluded `output/` image-generation intermediate files from publish by adding it to `.gitignore`.
- Published the confirmed files to GitHub Pages.

## 2026-07-09 - Open Design - one-screen cooking page

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `frontend/prototype/assets/dishes/plain/*.png`

Behavior changes:

- 做菜指引页改为一屏布局：做菜步骤和 5 分钟计时在同一视口内压缩展示，取消该页内部滚动条。
- 移动端做菜页改为上下各半的紧凑布局，计时器表盘按可用高度缩小，保留开始/重置按钮。
- 菜品卡优先使用 `assets/dishes/plain/{dishId}.png` 的菜品图片，并保留 SVG fallback。
- Bumped app version to `2026.07.09.4`.

## 2026-07-09 - Codex - confirmed and published Open Design changes

Files confirmed for publish:

- `START_HERE.md`
- `docs/CHANGELOG.md`
- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `frontend/prototype/assets/icons/fiveish-meals-icon.svg`
- `frontend/prototype/assets/icons/fiveish-meals-icon-192.png`
- `frontend/prototype/assets/icons/fiveish-meals-icon-512.png`
- `frontend/prototype/assets/icons/fiveish-meals-icon-1024.png`
- `frontend/prototype/assets/icons/apple-touch-icon.png`
- `frontend/prototype/assets/icons/favicon-32.png`

Confirmation:

- Reviewed Open Design's 2026-07-09 changelog entries through version
  `2026.07.09.3`.
- Confirmed the inline script syntax-checks with Node.
- Confirmed previously required logic is still present:
  - 15:00 daily reset.
  - `fiveishMeals.dailyMenu.v3`.
  - shared label draw cache.
  - concrete dish category lock.
  - update-check banner.
- Published the confirmed files to GitHub Pages.

## 2026-07-09 - Open Design - recipe library tabs and mobile tray sizing

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- Open Design preview copy: `C:\Users\lzz\Documents\5分料理plus\current-design.html`

Behavior changes:

- Made the recipe library tabs strictly scoped: `菜品` only shows individual dishes, while `菜单` only shows menu combinations.
- Removed the unused `清空` and `安装入口` buttons from the recipe library toolbar.
- Enlarged the mobile swap/add tray into a bottom drawer with a minimum height of `66svh` and vertical scrolling options.
- Bumped app version from `2026.07.09.2` to `2026.07.09.3`.

Verification:

- Synced the updated main prototype into the Open Design preview copy.
- Syntax-check inline script with Node.

## 2026-07-09 - Open Design - mobile chip/header and reveal playback fixes

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- Open Design preview copy: `C:\Users\lzz\Documents\5分料理plus\current-design.html`

Behavior changes:

- Restored the home breakfast/lunch/dinner chips to a compact three-column inline layout on mobile.
- Added mobile top safe spacing so the fixed quick-action buttons no longer overlap draw-page mottos or cooking-guide content.
- Changed draw-card reveal playback so the flip animation is recorded per reset-day and only plays once per day, including when returning via `返回上一步`.
- Removed the reveal class after playback completes so hidden/showing the draw page does not retrigger CSS animation.
- Bumped app version from `2026.07.09.1` to `2026.07.09.2`.

Verification:

- Synced the updated main prototype into the Open Design preview copy.
- Syntax-check inline script with Node.

## 2026-07-09 - Open Design - mobile cooking flow refinements

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `frontend/prototype/assets/icons/fiveish-meals-icon.svg`
- `frontend/prototype/assets/icons/fiveish-meals-icon-192.png`
- `frontend/prototype/assets/icons/fiveish-meals-icon-512.png`
- `frontend/prototype/assets/icons/fiveish-meals-icon-1024.png`
- `frontend/prototype/assets/icons/apple-touch-icon.png`
- `frontend/prototype/assets/icons/favicon-32.png`
- Open Design preview copy: `C:\Users\lzz\Documents\5分料理plus\current-design.html`

Behavior changes:

- Combined the cooking guide and five-minute timer into one cooking page.
- Changed the recipe library from side-by-side menu/dish modules to product tabs for `菜品` and `菜单`.
- Updated the PWA desktop icon steam strokes so all three steam lines lean in the same direction. The home-screen inline rice-cooker illustration was not changed.
- Tightened mobile draw-card widths so four dish cards can fit without horizontal scrolling in normal mobile widths.
- Stabilized the mobile home meal chips so breakfast/lunch/dinner no longer clip on narrow screens.
- Changed draw-page buttons from `重新抽全部` to `全部重抽`, and from `开始做菜` to `开始`.
- Leaving the draw page now clears transient draw UI state such as the tray and remove mode, while preserving the saved daily menu.
- Kept the 15:00 daily reset, `fiveishMeals.dailyMenu.v3`, shared label draw cache, concrete-dish category lock, and app update banner behavior from the previous Codex changes.
- Bumped app version from `2026.07.08.3` to `2026.07.09.1`.

Verification:

- Regenerated PWA PNG icons from the updated SVG.
- Synced the updated main prototype into the Open Design preview copy.
- Syntax-check inline script with Node.

## 2026-07-08 - Codex - concrete dish locks category

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Behavior changes:

- Extended shared draw resolution. A concrete dish now also locks its own
  category label for the same draw.
- Example: if one card is the concrete dish `虾饼`, and another card is the
  category token `[小食]`, the `[小食]` card resolves to `虾饼`.
- This is implemented by remembering a concrete dish's `label` in the same
  shared label cache previously used for `[label]` tokens.
- Bumped app version from `2026.07.08.2` to `2026.07.08.3`, so installed PWAs
  that already have update checking can prompt users to refresh.

Verification:

- Syntax-check inline script with Node.
- Standalone rule check: template `["虾饼"]` followed by template `["[小食]"]`
  resolves both cards to `虾饼`.

## 2026-07-08 - Codex

Published site:

- Public repo: `https://github.com/GeorgeCravis/fiveish-meals`
- GitHub Pages: `https://georgecravis.github.io/fiveish-meals/`
- Pages source: `.github/workflows/pages.yml` uploads `frontend/prototype`.

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `frontend/prototype/.nojekyll`
- `.gitignore`

Behavior changes:

- Added `.nojekyll` so GitHub Pages serves the static prototype directly.
- Added `Image-gen-url.txt` to `.gitignore`, alongside the existing API key
  ignore rules, so local image-generation config is not published.
- Changed daily menu cache prefix from `fiveishMeals.dailyMenu.v2` to
  `fiveishMeals.dailyMenu.v3`.
- Changed the daily menu reset boundary from midnight to 15:00 local time.
  Before 15:00, the app still uses the previous menu date; at and after 15:00,
  it starts a new menu date.
- Added shared label resolution during menu draws. If two cards in the same
  draw use the same label token, such as `[硬菜]`, they resolve to the same
  concrete dish. Example: if lunch `[硬菜]` resolves to chicken wings, dinner
  `[硬菜]` also uses chicken wings.
- Applied shared label resolution to initial draw, full reroll, single-meal
  reroll, and manual menu-template changes.
- Added in-app update checking:
  - Current app version is stored in `APP_VERSION` in `index.html`.
  - Published version is stored in `frontend/prototype/version.json`.
  - The app checks for updates on startup, when it returns to the foreground,
    on window focus, and every five minutes.
  - If `version.json` is newer than `APP_VERSION`, a bottom update banner is
    shown.
  - Tapping the update button clears available browser caches and reloads with
    a version query parameter.

Verification:

- Extracted and syntax-checked the inline script with Node.
- Verified date-key behavior with a standalone Node check:
  - `2026-07-08 14:59` maps to `2026-07-07`.
  - `2026-07-08 15:00` maps to `2026-07-08`.
- Verified same-label draw behavior with a standalone Node check: lunch and
  dinner `[硬菜]` resolve to the same dish.
- Verified GitHub Pages deployment succeeded.
- Verified live page returns HTTP 200 and contains:
  - `fiveishMeals.dailyMenu.v3`
  - `MENU_RESET_HOUR = 15`
  - `checkForAppUpdate`
  - `update-banner`
- Verified live `version.json` returns valid JSON with version `2026.07.08.2`.

Notes for Open Design:

- Do not overwrite `frontend/prototype/index.html` from an older design export
  without preserving the behavior changes above.
- If Open Design exports a new visual version, merge it onto the current
  `index.html` or explicitly re-apply:
  - 15:00 daily reset.
  - shared label draw cache.
  - `version.json` update check.
  - bottom update banner DOM/CSS.
- When publishing a new version, bump both `APP_VERSION` in
  `frontend/prototype/index.html` and `version` in
  `frontend/prototype/version.json`.


## 2026-07-19 - Codex

Files changed:

- rontend/prototype/index.html`r
- rontend/prototype/version.json`r
- docs/CHANGELOG.md`r

Behavior changes:

- Kept the '昨天的剩菜' entry only on the home screen and hid it on other pages.
- Simplified recipe library menu cards to show only the combo name and meal source.
- Deduplicated repeated combo labels in the recipe library display.
- Changed recipe library cards so clicking again toggles the item back to enabled.
- Disabled dishes and menu templates are now excluded from draw pools.


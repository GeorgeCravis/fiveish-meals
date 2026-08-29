# Change Log

This file is the shared edit log for Codex, Open Design, and any future tooling.
Before changing the prototype, read this file and append a dated entry after the
change. Keep entries factual: what changed, where, why, and whether it was
published.

## 2026-08-29 - Codex - published 2026.08.29.9 timer title and draw motto

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Changes:

- Added a visible `5分Timer` title directly above the timer clock face without
  restoring the old `计时` label.
- Removed the draw-page `5分哲理` card treatment so the motto sits directly on
  the page background as a centered, lightweight text treatment.
- Bumped app version from `2026.08.29.8` to `2026.08.29.9` for update detection.

## 2026-08-29 - Codex - published 2026.08.29.8 image cache and motto cycle

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/assets/dishes/plain/*.png`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Changes:

- Confirmed the dish-image service worker caches local PNG dish images after
  first fetch, but reduced first-load cost by resizing 34 local dish images to a
  mobile-friendly maximum edge of 640 px.
- Reduced dish image payload from about 40 MB to about 4 MB while keeping the
  same local file paths for existing PWA image references.
- Tightened draw-page meal action focus handling so tap/click actions release
  the visual pressed state after reroll, add, combo, remove, and remove-dish
  actions.
- Hid the `昨天的剩菜` top-right entry outside the home screen.
- Changed the `5分哲理` page to use a shuffled round bag: every motto appears
  once before the next shuffled round begins.
- Bumped app version from `2026.08.29.7` to `2026.08.29.8` for update detection
  and dish-cache cache busting.

## 2026-08-29 - Codex - published 2026.08.29.7 timer and leftovers polish

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Changes:

- Made recipe-library menu combination cards render source and pairing text on
  one line, with long combinations truncated instead of wrapping vertically.
- Reduced the gap between the draw-page `5分哲理` panel and the meal results.
- Changed the draw-page primary action label from `开始` to `做菜`.
- Reordered the timer screen so the clock appears before cooking steps, removed
  the visible `5分Timer` and `计时` labels there, and changed the idle timer
  button label from `开始` to `计时`.
- Vertically centered cooking-step text and tightened guide-card vertical
  spacing.
- Made `选择昨天剩菜` first load yesterday's saved menu, then fall back to the
  most recent previous locally saved menu when yesterday has no record.
- Bumped app version from `2026.08.29.6` to `2026.08.29.7` for update detection.

Notes:

- Leftover history is still local to the same browser/device because the app has
  no shared backend storage.

## 2026-08-29 - Codex - prepared 2026.08.29.6 draw controls polish

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Changes:

- Renamed the draw-page motto panel label from `五分哲思` to `5分哲理`.
- Compactly aligned each meal label with its reroll, combo, add, and remove
  controls in one row to reduce vertical space in the draw results.
- Removed persistent visual active styling from combo/add buttons after use and
  blurred draw action buttons after clicks so they do not look held down.
- Kept remove mode functional through `aria-pressed`, but changed its visual
  treatment from a filled pressed button to a lighter danger-colored control.
- Bumped app version from `2026.08.29.5` to `2026.08.29.6` for update detection.

Behavior preserved:

- Utility-page back navigation fix from `2026.08.29.5`.
- Menu-combination cards show only pairing text.
- Dish cards omit `无需解冻` for no-thaw dishes.

## 2026-08-29 - Codex - published 2026.08.29.5 utility navigation and recipe labels

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Changes:

- Changed `菜品库` and `5分哲理` shortcut navigation so switching between
  utility pages no longer stacks utility pages in history. Tapping `返回` now
  returns to the nearest main-flow page: `首页`, `抽卡`, or `做菜/Timer`.
- Simplified recipe-library menu-combination cards to show only the pairing
  text, removing the repeated dish-image card strip.
- Removed the menu detail lead image so menu-combination detail text occupies
  the full detail panel width.
- Hid the `无需解冻` line on dish cards and dish details; only dishes that need
  thawing show a thawing notice.
- Bumped app version from `2026.08.29.4` to `2026.08.29.5` for update detection.

Behavior preserved:

- Top action buttons remain on one row.
- Meal selection redraw fix.
- Android light background fix.
- Current root `motto.txt` remains synced into the published app.

## 2026-08-29 - Codex - published 2026.08.29.4 action row and motto width fix

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Changes:

- Fixed the top quick-action group wrapping into two rows when all five buttons
  are visible by forcing a single no-wrap row and allowing icon buttons to
  shrink slightly on narrow screens.
- Fixed the `五分哲理` card feeling width-variable with short mottos by giving
  the stage/card a stable width and letting text use the full card width.
- Delayed motto line wrapping by removing the old `16em` paragraph max-width
  constraint while keeping normal Chinese line breaking.
- Bumped app version from `2026.08.29.3` to `2026.08.29.4` for update detection.

Behavior preserved:

- Meal selection redraw fix.
- Android light background fix.
- Current root `motto.txt` remains synced into the published app.
- Dish-image cache rotates with the app version.

## 2026-08-29 - Codex - published 2026.08.29.3 meal-selection redraw fix

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Changes:

- Fixed a home-screen meal selection bug: if the user removed `早饭`, drew a
  daily menu, returned home, re-selected `早饭`, and started again, the app no
  longer restores the older saved menu that omitted breakfast.
- Added meal-selection comparison before reusing a saved daily menu. If the
  current home selection differs from the saved menu's meals, the app now
  regenerates and saves a new menu for the selected meals.
- Kept selected meal ordering stable as `早饭 / 午饭 / 晚饭` when a meal is
  re-added.
- Bumped app version from `2026.08.29.2` to `2026.08.29.3` for update detection.

Behavior preserved:

- Reusing today's saved menu still works when the meal selection is unchanged.
- Current root `motto.txt` remains synced into the published app.
- Dish-image cache rotates with the app version.
- Android light background fix.

## 2026-08-29 - Codex - published 2026.08.29.2 Android light background fix

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/manifest.webmanifest`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Changes:

- Added an explicit light color-scheme meta tag and `color-scheme: only light`
  at the document root so Android Chrome/WebView does not auto-darken the app.
- Added solid fallback backgrounds to `html`, `body`, and `main` so transparent
  viewport gaps cannot render as black behind the warm paper background.
- Aligned the PWA manifest `background_color` and `theme_color` with the current
  Fiveish visual palette.
- Bumped app version from `2026.08.29.1` to `2026.08.29.2` for update detection.

Behavior preserved:

- Current root `motto.txt` remains synced into the published app.
- Dish-image cache rotates with the app version.
- Mobile compact layout and desktop overflow fix.
- 15:00 daily reset.

## 2026-08-29 - Codex - published 2026.08.29.1 hard-code audit and cache fix

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `frontend/prototype/dish-cache-sw.js`
- `docs/CHANGELOG.md`

Changes:

- Audited the published prototype for source-data drift similar to the motto
  sync issue.
- Confirmed `dishCatalog` and `menuTemplates` currently match
  `菜品菜单.xlsx`: 34 dishes and 8 menu templates.
- Changed the dish-image service worker registration to include `APP_VERSION`
  in the service worker URL, so image cache names rotate with app releases.
- Changed `dish-cache-sw.js` to read its cache version from its own `?v=...`
  query parameter, with `2026.08.29.1` as the fallback version.
- Bumped app version from `2026.08.28.1` to `2026.08.29.1` for update
  detection.

Behavior preserved:

- Current root `motto.txt` remains synced into the published app.
- Mobile compact layout and desktop overflow fix.
- 15:00 daily reset.
- Shared label draw cache and concrete-dish category lock.

## 2026-08-28 - Codex - published 2026.08.28.1 motto sync fix

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `scripts/sync_mottos.py`
- `docs/CHANGELOG.md`

Changes:

- Synced the app's `summaryMottos` array from the current root `motto.txt`
  list, reducing the published Fiveish motto list from the old hard-coded 19
  entries to the current 9 entries.
- Added `scripts/sync_mottos.py` so future motto edits can be pushed into the
  published prototype before deployment.
- Bumped app version from `2026.07.20.2` to `2026.08.28.1` for update detection.

Behavior preserved:

- Mobile compact layout and desktop overflow fix.
- 15:00 daily reset.
- Shared label draw cache and concrete-dish category lock.
- Update-check banner and cache-clearing update button.

## 2026-07-20 - Codex - published 2026.07.20.2 desktop overflow fix

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Changes:

- Added a desktop-only layout override for screens wider than 760px so pages can
  grow and use page-level scrolling instead of being clipped to `100svh`.
- Removed desktop height clipping from the cooking guide, recipe library,
  recipe detail, and leftovers list while preserving the existing mobile rules.
- Bumped app version from `2026.07.20.1` to `2026.07.20.2` for update detection.

Behavior preserved:

- Mobile compact layout and PWA install behavior.
- 15:00 daily reset.
- Shared label draw cache and concrete-dish category lock.
- Update-check banner and cache-clearing update button.
- Dish-image service worker cache and idle-time warmup.

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


## 2026-07-20 - Codex

Files changed:

- `.github/workflows/pages.yml`
- `.github/workflows/deploy-aliyun-oss.yml`
- `docs/ALIYUN_DEPLOY.md`
- `docs/CODEX_HANDOFF.md`
- `START_HERE.md`
- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`

Behavior changes:

- Restored GitHub Pages as the active deployment target.
- Removed the Alibaba Cloud OSS deployment workflow and deployment notes.
- Updated the in-app deployment checklist back to GitHub Pages.
- Bumped the app version to `2026.07.20.1`.

## 2026-07-19 - Codex

Files changed:

- `frontend/prototype/index.html`
- `frontend/prototype/version.json`
- `docs/CHANGELOG.md`
- `.github/workflows/deploy-aliyun-oss.yml`
- `docs/ALIYUN_DEPLOY.md`
- `docs/CODEX_HANDOFF.md`
- `START_HERE.md`

Behavior changes:

- Moved the leftovers shortcut into the top-right action bar so it sits beside the other global buttons.
- Reworked the recipe library menu view into stacked combo cards that show the dishes inside each combo as cards.
- Added card-style rendering for the menu-library combo contents.
- Hid guide step 0 when there is nothing to prep or thaw.
- Kept steps 1-3 in order but removed any empty appliance step instead of showing a blank step.
- Switched the deployment workflow from GitHub Pages to Alibaba Cloud OSS.


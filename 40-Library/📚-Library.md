---
type: index
status: 进行中
tags: [书架, 已读书籍]
created: 2026-08-06
updated: 2026-08-06
---

# 📚 书架

> 已读书籍自动聚合，按分类展示。新增书籍：`Cmd/Ctrl + P` → 输入 "Templater: Create new note from template" → 选择 `T-book`。

```dataviewjs
// ============================================================
// 40-Library 卡片画廊
// 扫描 40-Library 下所有 type: book 的笔记，按分类渲染卡片
// ============================================================

const CATEGORIES = {
  "cs-arch":  { name: "计算机体系结构", emoji: "🖥️" },
  "os":       { name: "操作系统",       emoji: "⚙️" },
  "network":  { name: "计算机网络",     emoji: "🌐" },
  "algo":     { name: "算法与数据结构", emoji: "🔢" },
  "lang":     { name: "编程语言",       emoji: "📝" },
  "swe":      { name: "软件工程",       emoji: "🏗️" },
  "math":     { name: "数学",           emoji: "📐" },
  "general":  { name: "通识/科普",      emoji: "💡" },
  "other":    { name: "文学/其他",      emoji: "📖" }
};

// ---------- 查询 ----------
const allBooks = dv.pages('"40-Library"').where(p => p.type === "book");

if (allBooks.length === 0) {
  dv.paragraph("_书架还是空的，用 Templater 添加第一本书吧 📖_");
} else {

  // ---------- 统计 ----------
  const now = new Date();
  const thisMonth = `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}`;
  const thisMonthBooks = allBooks.where(p => p.read_date && String(p.read_date).startsWith(thisMonth));
  const avgRating = allBooks.where(p => p.rating).length
    ? (allBooks.where(p => p.rating).values.rating.reduce((a,b) => a + Number(b), 0) / allBooks.where(p => p.rating).length).toFixed(1)
    : "—";

  // 找出书的数量最多的分类
  let topCat = "—";
  let topCount = 0;
  for (const [id, cat] of Object.entries(CATEGORIES)) {
    const count = allBooks.where(p => p.category === id).length;
    if (count > topCount) { topCount = count; topCat = cat.emoji + " " + cat.name; }
  }

  dv.el("div",
    `<div class="book-stats">
      <div class="stat-card"><div class="stat-number">${allBooks.length}</div><div class="stat-label">📚 总册数</div></div>
      <div class="stat-card"><div class="stat-number">${thisMonthBooks.length}</div><div class="stat-label">📅 本月在读</div></div>
      <div class="stat-card"><div class="stat-number">${avgRating}</div><div class="stat-label">⭐ 平均评分</div></div>
      <div class="stat-card"><div class="stat-number">${topCount}本</div><div class="stat-label">🏆 ${topCat}</div></div>
    </div>`
  );

  // ---------- 画廊 ----------
  const gallery = dv.container.createDiv({cls: 'book-gallery'});

  let hasContent = false;

  for (const [catId, cat] of Object.entries(CATEGORIES)) {
    const books = allBooks.where(p => p.category === catId);
    if (books.length === 0) continue;
    hasContent = true;

    // 分类标题
    const section = gallery.createDiv({cls: 'book-category'});
    const header = section.createDiv({cls: 'category-header'});
    header.createSpan({cls: 'emoji', text: cat.emoji});
    header.createSpan({cls: 'name', text: cat.name});
    header.createSpan({cls: 'count', text: `${books.length} 本`});

    // 卡片网格
    const grid = section.createDiv({cls: 'book-grid'});

    for (const book of books) {
      const card = grid.createDiv({cls: 'book-card'});

      // 点击卡片跳转
      card.addEventListener('click', (e) => {
        if (window.getSelection()?.toString()) return;  // 不拦截文字选择
        app.workspace.openLinkText(book.file.path, '', false);
      });
      card.style.cursor = 'pointer';

      // --- 封面 ---
      const coverDiv = card.createDiv({cls: 'book-cover'});
      const coverSrc = book.cover ? String(book.cover).trim() : '';
      let imgLoaded = false;

      if (coverSrc) {
        try {
          let url;
          if (coverSrc.startsWith('http://') || coverSrc.startsWith('https://')) {
            url = coverSrc;
          } else {
            // 去掉可能的 wikilink 语法 [[xxx]]
            const clean = coverSrc.replace(/^\[\[|\]\]$/g, '');
            url = app.vault.adapter.getResourcePath(clean);
          }
          const img = coverDiv.createEl('img', { attr: { src: url, loading: 'lazy' } });
          imgLoaded = true;
        } catch(e) {}
      }

      if (!imgLoaded) {
        const placeholder = coverDiv.createDiv({cls: 'book-cover-placeholder'});
        placeholder.createSpan({cls: 'icon', text: '📖'});
      }

      // --- 信息区 ---
      const info = card.createDiv({cls: 'book-info'});

      // 书名
      const titleDiv = info.createDiv({cls: 'book-title'});
      titleDiv.createEl('a', {
        text: book.file.name,
        attr: { 'data-href': book.file.path }
      });
      // 阻止书名链接的冒泡（卡片本身已有点击事件）
      titleDiv.querySelector('a').addEventListener('click', (e) => {
        e.stopPropagation();
        app.workspace.openLinkText(book.file.path, '', false);
      });

      // 作者（若有）
      if (book.author && String(book.author).trim()) {
        info.createDiv({cls: 'book-author', text: String(book.author).trim()});
      }

      // 评分（若有）
      if (book.rating) {
        const stars = parseInt(book.rating) || 0;
        if (stars > 0) {
          const ratingDiv = info.createDiv({cls: 'book-rating'});
          for (let i = 1; i <= 5; i++) {
            ratingDiv.createSpan({
              cls: i <= stars ? 'star' : 'star-empty',
              text: i <= stars ? '★' : '☆'
            });
          }
        }
      }

      // 一句话总结（若有）
      if (book.summary && String(book.summary).trim()) {
        info.createDiv({cls: 'book-summary', text: String(book.summary).trim()});
      }
    }
  }

  if (!hasContent) {
    dv.paragraph("_暂无分类数据_");
  }
}
```

## 📋 分类一览

| 分类 | 册数 |
|------|------|
| 🖥️ 计算机体系结构 | `$= dv.pages('"40-Library"').where(p => p.type === "book" && p.category === "cs-arch").length` |
| ⚙️ 操作系统 | `$= dv.pages('"40-Library"').where(p => p.type === "book" && p.category === "os").length` |
| 🌐 计算机网络 | `$= dv.pages('"40-Library"').where(p => p.type === "book" && p.category === "network").length` |
| 🔢 算法与数据结构 | `$= dv.pages('"40-Library"').where(p => p.type === "book" && p.category === "algo").length` |
| 📝 编程语言 | `$= dv.pages('"40-Library"').where(p => p.type === "book" && p.category === "lang").length` |
| 🏗️ 软件工程 | `$= dv.pages('"40-Library"').where(p => p.type === "book" && p.category === "swe").length` |
| 📐 数学 | `$= dv.pages('"40-Library"').where(p => p.type === "book" && p.category === "math").length` |
| 💡 通识/科普 | `$= dv.pages('"40-Library"').where(p => p.type === "book" && p.category === "general").length` |
| 📖 文学/其他 | `$= dv.pages('"40-Library"').where(p => p.type === "book" && p.category === "other").length` |

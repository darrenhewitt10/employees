// Renders docs/*.md into a static HTML site in _site/ for Netlify.
import { readdir, readFile, writeFile, mkdir, rm } from "node:fs/promises";
import { join } from "node:path";
import { marked } from "marked";

const SRC = "docs";
const OUT = "_site";

const files = (await readdir(SRC)).filter((f) => f.endsWith(".md"))
  .sort((a, b) => (a === "README.md" ? -1 : b === "README.md" ? 1 : a.localeCompare(b)));
const htmlName = (f) => (f === "README.md" ? "index.html" : f.replace(/\.md$/, ".html"));
const titleOf = (md, f) => (md.match(/^#\s+(.+)$/m)?.[1] ?? f).replace(/[`*]/g, "");

// Heading ids that match GitHub-style anchors used in the docs.
const slug = (text) =>
  text.toLowerCase().trim().replace(/<[^>]+>/g, "").replace(/[^\w\- ]/g, "").replace(/ /g, "-");
marked.use({
  gfm: true,
  renderer: {
    heading({ tokens, depth, text }) {
      return `<h${depth} id="${slug(text)}">${this.parser.parseInline(tokens)}</h${depth}>\n`;
    },
    link({ href, title, tokens }) {
      const label = this.parser.parseInline(tokens);
      let url = href;
      if (!/^[a-z]+:/i.test(url)) url = url.replace(/^README\.md/, "index.html").replace(/\.md(#|$)/, ".html$1");
      const ext = /^https?:/i.test(url) ? ' target="_blank" rel="noopener"' : "";
      return `<a href="${url}"${title ? ` title="${title}"` : ""}${ext}>${label}</a>`;
    },
  },
});

const docs = [];
for (const f of files) {
  const md = await readFile(join(SRC, f), "utf8");
  docs.push({ f, md, title: titleOf(md, f), out: htmlName(f) });
}

const nav = docs
  .map((d) => `<li><a href="${d.out}">${d.f === "README.md" ? "Overview" : d.title.replace(/^\d+\s+—\s+/, "").split(" — ")[0]}</a></li>`)
  .join("");

const page = (d, body) => `<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${d.title}</title>
<style>
:root{--bg:#fbfbfa;--fg:#1d1d1b;--muted:#5d5d58;--line:#e2e1dc;--accent:#1f5fae;--code:#f0efea}
@media (prefers-color-scheme:dark){:root{--bg:#161615;--fg:#e9e8e3;--muted:#a3a29b;--line:#33332f;--accent:#7fb0ef;--code:#22221f}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 system-ui,-apple-system,"Segoe UI",sans-serif}
.wrap{display:grid;grid-template-columns:260px minmax(0,1fr);max-width:1280px;margin:0 auto}
nav{position:sticky;top:0;height:100vh;overflow:auto;padding:24px 16px;border-right:1px solid var(--line);font-size:14px}
nav strong{display:block;margin-bottom:8px}nav ul{list-style:none;padding:0;margin:0}nav li{margin:4px 0}
nav a{color:var(--muted);text-decoration:none}nav a:hover{color:var(--accent)}
main{padding:32px 40px;min-width:0}a{color:var(--accent)}
table{border-collapse:collapse;display:block;overflow-x:auto;margin:16px 0;font-size:14px}
th,td{border:1px solid var(--line);padding:6px 10px;vertical-align:top;text-align:left}th{background:var(--code)}
code{background:var(--code);padding:1px 4px;border-radius:4px;font-size:.9em}pre{background:var(--code);padding:12px;overflow-x:auto;border-radius:6px}pre code{padding:0}
blockquote{margin:16px 0;padding:4px 16px;border-left:3px solid var(--accent);color:var(--muted)}
@media (max-width:800px){.wrap{display:block}nav{position:static;height:auto;border-right:0;border-bottom:1px solid var(--line);padding:16px}main{padding:16px}}
</style></head>
<body><div class="wrap"><nav><strong>AI Trading Research</strong><ul>${nav}</ul></nav>
<main>${body}</main></div></body></html>
`;

await rm(OUT, { recursive: true, force: true });
await mkdir(OUT, { recursive: true });
for (const d of docs) await writeFile(join(OUT, d.out), page(d, marked.parse(d.md)));
console.log(`Built ${docs.length} pages into ${OUT}/`);

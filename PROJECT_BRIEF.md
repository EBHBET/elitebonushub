# EliteBonusHub.bet — Cowork Project Brief

> ⚠️ **STALE — do not treat as current state (flagged 2026-07-14).** This brief describes an early phase of the project (the `EliteBonusHub_Agent.html` browser tool, a GA4 placeholder ID, "~5-8 articles published," the old `C:\Projects\Aff\EBH` path). None of that matches the live repo today: content is now authored directly in this Claude Code session (not via the agent tool), GA4 has a real working measurement ID, the site has 150+ pages across EN/FR/ES, and GSC/PSI/CrUX credentials are authenticated (see the "EBH GSC authenticated" memory / `EBH SEO/elitebonushub.bet-audit/`). **For current state, trust the live repo, `SEO_STRATEGY.md` §7, `CONTENT-BACKLOG.md`, and `BACKLINK_STRATEGY.md` over this file.** Kept here as historical record, not instructions to follow.


## ⚠️ Memory isolation — read this first

This project must operate as a **self-contained context**. Do not pull in, reference, or apply general memory, past conversation history, or unrelated project knowledge from outside this package when working on EliteBonusHub tasks.

Specifically:
- Treat this `PROJECT_BRIEF.md` file and the accompanying source files as the **complete and authoritative context** for this project. Do not assume facts about EliteBonusHub that aren't written here or verifiable in the live repo/site — if something is unclear or missing, say so and ask, rather than inferring from general crypto/casino/affiliate-marketing knowledge that may not apply to this specific site's actual setup.
- Do not carry over assumptions, terminology, decisions, or conventions from any other project Carlos may be running (e.g. Impetus Protocol, DartFrog Builder, the social media agent, or any other unrelated venture). Those are separate projects with separate logic, separate tech stacks, and separate business rules. Mixing them in is a contamination risk — for example, do not apply Impetus Protocol's tokenomics/NFT/staff-persona conventions to EliteBonusHub, and do not apply EliteBonusHub's affiliate-marketing logic to any other project.
- If this Cowork session has access to broader memory/history features, explicitly scope any lookups to this project's own files and the live elitebonushub.bet domain/repo — not to memory of past conversations about other ventures.
- When in doubt about whether a fact, decision, or convention belongs to this project, treat it as **out of scope** unless it is written in this brief or directly verifiable in the EliteBonusHub GitHub repo / live site.
- At the start of any new session on this project, re-read this brief in full before taking action, rather than relying on a prior session's summarized memory of it — the brief is the source of truth, not anyone's recollection of it.

## ⚠️ Always open sessions at this exact folder — not a subfolder

**Canonical root: `C:\Projects\Sites\EBH`** (this file's own location — moved here 2026-07-13 from `C:\Projects\Aff\EBH`, as part of consolidating all site projects under one `C:\Projects\Sites\` master folder alongside KantanPrep, ElderlyCare, and Pinterest fashion). Claude Code's auto-memory is keyed to the exact working-directory path a session starts at — opening one level down (e.g. `Design\`, `EBH SEO\`, or any other subfolder) creates a **separate, isolated memory scope** that can't see anything written from the root, and vice versa. This has already happened here: by 2026-07-12 this project had fragmented across 5 different memory scopes (root, `Design`, `EBH SEO`, `EBH SEO\handoff-2026-07-09`, `EBH SEO\.secrets`) purely because different sessions opened at different subfolders — not because of anything project-specific.

**In VS Code:** open the folder `C:\Projects\Sites\EBH` itself (File → Open Folder), not any subfolder inside it, even if the task at hand only touches `Design\` or `EBH SEO\`.

**In the Desktop app:** same rule if not using a Cowork Project — point sessions at this root. (If this work ever migrates to a Cowork Project, Cowork's own per-project memory scoping replaces this concern entirely for Desktop sessions — but that hasn't been set up yet as of 2026-07-12.)

This doesn't affect git or file safety — commits/pushes work the same regardless of session root. It only affects what Claude remembers between sessions.

## What this project is

EliteBonusHub is a crypto casino affiliate website that earns commission when visitors click through to partner casinos (Stake, BC.Game, Cloudbet) and deposit. The business model is SEO-driven content marketing — articles and reviews rank in Google search, visitors read them, click affiliate links, and the site earns a CPA or revenue-share commission.

**Live domain:** https://elitebonushub.bet
**GitHub repo:** github.com/EBHBET/elitebonushub (GitHub Pages hosting)
**Owner:** Carlos, based in Costa Rica
**Stage:** Site is live, ~5-8 articles published, zero confirmed organic traffic yet, domain registered June 9 2026 (very new)

## Business model and revenue mechanics

Visitor arrives via Google search → reads casino review/guide → clicks affiliate link → signs up and deposits at casino → EliteBonusHub earns CPA commission (typically $100-200 per depositor) or revenue share.

**Active affiliate partners:**
- Stake — https://stake.com/?c=M8AE5RDv — 200% bonus up to 1 BTC, no KYC
- BC.Game — https://bc.game/i-97mlzobrj1-n/ — 180% up to 3 BTC, 100+ coins
- Cloudbet — https://cldbt.cloud/go/en/landing/bitcoin-casino?af_token=e7d441743c4fdf2721dd3700d64d3919&aftm_campaign=1st — 100% up to 5 BTC + $2,500, has unique "Whale Mode" no-limit betting feature

**Affiliate applications submitted/pending:** Boomerang Partners, PIN-UP Partners, N1 Partners — all requested traffic source/GEO info, responses sent positioning the site as SEO content with 10-12 monthly depositor volume in growth phase.

## Site architecture

**index.html** — homepage. Dark theme (near-black #080808 background, gold #D4A017 accent), Cinzel serif for headings + Inter sans for body. Casino comparison cards (Stake/BC.Game/Cloudbet/Rollbit/Metaspins — last two have no live affiliate links yet), email capture popup (shows ONLY on first visit via localStorage `ebh_visited` flag — this was a bug that got fixed, verify it's still working), FAQ section with FAQPage schema markup, Guides teaser section linking to guides.html, responsible gambling section, footer.

**guides.html** — article hub page. Hero section featuring the lead article (currently Cloudbet Whale Mode), sticky category nav (All/Reviews/Guides/Bonuses/High Roller) with live counts, article grid that is supposed to auto-detect which articles exist in the GitHub repo via the GitHub Contents API and only show those as clickable — this has been unreliable (see Known Issues below), CTA strip with affiliate links at bottom.

**Individual article pages** (e.g. cloudbet-whale-mode.html, best-crypto-crash-game-sites.html) — each is a full standalone HTML page with its own embedded CSS, dark-gold styling matching the brand, article hero with breadcrumb, body content (H1, intro, quick-verdict box, H2 sections, casino-picks div with affiliate CTAs, comparison table, pros/cons grid), footer with all 3 affiliate CTAs and responsible gambling disclosure.

**sitemap.xml** — must always use https://elitebonushub.bet/ URLs, NEVER github.io subdomain URLs (this was a recurring bug — Search Console rejected the sitemap multiple times because it contained the wrong domain).

**robots.txt** — simple allow-all pointing to sitemap.

**EliteBonusHub_Agent.html** — the standalone content-generation and site-management tool. See "The Agent Tool" section below — this is the most complex and most bug-prone part of the project.

## Brand identity

- **Logo:** gold crown with jewels (ruby, sapphires, pearls) above "EBH" lettering in serif gold, transparent PNG (black background removed via pixel-threshold transparency). Master file: ebh_logo_transparent.png. Embedded as base64 in HTML head for favicon, and used as `<img>` tag in nav (not the old inline SVG placeholder).
- **Color palette:** --gold:#D4A017, --gold-lt:#F0C84A, --dark:#080808/#0a0a0a, --dark2:#0F0F0F/#111, --dark3:#161616, --dark4:#1E1E1E/#1e1e1e, --border:#2A2A2A, --text:#F0EDE6, --muted:#9A9690
- **Fonts:** Cinzel (serif, 700/900 weight) for headings/logo text, Inter (400-700 weight) for body
- **Tone:** "Crypto Casino Experts" — authoritative, VIP/exclusive positioning, not cheap or spammy

## The Agent Tool — EliteBonusHub_Agent.html

This is a single-file HTML+JS application (no build step, no server) that Carlos runs locally via **VS Code Live Server** (NOT by double-clicking — file:// origin breaks API calls due to CORS/security restrictions on Anthropic's API).

**Critical technical lessons learned (do not repeat these mistakes):**

1. **Script placement matters.** Early version had `<script>` at the bottom of the HTML with `oninput="saveKeys()"` handlers on inputs near the top — this caused `ReferenceError: saveKeys is not defined` because the DOM elements rendered and fired events before the script tag (at the bottom) had loaded. Fix: script must be in `<head>`, with init logic wrapped in `DOMContentLoaded`.

2. **Closing HTML tags inside JS template literals break the browser parser.** The agent generates full article HTML inside a JS template literal (backticks) that itself contains `</style>`, `</head>`, `</body>`, `</html>` as literal strings (because it's building a complete HTML document as a string). The browser's HTML parser sees `</style>` inside the outer `<script>` tag and thinks the script block ended there — causing `Uncaught SyntaxError: Unexpected end of input`. Node.js `--check` does NOT catch this because it only parses JS, not HTML+JS together. Fix: escape every closing tag inside the template literal as `<\/style>`, `<\/head>`, `<\/body>`, `<\/html>` etc. ALWAYS test by actually loading in a browser, not just `node --check`.

3. **GitHub API auth format.** Must use `Authorization: Bearer <token>` with `X-GitHub-Api-Version: 2022-11-28` header — NOT the deprecated `Authorization: token <token>` format. The deprecated format sometimes works on the first call and fails on subsequent calls, which is confusing to debug.

4. **`atob()` breaks on large base64 strings.** When the agent tried to fetch index.html (1.2MB+) from GitHub, decode it with `atob()`, modify it, and push it back, the decode operation corrupted the file and produced a blank page live on production. **Never use atob/btoa round-tripping on files over ~500KB in browser JS.** For large files, build the modified content fresh from a template rather than fetching-decoding-modifying-reencoding.

5. **GitHub Contents API caching.** The guides.html auto-detection (checking which articles exist via `fetch('https://api.github.com/repos/.../contents/')`) was unreliable — deleted articles kept appearing because of browser caching. Needed `?t=Date.now()` cache-busting AND a full reset of the local "liveSet" object on every check, not an incremental merge.

6. **Affiliate links not appearing in generated articles.** The Claude system prompt for article generation needs EXPLICIT, repeated, mandatory instructions with the literal URLs spelled out — a vague instruction like "include affiliate links naturally" gets ignored. The working version lists every casino name + exact URL + exact bonus text in the prompt and says "MANDATORY" with the exact `<a>` tag format required.

7. **Claude hallucinated wrong dates (2024) in generated content** until the system prompt explicitly said "CRITICAL: Use ONLY the year 2026. Never write 2024 or 2025" in multiple places.

8. **Claude wrapped output in markdown code fences (```html) and used markdown headers (##)** instead of clean HTML until explicitly told "Output clean HTML ONLY. No markdown, no backticks, no code fences. Start directly with an h1 tag."

**Current agent tabs/features:**
- Keys tab — Anthropic API key, GitHub username/repo/token, validate button
- Deploy tab — manual deploy buttons, push individual files (guides.html, index.html)
- Pipeline tab — "Full run" generates one article end-to-end (topic→research→write→deploy→update guides.html+sitemap), 5-step visual progress
- Articles tab — lists live articles from GitHub, delete button (should cascade: delete file → rebuild guides.html → rebuild sitemap), per-article affiliate-link-update button
- Affiliates tab — add/remove affiliate partners (name, URL, bonus text, logo upload, notes), "push to all articles" button that's supposed to use Claude to rewrite affiliate sections in existing articles
- SEO tab — competitor analysis (asks Claude to identify top-ranking competitor sites for a seed keyword, analyzes each one's apparent SEO patterns/keywords, synthesizes recommendations, can apply meta tag + schema changes to index.html), keyword database table (keyword/type/volume/difficulty/source/priority), hashtag generation for future X/social use
- Log tab — activity feed

**Known issues with the agent (unverified whether all are still present — audit needed):**
- The "Apply SEO improvements" feature that fetches+modifies+pushes index.html via atob is fragile on large files (see lesson #4) — caused a full site outage once already. May need to be redesigned to NOT round-trip the entire file through atob/btoa.
- Affiliate link push-to-all-articles function has not been verified to reliably work at scale across many articles — needs testing.
- No verification that GitHub token validation / auth works consistently call-to-call.
- guides.html article-detection logic has been patched multiple times (hardcoded fallback list + API check) — fragile, should be redesigned to be more deterministic (e.g. agent maintains an authoritative articles.json manifest file in the repo that both guides.html and the agent read/write, instead of relying on live GitHub API directory listing + guesswork).

## X / Social posting — explicitly deferred

Decision was made to abandon paid X/social scheduling APIs (Buffer required payment beyond free tier, Zernio also charges per API call) for now. The SEO tab generates hashtag keywords for future use, but there is NO live social posting capability currently. This should only be revisited once the site is profitable enough to justify the API cost. Do not re-add X posting integration unless explicitly asked.

## Known content quality issues (may or may not be fixed — verify)

- Early generated articles had markdown artifacts (## headers, ```html fences), wrong years (2024), no embedded affiliate links, generic stock-photo-style images that didn't match context (a dog emoji was used for "Whale Mode" instead of a whale — fixed to 🐋).
- Several early broken/malformed articles were manually deleted from the GitHub repo by Carlos. Some had to be regenerated.
- No verification has been done on whether the CURRENT live articles are complete, well-formatted, and not truncated (mid-sentence cutoffs are a known risk when max_tokens is too low for the requested word count — system prompt asks for 1,400+ words but article generation max_tokens parameter should be checked, it was set to 1000 tokens in at least one version which is far too low to produce 1,400 words and would truncate).

## DNS / hosting setup (for reference, should be stable now)

- Domain registrar: Porkbun
- Nameservers: pointed to Cloudflare (chase.ns.cloudflare.com / leanna.ns.cloudflare.com) — DNS records are managed IN CLOUDFLARE, not Porkbun, this caused confusion
- DNS records in Cloudflare: 4x A records → GitHub Pages IPs (185.199.108.153, .109.153, .110.153, .111.153), CNAME www → ebhbet.github.io
- All records must be "DNS only" (grey cloud), NOT proxied (orange cloud) — GitHub Pages doesn't work behind Cloudflare's proxy
- A CNAME-vs-CAA record type mismatch in Cloudflare caused the www subdomain to fail for a while — was fixed
- GitHub Pages custom domain set to elitebonushub.bet, HTTPS enforced (cert auto-issued by Let's Encrypt via GitHub)
- www.elitebonushub.bet showed "improperly configured" intermittently — root domain elitebonushub.bet works fine, www is lower priority

## Analytics / tracking

GA4 tag is embedded in index.html and article pages BUT still using placeholder `G-XXXXXXXXXX` — needs Carlos's real Measurement ID substituted in. Tracks page views, affiliate link clicks (custom event keyed on URL pattern matching stake.com/bc.game/cldbt.cloud), email popup shown + email signup events.

## Email capture

Cloudflare Worker (mailchimp-worker.js) proxies email signups to Mailchimp API securely (API key not exposed client-side). Mailchimp Audience ID and server prefix are in the worker. Welcome email (EBH_Welcome_Email.html) is built as Mailchimp-compatible HTML (table-based layout, inline styles, *|UNSUB|* and *|UPDATE_PROFILE|* merge tags) with embedded base64 logo, teases 3 upcoming guide topics (slot strategy, blackjack/bet-progression/bankroll, casino history — NOT YET WRITTEN as articles), shows all 3 affiliate offers.

## Indexing / SEO status as of last check

**CONFIRMED: zero pages indexed by Google as of last `site:elitebonushub.bet` search.** Domain is ~1 week old. Search Console verification status unknown/unconfirmed — Carlos has been told to verify but completion not confirmed. Sitemap submission status unconfirmed. This is priority #1 to verify and fix.

---

# INSTRUCTIONS FOR THIS COWORK PROJECT — DO THE FOLLOWING IN ORDER

## 1. Verify indexing status and check rankings

- Check whether https://elitebonushub.bet and its subpages are indexed by Google (site: search, Search Console API if credentials available, or guide Carlos through manual Search Console check).
- Check whether Google Search Console is verified for this property. If not, walk through verification.
- Check whether sitemap.xml has been successfully submitted and accepted (no errors).
- For any keywords in the agent's keyword database (or the TOPICS list in EliteBonusHub_Agent.html), check current ranking position if any (likely none yet, but establish baseline).
- Report findings clearly: indexed/not indexed, verified/not verified, sitemap status, baseline rankings (likely "not ranking" for everything — that's fine, just confirm).

## 2. Audit design against industry-standard best practices

- Review index.html, guides.html, and at least 2-3 article pages against modern web design and affiliate-site UX best practices: visual hierarchy, mobile responsiveness, page load performance (the HTML files are very large — 1-1.5MB+ for index.html due to base64-embedded images — flag this as a performance concern), accessibility (alt text, contrast ratios, semantic HTML), trust signals (affiliate disclosure visibility, responsible gambling messaging placement), CTA clarity and placement, navigation usability.
- Compare against what top-ranking competitor casino affiliate sites (askgamblers.com, casino.guru, bestbitcoincasino.org) do well that this site doesn't.
- Specifically check: are images optimized or are they bloating page weight via inline base64? Should images be extracted to separate files with proper caching headers instead of inlined? Is the dark theme accessible (contrast ratios meet WCAG AA)? Is the site usable on mobile (test responsive breakpoints)?
- Produce a prioritized list of design issues with severity (critical/high/medium/low) and recommended fixes.

## 3. Verify content completeness — check for truncation

- Audit every live article HTML file in the repo. Check for: incomplete sentences/paragraphs at the end (truncation from token limits), missing closing tags, broken HTML structure, missing affiliate links, markdown artifacts (##, ```, ** that weren't converted to HTML), placeholder/template text that wasn't filled in (e.g. "[Pro 1]", "[Article title]").
- Cross-reference against the system prompt used by the agent (max_tokens parameter, word count requested) to determine if truncation is structurally likely and fix the root cause (increase max_tokens appropriately for the requested word count — roughly 1.5 tokens per word for English content, so 1,400 words needs at least ~2,500-3,000 output tokens, with safety margin).
- Report which specific articles (by filename) have issues and what the specific issue is.

## 4. Assess keyword usage

- Review the keyword database/TOPICS list currently in the agent against actual keyword opportunity (search volume vs difficulty vs relevance to a brand-new domain — brand-new sites should prioritize LOW difficulty, decent volume, high commercial intent keywords first, not compete for "best crypto casino 2026" type head terms immediately).
- Check keyword usage WITHIN existing published articles — is the target keyword actually present in title, H1, first paragraph, at least one H2, naturally throughout? Is there keyword cannibalization (multiple articles targeting the same exact keyword)?
- Assess the title/meta description patterns site-wide for consistency and click-through optimization.
- Recommend a revised, prioritized keyword strategy specifically suited to a domain with zero authority and zero backlinks — i.e. long-tail, low-competition, high-intent terms first (e.g. "[specific casino] no deposit bonus code", "[specific casino] withdrawal time", branded + modifier combos) rather than competing head-on for generic head terms that established sites with thousands of backlinks dominate.

## 5. Programmatically fix what needs fixing

Based on findings from steps 1-4, implement fixes directly in the codebase. Priority order:
1. Any indexing blockers (missing verification tags, sitemap errors, robots.txt issues)
2. Truncated/broken article content
3. Site structure issues affecting crawlability (internal linking, sitemap completeness, canonical tags)
4. Performance issues (especially the base64-image-bloat problem — strongly consider extracting images to separate optimized files served from the repo rather than inlining as base64, which bloats every page load)
5. Keyword optimization fixes in existing content
6. Design/UX issues from the audit, prioritized by severity

**When making fixes, follow the lessons in "Critical technical lessons learned" above** — especially regarding atob/btoa on large files, escaping closing tags inside JS template literals, and GitHub API auth format. Test every change by actually rendering it, not just syntax-checking.

## 6. Revamp the content-generation approach for short-attention-span, "viral" content

Carlos has explicitly requested that content be redesigned for people who will NOT read long-form articles. This is a significant strategic shift from the current 1,400+ word article format. Recommend and implement:
- Shorter, scannable content formats: bullet-heavy structure, bold key takeaways, TL;DR/quick-verdict boxes at the very top (already exists in some articles — make it more prominent and make it the PRIMARY content for skimmers, with full detail below for those who want it)
- Consider a "snackable" content layer: short-form summary cards, comparison tables as the hero content (not buried mid-article), visual-first presentation
- Headlines and hooks optimized for shareability — curiosity gaps, specific numbers, "X vs Y" framing
- Evaluate whether the current 1,400-word format should be SUPPLEMENTED (not necessarily replaced) with shorter companion formats: a punchy 300-400 word "quick take" version of each topic, FAQ-style snippets that can rank for voice search and appear as Google featured snippets, social-shareable graphics/stat callouts
- This connects to SEO too — Google increasingly rewards content that directly answers the query fast (featured snippets, "People Also Ask") over walls of text. Short, direct, well-structured answers near the top of a page can outrank longer competitor content.
- Propose a revised article template and a revised Claude system prompt for the agent's content generation that produces this style, and implement it in EliteBonusHub_Agent.html's `buildArticleHtml()` function and the article-writing system prompt.

## 7. Review and improve the agent tool itself — ASK PERMISSION BEFORE IMPLEMENTING

Audit EliteBonusHub_Agent.html as a piece of software (not just its output). Look for:
- Architectural fragility (see "Known issues" above — especially the guides.html article-detection logic and the atob/btoa large-file problem)
- Whether an articles.json manifest file (maintained by the agent, committed to the repo, read by both the agent and guides.html) would be more reliable than live-querying the GitHub Contents API and guessing
- Error handling gaps — what happens if a GitHub API call fails mid-pipeline? Is state left inconsistent (e.g. article generated and shown as "live" locally but never actually pushed)?
- Whether the single-giant-HTML-file-with-inline-everything architecture is still the right call, or whether splitting into separate JS modules (still client-side, still no build step required) would make the codebase more maintainable
- Whether max_tokens settings throughout are appropriate for the content lengths being requested (see point 3)
- Security: API keys are stored in localStorage in plaintext — acceptable for a single-user local tool but worth flagging
- **Present a list of proposed improvements with clear explanations of the problem each one solves and the tradeoffs involved. Wait for explicit approval from Carlos before implementing ANY of them.** This is different from steps 1-6 which should be implemented directly — step 7 is audit-and-propose only, not audit-and-fix.

---

# Files included in this package

- `EliteBonusHub_Agent.html` — the content/site management tool (source of truth for current agent capabilities)
- `EliteBonusHub_site.html` — current homepage (upload as index.html)
- `guides.html` — article hub page
- `cloudbet-whale-mode.html` — sample article (the flagship/featured one)
- `sitemap.xml`, `robots.txt` — SEO infrastructure files
- `mailchimp-worker.js` — Cloudflare Worker for secure email capture
- `EBH_Welcome_Email.html` — Mailchimp welcome automation email
- `ebh_logo_transparent.png`, `favicon.png`, `apple-touch-icon.png` — brand assets
- This file (`CLAUDE.md`) — full project context and task instructions

Carlos's GitHub repo (github.com/EBHBET/elitebonushub) is the live source of truth for what's actually deployed — the files in this package reflect the last known-good versions but this Cowork project should verify against the live repo / live site where possible rather than assuming these local files are 100% in sync with production.

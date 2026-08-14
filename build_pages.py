#!/usr/bin/env python3
"""Generate audience landing pages for Everbuilt Studio.

Each entry in PAGES becomes for/<slug>.html. Add a new dict to add a page —
this is also the engine for future programmatic SEO pages.
Run: python3 build_pages.py
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).parent

PAGES = [
    {
        "slug": "small-business",
        "title": "Website Design for Small Businesses",
        "meta_title": "Small Business Website Design — Own It Outright, $0/Month | Everbuilt Studio",
        "meta_desc": "Premium small business websites from $2,950 — delivered in days, with $0/month hosting forever. No agency retainers, no DIY-builder subscriptions. You own everything.",
        "kicker": "For businesses",
        "h1": "A website that wins customers — without the monthly bleed",
        "lede": "Most businesses are stuck between two bad options: a $35K agency that rents you your own site back, or a DIY builder that charges forever and still looks DIY. We built the third option.",
        "pains_head": "Sound familiar?",
        "pains": [
            "You're paying $30–500 a month and can't say exactly what for",
            "Your site looks like a template, because it is one",
            "Every small change means a ticket, an invoice, or a lost weekend",
            "The agency owns your site in every way that matters",
        ],
        "get_head": "What you get with Everbuilt",
        "gets": [
            ("Premium custom design", "Designed to make your business look like the biggest player on the block — no templates, no stock layouts."),
            ("Launched in days", "Launch tier ships in about a week. You approve a finished preview before the balance is due."),
            ("$0/month hosting, forever", "Modern edge architecture with no servers means no hosting bill. Not a promo — physics."),
            ("Total ownership", "Code, content, domain, admin keys. Fire us anytime and lose nothing."),
        ],
        "proof": "We used this exact architecture to launch a national nonprofit's site — 2,100+ photos, zero downtime, $0/month since launch day. Your business gets the same build quality at a fraction of agency prices.",
        "price_line": "Most businesses start with <strong>Launch at $2,950</strong> or <strong>Signature from $7,500</strong> — one price, 50% deposit, 90 days of free care included.",
        "cta_head": "See your website remade — free",
        "cta_sub": "Send us your current site and we'll return a finished premium remake, no strings attached.",
    },
    {
        "slug": "nonprofits",
        "title": "Website Design for Nonprofits",
        "meta_title": "Nonprofit Website Design — $0/Month Hosting Forever | Everbuilt Studio",
        "meta_desc": "Premium nonprofit websites with $0/month hosting — every dollar you don't spend on maintenance goes to your mission. We launched a national nonprofit tour with zero downtime.",
        "kicker": "For nonprofits & organizations",
        "h1": "Every dollar you don't spend on hosting goes to your mission",
        "lede": "Nonprofits get squeezed hardest by website costs: agency retainers, maintenance contracts, platform fees — all paid with donor money. Our flagship client is a national nonprofit. They pay $0/month.",
        "pains_head": "The nonprofit website trap",
        "pains": [
            "Maintenance contracts eating $2,400–6,000 of donor money per year",
            "A site your team can't update without calling someone",
            "Galleries and event calendars that break under real content volume",
            "Board members asking why the website costs so much and does so little",
        ],
        "get_head": "What your organization gets",
        "gets": [
            ("A site your team runs", "Admin panel for photos and pages; events managed from a spreadsheet your staff already knows how to use."),
            ("$0/month, in writing", "No hosting bill, no maintenance requirement, ever. Care plans exist but are genuinely optional."),
            ("Galleries at any scale", "Our media pipeline handled 78GB and 2,100+ photos for a 50-state tour. Yours will not be the build that breaks it."),
            ("A safe launch", "Zero-downtime cutover with your email untouched — guaranteed in writing. Boards love that sentence."),
        ],
        "proof": "us250tour.com — the national tour for America's 250th anniversary — is our flagship build: delivered for $7,500 against $35–60K agency quotes, launched with zero minutes of downtime, and hosted for $0/month ever since.",
        "price_line": "Most organizations fit <strong>Signature from $7,500</strong>. That's a one-time cost — then the site serves your mission for free, indefinitely.",
        "cta_head": "Show your board a finished remake first",
        "cta_sub": "Send us your current site. We'll return a premium remake you can put in front of your board — free.",
    },
    {
        "slug": "founders",
        "title": "MVP & App Development for Founders",
        "meta_title": "MVP Development for Founders — Fixed Scope, You Own the Code | Everbuilt Studio",
        "meta_desc": "Web apps, SaaS MVPs, and mobile apps built lean and fast from $15K. Fixed-scope quotes, no meter running, and you own the entire codebase from day one.",
        "kicker": "For founders & startups",
        "h1": "Validate the idea before you burn the budget",
        "lede": "Dev shops bill hourly and grow the scope. Freelancers disappear. We build MVPs the way we build everything: fixed scope, lean architecture, shipped fast, and the codebase is yours from the first commit.",
        "pains_head": "Why founders get burned",
        "pains": [
            "Hourly billing that rewards slow work and punishes clarity",
            "A six-month build for an idea that needed six weeks of validation",
            "Infrastructure bills before you have a single user",
            "Code you don't own, in a stack only the vendor understands",
        ],
        "get_head": "How we build for founders",
        "gets": [
            ("Fixed-scope quotes", "We scope precisely, quote a number, and hold it. Change requests are priced, not smuggled in."),
            ("Lean by default", "Static-first, serverless where possible — your running costs start near zero and scale with actual users, not ambition."),
            ("Web and mobile", "Web apps, SaaS MVPs, and mobile apps for iOS and Android from a shared codebase where it makes sense."),
            ("Your code, your repo", "Full ownership from day one. Raise a round, hire a CTO, switch vendors — the code comes with you."),
        ],
        "proof": "The same discipline behind our national nonprofit launch — productized pipelines, zero-downtime shipping, no meeting-industrial-complex — applied to product builds. Days-to-weeks, not quarters.",
        "price_line": "Platform builds start at <strong>$15K</strong> with 50% deposit. Landing page + waitlist validation builds fit our <strong>Launch tier at $2,950</strong>.",
        "cta_head": "Scope your build this week",
        "cta_sub": "Tell us what you're building and we'll come back with a fixed-scope plan within one business day.",
    },
    {
        "slug": "personal",
        "title": "Personal Websites & Portfolios",
        "meta_title": "Personal Website Design — Portfolios, Authors, Coaches | Everbuilt Studio",
        "meta_desc": "A personal website that looks like you hired an agency — because you did. Portfolios, personal brands, authors, and coaches from $2,950, with $0/month hosting forever.",
        "kicker": "For individuals",
        "h1": "Look like you hired an agency. Because you did.",
        "lede": "Your name deserves better than a template with your photo in it. We build personal sites — portfolios, author pages, coaching brands — at agency standard, owned outright, hosted for $0/month.",
        "pains_head": "The personal-site problem",
        "pains": [
            "Squarespace-with-your-name-on-it looks exactly like everyone else's",
            "$30–50 every month, forever, for a site you touch twice a year",
            "DIY weekends that end with something you're not proud to send",
            "Your work is excellent — your website says otherwise",
        ],
        "get_head": "What you get",
        "gets": [
            ("Design worthy of your name", "Custom typography, real art direction, a site that reads as premium in the first second."),
            ("One price, then free forever", "Pay once from $2,950. Then $0/month hosting for as long as you keep it."),
            ("Fast everywhere", "Instant loads on any phone — the difference people feel but can't name."),
            ("Easy updates", "Update your work, writing, or offers yourself — or send it to us on a care plan."),
        ],
        "proof": "The same architecture we used to launch a national nonprofit's site — premium design, blur-up image galleries, $0/month hosting — scaled to a personal brand.",
        "price_line": "Personal sites are our <strong>Launch tier: $2,950</strong>, delivered in about a week, 90 days of free care included.",
        "cta_head": "Send us what you have today",
        "cta_sub": "An old site, a LinkedIn, a folder of work — we'll show you what it could look like, free.",
    },
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{meta_title}</title>
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="https://everbuiltstudio.com/for/{slug}.html">
<meta property="og:type" content="website">
<meta property="og:title" content="{title} | Everbuilt Studio">
<meta property="og:description" content="{meta_desc}">
<meta property="og:url" content="https://everbuiltstudio.com/for/{slug}.html">
<meta property="og:image" content="https://everbuiltstudio.com/assets/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/styles.css">
</head>
<body>

<nav class="nav">
  <div class="wrap nav-inner">
    <a class="brand" href="../index.html">
      <svg width="26" height="26" viewBox="0 0 26 26" fill="none" aria-hidden="true">
        <rect x="1" y="1" width="24" height="24" rx="5" fill="#17140F"/>
        <path d="M7 8h12M7 13h9M7 18h12" stroke="#C2481B" stroke-width="2.4" stroke-linecap="round"/>
      </svg>
      Everbuilt<span>.</span>
    </a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M4 7h16M4 12h16M4 17h16" stroke="#17140F" stroke-width="2" stroke-linecap="round"/></svg>
    </button>
    <ul class="nav-links">
      <li><a href="../work/us250.html">Work</a></li>
      <li><a href="../index.html#audiences">Who we serve</a></li>
      <li><a href="../index.html#pricing">Pricing</a></li>
      <li><a href="../index.html#process">Process</a></li>
      <li><a href="../index.html#faq">FAQ</a></li>
      <li><a class="nav-cta" href="../index.html#contact">Start a project</a></li>
    </ul>
  </div>
</nav>

<header class="page-hero">
  <div class="wrap">
    <p class="kicker">{kicker}</p>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="section-head">
      <h2>{pains_head}</h2>
    </div>
    <ul class="contact-points" style="max-width: 640px;">
{pains_html}
    </ul>
  </div>
</section>

<section style="background: var(--surface); border-top: 1px solid var(--line); border-bottom: 1px solid var(--line);">
  <div class="wrap">
    <div class="section-head">
      <h2>{get_head}</h2>
    </div>
    <div class="aud-grid">
{gets_html}
    </div>
    <div class="care-note" style="margin-top: 34px;">
      <b>Proof, not promises:</b> {proof}
    </div>
  </div>
</section>

<section>
  <div class="wrap-narrow" style="text-align:center;">
    <p class="lede" style="max-width: 56ch; margin: 0 auto;">{price_line}</p>
    <div class="cta-band" style="padding-bottom: 20px;">
      <h2>{cta_head}</h2>
      <p>{cta_sub}</p>
      <a class="btn btn-primary" href="../index.html#contact">Start the conversation</a>
    </div>
  </div>
</section>

<footer>
  <div class="wrap footer-inner">
    <div>
      <div class="brand" style="font-size:1.1rem; margin-bottom:8px;">Everbuilt<span>.</span></div>
      <div>Built once. Yours forever.</div>
    </div>
    <ul class="footer-links">
      <li><a href="../work/us250.html">Work</a></li>
      <li><a href="small-business.html">For businesses</a></li>
      <li><a href="nonprofits.html">For nonprofits</a></li>
      <li><a href="founders.html">For founders</a></li>
      <li><a href="personal.html">For individuals</a></li>
      <li><a href="../index.html#contact">Contact</a></li>
    </ul>
  </div>
  <div class="wrap" style="margin-top: 30px; font-size: 0.8rem;">© <span id="year"></span> Everbuilt Studio. All rights reserved.</div>
</footer>

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.14/dist/lenis.min.js"></script>
<script src="../assets/main.js"></script>
</body>
</html>
"""


def render(page: dict) -> str:
    pains_html = "\n".join(
        f"      <li>{html.escape(p)}</li>" for p in page["pains"]
    )
    gets_html = "\n".join(
        f"""      <div class="aud-card" style="cursor:default;">
        <h3>{html.escape(t)}</h3>
        <p style="margin-bottom:0;">{html.escape(d)}</p>
      </div>"""
        for t, d in page["gets"]
    )
    return TEMPLATE.format(
        slug=page["slug"],
        meta_title=html.escape(page["meta_title"]),
        meta_desc=html.escape(page["meta_desc"]),
        title=html.escape(page["title"]),
        kicker=html.escape(page["kicker"]),
        h1=html.escape(page["h1"]),
        lede=html.escape(page["lede"]),
        pains_head=html.escape(page["pains_head"]),
        pains_html=pains_html,
        get_head=html.escape(page["get_head"]),
        gets_html=gets_html,
        proof=html.escape(page["proof"]),
        price_line=page["price_line"],  # contains intentional <strong> markup
        cta_head=html.escape(page["cta_head"]),
        cta_sub=html.escape(page["cta_sub"]),
    )


def main() -> None:
    out_dir = ROOT / "for"
    out_dir.mkdir(exist_ok=True)
    for page in PAGES:
        path = out_dir / f"{page['slug']}.html"
        path.write_text(render(page), encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

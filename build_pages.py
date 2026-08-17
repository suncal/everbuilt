#!/usr/bin/env python3
"""Everbuilt Studio page factory — audience pages, industry pages, guide
articles, and sitemap.xml, all generated from data below.

Add a dict to PAGES (audience/industry landing pages → for/<slug>.html) or
ARTICLES (long-form guides → guides/<slug>.html), run, commit, push:
GitHub Pages deploys automatically.

Run: python3 build_pages.py
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).parent
DOMAIN = "https://everbuiltstudio.com"

# ============================================================
# Landing pages (for/<slug>.html)
# ============================================================
PAGES = [
    # ---- audiences (original four) ----
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
    # ---- industries (programmatic SEO expansion) ----
    {
        "slug": "restaurants",
        "title": "Restaurant Website Design",
        "meta_title": "Restaurant Website Design — Menus, Photos, $0/Month | Everbuilt Studio",
        "meta_desc": "A restaurant website that makes people hungry: full-bleed food photography, an always-current menu you edit yourself, and $0/month hosting. From $2,950, live in about a week.",
        "kicker": "For restaurants & cafés",
        "h1": "A website that makes people hungry",
        "lede": "Your food is the marketing. Your website's job is to get out of its way — huge photography, an accurate menu, hours that are never wrong, and a reservation path with zero friction.",
        "pains_head": "The restaurant website trap",
        "pains": [
            "A PDF menu from two price changes ago",
            "Stock photos of food you don't serve",
            "$99/month for a template the platform owns",
            "Hours buried three taps deep while Google shows a competitor's",
        ],
        "gets": [
            ("Menu you edit yourself", "Change a price or 86 a dish from a spreadsheet — the site updates in minutes. No developer, no ticket."),
            ("Photography-first design", "Full-bleed, fast-loading food photography with blur-up loading. Your dishes are the hero, not our template."),
            ("Reservation & ordering links", "OpenTable, Resy, Toast, DoorDash — wired wherever your systems already live."),
            ("$0/month hosting", "Pay once. The site runs free, forever, on global edge infrastructure."),
        ],
        "get_head": "What your restaurant gets",
        "proof": "Our media pipeline processed 2,100+ photos for a national client launch — a dinner menu and a photo gallery will not break it. Zero-downtime launch, your Google Business Profile untouched.",
        "price_line": "Most restaurants fit <strong>Launch at $2,950</strong> — one price, live in about a week, menu training included.",
        "cta_head": "Send us your current site — even the PDF menu",
        "cta_sub": "We'll return a finished remake with your food front and center. Free.",
    },
    {
        "slug": "law-firms",
        "title": "Law Firm Website Design",
        "meta_title": "Law Firm Website Design — Credibility That Converts | Everbuilt Studio",
        "meta_desc": "Law firm websites that look like the retainer you charge: premium design, practice-area pages that rank, attorney profiles, and $0/month hosting. From $2,950.",
        "kicker": "For law firms & attorneys",
        "h1": "Your website is your first oral argument",
        "lede": "Clients judge a firm's competence by its website in under a second. Most firm sites lose that judgment — dated templates, stock gavels, and a hosting contract billed like a utility.",
        "pains_head": "Why most firm websites lose clients",
        "pains": [
            "A template that looks like every other firm in the county",
            "Practice-area pages too thin to rank for anything",
            "A 'web guy' who bills hourly for comma changes",
            "No clear path from visitor to consultation",
        ],
        "get_head": "What your firm gets",
        "gets": [
            ("Authority-grade design", "Restrained, premium, typographically serious — the visual equivalent of a corner office."),
            ("Practice-area architecture", "A dedicated, substantive page per practice area — the structure Google rewards and clients actually read."),
            ("Consultation funnel", "Prominent contact and intake forms on every page, wired to your inbox with a redundant capture safety net."),
            ("Own it outright", "The code, content, and domain are the firm's property. No vendor lock-in — you of all people know why that matters."),
        ],
        "proof": "The same build system launched a national organization's site with zero minutes of downtime and $0/month hosting since. Your firm's site gets the same engineering discipline.",
        "price_line": "Solo and small firms fit <strong>Launch at $2,950</strong>; multi-practice firms with intake workflows fit <strong>Signature from $7,500</strong>.",
        "cta_head": "See your firm's site remade — free",
        "cta_sub": "Send us your current site. We'll return a finished remake worthy of your letterhead.",
    },
    {
        "slug": "real-estate",
        "title": "Real Estate Agent Website Design",
        "meta_title": "Real Estate Website Design — Personal Brand That Lists | Everbuilt Studio",
        "meta_desc": "Real estate websites that build your personal brand beyond the brokerage template: listing galleries, neighborhood pages, lead capture, $0/month hosting. From $2,950.",
        "kicker": "For real estate agents & teams",
        "h1": "Stop marketing your brokerage. Start marketing you.",
        "lede": "The brokerage template makes every agent look identical. The agents winning listings have their own brand, their own site, and their own lead flow — owned outright, not rented from a portal.",
        "pains_head": "The agent website problem",
        "pains": [
            "A brokerage subdomain that promotes the brokerage, not you",
            "Portal profiles that sell your leads to competing agents",
            "$50–150/month website builders with MLS widgets from 2015",
            "Listing photos crammed into a gallery that ruins them",
        ],
        "get_head": "What you get",
        "gets": [
            ("A personal brand site", "Your name, your face, your sold record — designed like a luxury brand, because that's the market you want."),
            ("Listing galleries done right", "Full-bleed photography with blur-up loading — the same pipeline that processed 2,100+ photos for a national launch."),
            ("Neighborhood pages", "A page per farm area — the content structure that ranks for '[neighborhood] homes for sale' searches."),
            ("Lead capture you own", "Every inquiry goes to you. No portal reselling your buyer to three other agents."),
        ],
        "proof": "Built on the architecture we used for a national organization's launch: zero downtime, $0/month hosting, and galleries that handle professional photography at full quality.",
        "price_line": "Agent sites fit <strong>Launch at $2,950</strong>; teams with neighborhood/SEO architecture fit <strong>Signature from $7,500</strong>.",
        "cta_head": "Send us your current profile or site",
        "cta_sub": "We'll return a personal-brand remake that makes the brokerage template embarrassing. Free.",
    },
    {
        "slug": "clinics",
        "title": "Medical & Dental Practice Website Design",
        "meta_title": "Medical & Dental Website Design — Trust at First Sight | Everbuilt Studio",
        "meta_desc": "Websites for medical, dental, and wellness practices: calm premium design, service pages that rank, online booking links, and $0/month hosting. From $2,950.",
        "kicker": "For clinics & practices",
        "h1": "Patients choose the practice that looks like it cares",
        "lede": "Before anyone reads a word, your website has told them whether your practice is modern or dated, calm or chaotic. Most practice sites send exactly the wrong signal — then charge you monthly for it.",
        "pains_head": "The practice website problem",
        "pains": [
            "A healthcare-template site that feels like a waiting room from 2009",
            "Service pages too generic to rank for the procedures you actually want",
            "A vendor contract where you pay monthly and own nothing",
            "New-patient forms that live on paper or a third-party portal maze",
        ],
        "get_head": "What your practice gets",
        "gets": [
            ("Calm, premium design", "Clean typography, real photography of your practice, and the visual reassurance patients decide by."),
            ("Procedure pages that rank", "A substantive page per service — implants, orthodontics, physio, aesthetics — structured the way Google rewards."),
            ("Booking integration", "Zocdoc, NexHealth, Calendly, or your PMS — the 'book now' path wired to whatever you already use."),
            ("Own it, $0/month", "One-time build, no hosting bill, no vendor dependency. Your practice's asset, on your practice's domain."),
        ],
        "proof": "The same engineering that launched a national organization with zero downtime — applied to the site your patients see before they ever call.",
        "price_line": "Single-location practices fit <strong>Launch at $2,950</strong>; multi-provider practices with procedure architecture fit <strong>Signature from $7,500</strong>.",
        "cta_head": "See your practice's site remade — free",
        "cta_sub": "Send us your current site and we'll return a finished, calmer, more credible remake.",
    },
    {
        "slug": "churches",
        "title": "Church & Ministry Website Design",
        "meta_title": "Church Website Design — Welcoming, Simple, $0/Month | Everbuilt Studio",
        "meta_desc": "Church websites that welcome first-time visitors: service times up front, sermons, events your team updates from a spreadsheet, and $0/month hosting forever. From $2,950.",
        "kicker": "For churches & ministries",
        "h1": "Your website is the new front door",
        "lede": "Nearly every first-time visitor checks the website before the service. If the times are wrong, the photos are stock, or the site feels abandoned — they've already decided. Every dollar saved on hosting is a dollar for ministry.",
        "pains_head": "The church website problem",
        "pains": [
            "Service times buried while the homepage plays a video no one asked for",
            "An events calendar that's three months out of date",
            "A volunteer 'web person' who moved away with the passwords",
            "Monthly platform fees paid out of the offering",
        ],
        "get_head": "What your church gets",
        "gets": [
            ("Visitor-first homepage", "Times, location, what to expect — the first-timer's questions answered above the fold."),
            ("Events from a spreadsheet", "Your team edits a Google Sheet; the site calendar updates in minutes. No training, no passwords lost."),
            ("Sermons & media", "Embedded from YouTube or podcast feeds — the platforms you already use, presented beautifully."),
            ("$0/month forever", "One-time build. No hosting bill drawn from the offering, ever. The site is the church's property."),
        ],
        "proof": "Our spreadsheet-driven events system was built for a national nonprofit tour — their team updates the site with zero technical staff. Yours will too.",
        "price_line": "Most churches fit <strong>Launch at $2,950</strong> — one-time, with 90 days of free care and volunteer handoff training.",
        "cta_head": "Send us your current site",
        "cta_sub": "We'll return a warmer, clearer remake your board can see live. Free.",
    },
    {
        "slug": "contractors",
        "title": "Contractor & Trades Website Design",
        "meta_title": "Contractor Website Design — Win Bigger Jobs | Everbuilt Studio",
        "meta_desc": "Websites for contractors, remodelers, and trades: project galleries that sell craftsmanship, service-area pages, lead forms, and $0/month hosting. From $2,950.",
        "kicker": "For contractors & trades",
        "h1": "Charge premium rates? Look like it.",
        "lede": "Homeowners shortlist contractors from their websites before a single call. A $30K remodel client expects a $30K-looking portfolio — not a Facebook page and a logo from 2011.",
        "pains_head": "Why good contractors lose bids",
        "pains": [
            "Your best work lives in your phone's camera roll, not on the web",
            "A lead-gen site funneling 'your' leads to three competitors",
            "Service-area pages that don't exist, so nearby towns never find you",
            "A template site that says budget when your work says premium",
        ],
        "get_head": "What your company gets",
        "gets": [
            ("Project galleries that sell", "Before/afters and finished work, full-bleed and fast — the same photo pipeline from our national-scale launch."),
            ("Service-area pages", "A page per town you serve — the structure that ranks for 'remodeler near [town]' searches."),
            ("Leads that are yours", "Quote-request forms straight to your inbox. No shared leads, no per-lead fees."),
            ("Own it, $0/month", "Pay once. No website subscription eating margin on every job."),
        ],
        "proof": "We processed 78GB of client photography for a national launch — your project portfolio is exactly the kind of content this architecture was built for.",
        "price_line": "Most trades fit <strong>Launch at $2,950</strong>; multi-crew companies with service-area SEO fit <strong>Signature from $7,500</strong>.",
        "cta_head": "Send us your current site — or just your photos",
        "cta_sub": "We'll return a portfolio-grade remake that matches the work you actually do. Free.",
    },
]

# ============================================================
# Guide articles (guides/<slug>.html) — informational/commercial intent
# ============================================================
ARTICLES = [
    {
        "slug": "how-much-does-a-website-cost",
        "title": "How Much Does a Website Cost in 2026?",
        "meta_title": "How Much Does a Website Cost in 2026? Real Numbers | Everbuilt Studio",
        "meta_desc": "Real 2026 website pricing: DIY builders $192–600/yr forever, freelancers $1–5K, agencies $35–60K plus retainers — and the flat-fee model that ends monthly costs entirely.",
        "kicker": "Pricing guide",
        "h1": "How much does a website cost in 2026? The honest numbers.",
        "lede": "Most pricing guides are written to hide the real answer. Here it is up front: the sticker price matters less than the monthly bleed that follows it. This guide covers both.",
        "sections": [
            ("The four ways to buy a website", [
                "There are only four real options, and each hides its true cost in a different place. <strong>DIY builders</strong> (Wix, Squarespace) charge $16–50/month — $192–600 a year, forever, for a site you build yourself on a platform you don't own. <strong>Freelancers</strong> charge $1,000–5,000 up front, plus hosting, plus whatever their availability looks like next year. <strong>Agencies</strong> charge $35,000–60,000 for a custom build, then $200–500/month in 'maintenance' — and the contract often says they own the code. <strong>Design subscriptions</strong> run $2,500–5,000 per month with unlimited requests, which is excellent value right up until you do the annual math.",
            ]),
            ("The cost nobody puts on the invoice", [
                "A $35/month builder subscription is $2,100 over five years. A $300/month agency maintenance contract is $18,000 over the same period — often more than the original build. The web industry's core business model is not building websites; it is renting them back to their owners. When you compare quotes, multiply every monthly number by 60 and add it to the sticker price. The rankings change dramatically.",
            ]),
            ("What a fair flat-fee build looks like", [
                "Modern edge infrastructure (the same class of hosting used by major tech companies) has a free tier generous enough to run most business websites at genuinely $0/month — no servers, no database, unlimited bandwidth. A studio that architects for it can charge once and hand over everything: code, content, domain, admin keys. Our own pricing on that model: <strong>$2,950</strong> for a premium 5-page site, <strong>$7,500+</strong> for large builds with galleries and admin tooling, <strong>$15K+</strong> for web and mobile apps. After launch: $0/month, with optional care plans if you want a team on call.",
                "The proof it works at scale: we launched a national nonprofit's site — 2,100+ photos, an admin panel, a zero-downtime domain cutover — for $7,500 against agency quotes of $35–60K. It has cost $0/month since launch day.",
            ]),
            ("Questions to ask any web vendor", [
                "Who owns the code and content when we part ways? What happens to the site if I stop paying you? What is the all-in five-year cost, including every monthly fee? Can my team update content without paying you? If a vendor squirms on any of these, you've found where the real price lives.",
            ]),
        ],
        "cta_head": "Want the flat-fee version of your website?",
        "cta_sub": "Send us your current site. We'll return a finished premium remake — free — and a fixed quote with no monthly anything.",
    },
    {
        "slug": "squarespace-alternative",
        "title": "The Squarespace Alternative for People Who Want to Own Their Site",
        "meta_title": "Squarespace Alternative — Own Your Website, Pay $0/Month | Everbuilt Studio",
        "meta_desc": "Squarespace costs $192–588/year forever and owns your site. The alternative: a custom-built website you own outright with $0/month hosting — from $2,950 once.",
        "kicker": "Comparison",
        "h1": "The Squarespace alternative: own it, and stop paying rent",
        "lede": "Squarespace is genuinely good at what it is — a $16–49/month landlord. The question is whether you want to rent your website forever, or own it.",
        "sections": [
            ("What Squarespace actually costs", [
                "The Business plan is $33/month billed annually — $396/year. Over five years, that's $1,980 for a site that still looks like a template, still carries platform limits, and still goes dark the month you stop paying. The subscription price also buys you a hard ceiling: your design is bounded by what the template system allows, your speed is what the platform serves, and your export options are deliberately incomplete.",
            ]),
            ("What 'owning your website' means", [
                "An owned website is a set of files — yours — on a domain — yours — deployable anywhere, editable by any developer alive, with no platform that can raise prices or sunset features underneath you. Modern static architecture makes owned sites <em>faster</em> than platform sites and hostable for genuinely $0/month on global edge infrastructure. Stop paying anyone, and the site simply keeps running.",
            ]),
            ("The math and the catch", [
                "A custom-built owned site at $2,950 costs less than five years of Squarespace Business — and at year six you're $2,000 ahead and climbing, with a site designed rather than templated. The honest catch: you need someone to build it well the first time, and you should demand they hand over everything. That's our entire model: from $2,950, delivered in about a week, you own the code, the content, and the domain, with 90 days of free care and optional support after. We launched a national nonprofit on this architecture — $0/month since day one.",
            ]),
        ],
        "cta_head": "See your Squarespace site rebuilt as something you own",
        "cta_sub": "Send us your current site. We'll return a finished custom remake — free — so you can compare before deciding anything.",
    },
    {
        "slug": "website-in-a-week",
        "title": "Can You Really Get a Premium Website in a Week?",
        "meta_title": "Website in a Week — How Days-Not-Months Actually Works | Everbuilt Studio",
        "meta_desc": "Yes, a premium custom website can launch in about a week — if the studio has productized the slow parts. Here's the honest day-by-day breakdown of how it works.",
        "kicker": "Process",
        "h1": "A premium website in a week: how it actually works",
        "lede": "Agencies quote 3–6 months. We ship in days. Neither number is magic — the difference is where the time actually goes, and who's paying for it.",
        "sections": [
            ("Where agency months actually go", [
                "Discovery workshops, stakeholder interviews, three rounds of wireframes, design-review cycles, a development handoff, a QA phase, a launch committee. Most of it is process built for six-figure projects and billed accordingly. The actual design-and-build work inside a typical business website is measured in days — it's the meeting-industrial-complex around it that's measured in months.",
            ]),
            ("The week, day by day", [
                "<strong>Day 0:</strong> you request a free remake; we build a finished homepage and send a live link — before any contract. <strong>Day 1:</strong> you say yes, pay the 50% deposit, and send your content. <strong>Days 2–5:</strong> we build the full site at a private preview link; you comment, we revise same-day. <strong>Days 6–7:</strong> zero-downtime launch on your domain, with your email untouched — guaranteed in writing. The speed comes from productized pipelines: media processing, form wiring, and DNS cutover runbooks proven on a national-scale launch, not reinvented per project.",
            ]),
            ("What speed doesn't cost you", [
                "Fast doesn't mean template. Every build is custom-designed; the remake you approve on day 0 is the design standard for the whole site. It also doesn't mean fragile: our launch runbook took a national nonprofit live with zero minutes of downtime, 2,100+ photos processed, and $0/month hosting after. Speed is an engineering outcome, not a corner cut.",
            ]),
        ],
        "cta_head": "Start your week with the free remake",
        "cta_sub": "Send us your current site today; see your new homepage this week — free, no meeting required.",
    },
]

# ============================================================
# Shared chrome
# ============================================================
NAV = """<nav class="nav">
  <div class="wrap nav-inner">
    <a class="brand" href="{root}index.html">
      <svg width="26" height="26" viewBox="0 0 26 26" fill="none" aria-hidden="true">
        <rect x="1" y="1" width="24" height="24" rx="5" fill="#F2EDE4"/>
        <path d="M7 8h12M7 13h9M7 18h12" stroke="#FF5A28" stroke-width="2.4" stroke-linecap="round"/>
      </svg>
      Everbuilt<span>.</span>
    </a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none"><path d="M4 7h16M4 12h16M4 17h16" stroke="#17140F" stroke-width="2" stroke-linecap="round"/></svg>
    </button>
    <ul class="nav-links">
      <li><a href="{root}work/us250.html">Work</a></li>
      <li><a href="{root}index.html#immersive">Immersive</a></li>
      <li><a href="{root}index.html#audiences">Who we serve</a></li>
      <li><a href="{root}index.html#pricing">Pricing</a></li>
      <li><a href="{root}index.html#process">Process</a></li>
      <li><a href="{root}index.html#faq">FAQ</a></li>
      <li><a class="nav-cta" href="{root}index.html#contact">Start a project</a></li>
    </ul>
  </div>
</nav>"""

FOOTER = """<footer>
  <div class="wrap footer-inner">
    <div>
      <div class="brand" style="font-size:1.1rem; margin-bottom:8px;">Everbuilt<span>.</span></div>
      <div>Built once. Yours forever.</div>
    </div>
    <ul class="footer-links">
      <li><a href="{root}work/us250.html">Work</a></li>
      <li><a href="{root}work/immersive.html">Immersive builds</a></li>
      <li><a href="{root}for/small-business.html">For businesses</a></li>
      <li><a href="{root}for/nonprofits.html">For nonprofits</a></li>
      <li><a href="{root}for/founders.html">For founders</a></li>
      <li><a href="{root}for/personal.html">For individuals</a></li>
      <li><a href="{root}index.html#contact">Contact</a></li>
    </ul>
  </div>
  <div class="wrap footer-industries">
    <span>Industries:</span>
    <a href="{root}for/restaurants.html">Restaurants</a>
    <a href="{root}for/law-firms.html">Law firms</a>
    <a href="{root}for/real-estate.html">Real estate</a>
    <a href="{root}for/clinics.html">Clinics</a>
    <a href="{root}for/churches.html">Churches</a>
    <a href="{root}for/contractors.html">Contractors</a>
    <span style="margin-left:14px;">Guides:</span>
    <a href="{root}guides/how-much-does-a-website-cost.html">Website costs 2026</a>
    <a href="{root}guides/squarespace-alternative.html">Squarespace alternative</a>
    <a href="{root}guides/website-in-a-week.html">Website in a week</a>
  </div>
  <div class="wrap" style="margin-top: 24px; font-size: 0.8rem;">© <span id="year"></span> Everbuilt Studio. All rights reserved.</div>
</footer>"""

SCRIPTS = """<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.14/dist/lenis.min.js"></script>
<script src="{root}assets/main.js"></script>"""

HEAD = """<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{meta_title}</title>
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title} | Everbuilt Studio">
<meta property="og:description" content="{meta_desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{domain}/assets/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,500;0,600;0,700;1,500&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/styles.css">"""

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
{head}
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Service","name":{title_json},"provider":{{"@type":"ProfessionalService","name":"Everbuilt Studio","url":"{domain}/"}},"areaServed":"United States","description":{desc_json}}}
</script>
</head>
<body>

{nav}

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

{footer}

{scripts}
</body>
</html>
"""

ARTICLE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
{head}
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":{title_json},"description":{desc_json},"author":{{"@type":"Organization","name":"Everbuilt Studio"}},"publisher":{{"@type":"Organization","name":"Everbuilt Studio","url":"{domain}/"}},"mainEntityOfPage":"{canonical}"}}
</script>
</head>
<body>

{nav}

<header class="page-hero">
  <div class="wrap">
    <p class="kicker">{kicker}</p>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
  </div>
</header>

<section style="padding-top: 56px;">
  <div class="wrap">
    <div class="prose">
{body_html}
    </div>
    <div class="cta-band">
      <h2>{cta_head}</h2>
      <p>{cta_sub}</p>
      <a class="btn btn-primary" href="../index.html#contact">Get the free remake</a>
    </div>
  </div>
</section>

{footer}

{scripts}
</body>
</html>
"""

import json


def make_head(title, meta_title, meta_desc, canonical, root, og_type="website"):
    return HEAD.format(
        meta_title=html.escape(meta_title), meta_desc=html.escape(meta_desc),
        canonical=canonical, title=html.escape(title), root=root,
        domain=DOMAIN, og_type=og_type,
    )


def render_page(page):
    root = "../"
    canonical = f"{DOMAIN}/for/{page['slug']}.html"
    pains_html = "\n".join(f"      <li>{html.escape(p)}</li>" for p in page["pains"])
    gets_html = "\n".join(
        f"""      <div class="aud-card" style="cursor:default;">
        <h3>{html.escape(t)}</h3>
        <p style="margin-bottom:0;">{html.escape(d)}</p>
      </div>"""
        for t, d in page["gets"]
    )
    return PAGE_TEMPLATE.format(
        head=make_head(page["title"], page["meta_title"], page["meta_desc"], canonical, root),
        title_json=json.dumps(page["title"]), desc_json=json.dumps(page["meta_desc"]),
        domain=DOMAIN, canonical=canonical,
        nav=NAV.format(root=root), footer=FOOTER.format(root=root),
        scripts=SCRIPTS.format(root=root),
        kicker=html.escape(page["kicker"]), h1=html.escape(page["h1"]),
        lede=html.escape(page["lede"]), pains_head=html.escape(page["pains_head"]),
        pains_html=pains_html, get_head=html.escape(page["get_head"]),
        gets_html=gets_html, proof=html.escape(page["proof"]),
        price_line=page["price_line"],
        cta_head=html.escape(page["cta_head"]), cta_sub=html.escape(page["cta_sub"]),
    )


def render_article(art):
    root = "../"
    canonical = f"{DOMAIN}/guides/{art['slug']}.html"
    parts = []
    for h2, paras in art["sections"]:
        parts.append(f"      <h2>{html.escape(h2)}</h2>")
        for p in paras:
            parts.append(f"      <p>{p}</p>")  # paragraphs carry intentional markup
    return ARTICLE_TEMPLATE.format(
        head=make_head(art["title"], art["meta_title"], art["meta_desc"], canonical, root, og_type="article"),
        title_json=json.dumps(art["title"]), desc_json=json.dumps(art["meta_desc"]),
        domain=DOMAIN, canonical=canonical,
        nav=NAV.format(root=root), footer=FOOTER.format(root=root),
        scripts=SCRIPTS.format(root=root),
        kicker=html.escape(art["kicker"]), h1=html.escape(art["h1"]),
        lede=html.escape(art["lede"]), body_html="\n".join(parts),
        cta_head=html.escape(art["cta_head"]), cta_sub=html.escape(art["cta_sub"]),
    )


def write_sitemap():
    urls = [f"{DOMAIN}/", f"{DOMAIN}/work/us250.html", f"{DOMAIN}/work/immersive.html"]
    urls += [f"{DOMAIN}/for/{p['slug']}.html" for p in PAGES]
    urls += [f"{DOMAIN}/guides/{a['slug']}.html" for a in ARTICLES]
    body = "\n".join(
        f"  <url><loc>{u}</loc><priority>{'1.0' if u.endswith('.com/') else '0.8'}</priority></url>"
        for u in urls
    )
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{body}\n</urlset>\n",
        encoding="utf-8",
    )
    print(f"wrote sitemap.xml ({len(urls)} urls)")


def main():
    (ROOT / "for").mkdir(exist_ok=True)
    (ROOT / "guides").mkdir(exist_ok=True)
    for page in PAGES:
        path = ROOT / "for" / f"{page['slug']}.html"
        path.write_text(render_page(page), encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")
    for art in ARTICLES:
        path = ROOT / "guides" / f"{art['slug']}.html"
        path.write_text(render_article(art), encoding="utf-8")
        print(f"wrote {path.relative_to(ROOT)}")
    write_sitemap()


if __name__ == "__main__":
    main()

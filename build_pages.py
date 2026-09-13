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
    {
        "slug": "photographers",
        "title": "Photographer Website Design",
        "meta_title": "Photographer Website Design — Own Your Portfolio | Everbuilt Studio",
        "meta_desc": "Photography websites built for full-resolution work: fast galleries, blur-up loading, client proofing links, and $0/month hosting. From $2,950, live in about a week.",
        "kicker": "For photographers & studios",
        "h1": "Your portfolio deserves better than a platform's compression",
        "lede": "You spend hours on a single edit, then hand it to a template that crushes it to 1200px, watermarks the loading state, and charges you monthly to keep it online. Photographers have the most to lose from renting their own website.",
        "pains_head": "The photographer website trap",
        "pains": [
            "Portfolio platforms re-compressing your work until the grade is gone",
            "$20–50/month forever — and your galleries vanish the month you stop",
            "Galleries that stall on mobile, so clients never reach image 40",
            "Every other shooter in your city on the exact same three templates",
        ],
        "get_head": "What your studio gets",
        "gets": [
            ("Galleries built for real volume", "We processed 78GB of media and optimized 2,100+ photos for a national client launch. A wedding gallery or a 300-frame portfolio is well inside what this pipeline was engineered for."),
            ("Your grade, preserved", "Modern responsive image sets — the browser gets the right resolution for the screen instead of one over-compressed file for everyone. Blur-up loading so nothing ever appears broken mid-scroll."),
            ("Proofing and booking wired in", "Pixieset, ShootProof, Pic-Time, Honeybook, Calendly — your existing client-delivery and inquiry tools linked cleanly, not replaced."),
            ("Own the whole portfolio", "Code, images, domain, admin keys. No platform can sunset a feature, raise your rate, or hold a decade of work hostage."),
        ],
        "proof": "Our media pipeline was built for a national nonprofit tour: 78GB processed, 2,100+ photos optimized, zero downtime at launch, and $0/month hosting since. That's the same pipeline your portfolio runs on.",
        "price_line": "Most photographers fit <strong>Launch at $2,950</strong>; studios with large multi-gallery archives fit <strong>Signature from $7,500</strong>.",
        "cta_head": "Send us your portfolio as it stands today",
        "cta_sub": "A platform page, an Instagram grid, a folder of finals — we'll return a finished remake with your work at full quality. Free.",
    },
    {
        "slug": "accountants",
        "title": "Website Design for Accountants & CPA Firms",
        "meta_title": "Accountant & CPA Website Design — Credibility, $0/Month | Everbuilt Studio",
        "meta_desc": "CPA and accounting firm websites that signal precision: service pages that rank, secure client-portal links, and $0/month hosting. From $2,950, live in about a week.",
        "kicker": "For accountants & CPA firms",
        "h1": "You audit their books. They audit your website.",
        "lede": "A prospect deciding between two CPAs picks the one whose website looks like it files things on time. Most firm sites look like they were filed in 2012 — and bill monthly for the privilege.",
        "pains_head": "The accounting firm website problem",
        "pains": [
            "A dated template that undercuts the precision you sell",
            "Service pages too thin to rank for 'tax preparation near me'",
            "A monthly website bill you'd flag in any client's P&L",
            "No clear path from visitor to booked consultation before tax season peaks",
        ],
        "get_head": "What your firm gets",
        "gets": [
            ("Precision-grade design", "Clean, conservative, typographically exact — the visual equivalent of a reconciled ledger."),
            ("Service pages that rank", "Tax prep, bookkeeping, payroll, advisory — a substantive page per service line, structured the way search engines reward."),
            ("Portal & booking wired in", "Links to your client portal, document upload, and scheduling — integrated cleanly with what you already run."),
            ("A one-time cost you'd approve", "Pay once from $2,950, own everything, $0/month hosting. The five-year math wins any comparison you run."),
        ],
        "proof": "The same architecture launched a national nonprofit with zero downtime and has cost $0/month since. Your firm gets engineering discipline that matches your professional standard.",
        "price_line": "Solo CPAs fit <strong>Launch at $2,950</strong>; multi-partner firms with service-line SEO fit <strong>Signature from $7,500</strong>.",
        "cta_head": "See your firm's site remade before tax season",
        "cta_sub": "Send us your current site. We'll return a finished remake your partners can approve on sight. Free.",
    },
    {
        "slug": "salons-spas",
        "title": "Salon & Spa Website Design",
        "meta_title": "Salon & Spa Website Design — Book More Clients | Everbuilt Studio",
        "meta_desc": "Salon and spa websites that feel like the experience you sell: service menus, stylist profiles, online booking links, and $0/month hosting. From $2,950.",
        "kicker": "For salons, spas & studios",
        "h1": "Your website should feel like walking in",
        "lede": "Clients book the salon that already feels premium before they touch the door handle. A cramped template with a PDF price list doesn't sell a $200 balayage — atmosphere does.",
        "pains_head": "Why salon websites lose bookings",
        "pains": [
            "A booking link buried three taps deep while Instagram DMs pile up",
            "A price list that's a photo of a laminated sheet",
            "Platform templates that look like every other salon in town",
            "Monthly website fees quietly eating a client's worth of revenue",
        ],
        "get_head": "What your salon gets",
        "gets": [
            ("Atmosphere-first design", "Full-bleed photography of your space and your work, typography that matches your brand's price point."),
            ("A real service menu", "Services, tiers, and prices your team updates from a spreadsheet — live on the site in minutes."),
            ("Booking wired to your system", "Vagaro, GlossGenius, Square, Booksy — 'book now' goes exactly where your calendar already lives."),
            ("Own it, $0/month", "Pay once. No subscription nibbling your margin every month, forever."),
        ],
        "proof": "Our spreadsheet-driven content system was built for a national tour whose team updates the site with zero technical staff — your front desk can run yours the same way.",
        "price_line": "Most salons and spas fit <strong>Launch at $2,950</strong> — live in about a week, booking wired, menu training included.",
        "cta_head": "Send us your current site or your Instagram",
        "cta_sub": "We'll return a remake that finally matches your work. Free, no strings.",
    },
    {
        "slug": "gyms",
        "title": "Gym & Fitness Studio Website Design",
        "meta_title": "Gym & Fitness Studio Website Design — Convert Sign-ups | Everbuilt Studio",
        "meta_desc": "Gym and fitness studio websites built to convert: class schedules your team edits, trial-offer funnels, coach profiles, and $0/month hosting. From $2,950.",
        "kicker": "For gyms & fitness studios",
        "h1": "Every empty class slot is a website problem",
        "lede": "People decide to try a gym at 11pm on their phone. If your schedule is a screenshot, your trial offer is buried, and the page takes six seconds to load — they're asleep before they convert.",
        "pains_head": "Why gym websites underperform",
        "pains": [
            "A class schedule that's a screenshot from three schedule changes ago",
            "The free-trial offer hidden below fold-after-fold of stock photos",
            "Franchise-template sameness when your community is the product",
            "Software-bundled websites that hold your domain hostage",
        ],
        "get_head": "What your gym gets",
        "gets": [
            ("Trial-first funnel", "The intro offer front and center, with a form or booking link that works on a phone at 11pm."),
            ("Live schedule from a spreadsheet", "Your coaches edit a sheet; the site updates in minutes. No developer, no stale screenshots."),
            ("Coaches & community up front", "Real photos, real trainer bios — the reason people pick a local gym over a franchise app."),
            ("Own it, $0/month", "One-time build. Your member software can change; your website and domain stay yours."),
        ],
        "proof": "The spreadsheet-driven events system powering a national tour's schedule runs your class timetable just as easily — updated by your team, not a vendor.",
        "price_line": "Most gyms and studios fit <strong>Launch at $2,950</strong>; multi-location operations fit <strong>Signature from $7,500</strong>.",
        "cta_head": "Send us your current site",
        "cta_sub": "We'll return a remake with your trial offer doing the work it should. Free.",
    },
    {
        "slug": "landscapers",
        "title": "Landscaping Company Website Design",
        "meta_title": "Landscaping Website Design — Win Bigger Projects | Everbuilt Studio",
        "meta_desc": "Landscaping and lawn care websites with project galleries that sell, service-area pages that rank, and quote forms that are yours alone. $0/month hosting. From $2,950.",
        "kicker": "For landscapers & lawn care",
        "h1": "Your work is visual. Your website should be devastating.",
        "lede": "A $60K outdoor living project is sold by photos, not promises. If your best transformations live in a phone gallery instead of a portfolio that loads instantly, you're bidding with one hand tied.",
        "pains_head": "Why landscapers lose the big bids",
        "pains": [
            "Before/after photos trapped in your camera roll and old Facebook posts",
            "Lead platforms selling 'your' inquiry to three competitors",
            "No pages for the towns you serve, so nearby searches skip you",
            "A site that says mow-and-blow when you sell design-and-build",
        ],
        "get_head": "What your company gets",
        "gets": [
            ("Transformation galleries", "Before/afters full-bleed and fast — the same media pipeline that processed 78GB for a national launch."),
            ("Service-area pages", "A page per town you serve, structured to rank for 'landscaper near [town]'."),
            ("Quote requests that are yours", "Forms straight to your inbox with a redundant capture net. No shared leads, no per-lead fees."),
            ("Own it, $0/month", "Pay once. No subscription eating margin through the winter months."),
        ],
        "proof": "We processed 2,100+ photos for a national client launch — a season of project photography is exactly what this architecture was built to showcase.",
        "price_line": "Most landscaping companies fit <strong>Launch at $2,950</strong>; design-build firms with service-area SEO fit <strong>Signature from $7,500</strong>.",
        "cta_head": "Send us your photos — even just your camera roll",
        "cta_sub": "We'll return a portfolio-grade remake that bids at your real level. Free.",
    },
    {
        "slug": "plumbers",
        "title": "Plumbing Company Website Design",
        "meta_title": "Plumber Website Design — Calls, Not Clicks | Everbuilt Studio",
        "meta_desc": "Plumbing websites engineered for the emergency call: tap-to-call above the fold, service pages that rank, reviews up front, and $0/month hosting. From $2,950.",
        "kicker": "For plumbers & plumbing companies",
        "h1": "A burst pipe doesn't browse. It calls the first credible result.",
        "lede": "Plumbing search is the most urgent traffic on the internet — and most plumbing websites bury the phone number under a slideshow. Your site has one job at 2am: get tapped.",
        "pains_head": "Why plumbing sites lose the emergency call",
        "pains": [
            "Phone number below the fold on mobile — where every emergency search happens",
            "Lead-gen sites reselling 'your' emergency to whoever pays most",
            "One generic services page instead of pages that rank per job type",
            "A monthly website bill that outlasted three vans",
        ],
        "get_head": "What your company gets",
        "gets": [
            ("Tap-to-call architecture", "Number pinned at the top of every page, tap-to-call on mobile, emergency framing above the fold."),
            ("Job-type pages that rank", "Water heaters, drain cleaning, repipes, sewer lines — a page per service, the structure search rewards."),
            ("Reviews front and center", "Your Google reviews pulled into the page where the deciding moment happens."),
            ("Own it, $0/month", "One-time build, no subscription. Your website should be the one thing that never springs a leak in the budget."),
        ],
        "proof": "Built on the runbook that launched a national site with zero minutes of downtime — because downtime for you is a missed emergency call.",
        "price_line": "Most plumbing companies fit <strong>Launch at $2,950</strong>; multi-truck operations with service-area SEO fit <strong>Signature from $7,500</strong>.",
        "cta_head": "Send us your current site",
        "cta_sub": "We'll return a remake built around the phone call. Free.",
    },
    {
        "slug": "hvac",
        "title": "HVAC Company Website Design",
        "meta_title": "HVAC Website Design — Seasonal Surges, Owned Leads | Everbuilt Studio",
        "meta_desc": "HVAC websites built for the July breakdown and the January freeze: emergency call paths, service pages that rank, financing info, and $0/month hosting. From $2,950.",
        "kicker": "For HVAC companies",
        "h1": "When the AC dies in July, your website has 10 seconds",
        "lede": "HVAC demand arrives in surges — heat waves, cold snaps, the first 90° weekend. The companies that win those surges have a site that loads instantly, ranks for the job, and puts the number where a sweating homeowner's thumb already is.",
        "pains_head": "Why HVAC sites miss the surge",
        "pains": [
            "Franchise-grade template with the phone number playing hide and seek",
            "No pages for AC repair vs furnace replacement vs mini-splits — so none of them rank",
            "Financing options nowhere to be found on a $12K replacement decision",
            "Paying monthly for a site the software vendor actually controls",
        ],
        "get_head": "What your company gets",
        "gets": [
            ("Surge-ready speed", "Static architecture that loads instantly under load — no server to melt down in a heat wave."),
            ("Service & equipment pages", "Repair, replacement, maintenance plans, heat pumps, mini-splits — each its own ranking page."),
            ("Financing made visible", "Your financing partners and maintenance-plan pricing presented clearly on the pages where $12K decisions happen."),
            ("Own it, $0/month", "Pay once, own everything. The only thing in your business with zero recurring cost."),
        ],
        "proof": "The same zero-downtime launch runbook we used for a national client — because your site going dark during a cold snap is revenue you never get back.",
        "price_line": "Most HVAC companies fit <strong>Launch at $2,950</strong>; multi-county operations fit <strong>Signature from $7,500</strong>.",
        "cta_head": "Get the remake before the next surge",
        "cta_sub": "Send us your current site; we'll return a finished remake built for the season that pays your year. Free.",
    },
    {
        "slug": "roofers",
        "title": "Roofing Company Website Design",
        "meta_title": "Roofing Website Design — Storm-Season Ready | Everbuilt Studio",
        "meta_desc": "Roofing company websites that win the storm-season search: inspection CTAs, project galleries, insurance-claim guidance pages, and $0/month hosting. From $2,950.",
        "kicker": "For roofing companies",
        "h1": "After the hailstorm, homeowners search. Be findable, be credible, be first.",
        "lede": "Roofing is bought twice: in panic after a storm, and in research mode for a replacement. Your website has to win both — instant credibility for the panic buyer, real information for the researcher.",
        "pains_head": "Why roofing sites lose jobs",
        "pains": [
            "Indistinguishable from the storm-chaser sites homeowners are warned about",
            "No insurance-claim guidance when that's the first question every hail victim has",
            "Drone shots of your best roofs sitting unused in a hard drive",
            "Lead services reselling the same roof to four contractors",
        ],
        "get_head": "What your company gets",
        "gets": [
            ("Local-and-legit signals", "Real address, real crew photos, real project gallery, license numbers visible — everything that separates you from the storm-chasers."),
            ("Insurance-claim content", "A clear claims-process page that answers the panicked homeowner's first question and positions you as the guide."),
            ("Free-inspection funnel", "The inspection offer above the fold with a form that hits your inbox instantly — yours alone."),
            ("Own it, $0/month", "One-time build. No monthly bill riding on every square you install."),
        ],
        "proof": "Project galleries run on the pipeline that processed 78GB of media for a national launch — your drone footage and finished roofs are light work.",
        "price_line": "Most roofing companies fit <strong>Launch at $2,950</strong>; storm-market operations with claims content fit <strong>Signature from $7,500</strong>.",
        "cta_head": "Send us your current site",
        "cta_sub": "We'll return a remake that looks like the company you'd let on your own roof. Free.",
    },
    {
        "slug": "wedding-venues",
        "title": "Wedding Venue Website Design",
        "meta_title": "Wedding Venue Website Design — Tours Booked From the Page | Everbuilt Studio",
        "meta_desc": "Wedding venue websites that sell the feeling: full-bleed galleries, real pricing guidance, tour booking, and $0/month hosting. From $2,950, live in about a week.",
        "kicker": "For wedding venues & event spaces",
        "h1": "Couples fall in love with venues online first",
        "lede": "By the time a couple requests a tour, your website has already made the shortlist decision for them. Venues lose bookings to worse spaces with better galleries every single weekend.",
        "pains_head": "Why venue websites lose bookings",
        "pains": [
            "Gallery photos compressed until the golden hour looks beige",
            "'Contact us for pricing' walls that make couples assume the worst",
            "A tour-request form that feels like a mortgage application",
            "Platform sites that rank The Knot's page for your own venue above yours",
        ],
        "get_head": "What your venue gets",
        "gets": [
            ("Galleries that sell the feeling", "Full-bleed, fast, color-true — the same media pipeline that handled 2,100+ photos for a national launch."),
            ("Pricing transparency that filters", "Starting-at pricing and package outlines that pre-qualify couples before the tour."),
            ("Two-field tour request", "Date + email. The lowest-friction path from scrolling to standing in your space."),
            ("Own it, $0/month", "Pay once. Your venue's most-viewed marketing asset shouldn't have a subscription."),
        ],
        "proof": "Our media pipeline was built for a 50-state tour's photography volume — a wedding season of galleries is exactly the workload it was engineered for.",
        "price_line": "Most venues fit <strong>Signature from $7,500</strong> (galleries at real volume); single-space venues fit <strong>Launch at $2,950</strong>.",
        "cta_head": "Send us your current site and your best gallery",
        "cta_sub": "We'll return a remake that books tours on sight. Free.",
    },
    {
        "slug": "therapists",
        "title": "Therapist & Counseling Practice Website Design",
        "meta_title": "Therapist Website Design — Warmth That Converts | Everbuilt Studio",
        "meta_desc": "Therapy and counseling websites that feel safe before the first session: warm design, specialty pages, insurance clarity, and $0/month hosting. From $2,950.",
        "kicker": "For therapists & counselors",
        "h1": "The first therapeutic moment is your website",
        "lede": "Someone finding a therapist is often having a hard week. A cluttered, clinical, or broken website adds friction exactly where there should be calm. Your site's job is to feel like the first good session.",
        "pains_head": "Why practice websites turn clients away",
        "pains": [
            "Directory profiles ranking above your own site for your own name",
            "Specialties listed as a comma-separated wall instead of pages that rank",
            "Insurance and rate questions unanswered — the #1 reason people don't reach out",
            "A monthly website bill on a solo practice's margins",
        ],
        "get_head": "What your practice gets",
        "gets": [
            ("Calm, warm design", "Soft typography, real photography, unhurried layout — the visual register of a safe room."),
            ("Specialty pages", "Anxiety, couples, EMDR, teens — a genuine page per specialty, which is how clients search and how you rank."),
            ("Clarity that converts", "Rates, insurance, and what-to-expect answered plainly — removing the questions that stop the first email."),
            ("Own it, $0/month", "One-time cost a solo practice can approve, then nothing, forever."),
        ],
        "proof": "The same engineering that launched a national organization's site — applied at the scale and budget of a private practice.",
        "price_line": "Most solo practices fit <strong>Launch at $2,950</strong>; group practices with specialty SEO fit <strong>Signature from $7,500</strong>.",
        "cta_head": "See your practice site remade",
        "cta_sub": "Send us your current site or directory profile. We'll return a remake that feels like your work. Free.",
    },
    {
        "slug": "veterinarians",
        "title": "Veterinary Clinic Website Design",
        "meta_title": "Veterinary Website Design — Trust at First Paw | Everbuilt Studio",
        "meta_desc": "Veterinary clinic websites that reassure worried owners: emergency info up front, service pages that rank, online booking links, and $0/month hosting. From $2,950.",
        "kicker": "For veterinary clinics",
        "h1": "Pet owners choose the clinic that feels kind before they call",
        "lede": "A worried owner at midnight isn't comparing your accreditations — they're feeling for warmth and checking if you're open. Most veterinary websites answer neither quickly.",
        "pains_head": "The veterinary website problem",
        "pains": [
            "Emergency hours and after-hours guidance buried below stock photos of retrievers",
            "Corporate-group templates that erase your clinic's personality",
            "Services listed but never explained — so 'vet dental cleaning near me' skips you",
            "A practice-management-bundled site you don't control",
        ],
        "get_head": "What your clinic gets",
        "gets": [
            ("Warmth with your real team", "Your vets, your techs, your clinic cat — the photos that make owners feel safe choosing you."),
            ("Emergency clarity", "Hours, after-hours protocol, and emergency partners answered at the top of every page."),
            ("Service pages that rank", "Dental, surgery, exotics, urgent care — a page per service line, structured for search."),
            ("Own it, $0/month", "Pay once. Independent clinics keep independence — your site isn't leverage for a software vendor."),
        ],
        "proof": "Launched on the zero-downtime runbook we used for a national organization — because a clinic's website going dark fails owners at the worst moment.",
        "price_line": "Most clinics fit <strong>Launch at $2,950</strong>; multi-doctor practices fit <strong>Signature from $7,500</strong>.",
        "cta_head": "Send us your current site",
        "cta_sub": "We'll return a remake that feels like the clinic owners recommend to friends. Free.",
    },
    {
        "slug": "auto-repair",
        "title": "Auto Repair Shop Website Design",
        "meta_title": "Auto Repair Website Design — Trust Beats Chains | Everbuilt Studio",
        "meta_desc": "Auto repair shop websites that beat the chains on trust: transparent service pages, reviews up front, easy appointment requests, and $0/month hosting. From $2,950.",
        "kicker": "For auto repair shops",
        "h1": "People don't fear car repairs. They fear being taken.",
        "lede": "The independent shop's edge over the chains has always been trust — and trust now gets decided on a phone screen before anyone drives over. Most shop websites squander it with clutter and coupons.",
        "pains_head": "Why shop websites leak customers",
        "pains": [
            "A template screaming 'coupon mailer' when your edge is honesty",
            "Services listed with no plain-English explanation or price guidance",
            "Reviews — your best asset — living only on Google, never on your site",
            "Monthly website fees from an auto-industry vendor that owns your content",
        ],
        "get_head": "What your shop gets",
        "gets": [
            ("Trust-first design", "Clean, honest, plain-spoken — with your real bays, real techs, and real certifications up front."),
            ("Plain-English service pages", "Brakes, diagnostics, transmissions, EV service — explained like you'd explain it at the counter, structured to rank."),
            ("Reviews on the page", "Your Google rating and best reviews where the decision happens, not a click away."),
            ("Own it, $0/month", "One-time build. The only part of the shop with zero recurring overhead."),
        ],
        "proof": "The same build discipline that launched a national organization's site with zero downtime — applied to the site that fills your bays.",
        "price_line": "Most shops fit <strong>Launch at $2,950</strong> — live in about a week, reviews wired, no monthly anything.",
        "cta_head": "Send us your current site",
        "cta_sub": "We'll return a remake that sells your honesty as hard as you've earned it. Free.",
    },
    {
        "slug": "private-schools",
        "title": "Private School & Preschool Website Design",
        "meta_title": "Private School Website Design — Enrollment Starts Online | Everbuilt Studio",
        "meta_desc": "Private school and preschool websites that drive enrollment: tour booking, program pages, real campus photography, and $0/month hosting. From $2,950.",
        "kicker": "For private schools & preschools",
        "h1": "Parents tour your website before they tour your campus",
        "lede": "Enrollment decisions start with a late-night search and a website judgment. A dated site whispers 'declining school' to exactly the families you want — regardless of what's true.",
        "pains_head": "The school website problem",
        "pains": [
            "A site last redesigned when your current seniors were in kindergarten",
            "Tuition and admissions info scattered across PDFs",
            "An events calendar the office can't update without the 'website parent'",
            "Program pages too thin to rank for 'Montessori preschool near me'",
        ],
        "get_head": "What your school gets",
        "gets": [
            ("Enrollment-first design", "Tour booking and inquiry forms prominent on every page — the website as admissions funnel, not brochure."),
            ("Programs that rank", "A substantive page per program and grade band — how parents search, and how you get found."),
            ("A calendar the office runs", "Events managed from a spreadsheet the front office already uses; the site updates in minutes."),
            ("Own it, $0/month", "One-time cost, board-approvable, then nothing — every saved dollar goes back to the classroom."),
        ],
        "proof": "Our spreadsheet-driven events system was built for a national tour and is run by non-technical staff — your front office will manage the site the same way.",
        "price_line": "Most schools fit <strong>Signature from $7,500</strong>; single-program preschools fit <strong>Launch at $2,950</strong>.",
        "cta_head": "Show your board a finished remake",
        "cta_sub": "Send us your current site. We'll return a remake worth putting in front of the enrollment committee. Free.",
    },
    {
        "slug": "event-planners",
        "title": "Event Planner Website Design",
        "meta_title": "Event Planner Website Design — Portfolios That Book | Everbuilt Studio",
        "meta_desc": "Event planning websites with portfolios that close: full-bleed galleries by event type, service tiers, inquiry funnels, and $0/month hosting. From $2,950.",
        "kicker": "For event planners & producers",
        "h1": "You sell flawless execution. Your website is exhibit A.",
        "lede": "A client trusting you with a $150K gala judges your attention to detail by the only work sample they can see for free: your website. A cluttered template is a portfolio stain.",
        "pains_head": "Why planner websites cost bookings",
        "pains": [
            "Your best events living in a phone gallery and a tagged-photos abyss",
            "One 'gallery' page mixing weddings, corporate, and birthdays into mush",
            "Inquiry forms that ask fifteen questions before saying hello",
            "A monthly platform fee on a business built on margins and timing",
        ],
        "get_head": "What your studio gets",
        "gets": [
            ("Portfolios by event type", "Weddings, corporate, galas, launches — separate galleries that rank separately and sell precisely."),
            ("Detail-obsessed design", "Typography and pacing that demonstrate the exact standard you promise clients."),
            ("A two-line inquiry", "Event date + email. Qualification happens in the conversation, not the form."),
            ("Own it, $0/month", "Pay once, own the whole thing — the same clean economics you build into your own contracts."),
        ],
        "proof": "Galleries run on the pipeline that processed 2,100+ photos for a national tour — a season of event photography is comfortably inside spec.",
        "price_line": "Most planners fit <strong>Launch at $2,950</strong>; production companies with multi-vertical portfolios fit <strong>Signature from $7,500</strong>.",
        "cta_head": "Send us your current site and three favorite events",
        "cta_sub": "We'll return a remake that books the next tier of client. Free.",
    },
    {
        "slug": "breweries",
        "title": "Brewery & Taproom Website Design",
        "meta_title": "Brewery Website Design — Taproom Traffic, Tap List Live | Everbuilt Studio",
        "meta_desc": "Brewery and taproom websites with live tap lists your team updates, event calendars, merch links, and $0/month hosting. From $2,950, live in about a week.",
        "kicker": "For breweries & taprooms",
        "h1": "Your beer has character. Your website shouldn't be a template.",
        "lede": "People check the tap list and tonight's food truck before they drive over. If your site is a stale template with last summer's seasonal, the group chat picks the other taproom.",
        "pains_head": "The brewery website problem",
        "pains": [
            "A tap list that's wrong by Thursday",
            "Events and food-truck schedules living only on Instagram stories",
            "A template that has none of the personality your cans do",
            "Monthly website fees on taproom margins",
        ],
        "get_head": "What your brewery gets",
        "gets": [
            ("Live tap list from a spreadsheet", "Your team updates a sheet when a keg kicks; the site updates in minutes. Always right, zero developer."),
            ("Events & food trucks on site", "The weekly schedule where search engines and group chats can find it — not buried in stories."),
            ("Label-grade design", "Your can art, your voice, your weird — a site with the same personality that sells your beer."),
            ("Own it, $0/month", "One-time build. The only thing in the brewery with no recurring cost."),
        ],
        "proof": "Our spreadsheet-driven system runs a national tour's live schedule — a tap list and event calendar are exactly the pattern it was built for.",
        "price_line": "Most taprooms fit <strong>Launch at $2,950</strong> — live in about a week, tap list wired, personality intact.",
        "cta_head": "Send us your current site and your best can art",
        "cta_sub": "We'll return a remake with your brewery's actual personality. Free.",
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
    {
        "slug": "wix-alternative",
        "title": "The Wix Alternative: Own Your Website Instead of Renting It",
        "meta_title": "Wix Alternative 2026 — Own Your Site, $0/Month | Everbuilt Studio",
        "meta_desc": "Wix costs $204–708/year forever, and your site dies when you stop paying. The alternative: a custom site you own outright with $0/month hosting — from $2,950 once.",
        "kicker": "Comparison",
        "h1": "The Wix alternative: stop renting, start owning",
        "lede": "Wix is a fine landlord — $17 to $59 a month, every month, forever. The alternative isn't another landlord. It's a deed.",
        "sections": [
            ("What Wix actually costs over time", [
                "Wix's useful business plans run $17–59/month billed annually — $204 to $708 a year. Five years in, you've paid $1,000–3,500 for a site built on templates, bounded by the platform's editor, and rendered by the platform's servers. And Wix's most important price is hidden: there is <strong>no real export</strong>. Your site cannot leave. The month you stop paying, it stops existing.",
            ]),
            ("The alternative model", [
                "A custom-built static site inverts every one of those terms: files you own, on a domain you control, served from global edge infrastructure whose free tier covers most business websites — genuinely $0/month. Any developer alive can work on it. No platform can raise the rent, retire your template, or hold your content. Modern static sites are also measurably faster than builder sites, which matters for both visitors and rankings.",
            ]),
            ("The math, honestly", [
                "Our Launch build is <strong>$2,950 once</strong> — under five years of a mid-tier Wix plan, and at year six you're ahead and climbing with a site that was designed, not assembled. The honest catch is the same one we give everyone: pay once only works if the builder hands over everything. We do — code, content, domain, admin keys — and we proved the architecture on a national nonprofit launch that has cost $0/month since day one.",
            ]),
        ],
        "cta_head": "See your Wix site rebuilt as something you own",
        "cta_sub": "Send us your Wix URL. We'll return a finished custom remake — free — so you can compare side by side.",
    },
    {
        "slug": "website-redesign-cost",
        "title": "Website Redesign Cost in 2026: What You Should Actually Pay",
        "meta_title": "Website Redesign Cost 2026 — Honest Pricing Guide | Everbuilt Studio",
        "meta_desc": "Website redesign pricing in 2026: freelancers $1,500–5K, agencies $15–75K plus retainers. What drives the price, what's padding, and the flat-fee alternative from $2,950.",
        "kicker": "Pricing guide",
        "h1": "What a website redesign should cost in 2026",
        "lede": "Redesign quotes for the same site routinely span $1,500 to $75,000. That spread isn't about your website — it's about the vendor's overhead. Here's how to read a quote.",
        "sections": [
            ("Why quotes vary 50x for the same site", [
                "A redesign quote prices three things: the actual design-and-build work, the vendor's process around it, and the vendor's business model after it. The work itself — for a typical business site — is measured in days. Agencies add discovery workshops, stakeholder rounds, and project management (that's the $15–75K), and most vendors of every size add the annuity: hosting markups, maintenance retainers, and CMS licensing that quietly double the five-year cost. When you compare quotes, separate the three. You should pay well for the first, sparingly for the second, and ideally never for the third.",
            ]),
            ("The questions that expose padding", [
                "Ask each bidder: What do I own when we're done? What's the all-in five-year number including every recurring fee? What happens if I stop paying you the month after launch? Can my team edit content without a ticket? A redesign that leaves you renting your own site hasn't fixed the expensive part.",
            ]),
            ("What a fair redesign looks like", [
                "Our model: a finished remake of your homepage <strong>before any contract — free</strong> — so you judge the design standard first. Then a flat fee: <strong>$2,950</strong> for most business sites, <strong>$7,500+</strong> for large builds with galleries and admin tooling. Zero-downtime relaunch on your domain with email untouched, everything handed over, and $0/month hosting after — an architecture we proved on a national nonprofit relaunch that hasn't paid a hosting bill since.",
            ]),
        ],
        "cta_head": "Start the redesign with the free remake",
        "cta_sub": "Send us your current site. The first deliverable costs nothing and arrives before any decision.",
    },
    {
        "slug": "website-maintenance-cost",
        "title": "Website Maintenance Costs: What's Real and What's a Subscription Trap",
        "meta_title": "Website Maintenance Cost 2026 — What's Real vs Padding | Everbuilt Studio",
        "meta_desc": "Typical website maintenance runs $50–500/month. Most of it pays for problems the architecture created. Here's what maintenance is real — and the $0/month alternative.",
        "kicker": "Pricing guide",
        "h1": "Most website maintenance fees pay for problems the vendor built in",
        "lede": "The average business pays $100–500 a month to 'maintain' a website. Here's the uncomfortable question: maintain against what, exactly?",
        "sections": [
            ("What maintenance fees actually cover", [
                "On a WordPress or CMS site, the fee is real work: core updates, plugin patches, security scanning, database backups, PHP upgrades, and fixing whatever broke when those things collided. That's $1,200–6,000 a year — paid not because your <em>content</em> changes, but because the architecture has moving parts that rust. The maintenance industry exists because the sites were built to need it.",
            ]),
            ("The architecture with nothing to maintain", [
                "A static site has no database to back up, no plugins to patch, no server to harden, and no version conflicts — there is nothing to rust. Served from edge networks with free tiers covering most business sites, the recurring cost is $0/month, and 'maintenance' reduces to what it always should have been: changing content when your business changes. We built a national nonprofit's site this way — heavy galleries, live event schedule, admin panel — and its maintenance bill since launch is zero.",
            ]),
            ("When a care plan is honestly worth it", [
                "Paying for a team on call is legitimate — for new pages, campaigns, and same-day edits you'd rather not do yourself. That's a service, not a survival fee, and it should be optional. Ours is exactly that: sites run free forever, and care plans ($295–595/month) exist only for owners who want hands on deck. Cancel anytime; the site doesn't care.",
            ]),
        ],
        "cta_head": "Escape the maintenance treadmill",
        "cta_sub": "Send us your current site and your monthly bill. We'll show you the remake and the $0/month math. Free.",
    },
    {
        "slug": "do-i-need-a-website",
        "title": "Do I Actually Need a Website in 2026? An Honest Answer",
        "meta_title": "Do I Need a Website in 2026? The Honest Answer | Everbuilt Studio",
        "meta_desc": "Instagram, Google Business Profile, marketplaces — do you still need a website in 2026? Honest answer: sometimes no. Here's the test, and what to build if it's yes.",
        "kicker": "Straight answer",
        "h1": "Do you actually need a website in 2026?",
        "lede": "A web studio should say 'yes, obviously.' The honest answer is 'usually — but not always, and not for the reason you think.' Here's the test.",
        "sections": [
            ("When you genuinely don't need one", [
                "If you're fully booked from referrals, sell exclusively through a marketplace that owns your traffic anyway, or run a personal-network business where every client shakes your hand first — a Google Business Profile and an active Instagram may honestly be enough. Don't let anyone sell you a website as a talisman. It's a tool, and tools need a job.",
            ]),
            ("The three jobs only a website does", [
                "<strong>Verification:</strong> people who hear about you check whether you're real; social profiles reassure less than a domain of your own. <strong>Search capture:</strong> Instagram doesn't rank for 'wedding photographer near me' — pages do, and that traffic has intent money follows. <strong>Ownership:</strong> every platform audience is rented; algorithms change, accounts get locked, reach gets throttled. A website is the only marketing asset that can't be taken from you — assuming you actually own it, which most builder subscriptions quietly prevent.",
            ]),
            ("If the answer is yes, don't rent one", [
                "The trap isn't skipping a website — it's paying forever for one. Builder plans run $200–700 a year for a template; agencies bolt on retainers. The alternative: pay once for a site you own outright, hosted for $0/month on modern edge infrastructure. Ours start at <strong>$2,950</strong>, live in about a week — and the first step is free: we remake your homepage (or build one from your Instagram) so you can see the answer before spending anything.",
            ]),
        ],
        "cta_head": "Find out what yours would look like — free",
        "cta_sub": "Send us your Instagram, your Google profile, or nothing but your business name. We'll send back a homepage.",
    },
    {
        "slug": "how-long-does-a-website-take",
        "title": "How Long Does It Take to Build a Website? Real Timelines",
        "meta_title": "How Long Does a Website Take to Build? Real Timelines | Everbuilt Studio",
        "meta_desc": "Agency websites take 3–6 months; freelancers 4–8 weeks; a productized studio ships in about a week. Where the time actually goes, and what speed does and doesn't cost.",
        "kicker": "Process",
        "h1": "How long a website really takes — and where the months go",
        "lede": "Ask five vendors for a timeline and you'll hear everything from 'this week' to 'next quarter.' All of them are telling the truth — about their own process, not about your website.",
        "sections": [
            ("The standard timelines, decoded", [
                "<strong>Agencies: 3–6 months.</strong> The build inside that window is days of actual work; the rest is discovery workshops, wireframe rounds, review cycles, and scheduling friction across two teams' calendars. <strong>Freelancers: 4–8 weeks</strong>, mostly queueing — you're one of several concurrent projects, and every feedback round waits for a context switch. <strong>DIY builders: 'a weekend'</strong> that becomes a month of evenings, which is why half of DIY sites never launch at all.",
            ]),
            ("What actually consumes the calendar", [
                "Three things, none of them design: waiting (for feedback, for assets, for the other party's calendar), rework (because nothing was agreed before building), and reinvention (rebuilding media pipelines, form wiring, and launch checklists from scratch per project). Remove those and the honest timeline for a premium business website is about a week.",
            ]),
            ("The one-week version, hour by honest hour", [
                "Our process removes the waiting by starting with the answer: a finished homepage remake, free, before any contract — that's the design agreement, settled on day zero. Then content in on day 1, full build at a private preview by day 5 with same-day revisions, and a zero-downtime launch on your domain by day 7 — on runbooks proven on a national nonprofit launch (2,100+ photos, email untouched, zero minutes down). Speed isn't a corner cut; it's what's left when the meeting-industrial-complex is deleted.",
            ]),
        ],
        "cta_head": "Start the clock with the free remake",
        "cta_sub": "Send your current site today — see your new homepage this week, before you've spent a dollar.",
    },
]

# ============================================================
# Local long-tail matrix (local/<industry>-website-design-<city>.html)
# Search Console showed Google surfacing our generic industry pages for
# city-level queries ("website design for lawyer chattanooga") — these pages
# give those queries an exact-match, genuinely useful landing page.
# We are honest about being a remote studio: no fake local addresses.
# ============================================================
CITIES = [
    {"slug": "chattanooga", "name": "Chattanooga", "state": "TN",
     "flavor": "Chattanooga runs on some of the fastest municipal internet in America — the original Gig City — and its business scene, from the revitalized riverfront to the Southside, expects websites that keep up."},
    {"slug": "memphis", "name": "Memphis", "state": "TN",
     "flavor": "Memphis is a working city — logistics muscle, a world-famous food culture, and neighborhoods full of businesses that compete on reputation rather than gloss."},
    {"slug": "everett", "name": "Everett", "state": "WA",
     "flavor": "Everett sits at the working edge of Puget Sound — aerospace money, a growing waterfront district, and customers who research everything online before they drive anywhere."},
    {"slug": "atlanta", "name": "Atlanta", "state": "GA",
     "flavor": "Atlanta's sprawl means customers choose from dozens of options in every category — and choose fast, on their phones, usually from whoever looked most credible in the first five seconds."},
    {"slug": "nashville", "name": "Nashville", "state": "TN",
     "flavor": "Nashville's boom brought newcomers, tourists, and competition in equal measure — every established business now competes online with a well-funded new arrival."},
    {"slug": "charlotte", "name": "Charlotte", "state": "NC",
     "flavor": "Charlotte's banking-town polish sets the visual bar high — customers here are used to professional presentation, and a dated website reads louder against that backdrop."},
    {"slug": "raleigh", "name": "Raleigh", "state": "NC",
     "flavor": "Raleigh and the Research Triangle have one of the most educated customer bases in the country — people who read past the first page and notice when a website respects their intelligence."},
    {"slug": "tampa", "name": "Tampa", "state": "FL",
     "flavor": "Tampa is growing faster than its service businesses can keep up with — which means the ones that look established online capture a disproportionate share of the new arrivals."},
    {"slug": "boise", "name": "Boise", "state": "ID",
     "flavor": "Boise's growth brought a wave of transplants who found their last dentist, lawyer, and gym through search — and they're doing it again here."},
    {"slug": "tucson", "name": "Tucson", "state": "AZ",
     "flavor": "Tucson's mix of university energy and seasonal residents means a steady stream of people searching for local businesses from scratch, with no word-of-mouth to guide them."},
    {"slug": "richmond", "name": "Richmond", "state": "VA",
     "flavor": "Richmond blends historic neighborhoods with one of the South's best small-business food-and-culture scenes — a market where independent character wins, if people can find it."},
    {"slug": "louisville", "name": "Louisville", "state": "KY",
     "flavor": "Louisville's economy runs on healthcare, logistics, and a bourbon-fueled tourism wave — three streams of customers who all start with a search."},
]

LOCAL_INDUSTRIES = [
    {"slug": "law-firm", "label": "Law Firm", "plural": "law firms", "parent": "law-firms",
     "angle": "Legal clients hire credibility. Before anyone calls your office, they've compared your website against every other firm that came up — and a dated template quietly argues against you. A firm site needs authority-grade design, a substantive page per practice area (that's what ranks), and a consultation path on every page.",
     "pains": ["A template that looks like every other firm in the county", "Practice-area pages too thin to rank", "No clear path from visitor to consultation", "A 'web guy' billing hourly for comma changes"]},
    {"slug": "restaurant", "label": "Restaurant", "plural": "restaurants", "parent": "restaurants",
     "angle": "Diners decide from a phone: menu, photos, hours, distance. A PDF menu from two price changes ago or stock photos of food you don't serve cost covers every single night. A restaurant site needs full-bleed photography of your actual food, a menu your team edits themselves, and hours that are never wrong.",
     "pains": ["A PDF menu from two price changes ago", "Stock photos of food you don't serve", "Hours buried while a competitor's show in search", "$99/month for a template the platform owns"]},
    {"slug": "real-estate", "label": "Real Estate", "plural": "real estate agents", "parent": "real-estate",
     "angle": "The brokerage template makes every agent identical — and portals resell your buyer to competing agents. Winning agents run their own brand: their name, their sold record, their neighborhoods, on a site they own. Listing photography deserves galleries that load instantly and keep the color grade intact.",
     "pains": ["A brokerage subdomain promoting the brokerage, not you", "Portals reselling your leads to competitors", "Listing photos crushed by a template gallery", "No pages for the neighborhoods you actually farm"]},
    {"slug": "dental", "label": "Dental & Medical", "plural": "dental and medical practices", "parent": "clinics",
     "angle": "Patients choose the practice that looks like it cares — calm design, real photos of your practice, and clear answers on insurance and booking. A substantive page per procedure is both what patients want to read and what search engines reward.",
     "pains": ["A healthcare template that feels like a 2009 waiting room", "Procedure pages too generic to rank", "Booking hidden behind a phone-tag wall", "A vendor site you pay monthly and don't own"]},
    {"slug": "contractor", "label": "Contractor", "plural": "contractors and remodelers", "parent": "contractors",
     "angle": "A $30K remodel client expects a $30K-looking portfolio. Homeowners shortlist from websites before a single call — and your best work is probably sitting in a phone camera roll instead of a gallery that closes bids. Project galleries, service-area pages, and quote forms that are yours alone.",
     "pains": ["Your best work trapped in a camera roll", "Lead sites selling 'your' homeowner to three competitors", "No pages for nearby towns you serve", "A template that says budget when your work says premium"]},
]

LOCAL_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
{head}
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Service","name":{title_json},"provider":{{"@type":"ProfessionalService","name":"Everbuilt Studio","url":"{domain}/"}},"areaServed":{{"@type":"City","name":"{city_name}"}},"description":{desc_json}}}
</script>
</head>
<body>

{nav}

<header class="page-hero">
  <div class="wrap">
    <p class="kicker">{label} websites — {city_name}, {state}</p>
    <h1>{h1}</h1>
    <p class="lede">{flavor}</p>
  </div>
</header>

<section style="padding-top: 56px;">
  <div class="wrap">
    <div class="prose">
      <p>{angle}</p>
      <p>Everbuilt Studio is a remote-first studio — we build for {plural} across the United States, including {city_name}, without local-agency overhead or local-agency invoices. Every build is delivered in days, owned outright by you, and hosted for <strong>$0/month, forever</strong>. We proved the model on a national nonprofit launch: 2,100+ photos processed, zero minutes of downtime, and no hosting bill since.</p>
      <h2>What {city_name} {plural} usually struggle with</h2>
      <ul>
{pains_html}
      </ul>
      <h2>What you get instead</h2>
      <p>A custom-designed site — no templates — with the content structure that ranks, forms that deliver to your inbox alone, and everything handed over at launch: code, content, domain, admin keys. Most {plural} fit <strong>Launch at $2,950</strong>; larger builds with galleries and admin tooling fit <strong>Signature from $7,500</strong>. Every build includes 90 days of free care, and hosting costs nothing, ever.</p>
      <p>More on how we build for {plural}: <a href="../for/{parent}.html">{label} website design</a> · Also serving {siblings}.</p>
    </div>
    <div class="cta-band">
      <h2>See your {city_name} {label_lower} site remade — free</h2>
      <p>Send us your current website (or just your name and city). We'll return a finished homepage remake — free, no call required.</p>
      <a class="btn btn-primary" href="../index.html#contact">Get the free remake</a>
    </div>
  </div>
</section>

{footer}

{scripts}
</body>
</html>
"""


def render_local(ind, city, cities):
    root = "../"
    slug = f"{ind['slug']}-website-design-{city['slug']}"
    canonical = f"{DOMAIN}/local/{slug}.html"
    title = f"{ind['label']} Website Design in {city['name']}, {city['state']}"
    meta_title = f"{ind['label']} Website Design {city['name']} — Own It, $0/Month | Everbuilt"
    meta_desc = (f"{ind['label']} website design for {city['name']}, {city['state']}: custom-built in about a week, "
                 f"owned outright, $0/month hosting. From $2,950 with a free homepage remake first.")
    pains_html = "\n".join(f"        <li>{html.escape(p)}</li>" for p in ind["pains"])
    others = [c for c in cities if c["slug"] != city["slug"]][:3]
    siblings = " · ".join(
        f'<a href="{ind["slug"]}-website-design-{c["slug"]}.html">{c["name"]}</a>' for c in others
    )
    return LOCAL_TEMPLATE.format(
        head=make_head(title, meta_title, meta_desc, canonical, root),
        title_json=json.dumps(title), desc_json=json.dumps(meta_desc),
        domain=DOMAIN, city_name=city["name"], state=city["state"],
        nav=NAV.format(root=root), footer=FOOTER.format(root=root),
        scripts=SCRIPTS.format(root=root),
        label=ind["label"], label_lower=ind["label"].lower(),
        plural=ind["plural"], parent=ind["parent"],
        h1=f"{ind['label']} website design in {city['name']} — built in days, owned outright",
        flavor=city["flavor"], angle=ind["angle"],
        pains_html=pains_html, siblings=siblings,
    ), slug, title


def write_local_hub(entries):
    root = "../"
    groups = {}
    for slug, title, ind_label in entries:
        groups.setdefault(ind_label, []).append((slug, title))
    parts = []
    for label, items in groups.items():
        parts.append(f"      <h2>{html.escape(label)} websites</h2>")
        links = " · ".join(
            f'<a href="{slug}.html">{html.escape(title.split(" in ")[-1])}</a>' for slug, title in items
        )
        parts.append(f"      <p>{links}</p>")
    hub = ARTICLE_TEMPLATE.format(
        head=make_head("Cities We Build For", "Website Design by City — Everbuilt Studio",
                       "Custom websites built remotely for businesses across the US — law firms, restaurants, real estate, dental practices, and contractors, city by city.",
                       f"{DOMAIN}/local/index.html", root),
        title_json=json.dumps("Cities We Build For"),
        desc_json=json.dumps("Custom websites for businesses across the US, city by city."),
        domain=DOMAIN, canonical=f"{DOMAIN}/local/index.html",
        nav=NAV.format(root=root), footer=FOOTER.format(root=root),
        scripts=SCRIPTS.format(root=root),
        kicker="Where we build", h1="One studio. Every city.",
        lede="We're remote-first: the same team, playbook, and $0/month architecture, wherever your customers are. Pages below for the industries and cities we get asked about most.",
        body_html="\n".join(parts),
        cta_head="Don't see your city? It doesn't matter.",
        cta_sub="We build remotely for the whole country. Send your current site and get a free remake this week.",
    )
    (ROOT / "local" / "index.html").write_text(hub, encoding="utf-8")
    print("wrote local/index.html")


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
    <a href="{root}for/photographers.html">Photographers</a>
    <span style="margin-left:14px;">Guides:</span>
    <a href="{root}guides/how-much-does-a-website-cost.html">Website costs 2026</a>
    <a href="{root}guides/website-redesign-cost.html">Redesign cost</a>
    <a href="{root}guides/website-maintenance-cost.html">Maintenance cost</a>
    <a href="{root}guides/squarespace-alternative.html">Squarespace alternative</a>
    <a href="{root}guides/wix-alternative.html">Wix alternative</a>
    <a href="{root}guides/website-in-a-week.html">Website in a week</a>
    <a href="{root}guides/do-i-need-a-website.html">Do I need a website?</a>
    <a href="{root}guides/how-long-does-a-website-take.html">How long does it take?</a>
    <span style="margin-left:14px;"><a href="{root}local/index.html" style="color:var(--ink-soft);">Cities we build for →</a></span>
  </div>
  <div class="wrap" style="margin-top: 24px; font-size: 0.8rem;">© <span id="year"></span> Everbuilt Studio. All rights reserved.</div>
</footer>"""

SCRIPTS = """<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.14/dist/lenis.min.js"></script>
<script src="{root}assets/main.js?v=20260817b"></script>"""

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
<link rel="stylesheet" href="{root}assets/styles.css?v=20260817b">"""

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
    urls += [f"{DOMAIN}/local/index.html"]
    urls += [f"{DOMAIN}/local/{i['slug']}-website-design-{c['slug']}.html"
             for i in LOCAL_INDUSTRIES for c in CITIES]
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
    (ROOT / "local").mkdir(exist_ok=True)
    hub_entries = []
    for ind in LOCAL_INDUSTRIES:
        for city in CITIES:
            page_html, slug, title = render_local(ind, city, CITIES)
            (ROOT / "local" / f"{slug}.html").write_text(page_html, encoding="utf-8")
            hub_entries.append((slug, title, ind["label"]))
    print(f"wrote {len(hub_entries)} local pages")
    write_local_hub(hub_entries)
    write_sitemap()


if __name__ == "__main__":
    main()

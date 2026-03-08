---
marp: true
theme: uncover
class: invert
paginate: true
backgroundColor: #0a0f1a
color: #E8ECF1
style: |
  /* ═══════════════════════════════════════════════════════════════
     INSTITUTIONAL FINANCE THEME
     Professional design for financial audience
     Clean, sophisticated, data-driven aesthetic
     ═══════════════════════════════════════════════════════════════ */

  /* CSS Variables - Institutional Color Palette */
  :root {
    /* Primary Colors - Professional Finance */
    --primary-color: #3B82F6;
    --secondary-color: #1E3A5F;
    --accent-color: #D4AF37;

    /* Semantic Colors - Muted & Professional */
    --success-color: #10B981;
    --danger-color: #EF4444;
    --warning-color: #F59E0B;
    --info-color: #06B6D4;
    --purple-color: #8B5CF6;

    /* Background System - Layered Depth */
    --bg-base: #0a0f1a;
    --bg-elevated: #0f1629;
    --bg-surface: #162033;
    --bg-hover: #1c2942;

    /* Border System */
    --border-subtle: rgba(255, 255, 255, 0.06);
    --border-default: rgba(255, 255, 255, 0.1);
    --border-emphasis: rgba(255, 255, 255, 0.15);

    /* Text Hierarchy */
    --text-primary: #E8ECF1;
    --text-secondary: #94A3B8;
    --text-muted: #64748B;

    /* Spacing Scale */
    --space-xs: 0.25rem;
    --space-sm: 0.5rem;
    --space-md: 1rem;
    --space-lg: 1.5rem;
    --space-xl: 2rem;

    /* Legacy compatibility */
    --background-light: rgba(255, 255, 255, 0.03);
    --background-medium: rgba(255, 255, 255, 0.06);
    --background-dark: rgba(255, 255, 255, 0.1);
    --border-light: rgba(255, 255, 255, 0.08);
    --border-medium: rgba(255, 255, 255, 0.12);
    --border-dark: rgba(255, 255, 255, 0.18);
    --card-gap: 0.8rem;
    --card-padding: 0.8rem;
    --border-radius: 8px;
  }

  /* ─── Base Typography ─── */
  section {
    font-size: 32px;
    padding: 25px;
    font-family: "Inter", "SF Pro Display", -apple-system, BlinkMacSystemFont, "PingFang SC", "Microsoft YaHei", sans-serif;
    font-weight: 400;
    line-height: 1.35;
    letter-spacing: 0.01em;
    background: linear-gradient(180deg, var(--bg-base) 0%, #070b14 100%);
  }

  /* Page number styling */
  section::after {
    color: var(--text-muted);
    font-size: 0.7em;
    font-weight: 500;
  }

  /* ─── Headings ─── */
  h1 {
    font-size: 1.8em;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: var(--text-primary);
  }

  h2 {
    font-size: 1.5em;
    margin-bottom: 0.5em;
    font-weight: 700;
    padding-bottom: 0.35em;
    letter-spacing: 0.03em;
    background: linear-gradient(90deg, white 0%, var(--accent-color) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  h3 {
    font-size: 1em;
    margin-bottom: 0.2em;
    font-weight: 600;
    color: var(--text-primary);
  }
  h4 {
    font-size: 0.9em;
    margin-bottom: 0.15em;
    font-weight: 500;
    color: var(--text-secondary);
  }

  /* ─── Content Elements ─── */
  table { font-size: 0.75em; width: 100%; }
  ul, ol { font-size: 0.8em; line-height: 1.35; }
  p { font-size: 0.85em; line-height: 1.25; color: var(--text-secondary); }
  strong { font-weight: 600; color: var(--text-primary); }
  .small { font-size: 0.72em; color: var(--text-muted); }

  /* ─── Grid Layouts ─── */
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; }
  .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.8rem; }
  .grid-auto { display: grid; grid-template-columns: 1fr auto 1fr; gap: 0.6rem; align-items: center; }

  /* ─── Modern Card System ─── */
  .card {
    padding: 0.8rem;
    background: var(--bg-elevated);
    border: 1px solid var(--border-subtle);
    border-radius: 8px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    transition: all 0.2s ease;
  }
  .card:hover {
    border-color: var(--border-default);
    box-shadow: 0 6px 24px rgba(0, 0, 0, 0.3);
  }

  /* Card variants with subtle left accent */
  .card-primary {
    background: linear-gradient(90deg, rgba(59, 130, 246, 0.15) 0%, var(--bg-elevated) 3%);
    border-left: 3px solid var(--primary-color);
  }
  .card-success {
    background: linear-gradient(90deg, rgba(16, 185, 129, 0.15) 0%, var(--bg-elevated) 3%);
    border-left: 3px solid var(--success-color);
  }
  .card-danger {
    background: linear-gradient(90deg, rgba(239, 68, 68, 0.15) 0%, var(--bg-elevated) 3%);
    border-left: 3px solid var(--danger-color);
  }
  .card-warning {
    background: linear-gradient(90deg, rgba(245, 158, 11, 0.15) 0%, var(--bg-elevated) 3%);
    border-left: 3px solid var(--warning-color);
  }
  .card-info {
    background: linear-gradient(90deg, rgba(6, 182, 212, 0.15) 0%, var(--bg-elevated) 3%);
    border-left: 3px solid var(--info-color);
  }
  .card-purple {
    background: linear-gradient(90deg, rgba(139, 92, 246, 0.15) 0%, var(--bg-elevated) 3%);
    border-left: 3px solid var(--purple-color);
  }
  .card-secondary {
    background: var(--bg-surface);
    border: 1px solid var(--border-default);
  }

  /* ─── Box Element ─── */
  .box {
    background: var(--bg-elevated);
    border: 1px solid var(--border-subtle);
    border-radius: 8px;
    padding: 0.8rem;
    margin: 0.5rem 0;
    text-align: center;
  }

  .arrow {
    text-align: center;
    font-size: 1.4em;
    color: var(--text-muted);
    margin: 0.3rem 0;
  }

  /* ─── Professional Table Styling ─── */
  table {
    border-collapse: separate;
    border-spacing: 0;
    border-radius: 10px;
    overflow: hidden;
    background: var(--bg-elevated);
    border: 1px solid var(--border-subtle);
  }
  th {
    background: var(--bg-surface);
    padding: 0.7rem 0.8rem;
    font-weight: 600;
    color: var(--text-primary);
    text-align: left;
    border-bottom: 1px solid var(--border-default);
    font-size: 0.85em;
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }
  td {
    padding: 0.6rem 0.8rem;
    border-bottom: 1px solid var(--border-subtle);
    color: var(--text-secondary);
  }
  tr:last-child td { border-bottom: none; }
  tr:hover td { background: var(--bg-hover); }

  /* Zebra striping - subtle */
  tbody tr:nth-child(even) { background: rgba(255, 255, 255, 0.02); }

  /* ─── Data Highlight Classes ─── */
  .positive { color: var(--success-color); font-weight: 600; }
  .negative { color: var(--danger-color); font-weight: 600; }
  .neutral { color: var(--warning-color); font-weight: 600; }
  .highlight { color: var(--accent-color); font-weight: 600; }

  /* ─── Metric/KPI Display ─── */
  .metric {
    text-align: center;
    padding: 0.5rem;
  }
  .metric-value {
    font-size: 1.8em;
    font-weight: 700;
    color: var(--accent-color);
    line-height: 1.2;
  }
  .metric-label {
    font-size: 0.75em;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 0.3rem;
  }

  /* ─── Subtle Animation for Presentations ─── */
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .animate-in {
    animation: fadeIn 0.4s ease-out forwards;
  }

  /* ─── Responsive Design ─── */
  @media (max-width: 768px) {
    section { font-size: 24px; padding: 20px; }
    .grid-2, .grid-3, .grid-auto { grid-template-columns: 1fr; gap: 0.8rem; }
  }

  /* ─── Lead/Title Slide Styling ─── */
  section.lead {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
  section.lead h1 {
    font-size: 2.5em;
    background: linear-gradient(135deg, var(--text-primary) 0%, var(--accent-color) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  section.lead h2 {
    border: none;
    font-size: 1.2em;
    color: var(--text-secondary);
    font-weight: 400;
  }
  section.lead h2::before { display: none; }
---

<!-- _class: lead -->

# DeFi Structured Yield Revolution
## Deep Comparison: Strata vs Pendle vs TradFi Products

<!--
[Study Notes - Page 1: Cover]

Core Concepts:
- DeFi Structured Yield Revolution: Innovation and reconstruction of traditional structured products in decentralized finance
- This presentation compares three product categories: Strata, Pendle, and TradFi structured products

Key Learning Points:
1. What are structured yield products?
2. How does DeFi transform traditional financial products?
3. What are the core differences between Strata vs Pendle?
4. What are the advantages and disadvantages of DeFi products compared to TradFi?

Background Knowledge:
- Structured products: Combining assets with different risk/return profiles to meet various investor needs
- DeFi: Decentralized Finance, blockchain-based financial services
- TradFi: Traditional Finance, centralized financial services from banks, brokers, etc.

Presentation Objective:
Understand the innovations, risks, and investment opportunities of DeFi structured products
-->

---

## Agenda

<style scoped>
.agenda-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.6rem;
  margin-top: 1rem;
}
.agenda-item {
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-left: 3px solid var(--accent-color);
  border-radius: 6px;
  padding: 0.7rem 0.8rem;
  display: flex;
  align-items: center;
  gap: 0.6rem;
  transition: all 0.2s ease;
}
.agenda-item:hover {
  background: var(--bg-surface);
  border-color: var(--border-default);
  border-left-color: var(--accent-color);
  transform: translateX(3px);
}
.agenda-number {
  font-size: 1.5em;
  font-weight: 700;
  color: var(--accent-color);
  min-width: 1.2em;
  text-align: center;
  line-height: 1;
  opacity: 0.9;
}
.agenda-content {
  flex: 1;
}
.agenda-title {
  font-size: 0.9em;
  font-weight: 500;
  color: var(--text-primary);
  margin: 0;
  line-height: 1.3;
}
</style>

<div class="agenda-grid">
<div class="agenda-item">
  <div class="agenda-number">01</div>
  <div class="agenda-content">
    <div class="agenda-title">Structured Yield Products Overview</div>
  </div>
</div>

<div class="agenda-item">
  <div class="agenda-number">02</div>
  <div class="agenda-content">
    <div class="agenda-title">Strata: Risk Tranching Protocol</div>
  </div>
</div>

<div class="agenda-item">
  <div class="agenda-number">03</div>
  <div class="agenda-content">
    <div class="agenda-title">Pendle: Yield Tokenization Platform</div>
  </div>
</div>

<div class="agenda-item">
  <div class="agenda-number">04</div>
  <div class="agenda-content">
    <div class="agenda-title">TradFi Equivalent Products</div>
  </div>
</div>

<div class="agenda-item">
  <div class="agenda-number">05</div>
  <div class="agenda-content">
    <div class="agenda-title">Core Dimension Comparative Analysis</div>
  </div>
</div>

<div class="agenda-item">
  <div class="agenda-number">06</div>
  <div class="agenda-content">
    <div class="agenda-title">Risk & Opportunity Assessment</div>
  </div>
</div>

<div class="agenda-item">
  <div class="agenda-number">07</div>
  <div class="agenda-content">
    <div class="agenda-title">Future Development Trends</div>
  </div>
</div>
</div>

<!--
[Study Notes - Page 2: Agenda]

Presentation Structure (7 sections):

1. Structured Yield Products Overview - Basic concepts, Traditional vs DeFi comparison
2. Strata: Risk Tranching Protocol - Core mechanism, product architecture, innovations
3. Pendle: Yield Tokenization Platform - PT/YT separation, product matrix
4. TradFi Equivalent Products - Traditional structured notes, senior/junior structures
5. Core Dimension Comparative Analysis - Technology, risk, users, regulation, innovation
6. Risk & Opportunity Assessment - Market size, risk factors, investment strategies
7. Future Development Trends - Industry outlook, key insights

Learning Path:
- Sections 1-3: Understand core mechanisms of each product
- Sections 4-5: Cross-comparison, identify differences and advantages
- Sections 6-7: Practical application, investment decisions

Suggested Time Allocation:
- Overview: 3 minutes
- Product introductions: 15 minutes (5 minutes each)
- Comparative analysis: 10 minutes
- Risks & trends: 8 minutes
- Q&A: 5-10 minutes
-->

---

## What Are Structured Yield Products?

<style scoped>
.definition-box {
  background: var(--bg-elevated);
  border: 1px solid var(--border-default);
  border-top: 3px solid var(--accent-color);
  border-radius: 8px;
  padding: 0.6rem 1.2rem;
  margin: 0 0 0.4rem 0;
  max-width: 100%;
  text-align: center;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
}
.definition-box h3 {
  margin: 0 0 0.3rem 0;
  font-size: 1.05em;
  font-weight: 600;
  color: var(--text-primary);
  line-height: 1.25;
}
.analogy {
  font-size: 0.8em;
  color: var(--text-muted);
  margin-top: 0.2rem;
}

.mechanism-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.6rem;
  max-width: 100%;
  margin: 0.4rem 0;
  font-size: 0.75em;
}
.mechanism-card {
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: 6px;
  padding: 0.5rem 0.6rem;
  text-align: center;
}
.mechanism-card.split {
  border-left: 3px solid var(--success-color);
}
.mechanism-card.customize {
  border-left: 3px solid var(--accent-color);
}
.mechanism-card.trade {
  border-left: 3px solid var(--info-color);
}
.mechanism-card h4 {
  margin: 0 0 0.25rem 0;
  font-size: 1.05em;
  font-weight: 600;
}
.mechanism-card.split h4 { color: var(--success-color); }
.mechanism-card.customize h4 { color: var(--accent-color); }
.mechanism-card.trade h4 { color: var(--info-color); }
.mechanism-card p {
  margin: 0;
  font-size: 0.9em;
  line-height: 1.2;
  color: var(--text-secondary);
}

.comparison-box {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.6rem;
  max-width: 100%;
  margin: 0.4rem 0 0 0;
  font-size: 0.75em;
}
.compare-side {
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: 6px;
  padding: 0.5rem 0.8rem;
  text-align: center;
}
.compare-side.tradfi {
  border-top: 3px solid var(--danger-color);
}
.compare-side.defi {
  border-top: 3px solid var(--success-color);
}
.compare-side h4 {
  margin: 0 0 0.35rem 0;
  font-size: 1.05em;
  font-weight: 600;
}
.compare-side.tradfi h4 { color: var(--danger-color); }
.compare-side.defi h4 { color: var(--success-color); }
.compare-side .item {
  margin: 0.25rem 0;
  font-size: 0.95em;
  line-height: 1.25;
  color: var(--text-secondary);
}
.compare-side .highlight {
  color: var(--accent-color);
  font-weight: 600;
}
</style>

<div class="definition-box">

### Split/restructure yield streams from a single asset<br/>to create financial products with different risk/return profiles

<div class="analogy">
Analogy: Slice yield into different portions, investors choose tiers based on risk appetite
</div>

</div>

<div class="mechanism-grid">
<div class="mechanism-card split">

#### Split Yield
<p>Divide yields into multiple tiers<br/>(e.g., Senior/Junior)</p>

</div>
<div class="mechanism-card customize">

#### Customize Risk
<p>Match different risk preferences<br/>(Conservative/Aggressive)</p>

</div>
<div class="mechanism-card trade">

#### Free Trading
<p>Tokenized for instant<br/>market trading</p>

</div>
</div>

<div class="comparison-box">
<div class="compare-side tradfi">

#### Traditional Finance (TradFi)

<div class="item">Entry Threshold: <span class="highlight">$100K+</span></div>
<div class="item">Pricing: Opaque black box</div>
<div class="item">Liquidity: No exit during lock-up</div>

</div>
<div class="compare-side defi">

#### DeFi Innovation

<div class="item">Entry Threshold: <span class="highlight">$10+</span></div>
<div class="item">Pricing: Transparent on-chain algorithm</div>
<div class="item">Liquidity: Trade & exit anytime</div>

</div>
</div>

<!--
[Study Notes - Page 3: What Are Structured Yield Products?]

Core objective of this page:
Help audience understand "structured yield products" in 30 seconds - what they are and why they're needed.

---

Part 1: Core Definition (Most Important!)

One-sentence definition:
Structured Yield Products = Split/restructure yield streams from a single asset to create financial products with different risk/return profiles

Breaking it down:
- Single asset: e.g., 100 ETH staked, a loan, an LP position
- Yield stream: Income generated by the asset (interest, fees, rewards, etc.)
- Split/restructure: Divide yields into different portions
- Different risk/return profiles: Some stable low-yield, some volatile high-yield

Why split?
Because different investors have different needs:
- Pension funds: Want stability, avoid volatility
- Hedge funds: Want high returns, can tolerate volatility
- Individual investors: Somewhere in between

Traditional approach: One product can only meet one type of need
Structured products: One asset, split to meet multiple needs

---

Part 2: Analogy

Imagine you have a large cake (= asset yield)

Traditional approach:
- Entire cake can only be sold to one person
- Those with small needs can't afford it or can't use it all
- Those with large needs don't have enough

Structured products:
- Cut the cake into small, medium, large pieces
- Small needs buy small pieces (Senior - stable yield)
- Large needs buy large pieces (Junior - high yield)
- Everyone is satisfied, higher asset utilization

Key insight:
Through splitting, the same asset can serve more people, improving capital efficiency!

---

Part 3: Three Core Mechanisms

Mechanism 1: Split Yield
- What: Divide yields into multiple tiers
- Example:
  * 100 ETH staked, annual yield 5 ETH
  * Split into: Senior tier (4 ETH fixed) + Junior tier (1-10 ETH variable)
- Benefit: Meet different risk preferences

Mechanism 2: Customize Risk
- What: Investors choose tiers based on risk tolerance
- Choices:
  * Conservative → Senior (priority, low risk/low return)
  * Aggressive → Junior (subordinate, high risk/high return)
  * Balanced → Mixed allocation
- Benefit: Everyone finds products suited to them

Mechanism 3: Free Trading
- What: Tokenize yield rights for anytime trading
- Traditional problem: Locked for 1 year after purchase, no exit
- DeFi solution:
  * Senior Token, Junior Token tradable on DEX
  * Sell and exit anytime
  * No need to wait until maturity
- Benefit: Enhanced liquidity, reduced risk

---

Part 4: TradFi vs DeFi Comparison

Traditional Finance (TradFi) limitations:

1. High threshold: $100K+
   - Requires "accredited investor" status
   - Ordinary people cannot participate
   - Example: JPMorgan structured notes, minimum $100,000

2. Opaque pricing
   - Pricing algorithm is a black box
   - Investors don't know how it's calculated
   - Institutions may charge high hidden fees

3. Poor liquidity
   - Lock-up period 1-5 years
   - Early exit requires high penalties
   - Or simply cannot exit

DeFi innovation breakthroughs:

1. Low threshold: $10+
   - Anyone can participate
   - Minimum investment can be just a few dollars
   - True financial democratization

2. Transparent pricing
   - Smart contract code is open source
   - Pricing algorithm publicly verifiable
   - Fees clearly displayed

3. High liquidity
   - Tokenized for instant trading
   - Free trading on Uniswap and other DEXs
   - No need to wait until maturity

Key comparison data:
| Dimension | TradFi | DeFi |
|-----------|--------|------|
| Minimum Investment | $100,000 | $10 |
| Pricing Transparency | Black box | Fully transparent |
| Liquidity | Locked 1-5 years | Trade anytime |
| Access Requirements | Accredited investor | Permissionless |

---

Presentation tips:

Opening (10 sec):
"What are structured yield products? Simply put, it's slicing the asset yield cake—cutting it into different sized portions so everyone can choose the slice that suits them."

Core mechanisms (30 sec):
"It has three core mechanisms:
1. Split yield—divide into multiple tiers
2. Customize risk—match different preferences
3. Free trading—tokenized for anytime trading"

DeFi advantages (20 sec):
"Where's the DeFi innovation? Two key breakthroughs:
1. Threshold from $100K to $10—everyone can participate
2. From black box pricing to transparent algorithms—fully verifiable"

Transition to next page:
"Now that we understand the basic concepts, let's look at the four core values of DeFi structured products..."

---

Anticipated Q&A:

Q1: How does "splitting yield" actually work?
A: Through smart contract automatic distribution. For example:
- Total yield enters the contract
- Contract first pays Senior tier fixed yield
- Remaining goes entirely to Junior tier
- Fully automated, no manual intervention

Q2: Why tokenize?
A: Benefits of tokenization:
- Tradable on DEX (liquidity)
- Can be used as collateral (composability)
- Can be transferred to others (flexibility)
- Ownership clearly recorded on-chain (transparency)

Q3: How is this different from traditional bonds?
A: Similarities:
- Both are fixed income products
- Both have risk stratification

Differences:
- DeFi: Transparent, low threshold, high liquidity
- Traditional bonds: Opaque, high threshold, poor liquidity

Q4: Can ordinary people really participate?
A: Yes! You only need:
- A crypto wallet (e.g., MetaMask)
- Small amount of ETH (can start from $10)
- Basic DeFi knowledge
- No certification required

---

Key takeaways (5 keywords):

1. Split - Divide yield into different tiers
2. Customize - Match different risk preferences
3. Tokenize - Enable free trading
4. Low threshold - $10 vs $100K
5. Transparent - On-chain verifiable

One-sentence summary:
Structured yield products are "financial Lego"—decompose and reassemble yields so everyone can find an investment approach that suits them.

---

Success criteria for this page:
✅ Audience can explain structured yield products in their own words
✅ Audience understands why yield splitting is needed
✅ Audience knows DeFi's core advantages (low threshold + transparency)
✅ Audience is interested in subsequent content

If audience still doesn't understand, use this simplest example:
"Suppose you and a friend buy a house together to rent out, monthly rent $1000. You want stable income, your friend wants high returns. What to do?

Structured product solution:
- You take fixed $800/month (Senior)
- Friend takes remaining $200-2000/month (Junior, depending on occupancy rate)
- Both satisfied!

This is the essence of structured yield products."
-->

---

## Core Value Propositions

<style scoped>
.value-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  max-width: 90%;
  margin: 0 auto;
}
.value-card {
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: 10px;
  padding: 1.1rem 1.4rem;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  position: relative;
  overflow: hidden;
}
.value-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
}
.value-card.risk::before { background: var(--success-color); }
.value-card.yield::before { background: var(--accent-color); }
.value-card.liquidity::before { background: var(--info-color); }
.value-card.transparency::before { background: var(--primary-color); }
.value-card h3 {
  margin: 0.2rem 0 0.4rem 0;
  font-size: 1em;
  font-weight: 600;
}
.value-card.risk h3 { color: var(--success-color); }
.value-card.yield h3 { color: var(--accent-color); }
.value-card.liquidity h3 { color: var(--info-color); }
.value-card.transparency h3 { color: var(--primary-color); }
.value-card p {
  margin: 0;
  font-size: 0.85em;
  line-height: 1.4;
  color: var(--text-secondary);
}
</style>

<div class="value-grid">
<div class="value-card risk">

### Risk Customization
<p>Match varying investor risk appetites</p>

</div>
<div class="value-card yield">

### Yield Optimization
<p>Separate & restructure yield sources</p>

</div>
<div class="value-card liquidity">

### Enhanced Liquidity
<p>Tokenization enables secondary markets</p>

</div>
<div class="value-card transparency">

### Improved Transparency
<p>On-chain verifiable mechanisms</p>

</div>
</div>

<!--
[Study Notes - Page 4: Core Value Propositions]

Four core values of DeFi structured products:

1. Risk Customization
   - Meaning: Investors can choose different tiers based on risk tolerance
   - Examples:
     * Pension funds → Choose Senior tier (priority), capital preservation focus
     * Hedge funds → Choose Junior tier (subordinate), pursue high returns
     * Individual investors → Mixed allocation, balanced risk
   - Advantage: No longer "one size fits all," everyone finds suitable products

2. Yield Optimization
   - Meaning: Improve capital efficiency through separating and restructuring yield sources
   - Mechanism:
     * Split yield into fixed income (PT) and floating income (YT)
     * Different investors buy different parts
     * Total yield > yield from holding alone (through leverage and arbitrage)
   - Example: Pendle's PT/YT separation mechanism

3. Enhanced Liquidity
   - Meaning: Tokenize originally non-tradable yield rights, create secondary markets
   - Traditional problem: Cannot exit during lock-up after buying structured products
   - DeFi solution:
     * Tokenize yield rights (e.g., PT, YT, Senior Token)
     * Free trading on DEX
     * Exit anytime, no need to wait until maturity
   - Advantage: Improve capital efficiency, reduce liquidity risk

4. Improved Transparency
   - Meaning: All rules, pricing, fund flows are public on-chain
   - Specifics:
     * Smart contract code is open source, anyone can audit
     * Every transaction is traceable
     * Pricing algorithm is transparent, cannot be manipulated
     * Real-time view of pool status
   - Compared to TradFi: Traditional product pricing is opaque, investors are at information disadvantage

Key learning points:
- These four values are the core competitiveness of DeFi structured products
- Understand how each value addresses traditional finance pain points
- Consider: How attractive are these values to different types of investors?

Memory technique:
Risk-Yield-Liquidity-Transparency (RYLT)
-->

---

## Strata: Universal Risk Tranching Engine

<!--
[Study Notes - Page 5: Strata Product Introduction]

Core concept:
Strata = Universal risk tranching protocol that splits any yield-bearing asset into tokens with different risk levels

How it works:
1. Input: Any yield-bearing asset (e.g., stETH, aUSDC, etc.)
2. Processing: Smart contract splits into Senior (priority) and Junior (subordinate) tiers
3. Output: Two types of tokens with different risk/return profiles

Key features:
- Universality: Can tranche any DeFi yield-bearing asset
- Risk isolation: Senior tier gets priority on yield and principal; Junior tier takes more risk but gets higher returns
- Flexibility: Customizable tranching ratios and parameters

Strata's innovations:
- Not a product for specific assets, but a universal "risk tranching engine"
- Like "Lego blocks," can combine with any DeFi asset
- Brings TradFi's CDO (Collateralized Debt Obligation) concept to DeFi

Practical applications:
- Tranche stETH → Senior gets stable 4-6% APY, Junior gets leveraged 10-15% APY
- Tranche Aave deposits → Serve investors with different risk preferences

Key learning points:
- Strata's core is "risk redistribution"
- Senior and Junior are zero-sum: Junior takes risk, Senior gets protection
- Understand the waterfall distribution mechanism
-->

<style scoped>
.diagram {
  max-width: 92%;
  margin: 0.3rem auto;
  font-size: 0.78em;
}
.box-strata {
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-left: 3px solid var(--primary-color);
  border-radius: 6px;
  padding: 0.6rem 0.8rem;
  margin: 0.25rem 0;
  text-align: center;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.15);
}
.box-strata h4 {
  margin: 0 0 0.2rem 0;
  color: var(--primary-color);
  font-size: 1.05em;
  font-weight: 600;
}
.box-strata p {
  margin: 0;
  font-size: 0.92em;
  color: var(--text-secondary);
  line-height: 1.3;
}
.split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.6rem;
  margin-top: 0.25rem;
}
.box-senior {
  border-left-color: var(--success-color);
}
.box-senior h4 { color: var(--success-color); }
.box-junior {
  border-left-color: var(--danger-color);
}
.box-junior h4 { color: var(--danger-color); }
.diagram-arrow {
  text-align: center;
  font-size: 1.4em;
  margin: 0.1rem 0;
  color: var(--text-muted);
}
.diagram ul {
  text-align: left;
  font-size: 0.88em;
  margin: 0.2rem 0 0 0;
  padding-left: 1.1em;
  line-height: 1.35;
  color: var(--text-secondary);
}
.diagram li {
  margin: 0.18rem 0;
}
</style>

<!-- Strata Tranche Mechanism - CSS-based Diagram -->
<style scoped>
.strata-diagram {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.12rem;
  margin-top: 0.1rem;
}
.strata-level {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.strata-box {
  padding: 0.25rem 0.5rem;
  border-radius: 6px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}
.strata-box.input {
  background: linear-gradient(135deg, #3B82F6 0%, #1E3A5F 100%);
  border-left: 3px solid #3B82F6;
}
.strata-box.process {
  background: linear-gradient(135deg, #8B5CF6 0%, #5B21B6 100%);
  border-left: 3px solid #8B5CF6;
  border-bottom: 2px solid #A78BFA;
}
.strata-box h4 {
  margin: 0;
  font-size: 0.65em;
  color: #fff;
  font-weight: 700;
}
.strata-box p {
  margin: 0.05rem 0 0;
  font-size: 0.5em;
  color: rgba(255,255,255,0.85);
}
.strata-box .highlight {
  color: #D4AF37;
  font-weight: 600;
  font-size: 0.52em;
}
.strata-arrow-down {
  color: #94A3B8;
  font-size: 0.9em;
  line-height: 1;
}
.strata-split-row {
  display: flex;
  gap: 0.6rem;
  align-items: flex-start;
  justify-content: center;
}
.strata-tranche {
  width: 165px;
  padding: 0.25rem 0.35rem;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}
.strata-tranche.senior {
  background: linear-gradient(180deg, #10B981 0%, #047857 100%);
  border-top: 2px solid #34D399;
}
.strata-tranche.junior {
  background: linear-gradient(180deg, #EF4444 0%, #B91C1C 100%);
  border-top: 2px solid #F87171;
}
.strata-tranche h4 {
  margin: 0;
  font-size: 0.65em;
  color: #fff;
  font-weight: 700;
  text-align: center;
}
.strata-tranche-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.08rem;
}
.strata-tranche .subtitle {
  font-size: 0.45em;
  color: rgba(255,255,255,0.9);
  text-align: center;
  margin-bottom: 0.15rem;
}
.strata-tranche ul {
  margin: 0;
  padding-left: 0.8rem;
  font-size: 0.45em;
  color: rgba(255,255,255,0.95);
  line-height: 1.25;
}
.strata-output {
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  font-size: 0.5em;
  font-weight: 600;
  text-align: center;
}
.strata-output.senior {
  background: rgba(16, 185, 129, 0.2);
  border: 1px solid #10B981;
  color: #10B981;
}
.strata-output.junior {
  background: rgba(239, 68, 68, 0.2);
  border: 1px solid #EF4444;
  color: #EF4444;
}
.strata-legend {
  font-size: 0.45em;
  color: #64748B;
  margin-top: 0.1rem;
  background: rgba(255,255,255,0.03);
  padding: 0.15rem 0.4rem;
  border-radius: 4px;
  border: 1px solid rgba(255,255,255,0.08);
}
.strata-legend .green { color: #10B981; font-weight: 600; }
.strata-legend .red { color: #EF4444; font-weight: 600; }
</style>

<!-- Vertical Flow Layout with Waterfall -->
<div class="strata-diagram">
  <!-- Level 1: Input -->
  <div class="strata-level">
    <div class="strata-box input">
      <h4>INPUT</h4>
      <p>Yield Assets</p>
      <p class="highlight">stETH, sUSDe</p>
    </div>
  </div>

  <!-- Arrow down -->
  <div class="strata-arrow-down">↓</div>

  <!-- Level 2: Tranching Engine -->
  <div class="strata-level">
    <div class="strata-box process">
      <h4>TRANCHING ENGINE</h4>
      <p>Smart Contract</p>
      <p>Split by risk</p>
    </div>
  </div>

  <!-- Arrow down -->
  <div class="strata-arrow-down">↓</div>

  <!-- Level 3: Senior + Junior side by side with output arrows -->
  <div class="strata-split-row">
    <div class="strata-tranche-col">
      <div class="strata-tranche senior">
        <h4>SENIOR</h4>
        <div class="subtitle">Low Risk</div>
        <ul>
          <li>Stable 4-6% APY</li>
          <li>Priority payment</li>
          <li>First claim</li>
        </ul>
      </div>
      <div class="strata-arrow-down" style="color: #10B981;">↓</div>
      <div class="strata-output senior">Senior Token</div>
    </div>
    <div class="strata-tranche-col">
      <div class="strata-tranche junior">
        <h4>JUNIOR</h4>
        <div class="subtitle">High Return</div>
        <ul>
          <li>10-20% APY</li>
          <li>Bears first loss</li>
          <li>Residual yield</li>
        </ul>
      </div>
      <div class="strata-arrow-down" style="color: #EF4444;">↓</div>
      <div class="strata-output junior">Junior Token</div>
    </div>
  </div>

  <!-- Waterfall Legend -->
  <div class="strata-legend">
    Yield flows to <span class="green">Senior first</span> → <span class="red">Junior</span> gets remainder
  </div>
</div>

---

## Strata Key Innovations

<!--
[Study Notes - Page 6: Strata Key Innovations]

Core objective of this page:
Showcase Strata's three key innovations compared to traditional structured products

According to Strata's official documentation (docs.strata.money), Strata is defined as:
"Strata is a generalized risk-tranching protocol that brings structured yield products to any on-chain or off-chain yield strategy by splitting yield into two tokenized risk-based tranches."

---

Strata's Three Key Innovations:

1. Perpetual Tranching

This is Strata's most core innovation!

Meaning:
Strata's yield tranching structure is perpetual, with no maturity date, operating continuously

Comparison with traditional products:
- Traditional CDO/structured notes: Have fixed maturity dates (e.g., 3 years, 5 years)
  * Must liquidate at maturity
  * Investors need to reallocate funds
  * Reinvestment risk exists
  * Liquidity restricted before maturity

- Strata perpetual tranching: No maturity date
  * Yield continuously flows to Senior and Junior
  * Investors can enter/exit anytime (depending on liquidity)
  * More like equity investment than bonds
  * Long-term holders don't worry about maturity

Technical implementation:
- Smart contracts designed for perpetual operation
- Yield distribution executed automatically every block/day
- No "maturity liquidation" logic
- Investors exit via secondary market or redemption mechanism

Advantages:
- No reinvestment risk: No need to find new products after maturity
- Continuous compounding: Yields can be continuously reinvested
- Reduced friction costs: No need to frequently migrate funds
- Better liquidity: Tokenized for anytime trading

Example:
Traditional CDO investor:
- Bought 3-year CDO in 2020
- Matured in 2023, received principal + returns
- Need to find new investment opportunities
- May face changed market conditions

Strata investor:
- Bought srUSDe (Strata Senior USDe) in 2020
- Still holding in 2023, continuously earning yield
- Still holding in 2026, no action required
- Can sell tokens anytime when wanting to exit

Significance for DeFi:
- Better aligned with DeFi's "perpetual" nature (like perpetual contracts)
- Reduces user operational complexity
- Improves capital efficiency

---

2. Over-Collateralized Senior Protection

Official description:
"Strata Senior Tranche: An over-collateralized, yield-bearing synthetic dollar... It delivers superior risk-adjusted yield by providing protection against underlying strategy and collateral risks, guaranteed minimum yield tied to the benchmark rate, and uncapped upside exposure."

Core mechanism:
Junior tier provides over-collateralization, offering multiple protections for Senior tier

Collateralization ratios:
- Typical configuration: 60-80% Senior / 20-40% Junior
- Protection multiple provided by Junior: 1.5-4x
- E.g., 80/20 configuration: Junior must lose 100% before affecting Senior

Triple protection mechanism:

Protection 1: First Loss Tranche
- All losses first deducted from Junior
- Junior acts as "buffer"
- Only when Junior is completely depleted does it affect Senior

Protection 2: Guaranteed Minimum Yield
- Senior yield linked to benchmark rate
- E.g.: Guaranteed at least 3% APY
- Even if underlying strategy underperforms, minimum protection exists

Protection 3: Uncapped Upside
- When underlying strategy performs exceptionally
- Senior can also share excess returns
- Unlike traditional fixed income products with yield caps

Specific example:
Assume Strata tranches Aave lending pool, 80/20 configuration

Scenario A: Normal operation
- Lending yield: 5% APY
- Senior receives: 4% APY (guaranteed yield)
- Junior receives: 9% APY (leverage effect)
- Both satisfied ✅

Scenario B: Market crisis, bad debt occurs
- Lending yield: 3% APY
- Bad debt loss: 2%
- Net yield: 1%
- Senior still receives: 4% APY (subsidized from Junior)
- Junior bears loss: 1% - 4% = -15% APY
- Senior protected ✅

Scenario C: DeFi Summer, yield explosion
- Lending yield: 20% APY
- Senior receives: 6% APY (shares upside)
- Junior receives: 74% APY (massive leverage)
- Senior also enjoys bull market ✅

Comparison with 2008 financial crisis CDOs:

2008 CDO problems:
- Insufficient collateral: Poor quality subprime loans
- Rating errors: AAA-rated CDOs had high actual risk
- Opaque: Investors couldn't monitor risk in real-time
- Chain collapse: Senior tiers also suffered major losses

Strata improvements:
- Over-collateralization: Visible on-chain in real-time
- No ratings needed: Smart contracts execute automatically
- Fully transparent: All data public
- Automatic protection: Triggers threshold auto-adjustment

Actual data (srUSDe example):
- Senior (srUSDe): Receives stable USDe staking yield
- Junior (jrUSDe): Provides 150-250% over-collateralization
- Protection effect: Even with 30% USDe loss, Senior remains safe

---

3. Modular, Chain-Agnostic Architecture

Official description:
"Strata is a fully on-chain protocol with a modular, chain-agnostic architecture that enables expansion beyond USDe into a broad range of USD and non-USD assets and strategies across multiple ecosystems."

Core features:
Strata is not bound to specific assets or strategies, can tranche any yield source

Supported strategy types:

1. Curated lending vaults
   - Aave, Compound and other lending protocols
   - Institutional-grade lending pools
   - Peer-to-peer lending

2. Managed multi-strategy vaults
   - Yearn Finance-style yield aggregation
   - Auto-switching between multiple protocols
   - Dynamic yield optimization

3. Exotic delta-neutral strategies
   - Hedge fund-level complex strategies
   - Market-neutral arbitrage
   - Reduced price volatility risk

4. Tokenized private credit
   - Tokenize traditional private credit
   - On-chain corporate loans
   - A form of RWA (Real World Assets)

5. High-yield RWAs
   - Real estate yields
   - Commercial paper
   - Other off-chain asset yields

Chain-agnostic deployment:
- Not limited to Ethereum mainnet
- Deployable to any EVM-compatible chain:
  * Arbitrum (low gas fees)
  * Optimism (fast confirmations)
  * Polygon (high throughput)
  * Avalanche (low latency)
  * Base, Blast and other emerging L2s

Technical implementation:
- Standardized smart contract interfaces
- Adapter Pattern
- Cross-chain bridge integration
- Unified frontend interface

Advantages of modularity:

Advantage 1: Flexibility
- Switch underlying strategies when market conditions change
- No need to redeploy entire system
- Like "Lego blocks," freely combinable

Advantage 2: Scalability
- Easily add new yield strategies
- Support future innovative protocols
- Not limited to current DeFi ecosystem

Advantage 3: Risk diversification
- Not dependent on single protocol or asset
- Can tranche multiple strategies simultaneously
- Reduces single point of failure risk

Advantage 4: Cross-chain optimization
- Deploy on low gas fee chains
- Cover users across different chains
- Improve overall capital efficiency

Practical examples:

Example 1: Expanding from USDe to other assets
- Initial: Strata tranches Ethena's USDe
- Expansion: Can tranche any stablecoin (USDC, DAI)
- Future: Can tranche volatile assets like BTC, ETH

Example 2: Cross-chain deployment
- Ethereum mainnet: For large investors (security priority)
- Arbitrum: For regular users (low cost)
- Base: For Coinbase users (ease of use)
- Same product logic, different on-chain environments

Example 3: Strategy switching
- Initial: Tranche Aave USDC lending
- Market change: Compound has higher yield
- Action: Switch to Compound
- Result: Investors automatically enjoy higher returns

Compared to traditional finance:
- TradFi structured products:
  * Bound to specific assets (e.g., a CDO can only invest in subprime loans)
  * Limited to specific jurisdictions
  * Cannot deploy across markets

- Strata:
  * Supports any asset and strategy
  * Globally borderless
  * Multi-chain deployment

---

Summary: Synergy of Three Innovations

Perpetual Tranching + Over-Collateralization + Modular Architecture =
Next-generation DeFi Structured Products

1. Perpetual Tranching: Solves the "time" problem
   - No worries about maturity and reinvestment
   - Continuous compounding, long-term growth

2. Over-Collateralization: Solves the "safety" problem
   - Multiple protection mechanisms
   - Transparent and verifiable

3. Modular Architecture: Solves the "flexibility" problem
   - Adapts to any strategy and asset
   - Cross-chain deployment, global coverage

Strata's vision:
"Bring structured yield products to any on-chain or off-chain yield strategy"

These three innovations make Strata not just a "DeFi version of CDO,"
but a completely new, safer, more flexible, more enduring yield optimization protocol.

---

Key terms:

Perpetual:
- No maturity date, runs continuously
- Similar to Perpetual Futures

Over-Collateralization:
- Collateral value > Borrowed value
- Provides safety buffer

First Loss Tranche:
- Tier that bears primary losses
- Protects other tiers

Modular:
- Pluggable component design
- Like Lego blocks

Chain-Agnostic:
- Not dependent on specific blockchain
- Can deploy on multiple chains

Benchmark Rate:
- Reference rate, like US Treasury rate
- In Strata, may be USDe's base staking yield

Uncapped Upside:
- No ceiling on returns
- Can share excess returns

---

Presentation points:

Opening (5 sec):
"Strata's three innovations make it the next-generation DeFi structured product"

Explain each (10 sec each):
1. "Perpetual Tranching - No maturity date, continuous operation, like perpetual contracts"
2. "Over-Collateralization - Junior provides multiple protections, Senior is extremely safe"
3. "Modular Architecture - Supports any yield strategy, cross-chain deployment"

Summary (5 sec):
"These three combined create a safer, more flexible, more enduring yield optimization protocol"

Transition to next page:
"Having understood Strata's innovations, let's see how Pendle solves problems from another angle..."
-->

<style scoped>
.innovation-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.8rem;
  max-width: 94%;
  margin: 0 auto;
}
.innovation-card {
  background: var(--bg-elevated);
  border: 1px solid var(--border-subtle);
  border-radius: 8px;
  padding: 0.8rem;
  text-align: center;
  box-shadow: 0 3px 12px rgba(0, 0, 0, 0.15);
}
.innovation-card.perpetual {
  border-top: 3px solid var(--accent-color);
}
.innovation-card.collateral {
  border-top: 3px solid var(--success-color);
}
.innovation-card.modular {
  border-top: 3px solid var(--info-color);
}
.innovation-card h3 {
  margin: 0 0 0.4rem 0;
  font-size: 1.05em;
  font-weight: 600;
}
.innovation-card.perpetual h3 { color: var(--accent-color); }
.innovation-card.collateral h3 { color: var(--success-color); }
.innovation-card.modular h3 { color: var(--info-color); }
.innovation-card p {
  margin: 0;
  font-size: 0.95em;
  line-height: 1.35;
  color: var(--text-secondary);
}
</style>

<div class="innovation-grid">
<div class="innovation-card perpetual">

### Perpetual Tranching
<p>Continuous yield structure with no maturity date</p>

</div>
<div class="innovation-card collateral">

### Over-Collateralization
<p>Multiple protections for Senior tier</p>

</div>
<div class="innovation-card modular">

### Modular Architecture
<p>Supports any yield strategy</p>

</div>
</div>

---

## Pendle: Yield Tokenization Platform

<!--
[Study Notes - Page 7: Pendle Product Introduction]

Core concept:
Pendle = Yield tokenization protocol that separates principal and yield from yield-bearing assets into two independently tradeable tokens

PT/YT separation mechanism:
1. Input: Yield-bearing asset (e.g., stETH, aUSDC)
2. Separation:
   - PT (Principal Token) = Principal token, represents the right to redeem principal at maturity
   - YT (Yield Token) = Yield token, represents the right to all yield before maturity
3. Trading: PT and YT can be independently traded on AMM

How it works example:
Assume you have 100 stETH (5% annual yield):
- Deposit to Pendle → Receive 100 PT-stETH + 100 YT-stETH
- PT-stETH: Can redeem 100 stETH after 1 year (trades at discount, e.g., 95 ETH)
- YT-stETH: Receive all staking yield within 1 year (about 5 ETH)

Core value:
1. Fixed income: Buy PT = Lock in fixed yield (similar to bonds)
2. Yield leverage: Buy YT = Leveraged yield exposure (high risk, high return)
3. Hedging strategies: Combine PT/YT for complex strategies

Differences from Strata:
- Strata: Risk tranching (Senior vs Junior)
- Pendle: Yield separation (Principal vs Yield)
- Strata: Focuses on risk protection
- Pendle: Focuses on yield optimization

Practical use cases:
- Conservative investors: Buy PT, lock in fixed yield, like buying bonds
- Aggressive investors: Buy YT, get leveraged yield exposure
- Arbitrageurs: Profit from PT/YT price discrepancies

Key learning points:
- PT is similar to zero-coupon bond
- YT is similar to yield swap
- Understand the equation PT + YT = Original Asset
-->

<style scoped>
.pendle-diagram {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.12rem;
  margin-top: 0.1rem;
}
.pendle-level {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.pendle-box {
  padding: 0.25rem 0.5rem;
  border-radius: 6px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}
.pendle-box.input {
  background: linear-gradient(135deg, #8B5CF6 0%, #5B21B6 100%);
  border-left: 3px solid #8B5CF6;
}
.pendle-box.process {
  background: linear-gradient(135deg, #06B6D4 0%, #0891B2 100%);
  border-left: 3px solid #06B6D4;
  border-bottom: 2px solid #22D3EE;
}
.pendle-box h4 {
  margin: 0;
  font-size: 0.65em;
  color: #fff;
  font-weight: 700;
}
.pendle-box p {
  margin: 0.05rem 0 0;
  font-size: 0.5em;
  color: rgba(255,255,255,0.85);
}
.pendle-box .highlight {
  color: #D4AF37;
  font-weight: 600;
  font-size: 0.52em;
}
.pendle-arrow-down {
  color: #94A3B8;
  font-size: 0.9em;
  line-height: 1;
}
.pendle-split-row {
  display: flex;
  gap: 0.6rem;
  align-items: flex-start;
  justify-content: center;
}
.pendle-token {
  width: 165px;
  padding: 0.25rem 0.35rem;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}
.pendle-token.pt {
  background: linear-gradient(180deg, #06B6D4 0%, #0891B2 100%);
  border-top: 2px solid #22D3EE;
}
.pendle-token.yt {
  background: linear-gradient(180deg, #F59E0B 0%, #D97706 100%);
  border-top: 2px solid #FBBF24;
}
.pendle-token h4 {
  margin: 0;
  font-size: 0.65em;
  color: #fff;
  font-weight: 700;
  text-align: center;
}
.pendle-token-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.08rem;
}
.pendle-token .subtitle {
  font-size: 0.45em;
  color: rgba(255,255,255,0.9);
  text-align: center;
  margin-bottom: 0.15rem;
}
.pendle-token ul {
  margin: 0;
  padding-left: 0.8rem;
  font-size: 0.45em;
  color: rgba(255,255,255,0.95);
  line-height: 1.25;
}
.pendle-output {
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  font-size: 0.5em;
  font-weight: 600;
  text-align: center;
}
.pendle-output.pt {
  background: rgba(6, 182, 212, 0.2);
  border: 1px solid #06B6D4;
  color: #06B6D4;
}
.pendle-output.yt {
  background: rgba(245, 158, 11, 0.2);
  border: 1px solid #F59E0B;
  color: #F59E0B;
}
.pendle-legend {
  font-size: 0.45em;
  color: #64748B;
  margin-top: 0.1rem;
  background: rgba(255,255,255,0.03);
  padding: 0.15rem 0.4rem;
  border-radius: 4px;
  border: 1px solid rgba(255,255,255,0.08);
}
.pendle-legend .cyan { color: #06B6D4; font-weight: 600; }
.pendle-legend .orange { color: #F59E0B; font-weight: 600; }
</style>

<div class="pendle-diagram">
  <!-- Level 1: Input -->
  <div class="pendle-level">
    <div class="pendle-box input">
      <h4>INPUT</h4>
      <p>Yield-Bearing Assets</p>
      <p class="highlight">stETH, sDAI, LST</p>
    </div>
  </div>

  <!-- Arrow down -->
  <div class="pendle-arrow-down">↓</div>

  <!-- Level 2: Pendle Protocol -->
  <div class="pendle-level">
    <div class="pendle-box process">
      <h4>PENDLE PROTOCOL</h4>
      <p>Yield Tokenization</p>
      <p>Separate Principal + Yield</p>
    </div>
  </div>

  <!-- Arrow down -->
  <div class="pendle-arrow-down">↓</div>

  <!-- Level 3: PT + YT side by side with output arrows -->
  <div class="pendle-split-row">
    <div class="pendle-token-col">
      <div class="pendle-token pt">
        <h4>PT</h4>
        <div class="subtitle">Principal Token</div>
        <ul>
          <li>Fixed return</li>
          <li>Trades at discount</li>
          <li>Low volatility</li>
        </ul>
      </div>
      <div class="pendle-arrow-down" style="color: #06B6D4;">↓</div>
      <div class="pendle-output pt">Redeem at Maturity</div>
    </div>
    <div class="pendle-token-col">
      <div class="pendle-token yt">
        <h4>YT</h4>
        <div class="subtitle">Yield Token</div>
        <ul>
          <li>Floating yield</li>
          <li>Yield exposure</li>
          <li>High volatility</li>
        </ul>
      </div>
      <div class="pendle-arrow-down" style="color: #F59E0B;">↓</div>
      <div class="pendle-output yt">Collect Yield</div>
    </div>
  </div>

  <!-- Legend -->
  <div class="pendle-legend">
    <span class="cyan">PT</span> + <span class="orange">YT</span> = Original Asset (at maturity)
  </div>
</div>

---

## Pendle Product Matrix

<!--
[Study Notes - Page 8: Pendle Product Matrix]

Pendle's three product lines:

1. Fixed Income Products (PT)
   - Target users: Conservative investors, institutions
   - Features:
     * Lock in fixed yield, no worry about market volatility
     * Similar to traditional finance bonds
     * Redeem at face value at maturity
   - Return source: Buy discounted PT, receive face value difference at maturity
   - Risk: Interest rate risk (if market rates rise, PT price falls)
   - Example: Buy 100 PT-stETH at 95 ETH, redeem 100 ETH after 1 year, yield ≈ 5.26%

2. Leveraged Yield Products (YT)
   - Target users: Aggressive investors, traders
   - Features:
     * Leveraged yield exposure
     * High risk, high return
     * Value goes to zero at maturity (yield already distributed)
   - Return source: Receive all yield from underlying asset
   - Risk: If underlying asset yield drops, YT value shrinks significantly
   - Leverage multiple: Usually 2-5x, depends on maturity and market conditions

3. Liquidity Provision (LP)
   - Target users: Market makers, arbitrageurs
   - Features:
     * Provide liquidity for PT/YT, earn trading fees
     * Receive PENDLE token rewards
     * Bear impermanent loss risk
   - Return source:
     * Trading fees (usually 0.1-0.3%)
     * PENDLE token incentives
     * Possible protocol revenue sharing
   - Risk: Impermanent loss, smart contract risk

Portfolio strategies:
- Conservative: 80% PT + 20% LP
- Balanced: 50% PT + 30% YT + 20% LP
- Aggressive: 70% YT + 30% LP

Key learning points:
- PT and YT are complementary products for different risk preferences
- LP is the foundation of ecosystem, providing liquidity support
- Understand each product's risk/return characteristics
- Think: How to choose appropriate products based on market conditions?

Memory tips:
PT = Conservative (Principal), YT = Aggressive (Yield), LP = Market Making (Liquidity Provider)
-->

<style scoped>
.product-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.8rem;
  max-width: 94%;
  margin: 0 auto;
}
.product-card {
  background: linear-gradient(135deg, rgba(156, 39, 176, 0.15), rgba(156, 39, 176, 0.05));
  border: 2px solid;
  border-radius: 8px;
  padding: 0.9rem;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  position: relative;
}
.product-card.leverage {
  border-color: var(--danger-color);
  box-shadow: 0 4px 12px rgba(255, 107, 107, 0.2);
}
.product-card.spot {
  border-color: var(--info-color);
  box-shadow: 0 4px 12px rgba(33, 150, 243, 0.2);
}
.product-card.governance {
  border-color: var(--purple-color);
  box-shadow: 0 4px 12px rgba(156, 39, 176, 0.2);
}
.product-card h3 {
  margin: 0 0 0.4rem 0;
  margin-top: 1.8rem;
  font-size: 1.1em;
  font-weight: 700;
}
.product-card.leverage h3 { color: var(--danger-color); }
.product-card.spot h3 { color: var(--info-color); }
.product-card.governance h3 { color: var(--purple-color); }
.product-card p {
  margin: 0.2rem 0;
  font-size: 0.9em;
  line-height: 1.4;
  opacity: 0.9;
}
.product-tag {
  position: absolute;
  top: 0.6rem;
  right: 0.6rem;
  font-size: 0.7em;
  font-weight: 600;
  padding: 0.2rem 0.5rem;
  border-radius: 3px;
  background: rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.3);
  z-index: 1;
}
</style>

<div class="product-grid">
<div class="product-card leverage">
<span class="product-tag">Leverage</span>

### Boros
<p>Leveraged yield trading</p>
<p>Up to 10x leverage</p>

</div>
<div class="product-card spot">
<span class="product-tag">Spot</span>

### V2 Spot
<p>Spot yield trading</p>
<p>Fixed income access</p>

</div>
<div class="product-card governance">
<span class="product-tag">Governance</span>

### vePENDLE
<p>Governance token</p>
<p>Yield boost system</p>

</div>
</div>

---

## TradFi Structured Products

<!--
[Study Notes - Page 9: TradFi Structured Products]

Types of traditional finance structured products:

1. Structured Notes
   - Definition: Debt instruments issued by banks, returns linked to specific assets (stocks, indices, commodities)
   - Features:
     * Principal protection (partial or full)
     * Returns linked to underlying asset performance
     * Usually have lock-up periods (1-5 years)
   - Examples:
     * Principal-protected: 100% principal protection + 70% participation in S&P 500
     * Enhanced: 90% principal protection + 120% participation in S&P 500
   - Risks: Issuing bank credit risk, liquidity risk

2. CDO (Collateralized Debt Obligation)
   - Definition: Package debt assets (loans, bonds), tranche into different risk levels
   - Tranche structure:
     * Senior tier (AAA rated): Priority on principal and interest, low yield
     * Mezzanine tier (BBB rated): Medium risk and return
     * Equity tier (unrated): Last to receive distributions, high risk high return
   - 2008 financial crisis lessons:
     * Rating agencies failed, gave high ratings to subprime loan CDOs
     * Opaque pricing and risk assessment
     * Over-leveraging led to systemic risk
   - Comparison with Strata: Strata is a transparent on-chain version of CDO

3. Senior/Subordinate Structured Funds
   - Definition: Split fund shares into senior and subordinate tiers
   - Mechanism:
     * Senior: Fixed return (e.g., 8%), priority distribution
     * Subordinate: Residual returns, bears more risk
   - Applications: Private equity, real estate funds
   - Similarity to Strata: Both are risk-layered structures

Common features of TradFi structured products:
- ✅ Mature risk management frameworks
- ✅ Regulatory protection
- ❌ Opaque pricing
- ❌ High barriers (usually $100K+)
- ❌ Poor liquidity
- ❌ Reliance on intermediaries

Key learning points:
- TradFi structured products have decades of history, massive market size
- DeFi is reconstructing these products in a transparent, open way
- Understand TradFi's advantages (regulation, maturity) and disadvantages (opacity, high barriers)
-->

<style scoped>
.tradfi-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.8rem;
  max-width: 94%;
  margin: 0 auto;
}
.tradfi-card {
  background: linear-gradient(135deg, rgba(149, 165, 166, 0.15), rgba(149, 165, 166, 0.05));
  border: 2px solid;
  border-radius: 8px;
  padding: 0.8rem;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.15);
  position: relative;
}
.tradfi-card.notes {
  border-color: var(--success-color);
  box-shadow: 0 3px 10px rgba(76, 175, 80, 0.2);
}
.tradfi-card.cdo {
  border-color: var(--warning-color);
  box-shadow: 0 3px 10px rgba(255, 152, 0, 0.2);
}
.tradfi-card.derivatives {
  border-color: var(--info-color);
  box-shadow: 0 3px 10px rgba(33, 150, 243, 0.2);
}
.tradfi-tag {
  position: absolute;
  top: 0.6rem;
  right: 0.6rem;
  background: rgba(0, 0, 0, 0.5);
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-size: 0.65em;
  font-weight: 600;
  border: 1px solid rgba(255, 255, 255, 0.3);
  z-index: 1;
}
.tradfi-card.notes .tradfi-tag { color: var(--success-color); border-color: var(--success-color); }
.tradfi-card.cdo .tradfi-tag { color: var(--warning-color); border-color: var(--warning-color); }
.tradfi-card.derivatives .tradfi-tag { color: var(--info-color); border-color: var(--info-color); }
.tradfi-card h3 {
  margin: 0 0 0.4rem 0;
  margin-top: 1.8rem;
  font-size: 1.05em;
  font-weight: 700;
  text-align: center;
}
.tradfi-card.notes h3 { color: var(--success-color); }
.tradfi-card.cdo h3 { color: var(--warning-color); }
.tradfi-card.derivatives h3 { color: var(--info-color); }
.tradfi-card p {
  font-size: 0.85em;
  margin: 0.25rem 0;
  line-height: 1.5;
  opacity: 0.9;
}
</style>

<div class="tradfi-grid">
<div class="tradfi-card notes">
<span class="tradfi-tag">Principal Protected</span>

### Structured Notes
<p>• Principal protection</p>
<p>• Yield enhancement</p>
<p>• Equity-linked</p>

</div>
<div class="tradfi-card cdo">
<span class="tradfi-tag">Tranched</span>

### CDO
<p>• Tranched credit risk</p>
<p>• Asset-backed securities</p>
<p>• Re-securitization</p>

</div>
<div class="tradfi-card derivatives">
<span class="tradfi-tag">Derivatives</span>

### Interest Rate Derivatives
<p>• Interest rate swaps</p>
<p>• Caps/Floors</p>
<p>• Swaptions</p>

</div>
</div>

---

## Technical Architecture Comparison

<!--
[Study Notes - Page 10: Technical Architecture Comparison]

Technical capabilities radar chart interpretation:

This pentagon radar chart compares Strata, Pendle, and TradFi across 5 dimensions:

1. Transparency
   - Strata: 95 points - Smart contracts open source, all logic verifiable on-chain
   - Pendle: 85 points - Smart contracts open source, AMM mechanism transparent
   - TradFi: 40 points - Pricing models not public, black box operations
   - Key difference: DeFi inherently transparent, TradFi relies on trust

2. Composability
   - Strata: 90 points - Output tokens can be input for other protocols, highly modular
   - Pendle: 75 points - PT/YT composable, but relatively independent
   - TradFi: 30 points - Products closed, difficult to combine
   - Key difference: DeFi's "Lego blocks" characteristic vs TradFi's silo effect

3. Settlement Speed
   - Strata: 95 points - Real-time on-chain settlement, second-level confirmation
   - Pendle: 95 points - Real-time on-chain settlement
   - TradFi: 35 points - T+2 or longer settlement cycles
   - Key difference: Blockchain immediacy vs traditional finance delays

4. Innovation
   - Strata: 92 points - Dynamic risk adjustment, universal tranching engine
   - Pendle: 80 points - PT/YT separation mechanism, AMM innovation
   - TradFi: 45 points - Slow product innovation, regulatory constraints
   - Key difference: DeFi rapid iteration vs TradFi steady and conservative

5. Decentralization
   - Strata: 95 points - Fully decentralized, permissionless
   - Pendle: 70 points - Partially decentralized, has governance mechanisms
   - TradFi: 20 points - Highly centralized, relies on institutions
   - Key difference: Trust minimization vs trusting intermediaries

Comprehensive analysis:
- Strata and Pendle: Far surpass TradFi in transparency, composability, settlement speed, decentralization
- TradFi: Has advantages in regulatory compliance, user protection (not shown in this chart)
- Trend: DeFi technical advantages are clear, but needs improvement in regulation and user experience

Key learning points:
- Understand the meaning and importance of each dimension
- DeFi's technical advantages are disruptive
- TradFi's advantages are in regulation and maturity, not technology
- Future may be hybrid model: DeFi technology + TradFi regulation
-->

<style scoped>
.tech-container {
  max-width: 90%;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 1.5rem;
  font-size: 0.75em;
}
.radar-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 0.5rem;
}
.radar-title {
  font-size: 1.2em;
  font-weight: 700;
  color: var(--accent-color);
  margin-bottom: 0.8rem;
  text-align: center;
}
.radar-wrapper {
  width: 100%;
  max-width: 500px;
  margin-bottom: 0.8rem;
}
.radar-wrapper img {
  width: 100%;
  height: auto;
  display: block;
}
.radar-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
  font-size: 0.9em;
  width: 100%;
}
.legend-item {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  white-space: nowrap;
}
.legend-box {
  width: 1em;
  height: 1em;
  border-radius: 2px;
  flex-shrink: 0;
}
.legend-box.strata {
  background: rgba(45, 91, 255, 0.4);
  border: 2px solid #2D5BFF;
}
.legend-box.pendle {
  background: rgba(156, 39, 176, 0.4);
  border: 2px solid #9C27B0;
}
.legend-box.tradfi {
  background: rgba(149, 165, 166, 0.4);
  border: 2px solid #95A5A6;
}
.legend-item span {
  font-weight: 600;
}
.legend-item.strata span {
  color: #2D5BFF;
}
.legend-item.pendle span {
  color: #9C27B0;
}
.legend-item.tradfi span {
  color: #95A5A6;
}
.table-section {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.tech-table {
  width: 100%;
  font-size: 1em;
  border-collapse: collapse;
}
.tech-table th {
  background: rgba(45, 91, 255, 0.2);
  padding: 0.5rem 0.4rem;
  font-weight: 700;
  border: 1px solid rgba(255, 255, 255, 0.2);
  font-size: 0.9em;
}
.tech-table td {
  padding: 0.4rem;
  border: 1px solid rgba(255, 255, 255, 0.15);
  font-size: 0.85em;
  line-height: 1.4;
}
.tech-table td:first-child {
  font-weight: 600;
  color: var(--accent-color);
  background: rgba(241, 196, 15, 0.1);
}
.tech-table .strata-col { background: rgba(45, 91, 255, 0.1); }
.tech-table .pendle-col { background: rgba(156, 39, 176, 0.1); }
.tech-table .tradfi-col { background: rgba(149, 165, 166, 0.1); }
</style>

<div class="tech-container">

<div class="radar-section">
<div class="radar-title">Technical Capabilities Radar</div>

<div class="radar-wrapper">
  <img src="tech-radar-en.svg" alt="Technical Architecture Radar" style="width: 100%; max-width: 936px;">
</div>

<div class="radar-legend">
  <div class="legend-item strata">
    <div class="legend-box strata"></div>
    <span>Strata</span>
  </div>
  <div class="legend-item pendle">
    <div class="legend-box pendle"></div>
    <span>Pendle</span>
  </div>
  <div class="legend-item tradfi">
    <div class="legend-box tradfi"></div>
    <span>TradFi</span>
  </div>
</div>
</div>

<div class="table-section">
<table class="tech-table">
<thead>
  <tr>
    <th>Dimension</th>
    <th>Strata</th>
    <th>Pendle</th>
    <th>TradFi</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Transparency</td>
    <td class="strata-col">Fully on-chain</td>
    <td class="pendle-col">On-chain</td>
    <td class="tradfi-col">Limited</td>
  </tr>
  <tr>
    <td>Composability</td>
    <td class="strata-col">Highly composable</td>
    <td class="pendle-col">Moderately</td>
    <td class="tradfi-col">Low</td>
  </tr>
  <tr>
    <td>Settlement</td>
    <td class="strata-col">Real-time</td>
    <td class="pendle-col">Real-time</td>
    <td class="tradfi-col">T+2 or longer</td>
  </tr>
  <tr>
    <td>Innovation</td>
    <td class="strata-col">Chain-agnostic</td>
    <td class="pendle-col">AMM mechanism</td>
    <td class="tradfi-col">Traditional</td>
  </tr>
  <tr>
    <td>Decentralization</td>
    <td class="strata-col">Fully decentralized</td>
    <td class="pendle-col">Partially</td>
    <td class="tradfi-col">Centralized</td>
  </tr>
</tbody>
</table>
</div>

</div>

---

## Risk/Return Profile

<!--
[Study Notes - Page 11: Risk/Return Profile]

Risk/return comparison of three product types:

Strata Products:
1. Senior Tier
   - Expected return: 4-8% APY
   - Risk level: Low
   - Features: Priority on principal and yield, protected by Junior tier
   - Suitable for: Conservative investors, institutional capital
   - Risks: Smart contract risk, underlying asset risk (but buffered)

2. Junior Tier
   - Expected return: 12-25% APY
   - Risk level: High
   - Features: Bears first-loss risk, receives leveraged returns
   - Suitable for: Aggressive investors, high risk tolerance traders
   - Risks: May lose entire principal

Pendle Products:
1. PT (Principal Token)
   - Expected return: 3-6% fixed income
   - Risk level: Low-Medium
   - Features: Lock in fixed yield, similar to bonds
   - Suitable for: Investors seeking stable returns
   - Risks: Interest rate risk, smart contract risk

2. YT (Yield Token)
   - Expected return: 10-30% APY (high volatility)
   - Risk level: High
   - Features: Leveraged yield exposure, expires worthless
   - Suitable for: Investors bullish on underlying asset yields
   - Risks: Yield decline leads to value going to zero

3. LP (Liquidity Provision)
   - Expected return: 8-15% APY
   - Risk level: Medium
   - Features: Earn fees + token incentives
   - Suitable for: Market makers, long-term holders
   - Risks: Impermanent loss, smart contract risk

TradFi Products:
1. Structured Notes
   - Expected return: 2-8% APY
   - Risk level: Low-Medium
   - Features: Partial principal protection, returns linked to underlying
   - Suitable for: Conservative investors
   - Risks: Issuer credit risk, liquidity risk

2. CDO
   - Expected return: Senior 3-5%, Equity 15-25%
   - Risk level: Senior low, Equity high
   - Features: Tiered risk structure
   - Suitable for: Institutional investors with different risk preferences
   - Risks: Inaccurate ratings, systemic risk (2008 lesson)

Key comparisons:
- Yield: DeFi > TradFi (due to elimination of intermediary costs)
- Risk: DeFi smart contract risk vs TradFi credit risk
- Volatility: DeFi > TradFi (crypto market more volatile)
- Liquidity: DeFi > TradFi (tokenization brings liquidity)

Key learning points:
- High returns inevitably come with high risk
- Understand the risk sources of each product
- DeFi's additional risks: smart contracts, oracles, governance
- Match product selection to your risk tolerance
-->

<style scoped>
.risk-container {
  font-size: 0.65em;
  margin-top: 0.25rem;
  max-width: 94%;
  margin-left: auto;
  margin-right: auto;
}
.risk-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.5rem;
}
.risk-column {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}
.risk-column-title {
  font-size: 0.9em;
  font-weight: 700;
  text-align: center;
  padding: 0.3rem;
  border-radius: 4px;
  margin-bottom: 0.2rem;
}
.risk-column-title.strata {
  background: linear-gradient(135deg, rgba(45, 91, 255, 0.2), rgba(45, 91, 255, 0.1));
  color: var(--primary-color);
  border: 2px solid var(--primary-color);
}
.risk-column-title.pendle {
  background: linear-gradient(135deg, rgba(156, 39, 176, 0.2), rgba(156, 39, 176, 0.1));
  color: var(--purple-color);
  border: 2px solid var(--purple-color);
}
.risk-column-title.tradfi {
  background: linear-gradient(135deg, rgba(149, 165, 166, 0.2), rgba(149, 165, 166, 0.1));
  color: #95A5A6;
  border: 2px solid #95A5A6;
}
.risk-card {
  border-radius: 5px;
  padding: 0.4rem;
  border: 2px solid;
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.15);
  position: relative;
  background: rgba(255, 255, 255, 0.03);
}
.risk-card.low-risk {
  border-color: var(--success-color);
  box-shadow: 0 3px 8px rgba(76, 175, 80, 0.25);
}
.risk-card.mid-risk {
  border-color: var(--warning-color);
  box-shadow: 0 3px 8px rgba(255, 152, 0, 0.25);
}
.risk-card.high-risk {
  border-color: var(--danger-color);
  box-shadow: 0 3px 8px rgba(255, 107, 107, 0.25);
}
.risk-card h4 {
  margin: 0 0 0.25rem 0;
  font-size: 0.95em;
  font-weight: 700;
  text-align: center;
  padding-bottom: 0.2rem;
  line-height: 1.2;
}
.risk-hero {
  text-align: center;
  margin: 0.25rem 0;
  padding: 0.3rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 3px;
}
.risk-hero-label {
  font-size: 0.7em;
  opacity: 0.75;
  margin-bottom: 0.1rem;
  line-height: 1.1;
}
.risk-hero-value {
  font-size: 1.25em;
  font-weight: 700;
  color: var(--accent-color);
  line-height: 1.1;
}
.risk-meta {
  display: flex;
  justify-content: space-around;
  gap: 0.2rem;
  margin-top: 0.25rem;
}
.risk-meta-item {
  background: rgba(255, 255, 255, 0.04);
  padding: 0.2rem;
  border-radius: 3px;
  text-align: center;
  flex: 1;
}
.risk-meta-label {
  font-size: 0.65em;
  opacity: 0.7;
  display: block;
  margin-bottom: 0.08rem;
  line-height: 1.1;
}
.risk-meta-value {
  font-size: 0.8em;
  font-weight: 600;
  line-height: 1.1;
}
</style>

<div class="risk-container">
<div class="risk-grid">

<!-- Strata Column -->
<div class="risk-column">
<div class="risk-column-title strata">Strata</div>

<div class="risk-card low-risk">

#### Senior

<div class="risk-hero">
<div class="risk-hero-label">Annual Yield</div>
<div class="risk-hero-value">Benchmark+1-3%</div>
</div>

<div class="risk-meta">
<div class="risk-meta-item">
<span class="risk-meta-label">Risk</span>
<div class="risk-meta-value">Low</div>
</div>
<div class="risk-meta-item">
<span class="risk-meta-label">Liquidity</span>
<div class="risk-meta-value">High</div>
</div>
<div class="risk-meta-item">
<span class="risk-meta-label">Minimum</span>
<div class="risk-meta-value">$100</div>
</div>
</div>

</div>

<div class="risk-card high-risk">

#### Junior

<div class="risk-hero">
<div class="risk-hero-label">Annual Yield</div>
<div class="risk-hero-value">10-30%+</div>
</div>

<div class="risk-meta">
<div class="risk-meta-item">
<span class="risk-meta-label">Risk</span>
<div class="risk-meta-value">High</div>
</div>
<div class="risk-meta-item">
<span class="risk-meta-label">Liquidity</span>
<div class="risk-meta-value">High</div>
</div>
<div class="risk-meta-item">
<span class="risk-meta-label">Minimum</span>
<div class="risk-meta-value">$500</div>
</div>
</div>

</div>

</div>

<!-- Pendle Column -->
<div class="risk-column">
<div class="risk-column-title pendle">Pendle</div>

<div class="risk-card mid-risk">

#### Fixed

<div class="risk-hero">
<div class="risk-hero-label">Annual Yield</div>
<div class="risk-hero-value">Fixed 5-8%</div>
</div>

<div class="risk-meta">
<div class="risk-meta-item">
<span class="risk-meta-label">Risk</span>
<div class="risk-meta-value">Medium</div>
</div>
<div class="risk-meta-item">
<span class="risk-meta-label">Liquidity</span>
<div class="risk-meta-value">High</div>
</div>
<div class="risk-meta-item">
<span class="risk-meta-label">Minimum</span>
<div class="risk-meta-value">$50</div>
</div>
</div>

</div>

<div class="risk-card high-risk">

#### Leveraged

<div class="risk-hero">
<div class="risk-hero-label">Annual Yield</div>
<div class="risk-hero-value">15-50%+</div>
</div>

<div class="risk-meta">
<div class="risk-meta-item">
<span class="risk-meta-label">Risk</span>
<div class="risk-meta-value">High</div>
</div>
<div class="risk-meta-item">
<span class="risk-meta-label">Liquidity</span>
<div class="risk-meta-value">High</div>
</div>
<div class="risk-meta-item">
<span class="risk-meta-label">Minimum</span>
<div class="risk-meta-value">$200</div>
</div>
</div>

</div>

</div>

<!-- TradFi Column -->
<div class="risk-column">
<div class="risk-column-title tradfi">TradFi</div>

<div class="risk-card mid-risk">

#### Notes

<div class="risk-hero">
<div class="risk-hero-label">Annual Yield</div>
<div class="risk-hero-value">3-6%</div>
</div>

<div class="risk-meta">
<div class="risk-meta-item">
<span class="risk-meta-label">Risk</span>
<div class="risk-meta-value">Low-Med</div>
</div>
<div class="risk-meta-item">
<span class="risk-meta-label">Liquidity</span>
<div class="risk-meta-value">Low</div>
</div>
<div class="risk-meta-item">
<span class="risk-meta-label">Minimum</span>
<div class="risk-meta-value">$25K</div>
</div>
</div>

</div>

<div class="risk-card high-risk">

#### CDOs

<div class="risk-hero">
<div class="risk-hero-label">Annual Yield</div>
<div class="risk-hero-value">8-15%+</div>
</div>

<div class="risk-meta">
<div class="risk-meta-item">
<span class="risk-meta-label">Risk</span>
<div class="risk-meta-value">High</div>
</div>
<div class="risk-meta-item">
<span class="risk-meta-label">Liquidity</span>
<div class="risk-meta-value">Low</div>
</div>
<div class="risk-meta-item">
<span class="risk-meta-label">Minimum</span>
<div class="risk-meta-value">$100K</div>
</div>
</div>

</div>

</div>

</div>
</div>

---

## Target User Segments

<!--
[Study Notes - Page 12: Target User Segments]

Target user comparison for three product types:

Strata Target Users:
1. DeFi Native Users
   - Profile: Familiar with smart contracts, wallet operations
   - Needs: Further optimize risk/return on top of DeFi yields
   - Typical scenario: Tranche stETH, Senior gets stable yield, Junior gets leveraged yield

2. Risk Managers
   - Profile: Need granular risk control
   - Needs: Tranche portfolios, isolate risks
   - Typical scenario: DAO treasury tranches assets, Senior for operations, Junior for growth

3. Institutional Investors
   - Profile: Large capital, need compliance and risk management
   - Needs: Find TradFi-like risk tranching tools in DeFi
   - Typical scenario: Crypto funds use Strata to build tranched products

Pendle Target Users:
1. Fixed Income Seekers
   - Profile: Risk-averse, seeking stable returns
   - Needs: Lock in fixed yields in crypto markets
   - Typical scenario: Buy PT-stETH, lock in 5% APY

2. Yield Traders
   - Profile: Bullish/bearish on future yield rates
   - Needs: Trade yield curves
   - Typical scenarios:
     * Bullish on yield increase → Buy YT
     * Bearish on yield decrease → Sell YT or buy PT

3. Arbitrageurs
   - Profile: Looking for pricing errors
   - Needs: Arbitrage PT/YT price discrepancies
   - Typical scenario: Arbitrage when PT+YT price ≠ underlying asset price

TradFi Target Users:
1. High Net Worth Individuals
   - Profile: Assets $1M+, seeking asset allocation
   - Needs: Capital preservation, tax optimization
   - Typical scenario: Buy structured notes, partial principal protection + equity participation

2. Institutional Investors
   - Profile: Pension funds, insurance companies, endowments
   - Needs: Stable returns, regulatory compliance
   - Typical scenario: Invest in AAA-rated CDO, stable cash flows

3. Corporate Treasury
   - Profile: Corporate idle fund management
   - Needs: Liquidity management, yield optimization
   - Typical scenario: Buy short-term structured products, optimize cash management

User segment comparison:
- Entry barriers:
  * Strata/Pendle: From a few dollars, no KYC
  * TradFi: $100K+, accredited investor status required
- Technical requirements:
  * Strata/Pendle: Need to understand DeFi, wallets, smart contracts
  * TradFi: Through advisors/banks, low technical requirements
- Regulatory protection:
  * Strata/Pendle: No regulatory protection, self-custody
  * TradFi: Investor protection mechanisms exist

Key learning points:
- DeFi lowers entry barriers but raises technical barriers
- Different products serve users with different risk preferences
- Understanding target users helps choose appropriate products
-->

<style scoped>
.users-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.8rem;
  max-width: 94%;
  margin: 0 auto;
}
.user-card {
  background: rgba(45, 91, 255, 0.08);
  border: 2px solid rgba(45, 91, 255, 0.3);
  border-radius: 8px;
  padding: 0.75rem;
}
.user-card h3 {
  margin: 0 0 0.5rem 0;
  font-size: 0.95em;
  color: var(--primary-color);
  font-weight: 600;
  text-align: center;
}
.user {
  margin: 0.5rem 0;
  background: rgba(255, 255, 255, 0.05);
  padding: 0.5rem;
  border-radius: 6px;
}
.user strong {
  color: var(--accent-color);
  font-size: 0.95em;
  display: block;
  margin-bottom: 0.2rem;
}
.user p {
  margin: 0;
  font-size: 0.85em;
  opacity: 0.9;
  line-height: 1.3;
}
</style>

<div class="users-grid">
<div class="user-card">

### Strata Users
<div class="user">
<strong>Institutional Investors</strong>
<p>Stable yield + excess returns</p>
</div>
<div class="user">
<strong>DeFi Power Users</strong>
<p>High leverage opportunities</p>
</div>

</div>
<div class="user-card">

### Pendle Users
<div class="user">
<strong>Yield Traders</strong>
<p>Yield arbitrage</p>
</div>
<div class="user">
<strong>Fixed Income Investors</strong>
<p>Predictable cash flows</p>
</div>

</div>
<div class="user-card">

### TradFi Users
<div class="user">
<strong>Bank Asset Managers</strong>
<p>Compliant products</p>
</div>
<div class="user">
<strong>Pension Funds</strong>
<p>Principal protection</p>
</div>

</div>
</div>

---

## Regulatory Landscape

<!--
[Study Notes - Page 13: Regulatory Landscape Comparison]

Three dimensions of regulatory comparison:

1. Regulatory Framework

Strata/Pendle (DeFi):
- Current state: Regulatory vacuum, most countries have not yet clarified regulations
- Advantages:
  * High innovation freedom
  * Permissionless, globally accessible
  * Rapid iteration and experimentation
- Disadvantages:
  * Legal uncertainty
  * Lack of investor protection
  * May face future regulatory crackdowns
- Trends:
  * EU MiCA regulation (effective 2024)
  * US SEC increased enforcement
  * Countries gradually establishing DeFi regulatory frameworks

TradFi:
- Current state: Mature regulatory system
- Regulatory bodies:
  * US: SEC, CFTC, OCC
  * EU: ESMA, national financial regulators
  * China: CBIRC, CSRC
- Advantages:
  * Comprehensive investor protection
  * High market stability
  * Mature dispute resolution mechanisms
- Disadvantages:
  * Limited innovation
  * High compliance costs
  * High entry barriers

2. Compliance Requirements

Strata/Pendle:
- KYC/AML: Usually not required (decentralized)
- Disclosure: Smart contract code public, but no mandatory disclosure requirements
- Capital requirements: None
- Audit requirements: Voluntary smart contract audits
- Risk: May be deemed unregistered securities

TradFi:
- KYC/AML: Strictly required, must verify identity
- Disclosure: Detailed prospectus, periodic reports
- Capital requirements: Issuers must meet capital adequacy ratios
- Audit requirements: Mandatory financial audits
- Investor suitability: Must assess investor risk tolerance

3. Investor Protection

Strata/Pendle:
- Protection mechanisms:
  * Smart contract audits (non-mandatory)
  * Community governance
  * Open source code transparency
- Dispute resolution:
  * No formal mechanism
  * Relies on community consensus
  * May use on-chain governance
- Risks:
  * No compensation for smart contract vulnerabilities
  * Self-bear losses from hacks
  * No deposit insurance

TradFi:
- Protection mechanisms:
  * Deposit insurance (e.g., FDIC)
  * Investor compensation funds
  * Regulatory oversight
- Dispute resolution:
  * Court litigation
  * Arbitration mechanisms
  * Regulatory intervention
- Advantages:
  * Protection in institutional bankruptcy
  * Fraud can be prosecuted
  * Central bank backstop for systemic risk

Key insights:
- DeFi's regulatory dilemma: Decentralization vs regulatory requirements
- Future trend: Hybrid model
  * On-chain transparency + off-chain compliance
  * Decentralized technology + centralized compliance layer
  * Example: Permissioned DeFi

Key learning points:
- Regulation is not bad, it's a necessary means to protect investors
- DeFi needs to find balance between innovation and compliance
- Understanding regulatory risk is important consideration for DeFi investment
- Follow regulatory developments, may affect product availability
-->

<style scoped>
.regulation-container {
  max-width: 95%;
  margin: 0 auto;
  font-size: 0.76em;
}

/* Core comparison table */
.regulation-table-wrapper {
  margin-bottom: 0.4rem;
}
.regulation-table {
  width: 100%;
  border-collapse: collapse;
  background: linear-gradient(135deg, rgba(45, 91, 255, 0.08), rgba(45, 91, 255, 0.02));
  border-radius: 6px;
  overflow: hidden;
}
.regulation-table thead {
  background: linear-gradient(135deg, rgba(45, 91, 255, 0.3), rgba(45, 91, 255, 0.15));
}
.regulation-table th {
  padding: 0.35rem 0.3rem;
  font-weight: 700;
  font-size: 1em;
  border: 1px solid rgba(255, 255, 255, 0.2);
  text-align: center;
}
.regulation-table th:first-child {
  color: var(--accent-color);
  text-align: left;
  padding-left: 0.6rem;
  width: 18%;
}
.regulation-table th.defi-col {
  color: #2D5BFF;
  width: 41%;
}
.regulation-table th.tradfi-col {
  color: #95A5A6;
  width: 41%;
}
.regulation-table td {
  padding: 0.28rem 0.3rem;
  border: 1px solid rgba(255, 255, 255, 0.15);
  line-height: 1.3;
  font-size: 0.98em;
}
.regulation-table td:first-child {
  font-weight: 600;
  color: var(--accent-color);
  background: rgba(241, 196, 15, 0.08);
  padding-left: 0.6rem;
}
.regulation-table td.defi-col {
  background: rgba(45, 91, 255, 0.08);
}
.regulation-table td.tradfi-col {
  background: rgba(149, 165, 166, 0.08);
}
.regulation-table .positive {
  color: var(--success-color);
  font-weight: 600;
}
.regulation-table .negative {
  color: var(--danger-color);
  font-weight: 600;
}
.regulation-table .neutral {
  color: var(--warning-color);
  font-weight: 600;
}

/* Key insight box */
.regulation-insight {
  background: linear-gradient(135deg, rgba(241, 196, 15, 0.25), rgba(241, 196, 15, 0.08));
  border: 2px solid var(--accent-color);
  border-radius: 6px;
  padding: 0.35rem 0.8rem;
  text-align: center;
  box-shadow: 0 4px 15px rgba(241, 196, 15, 0.3);
}
.insight-icon {
  font-size: 1.3em;
  margin-right: 0.3rem;
  vertical-align: middle;
}
.insight-text {
  font-size: 1em;
  font-weight: 700;
  line-height: 1.35;
  color: #fff;
  vertical-align: middle;
}
.insight-highlight {
  color: var(--accent-color);
  font-weight: 800;
}
</style>

<div class="regulation-container">

<!-- Core comparison table -->
<div class="regulation-table-wrapper">
<table class="regulation-table">
<thead>
  <tr>
    <th>Dimension</th>
    <th class="defi-col">DeFi</th>
    <th class="tradfi-col">TRAD-FI</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Legal Framework</td>
    <td class="defi-col"><span class="negative">Unclear</span> - High regulatory uncertainty</td>
    <td class="tradfi-col"><span class="positive">Clear</span> - Established legal system</td>
  </tr>
  <tr>
    <td>Entry Barriers</td>
    <td class="defi-col"><span class="positive">Low</span> - No KYC, globally accessible</td>
    <td class="tradfi-col"><span class="negative">High</span> - Strict qualification requirements</td>
  </tr>
  <tr>
    <td>Innovation Speed</td>
    <td class="defi-col"><span class="positive">Fast</span> - No approval needed, rapid iteration</td>
    <td class="tradfi-col"><span class="negative">Slow</span> - Lengthy approval process</td>
  </tr>
  <tr>
    <td>Investor Protection</td>
    <td class="defi-col"><span class="negative">Weak</span> - Self-custody, no recourse</td>
    <td class="tradfi-col"><span class="positive">Strong</span> - Regulatory protection, dispute resolution</td>
  </tr>
  <tr>
    <td>Compliance Cost</td>
    <td class="defi-col"><span class="positive">Low</span> - Tech-driven, controllable costs</td>
    <td class="tradfi-col"><span class="negative">High</span> - Labor-intensive, ongoing investment</td>
  </tr>
  <tr>
    <td>Transparency</td>
    <td class="defi-col"><span class="positive">High</span> - On-chain public, real-time</td>
    <td class="tradfi-col"><span class="neutral">Medium</span> - Periodic disclosure, information lag</td>
  </tr>
</tbody>
</table>
</div>

<!-- Key insight -->
<div class="regulation-insight">
<span class="insight-icon">💡</span>
<span class="insight-text">
DeFi is transitioning from <span class="insight-highlight">"regulatory arbitrage"</span> to <span class="insight-highlight">"proactive compliance"</span>, forming a <span class="insight-highlight">complementary</span> rather than adversarial relationship with TradFi
</span>
</div>

</div>

---

## Innovation Highlights

<!--
[Study Notes - Page 14: Innovation Highlights Comparison]

Core innovation comparison of three product types:

Strata Innovation Highlights:
1. Universal Risk Tranching Engine
   - Innovation: Not targeting specific assets, but a universal tranching protocol
   - Significance: Any DeFi yield asset can be tranched
   - Analogy: Like "Uniswap for risk tranching"

2. Dynamic Risk Adjustment
   - Innovation: Automatically adjust risk parameters based on market conditions
   - Significance: More efficient than traditional fixed ratios
   - Technology: Uses oracles and algorithms for automatic rebalancing

3. Composability
   - Innovation: Output tokens can be input for other protocols
   - Significance: Creates infinite financial product combination possibilities
   - Example: Strata Senior → Aave collateral → Borrowing → Reinvestment

Pendle Innovation Highlights:
1. Yield Tokenization (PT/YT Separation)
   - Innovation: Separating principal and yield into independently tradable tokens
   - Significance: Created DeFi's "fixed income market"
   - TradFi comparison: Similar to zero-coupon bonds, but more flexible

2. AMM for Yield
   - Innovation: AMM specifically designed for yield trading
   - Technology: Pricing curve considering time decay
   - Significance: Provides liquidity and price discovery for PT/YT

3. vePENDLE Governance Model
   - Innovation: Vote-Escrowed model
   - Mechanism: Lock PENDLE → Get vePENDLE → Boosted returns + governance rights
   - Significance: Incentivizes long-term holding, reduces selling pressure

TradFi "Innovation" (relatively conservative):
1. Structured Notes
   - Features: Principal protection + market participation
   - Limitations: Complex product design, opaque
   - Issues: Risks exposed in 2008 financial crisis

2. CDO Tranching
   - Features: Tiered risk structure
   - Limitations: Ratings depend on third parties, may be inaccurate
   - Lessons: Over-securitization leads to systemic risk

3. Interest Rate Derivatives
   - Features: Hedge interest rate risk
   - Limitations: Only institutional access, retail cannot participate
   - Complexity: Requires specialized knowledge

Innovation comparison summary:

| Dimension | Strata | Pendle | TradFi |
|-----------|--------|--------|--------|
| Innovation Speed | Fast (monthly iterations) | Fast (monthly iterations) | Slow (yearly iterations) |
| Technical Innovation | High (smart contracts) | High (AMM+tokenization) | Low (traditional financial engineering) |
| Composability | Very High | High | Low |
| Transparency | Fully transparent | Fully transparent | Opaque |
| Entry Barriers | Low | Low | High |

Key insights:
- DeFi's innovation advantages:
  * Open source collaboration, fast innovation
  * Composability brings exponential innovation
  * Transparency reduces information asymmetry
- TradFi's innovation disadvantages:
  * Regulation limits innovation
  * Closed systems, difficult to combine
  * Innovation mainly serves institutions, not retail

Key learning points:
- DeFi is reconstructing traditional financial products, not simply copying
- Composability is DeFi's biggest innovation advantage
- Understanding each product's innovation helps evaluate long-term value
-->

<style scoped>
.highlight-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.5rem;
  max-width: 98%;
  margin: 0 auto;
}
.highlight-card {
  border-radius: 8px;
  padding: 0.7rem 0.5rem;
  text-align: center;
}
.highlight-card.strata {
  background: rgba(45, 91, 255, 0.1);
  border: 2px solid rgba(45, 91, 255, 0.3);
}
.highlight-card.pendle {
  background: rgba(156, 39, 176, 0.1);
  border: 2px solid rgba(156, 39, 176, 0.3);
}
.highlight-card.tradfi {
  background: rgba(44, 62, 80, 0.3);
  border: 2px solid rgba(44, 62, 80, 0.5);
}
.highlight-card h3 {
  margin: 0 0 0.4rem 0;
  font-size: 1em;
  font-weight: 600;
  word-break: keep-all;
  overflow-wrap: normal;
}
.highlight-card.strata h3 { color: var(--primary-color); }
.highlight-card.pendle h3 { color: var(--purple-color); }
.highlight-card.tradfi h3 { color: #95A5A6; }
.highlight-card p {
  margin: 0.2rem 0;
  font-size: 0.88em;
  line-height: 1.4;
  word-break: keep-all;
  overflow-wrap: normal;
}
</style>

<div class="highlight-grid">
<div class="highlight-card strata">

### Strata Innovation
<p>Universal risk tranching</p>
<p>Over-collateralization</p>
<p>Chain-agnostic design</p>

</div>
<div class="highlight-card pendle">

### Pendle Innovation
<p>Yield tokenization standard</p>
<p>Yield AMM</p>
<p>veTokenomics</p>

</div>
<div class="highlight-card tradfi">

### TradFi Strengths
<p>Mature risk models</p>
<p>Regulatory framework</p>
<p>Institutional network</p>

</div>
</div>

---

## Market Size & Growth

<!--
[Study Notes - Page 15: Market Size & Growth]

Market size comparison (2024 data):

TradFi Structured Products Market:
- Global size: ~$10-15 trillion
- Major markets:
  * US: $3-4 trillion
  * Europe: $4-5 trillion
  * Asia: $2-3 trillion
- Product type distribution:
  * Structured notes: 40%
  * CDO/CLO: 30%
  * Interest rate derivatives: 20%
  * Others: 10%
- Growth rate: 3-5% annually (mature market, slow growth)

DeFi Structured Products Market:
- Strata TVL: ~$50-100M (as of 2024)
- Pendle TVL: ~$3-5B (as of 2024, rapid growth)
- Overall DeFi structured products: ~$5-10B
- Share of total DeFi TVL: ~5-10%
- Growth rate: 50-100% annually (high growth phase)

Market size comparison analysis:
1. Absolute size:
   - TradFi is 1000-2000x DeFi
   - DeFi still in early stages
   - Massive growth potential

2. Growth speed:
   - DeFi growth rate is 10-20x TradFi
   - Significant compound growth effect
   - Expected to reach 1-5% of TradFi within 5-10 years

3. Penetration rate:
   - DeFi structured products: 5-10% of total DeFi TVL
   - TradFi structured products: Higher percentage of traditional finance
   - DeFi has significant room for penetration

Growth drivers:

DeFi growth drivers:
1. Technology maturity:
   - Layer 2 reduces gas fees
   - Improved cross-chain interoperability
   - Better user experience

2. Institutional adoption:
   - Traditional financial institutions entering DeFi
   - Regulatory frameworks gradually clarifying
   - More compliant products

3. Product innovation:
   - New yield sources (RWA, LSD, etc.)
   - More complex structured products
   - Better risk management tools

4. Market education:
   - Deeper user understanding of DeFi
   - More educational resources
   - Mature community ecosystem

TradFi growth constraints:
1. Regulatory limits: Innovation restricted
2. High costs: High intermediary fees
3. Low efficiency: Long settlement cycles
4. Entry barriers: Retail difficult to participate

Future projections (2025-2030):

Conservative projection:
- DeFi structured products TVL: $50-100B
- Annual growth rate: 30-50%
- Share of total DeFi TVL: 10-15%

Optimistic projection:
- DeFi structured products TVL: $200-500B
- Annual growth rate: 50-100%
- Share of total DeFi TVL: 15-20%
- Beginning to capture TradFi market share

Key milestones:
- 2025: Pendle TVL breaks $10B
- 2026: Mainstream institutions launch DeFi structured products
- 2027: Regulatory framework clear, compliant products explode
- 2028-2030: DeFi structured products become mainstream

Key learning points:
- DeFi market is small but growing rapidly
- Understanding growth drivers helps capture investment opportunities
- Follow TVL changes, reflects market confidence
- Long-term bullish on DeFi structured products
-->

<style scoped>
.market-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  max-width: 94%;
  margin: 0 auto;
  gap: 1rem;
  font-size: 0.75em;
}
.pie-section {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.pie-chart {
  position: relative;
  width: 280px;
  height: 280px;
  border-radius: 50%;
  background: conic-gradient(
    #95A5A6 0% 85%,
    var(--primary-color) 85% 86.5%,
    rgba(255, 255, 255, 0.15) 86.5% 100%
  );
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  margin: 0.5rem 0;
}
.pie-center {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #1a1a2e;
  width: 140px;
  height: 140px;
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: 2px solid rgba(255, 255, 255, 0.1);
}
.pie-center-title {
  font-size: 0.9em;
  opacity: 0.8;
  margin-bottom: 0.3rem;
}
.pie-center-value {
  font-size: 1.4em;
  font-weight: 700;
  color: var(--accent-color);
}
.legend {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-top: 0.5rem;
}
.legend-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(255, 255, 255, 0.05);
  padding: 0.4rem 0.6rem;
  border-radius: 5px;
}
.legend-color {
  width: 20px;
  height: 20px;
  border-radius: 3px;
  flex-shrink: 0;
}
.legend-color.tradfi { background: #95A5A6; }
.legend-color.defi { background: var(--primary-color); }
.legend-color.other { background: rgba(255, 255, 255, 0.15); }
.legend-text {
  flex: 1;
  display: flex;
  justify-content: space-between;
  font-size: 0.95em;
}
.legend-label { font-weight: 600; }
.legend-value { color: var(--accent-color); font-weight: 600; }
.growth-section {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
}
.growth-title {
  font-size: 1.1em;
  font-weight: 700;
  color: var(--primary-color);
  margin-bottom: 0.3rem;
  text-align: center;
}
.growth-card {
  background: linear-gradient(135deg, rgba(45, 91, 255, 0.15), rgba(45, 91, 255, 0.05));
  border: 2px solid;
  border-radius: 8px;
  padding: 0.7rem;
  text-align: center;
}
.growth-card.defi {
  border-color: var(--success-color);
  box-shadow: 0 4px 12px rgba(76, 175, 80, 0.2);
}
.growth-card.tradfi {
  border-color: #95A5A6;
  box-shadow: 0 4px 12px rgba(149, 165, 166, 0.2);
}
.growth-card h4 {
  margin: 0 0 0.4rem 0;
  font-size: 1em;
  font-weight: 700;
}
.growth-card.defi h4 { color: var(--success-color); }
.growth-card.tradfi h4 { color: #95A5A6; }
.cagr-value {
  font-size: 1.6em;
  font-weight: 700;
  color: var(--accent-color);
  margin: 0.3rem 0;
}
.growth-detail {
  font-size: 0.9em;
  opacity: 0.9;
  margin-top: 0.3rem;
  padding-top: 0.3rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
</style>

<div class="market-layout">
<div class="pie-section">

<div class="pie-chart">
  <div class="pie-center">
    <div class="pie-center-title">Total Market</div>
    <div class="pie-center-value">$10T</div>
  </div>
</div>

<div class="legend">
  <div class="legend-item">
    <div class="legend-color tradfi"></div>
    <div class="legend-text">
      <span class="legend-label">TradFi</span>
      <span class="legend-value">$8.5T (85%)</span>
    </div>
  </div>
  <div class="legend-item">
    <div class="legend-color defi"></div>
    <div class="legend-text">
      <span class="legend-label">DeFi</span>
      <span class="legend-value">$150B (1.5%)</span>
    </div>
  </div>
  <div class="legend-item">
    <div class="legend-color other"></div>
    <div class="legend-text">
      <span class="legend-label">Other</span>
      <span class="legend-value">$1.35T (13.5%)</span>
    </div>
  </div>
</div>

</div>

<div class="growth-section">

<div class="growth-title">Compound Annual Growth Rate (CAGR)</div>

<div class="growth-card defi">

#### DeFi Structured Products
<div class="cagr-value">100%+</div>
<div class="growth-detail">
  Strata: 140% | Pendle: 95%
</div>

</div>

<div class="growth-card tradfi">

#### TradFi Structured Products
<div class="cagr-value">8%</div>
<div class="growth-detail">
  Stable but slow growth
</div>

</div>

</div>
</div>

---

## Risk Factor Analysis (1/2)

<!--
[Study Notes - Page 16: Risk Factor Analysis (1/2)]

Risk matrix interpretation:
This risk matrix evaluates 6 major risks across two dimensions:
- X-axis: Probability of occurrence (Low/Medium/High)
- Y-axis: Impact level (Low/Medium/High)

6 major risk factors explained:

1. Smart Contract Risk (High probability/High impact)
- Position: Upper right corner (red zone) - requires most attention
- Probability: High
  * Multiple smart contract vulnerabilities in DeFi history
  * 2022: $3.1B stolen (mainly smart contract vulnerabilities)
  * Complex contracts more prone to bugs
- Impact: High
  * May result in total fund loss
  * Cannot recover (blockchain irreversible)
  * No insurance compensation
- Mitigation measures:
  * Choose protocols with multiple audits
  * Review audit reports (Certik, Trail of Bits, etc.)
  * Follow bug bounty programs
  * Diversify investments, don't all-in single protocol
- Real cases:
  * 2021 Poly Network: $611M stolen (later returned)
  * 2022 Ronin Bridge: $625M stolen
  * 2023 Euler Finance: $197M stolen (partially recovered)

2. Liquidity Risk (Medium probability/High impact)
- Position: Upper middle area (orange)
- Probability: Medium
  * Liquidity dries up during market panic
  * Small pools prone to liquidity issues
- Impact: High
  * Cannot exit positions
  * Forced to accept huge slippage
  * May trigger cascading liquidations
- Mitigation measures:
  * Choose protocols with high TVL
  * Check liquidity depth
  * Avoid trading during market panic
  * Set reasonable slippage tolerance
- Real cases:
  * May 2022 UST depeg, Curve 3pool liquidity dried up
  * March 2023 USDC depeg, multiple DeFi protocols liquidity crisis

3. Oracle Risk (Medium probability/High impact)
- Position: Upper middle area (orange)
- Probability: Medium
  * Oracle manipulation
  * Data source failure
  * Network latency causing price deviation
- Impact: High
  * Incorrect pricing leads to arbitrage losses
  * Unfair liquidations
  * Protocol fund losses
- Mitigation measures:
  * Use multiple oracles (Chainlink, Band, etc.)
  * Check oracle update frequency
  * Monitor oracle decentralization level
- Real cases:
  * Nov 2020 Compound liquidation event (Coinbase oracle failure)
  * 2022 Mango Markets manipulation ($110M loss)

Key learning points:
- Upper right corner risks (high probability + high impact) require priority attention
- Smart contract risk is DeFi's biggest risk
- Understand mitigation measures for each risk
- Risk management is more important than chasing high returns
-->

<style scoped>
.risk-analysis-container {
  max-width: 100%;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 0.7fr 1.3fr;
  gap: 0.3rem;
  font-size: 0.7em;
  align-items: start;
}

/* Risk matrix scatter plot */
.risk-matrix-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.matrix-title {
  font-size: 1em;
  font-weight: 700;
  color: var(--accent-color);
  margin-bottom: 0.3rem;
  text-align: center;
}
.risk-matrix {
  position: relative;
  width: 100%;
  max-width: 430px;
  border: 2px solid rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  overflow: hidden;
  background: linear-gradient(135deg, rgba(45, 91, 255, 0.05), rgba(45, 91, 255, 0.02));
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}
.risk-matrix img {
  width: 100%;
  height: auto;
  display: block;
}

/* Risk details table */
.risk-details {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 0.8rem;
}
.detail-title {
  font-size: 1.05em;
  font-weight: 700;
  color: var(--accent-color);
  margin-bottom: 0.35rem;
  text-align: center;
}
.risk-table {
  width: 100%;
  font-size: 1em;
  border-collapse: collapse;
}
.risk-table th {
  background: rgba(45, 91, 255, 0.2);
  padding: 0.32rem 0.35rem;
  font-weight: 700;
  border: 1px solid rgba(255, 255, 255, 0.2);
  font-size: 0.95em;
}
.risk-table td {
  padding: 0.28rem 0.35rem;
  border: 1px solid rgba(255, 255, 255, 0.15);
  font-size: 0.95em;
  line-height: 1.3;
  white-space: nowrap;
}
.risk-table td:first-child {
  font-weight: 600;
  text-align: left;
}
.risk-table td {
  text-align: center;
}
.priority-high { color: var(--danger-color); font-weight: 700; }
.priority-medium { color: var(--warning-color); font-weight: 700; }
.priority-low { color: var(--success-color); font-weight: 700; }
</style>

<div class="risk-analysis-container">

<!-- Left: Risk Matrix Chart -->
<div class="risk-matrix-container">
<div class="matrix-title">Risk Matrix</div>
<div class="risk-matrix">
<img src="risk-matrix-en.svg" alt="Risk Matrix Chart" style="width: 100%; height: 100%;">
</div>
</div>

<!-- Right: Risk Details Table -->
<div class="risk-details">
<div class="detail-title">Smart Contract Risk Details</div>
<table class="risk-table">
<thead>
  <tr>
    <th>Risk Type</th>
    <th>Probability</th>
    <th>Impact</th>
    <th>Priority</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1. Strata Contract Vuln.</td>
    <td>Med</td>
    <td>High</td>
    <td class="priority-high">High</td>
  </tr>
  <tr>
    <td>2. Pendle AMM Vuln.</td>
    <td>Med</td>
    <td>Med-High</td>
    <td class="priority-medium">Med</td>
  </tr>
  <tr>
    <td>3. Oracle Attack</td>
    <td>Med-High</td>
    <td>High</td>
    <td class="priority-high">High</td>
  </tr>
  <tr>
    <td>4. Governance Attack</td>
    <td>Low</td>
    <td>Med</td>
    <td class="priority-low">Low</td>
  </tr>
  <tr>
    <td>5. Liquidity Risk</td>
    <td>Med</td>
    <td>Med</td>
    <td class="priority-medium">Med</td>
  </tr>
  <tr>
    <td>6. Regulatory Risk</td>
    <td>High</td>
    <td>Med-High</td>
    <td class="priority-high">High</td>
  </tr>
</tbody>
</table>
</div>

</div>

---

## Risk Factor Analysis (2/2)

### Market Risk

<!--
[Study Notes - Page 17: Risk Factor Analysis (2/2)]

Continued analysis of remaining 3 major risks:

4. Regulatory Risk (Medium probability/Medium impact)
- Position: Center area (yellow)
- Probability: Medium
  * Uncertain regulatory policies across countries
  * SEC's tough stance on DeFi
  * May suddenly introduce restrictive policies
- Impact: Medium
  * May lead to protocol closure or restricted access
  * Token price volatility
  * But won't directly cause fund loss (can exit early)
- Specific risks:
  * Protocol deemed unregistered securities
  * Team members prosecuted
  * Geographic restrictions (IP blocking)
  * Tax compliance requirements
- Mitigation measures:
  * Follow regulatory developments
  * Choose highly decentralized protocols
  * Maintain proper tax records
  * Diversify across multiple jurisdictions
- Real cases:
  * 2023 Tornado Cash sanctioned
  * 2023 Binance SEC settlement
  * EU MiCA regulation effective 2024

5. Market Volatility Risk (High probability/Medium impact)
- Position: Right center area (yellow)
- Probability: High
  * Crypto market extremely volatile
  * Frequent 50%+ corrections
  * Heavily influenced by macro economy
- Impact: Medium
  * Asset value fluctuates significantly
  * May trigger liquidations
  * But won't go to zero (except extreme cases)
- Specific manifestations:
  * Underlying asset price volatility
  * Yield rate changes dramatically
  * PT/YT prices swing wildly
- Mitigation measures:
  * Use stablecoin products
  * Set stop-losses
  * Don't over-leverage
  * Hold long-term, don't chase pumps/dumps
- Real cases:
  * 2022 bear market: ETH from $4800 to $880 (-82%)
  * March 2023 USDC depeg event
  * 2024 post-ETF approval volatility

6. Operational Risk (Low probability/Medium impact)
- Position: Left center area (green) - relatively safe
- Probability: Low
  * Mainly user operational errors
  * Can be avoided through learning
- Impact: Medium
  * May lose partial funds
  * But usually not total loss
- Specific risks:
  * Sending to wrong address (unrecoverable)
  * Signing malicious transactions
  * Private key leak
  * Phishing websites
  * Excessive approvals
- Mitigation measures:
  * Use hardware wallet
  * Carefully verify addresses
  * Don't click suspicious links
  * Regularly check approvals (Revoke.cash)
  * Small test before large transfers
- Real cases:
  * Users mistakenly send assets to contract addresses
  * Signing malicious approvals leads to theft
  * Private key leak leads to wallet drain

Risk Management Strategies:

1. Diversification
- Don't put all funds in single protocol
- Suggestion: Single protocol no more than 20% of total assets

2. Risk Tiering
- High-risk funds: 10-20% (Junior, YT, etc.)
- Medium-risk funds: 30-40% (LP, balanced products)
- Low-risk funds: 40-60% (Senior, PT, stablecoins)

3. Continuous Monitoring
- Regularly check protocol TVL changes
- Follow audit report updates
- Track community discussions
- Set price alerts

4. Contingency Plan
- Prepare quick exit strategy
- Understand emergency withdrawal process
- Keep portion of liquid funds

Key learning points:
- No zero-risk investment, only risk management
- Understand characteristics and mitigation for each risk
- Allocate assets according to your risk tolerance
- Continuously learn and monitor risk dynamics
-->

<style scoped>
.risk-grid {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 0.7rem;
  font-size: 0.8em;
  max-width: 94%;
  margin: 0 auto;
}
.risk-card {
  background: rgba(255, 107, 107, 0.1);
  border: 2px solid rgba(255, 107, 107, 0.3);
  border-radius: 8px;
  padding: 0.8rem;
  text-align: center;
}
.risk-card h4 {
  margin: 0 0 0.3rem 0;
  font-size: 1em;
  color: var(--danger-color);
  font-weight: 600;
}
.risk-card .level {
  font-size: 0.85em;
  margin: 0.2rem 0;
  opacity: 0.9;
}
.risk-card .desc {
  font-size: 0.8em;
  margin-top: 0.3rem;
  opacity: 0.8;
  line-height: 1.3;
}
.risk-card.medium {
  background: rgba(255, 152, 0, 0.1);
  border-color: rgba(255, 152, 0, 0.3);
}
.risk-card.medium h4 { color: var(--warning-color); }
</style>

<div class="risk-grid">
<div class="risk-card medium">

#### Liquidity Drain
<div class="level">DeFi Medium Risk</div>
<div class="desc">Insufficient liquidity in extreme markets</div>

</div>
<div class="risk-card">

#### Underlying Asset Volatility
<div class="level">DeFi High Risk</div>
<div class="desc">Crypto asset price volatility</div>

</div>
<div class="risk-card medium">

#### Bank Run Risk
<div class="level">DeFi Med-High Risk</div>
<div class="desc">Mass redemptions cause system stress</div>

</div>
</div>

---

## Investment Strategy Recommendations

<!--
[Study Notes - Page 18: Investment Strategy Recommendations]

Investment strategies based on risk preference:

1. Conservative Investor Strategy

Goal: Capital preservation, stable returns
Risk tolerance: Low, max drawdown <5%
Expected returns: 4-6% APY

Asset allocation:
- Strata Senior 40%
  * Priority protection, lowest risk
  * Expected returns: 4-6% APY
  * Suitable for: Pension funds, conservative investors

- Pendle PT 30%
  * Lock in fixed returns
  * Expected returns: 3-5% APY
  * Suitable for: Seeking stable cash flows

- TradFi Structured Notes 20%
  * Principal protected products
  * Expected returns: 2-4% APY
  * Suitable for: Risk diversification, compliance

- Cash/Stablecoins 10%
  * Liquidity reserve
  * Emergency funds
  * Opportunity fund (buy dips during panic)

Operational advice:
- Hold long-term, don't trade frequently
- Regularly check protocol security
- Avoid using leverage
- Diversify across 3-5 protocols

Risk warning:
- Even conservative strategy has smart contract risk
- Consider DeFi insurance (e.g., Nexus Mutual)
- Don't invest more than 30% of total assets in DeFi

---

2. Balanced Investor Strategy

Goal: Balance risk and returns
Risk tolerance: Medium, max drawdown 10-15%
Expected returns: 8-12% APY

Asset allocation:
- Strata Senior 30%
  * Stable yield foundation
  * Expected returns: 4-6% APY

- Pendle PT 25%
  * Fixed income portion
  * Expected returns: 3-5% APY

- Strata Junior 20%
  * Enhanced returns
  * Expected returns: 12-18% APY
  * Assumes some risk

- Pendle YT 15%
  * Leveraged yield exposure
  * Expected returns: 15-25% APY
  * High risk, high reward

- Cash Reserve 10%
  * Liquidity management
  * Rebalancing funds

Operational advice:
- Rebalance quarterly
- Adjust allocation based on market conditions
  * Bull market: Increase Junior/YT proportion
  * Bear market: Increase Senior/PT proportion
- Use portion of returns to buy DeFi insurance
- Watch for new yield opportunities

Rebalancing strategy:
- Rebalance when any asset deviates ±5% from target
- Example: Junior rises from 20% to 26%, sell some to Senior

Risk management:
- Set stop-loss: Consider exit when Junior/YT drops 20%
- Diversify across 5-8 protocols
- Regularly check audit reports

---

3. Aggressive Investor Strategy (not shown on slide, but important)

Goal: Pursue high returns
Risk tolerance: High, can handle 30%+ drawdown
Expected returns: 15-30% APY

Asset allocation:
- Strata Junior 40%
  * Leveraged yields
  * Expected returns: 15-25% APY

- Pendle YT 30%
  * Yield rate trading
  * Expected returns: 20-40% APY

- LP Liquidity Provision 20%
  * Fees + incentives
  * Expected returns: 10-20% APY

- Cash Reserve 10%
  * Dip buying fund

Operational advice:
- Active trading, capture market opportunities
- Use leverage (cautiously)
- Monitor yield curve changes
- Quick stop-loss

Risk warning:
- May lose most of principal
- Requires professional knowledge and experience
- Not suitable for beginners
- Only use money you can afford to lose

---

Universal Investment Principles:

1. Diversification
- Don't all-in single protocol
- Spread across multiple product types
- Spread across multiple blockchains

2. Continuous Learning
- Understand product mechanics
- Follow protocol updates
- Learn risk management

3. Long-term Perspective
- Don't be affected by short-term volatility
- Power of compound interest
- Patiently wait for opportunities

4. Risk Management
- Only invest in products you understand
- Set stop-losses
- Regularly check and rebalance

Key learning points:
- Choose strategy based on your risk tolerance
- No "best" strategy, only "most suitable" strategy
- Adjust strategy when market conditions change
- Risk management more important than chasing high returns
-->

<style scoped>
.strategy-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.6rem;
  font-size: 0.78em;
  margin: 0.3rem auto 0 auto;
  max-width: 94%;
}
.strategy-card {
  background: linear-gradient(135deg, rgba(45, 91, 255, 0.15), rgba(45, 91, 255, 0.05));
  border: 2px solid;
  border-radius: 6px;
  padding: 0.5rem;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.15);
}
.strategy-card.conservative {
  border-color: var(--success-color);
  box-shadow: 0 3px 10px rgba(76, 175, 80, 0.2);
}
.strategy-card.balanced {
  border-color: var(--warning-color);
  box-shadow: 0 3px 10px rgba(255, 152, 0, 0.2);
}
.strategy-card h3 {
  margin: 0 0 0.35rem 0;
  font-size: 1.05em;
  font-weight: 700;
  text-align: center;
}
.strategy-card.conservative h3 { color: var(--success-color); }
.strategy-card.balanced h3 { color: var(--warning-color); }

.allocation {
  background: rgba(0, 0, 0, 0.3);
  padding: 0.4rem;
  margin: 0.3rem 0;
  border-radius: 5px;
  border-left: 3px solid var(--accent-color);
}
.allocation-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0.2rem 0;
  padding: 0.15rem 0;
}
.allocation-label {
  font-size: 0.95em;
  opacity: 0.9;
}
.allocation-value {
  font-size: 1.15em;
  font-weight: 700;
  color: var(--accent-color);
}

.metrics-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.35rem;
  margin-top: 0.4rem;
}
.metric-box {
  background: rgba(255, 255, 255, 0.05);
  padding: 0.3rem;
  border-radius: 4px;
  text-align: center;
  border: 2px solid rgba(255, 255, 255, 0.1);
}
.metric-label {
  font-size: 0.85em;
  opacity: 0.8;
  margin-bottom: 0.15rem;
}
.metric-value {
  font-size: 1.25em;
  font-weight: 700;
  color: var(--accent-color);
}
.metric-box.return { border-color: var(--success-color); }
.metric-box.risk { border-color: var(--danger-color); }
</style>

<div class="strategy-grid">
<div class="strategy-card conservative">

### Conservative Investor

<div class="allocation">
<div class="allocation-item">
  <span class="allocation-label">Strata Senior</span>
  <span class="allocation-value">40%</span>
</div>
<div class="allocation-item">
  <span class="allocation-label">Pendle Fixed</span>
  <span class="allocation-value">30%</span>
</div>
<div class="allocation-item">
  <span class="allocation-label">TradFi Notes</span>
  <span class="allocation-value">20%</span>
</div>
<div class="allocation-item">
  <span class="allocation-label">Cash/Stablecoins</span>
  <span class="allocation-value">10%</span>
</div>
</div>

<div class="metrics-grid">
<div class="metric-box return">
  <div class="metric-label">Expected Return</div>
  <div class="metric-value">4-6%</div>
</div>
<div class="metric-box risk">
  <div class="metric-label">Max Drawdown</div>
  <div class="metric-value">&lt;5%</div>
</div>
</div>

</div>
<div class="strategy-card balanced">

### Balanced Investor

<div class="allocation">
<div class="allocation-item">
  <span class="allocation-label">Strata Senior</span>
  <span class="allocation-value">30%</span>
</div>
<div class="allocation-item">
  <span class="allocation-label">Pendle Fixed</span>
  <span class="allocation-value">25%</span>
</div>
<div class="allocation-item">
  <span class="allocation-label">Strata Junior</span>
  <span class="allocation-value">20%</span>
</div>
<div class="allocation-item">
  <span class="allocation-label">Pendle Leveraged</span>
  <span class="allocation-value">15%</span>
</div>
<div class="allocation-item">
  <span class="allocation-label">Cash Reserve</span>
  <span class="allocation-value">10%</span>
</div>
</div>

<div class="metrics-grid">
<div class="metric-box return">
  <div class="metric-label">Expected Return</div>
  <div class="metric-value">8-12%</div>
</div>
<div class="metric-box risk">
  <div class="metric-label">Max Drawdown</div>
  <div class="metric-value">10-15%</div>
</div>
</div>

</div>
</div>

---

## Future Development Trends

<!--
[Study Notes - Page 19: Future Development Trends]
(Updated: March 2026)

Industry landscape as of 2026:

1. RWA Integration - NOW MATURING

Current state (2026):
- Tokenized US Treasuries: $15B+ on-chain (Ondo, Backed, OpenEden)
- Real estate tokenization gaining traction (RealT, Landshare)
- Structured products combining RWA yields with DeFi tranching

Achievements since 2024:
- Regulatory clarity in EU (MiCA), Singapore, UAE
- Major custodians offering tokenized asset services
- Integration with Pendle/Strata-style protocols

Next steps (2027+):
- Corporate bond tokenization at scale
- Cross-border RWA settlement
- Institutional-grade RWA structured products

---

2. Cross-chain Interoperability - ESTABLISHED

Current state (2026):
- LayerZero, Wormhole, Chainlink CCIP widely adopted
- Unified liquidity pools across L2s
- Cross-chain PT/YT trading standard

What was achieved (2024-2025):
- Major bridge security improvements post-2022 exploits
- Native cross-chain structured product deployment
- Gas optimization via L2 aggregation

---

3. AI-Driven Risk Management - NOW ACTIVE

Current state (2026):
- AI agents managing yield optimization strategies
- Real-time risk parameter adjustment
- Predictive analytics for yield curve modeling

Key deployments:
- AI-powered robo-advisors for DeFi yield products
- Automated Senior/Junior ratio rebalancing
- On-chain ML models for credit scoring

Next frontier (2027+):
- Autonomous protocol governance
- AI-generated structured product design
- Personalized risk profiling at scale

---

4. Regulatory Compliant Products - FRAMEWORK EMERGING

Current state (2026):
- MiCA in effect in EU (since Jan 2025)
- Singapore MAS licensed DeFi products
- US still evolving but clearer guidance emerging

Compliant DeFi models now live:
- Permissioned pools with KYC (Aave Arc successors)
- Hybrid on-chain/off-chain compliance layers
- Institutional DeFi platforms (Fireblocks, Anchorage integrations)

---

5. Complex Structured Products - GROWING

Current state (2026):
- Multi-layer tranching (Senior/Mezzanine/Junior) available
- Conditional trigger products in production
- Strata + Pendle combo products emerging

Innovations deployed:
- Embedded options in yield products
- Principal-protected DeFi vaults
- Dynamic yield allocation based on market conditions

---

Market Status (as of Q1 2026):

2024-2025 (COMPLETED):
✓ Cross-chain infrastructure matured
✓ Initial RWA integration successful
✓ AI tools began deployment
✓ MiCA and regional frameworks enacted

2026 (CURRENT):
→ Institutional adoption accelerating
→ DeFi structured product TVL: ~$45B
→ AI-driven strategies becoming standard
→ RWA-DeFi convergence underway

2027+ (PROJECTED):
- TVL target: $100B+
- Full TradFi-DeFi product parity
- Mainstream retail access via compliant rails
- Quantum-safe cryptography integration begins

Key insights:
- DeFi structured products have moved past early stage
- Institutional participation is now real, not theoretical
- Regulatory clarity is enabling, not hindering, growth
- AI and RWA are the current growth drivers
-->

<style scoped>
.trend-container {
  max-width: 94%;
  margin: 0.3rem auto 0 auto;
}
.timeline {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.5rem;
  font-size: 0.8em;
  margin-bottom: 0.3rem;
}
.timeline-phase {
  background: linear-gradient(135deg, rgba(45, 91, 255, 0.15), rgba(45, 91, 255, 0.05));
  border: 2px solid;
  border-radius: 6px;
  padding: 0.45rem;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.15);
  position: relative;
}
.timeline-phase.past {
  border-color: #6b7280;
  box-shadow: 0 3px 10px rgba(107, 114, 128, 0.2);
  opacity: 0.85;
}
.timeline-phase.current {
  border-color: var(--success-color);
  box-shadow: 0 3px 10px rgba(76, 175, 80, 0.3);
  background: linear-gradient(135deg, rgba(76, 175, 80, 0.2), rgba(76, 175, 80, 0.08));
}
.timeline-phase.near {
  border-color: var(--info-color);
  box-shadow: 0 3px 10px rgba(33, 150, 243, 0.2);
}
.timeline-phase.future {
  border-color: var(--purple-color);
  box-shadow: 0 3px 10px rgba(156, 39, 176, 0.2);
}
.timeline-phase h4 {
  margin: 0 0 0.25rem 0;
  font-size: 1.2em;
  font-weight: 700;
  text-align: center;
}
.timeline-phase.past h4 { color: #9ca3af; }
.timeline-phase.current h4 { color: var(--success-color); }
.timeline-phase.near h4 { color: var(--info-color); }
.timeline-phase.future h4 { color: var(--purple-color); }
.timeline-phase strong {
  display: block;
  margin-bottom: 0.25rem;
  font-size: 0.95em;
  color: var(--accent-color);
  text-align: center;
}
.timeline-phase p {
  margin: 0.15rem 0;
  font-size: 0.9em;
  line-height: 1.35;
  opacity: 0.9;
}

.innovations {
  background: linear-gradient(135deg, rgba(241, 196, 15, 0.15), rgba(241, 196, 15, 0.05));
  border: 2px solid var(--accent-color);
  border-radius: 6px;
  padding: 0.5rem;
  font-size: 0.78em;
  box-shadow: 0 3px 10px rgba(241, 196, 15, 0.2);
}
.innovations h3 {
  font-size: 1.05em;
  margin: 0 0 0.3rem 0;
  color: var(--accent-color);
  font-weight: 700;
  text-align: center;
}
.innovations ol {
  line-height: 1.45;
  margin: 0.2rem 0;
  padding-left: 1.5em;
}
.innovations li {
  margin: 0.2rem 0;
  font-size: 0.95em;
}
.innovations li strong {
  color: var(--accent-color);
  font-weight: 700;
}
</style>

<div class="trend-container">
<div class="timeline">
<div class="timeline-phase past">

#### 2024-25
Foundation
<p>• Cross-chain matured</p>
<p>• RWA protocols launched</p>
<p>• Basic AI tools emerged</p>

</div>
<div class="timeline-phase current">

#### 2026
Current State
<p>• AI-driven strategies</p>
<p>• RWA-DeFi integration</p>
<p>• Regulatory frameworks</p>

</div>
<div class="timeline-phase near">

#### 2027
Institutional Wave
<p>• Major TradFi adoption</p>
<p>• Compliant DeFi products</p>
<p>• $100B+ TVL target</p>

</div>
<div class="timeline-phase future">

#### 2028+
Mainstream
<p>• Full TradFi convergence</p>
<p>• Quantum-safe protocols</p>
<p>• Global retail access</p>

</div>
</div>

<div class="innovations">

### Current Innovation Focus (2026)
1. AI-Powered Risk Engines: Real-time dynamic yield optimization
2. RWA Structured Products: Tokenized treasuries & real estate tranching
3. Compliant DeFi Rails: MiCA-ready, institutional-grade infrastructure

</div>
</div>

---

## Summary: Key Insights

<!--
[Study Notes - Page 20: Summary Key Insights]

Summary of core points from the presentation:

1. Technology Advantage is in DeFi

Core argument:
DeFi far surpasses TradFi in transparency, composability, and innovation speed

Specific manifestations:
- Transparency:
  * Smart contract code is open source
  * All transactions viewable on-chain
  * Pricing algorithms public
  * vs TradFi's black box operations

- Composability:
  * Strata output can be Pendle input
  * Infinite combination possibilities
  * "Financial Legos"
  * vs TradFi's closed systems

- Innovation speed:
  * Monthly iterations vs yearly iterations
  * Permissionless innovation
  * Community-driven
  * vs TradFi's regulatory constraints

Data support:
- Tech radar chart: DeFi leads in 4 of 5 dimensions
- Strata/Pendle transparency 95 vs TradFi 40
- DeFi innovation speed is 10-20x TradFi

Key learning points:
- DeFi's technical advantages are structural, not temporary
- These advantages will persist long-term
- Investing in DeFi is investing in technological progress

---

2. Regulatory Advantage is in TradFi

Core argument:
TradFi has clear advantages in regulatory certainty and investor protection

Specific manifestations:
- Regulatory certainty:
  * Mature legal framework
  * Clear compliance requirements
  * Predictable regulatory environment
  * vs DeFi's regulatory vacuum

- Investor protection:
  * Deposit insurance (FDIC)
  * Investor compensation funds
  * Regulatory oversight
  * Legal recourse mechanisms
  * vs DeFi's "at your own risk"

- Institutional trust:
  * Decades of operational history
  * Brand reputation
  * Central bank backstop for systemic risk
  * vs DeFi's emerging nature

Risk comparison:
- TradFi: Credit risk, operational risk
- DeFi: Smart contract risk, regulatory risk

Key learning points:
- Regulation isn't bad, it's necessary to protect investors
- DeFi needs to find balance between innovation and compliance
- Future may be hybrid: DeFi technology + TradFi regulation

---

3. Convergence is the Future

Core argument:
The biggest opportunity is in DeFi-TradFi convergence, not opposition

Convergence directions:

a) RWA (Real World Assets) Integration
- Tokenize traditional assets
- Trade in DeFi
- Examples:
  * Treasury tokenization → Pendle yield separation
  * Real estate tokenization → Strata risk tranching
  * Corporate bonds → DeFi liquidity pools

b) Hybrid Products
- DeFi technology + TradFi assets
- On-chain transparency + off-chain compliance
- Examples:
  * Permissioned DeFi
  * Compliant stablecoin yield products
  * Institutional DeFi infrastructure

c) RegTech
- Using blockchain to meet regulatory requirements
- Automated compliance reporting
- On-chain KYC/AML verification

Market opportunity:
- RWA market size: Trillions of dollars
- Bridge for institutional capital into DeFi
- New yield sources

Timeline:
- 2024-2025: Initial RWA implementation
- 2026-2027: Hybrid products mature
- 2028-2030: Deep integration

Key learning points:
- Don't view DeFi and TradFi as adversaries
- Convergence is the biggest opportunity
- Follow RWA sector development

---

4. Risk Must Be Managed

Core argument:
Smart contract risk is DeFi's biggest challenge, must be taken seriously

Risk hierarchy:
1. Smart Contract Risk (highest priority)
   - Can cause total loss of funds
   - Cannot be recovered
   - Need: Audits, diversification, insurance

2. Liquidity Risk (high priority)
   - May not be able to exit
   - Need: Choose high TVL protocols

3. Market Volatility Risk (medium priority)
   - Asset value fluctuations
   - Need: Long-term holding, avoid excessive leverage

4. Regulatory Risk (medium priority)
   - Policy uncertainty
   - Need: Follow developments, diversify jurisdictions

Risk management framework:
- Diversify: No more than 20% in single protocol
- Risk grading: High/medium/low risk asset allocation
- Continuous monitoring: Regularly check audits, TVL
- Contingency plan: Prepare quick exit strategy

Insurance options:
- Nexus Mutual
- InsurAce
- Unslashed Finance

Key learning points:
- High returns inevitably come with high risks
- Risk management more important than chasing returns
- Never invest money you can't afford to lose
- Continuous learning and vigilance

---

Strategic Recommendations (3 time horizons):

Short-term (6-12 months): Learn and pilot
- Goal: Understand product mechanics, small-scale testing
- Actions:
  1. Deep dive into Strata, Pendle mechanics
  2. Small investment ($100-1000), experience products
  3. Establish risk assessment framework
  4. Follow audit reports and community discussions
- Capital allocation: 5-10% of total assets
- Expected outcome: Gain experience, avoid major losses

Medium-term (1-3 years): Increase allocation, develop hybrid products
- Goal: Expand DeFi investment, participate in RWA opportunities
- Actions:
  1. Increase DeFi structured products to 20-30%
  2. Follow RWA projects (e.g., Ondo, Maple)
  3. Participate in liquidity provision, earn extra returns
  4. Consider DeFi insurance
- Capital allocation: 20-30% of total assets
- Expected outcome: Stable returns, capture RWA opportunities

Long-term (3-5 years): Build complete product matrix, achieve convergence
- Goal: DeFi becomes significant part of portfolio
- Actions:
  1. Build diversified DeFi portfolio
  2. Participate in governance, influence protocol development
  3. Follow regulatory compliant products
  4. Consider institutional DeFi products
- Capital allocation: 30-50% of total assets
- Expected outcome: DeFi becomes mainstream, long-term compound returns

---

Final Summary:

DeFi structured products value proposition:
✅ Clear technology advantages (transparent, composable, fast innovation)
✅ Lower entry barriers (from $100K to $10)
✅ Improved capital efficiency (tokenization, liquidity)
✅ Create new yield opportunities

Challenges:
⚠️ Smart contract risk
⚠️ Regulatory uncertainty
⚠️ User experience barriers
⚠️ Market volatility

Investment advice:
1. Long-term bullish on DeFi structured products
2. Short-term caution, small-scale testing
3. Prioritize risk management
4. Follow RWA and regulatory compliant products
5. Continuous learning, stay vigilant

Remember:
- This is a high-risk, high-reward emerging field
- Only invest in products you understand
- Only invest money you can afford to lose
- Risk management always comes first

Key learning points:
- These 4 insights are the essence of the presentation
- Understand the balance between tech advantages and regulatory challenges
- Convergence is the future, not opposition
- Risk management is the key to success
-->

<style scoped>
.summary-container {
  max-width: 94%;
  margin: 0 auto;
}
.insight-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.45rem;
  margin-bottom: 0.4rem;
}
.insight {
  background: linear-gradient(135deg, rgba(45, 91, 255, 0.15), rgba(45, 91, 255, 0.05));
  border: 2px solid;
  border-radius: 6px;
  padding: 0.4rem 0.5rem;
  font-size: 0.75em;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.15);
}
.insight.tech {
  border-color: var(--info-color);
  box-shadow: 0 3px 10px rgba(33, 150, 243, 0.2);
}
.insight.regulation {
  border-color: #95A5A6;
  box-shadow: 0 3px 10px rgba(149, 165, 166, 0.2);
}
.insight.future {
  border-color: var(--success-color);
  box-shadow: 0 3px 10px rgba(76, 175, 80, 0.2);
}
.insight.risk {
  border-color: var(--warning-color);
  box-shadow: 0 3px 10px rgba(255, 152, 0, 0.2);
}
.insight h4 {
  margin: 0 0 0.2rem 0;
  font-size: 1.05em;
  font-weight: 700;
  text-align: center;
}
.insight.tech h4 { color: var(--info-color); }
.insight.regulation h4 { color: #95A5A6; }
.insight.future h4 { color: var(--success-color); }
.insight.risk h4 { color: var(--warning-color); }
.insight p {
  margin: 0;
  line-height: 1.35;
  opacity: 0.9;
  font-size: 0.95em;
  text-align: center;
}

.recommendations {
  background: linear-gradient(135deg, rgba(241, 196, 15, 0.15), rgba(241, 196, 15, 0.05));
  border: 2px solid var(--accent-color);
  border-radius: 6px;
  padding: 0.45rem 0.6rem;
  font-size: 0.82em;
  box-shadow: 0 3px 10px rgba(241, 196, 15, 0.2);
}
.recommendations h3 {
  margin: 0 0 0.3rem 0;
  font-size: 1.1em;
  font-weight: 700;
  color: var(--accent-color);
  text-align: center;
}
.recommendations ol {
  margin: 0.2rem 0;
  padding-left: 1.3em;
  line-height: 1.45;
}
.recommendations li {
  margin: 0.2rem 0;
  font-size: 1em;
}
.recommendations strong {
  color: var(--accent-color);
  font-weight: 700;
}
</style>

<div class="summary-container">
<div class="insight-grid">
<div class="insight tech">

#### Tech Advantage in DeFi
<p>Leading in transparency, composability, innovation speed</p>

</div>
<div class="insight regulation">

#### Regulatory Advantage in TradFi
<p>Strong regulatory certainty, investor protection</p>

</div>
<div class="insight future">

#### Convergence is the Future
<p>Biggest opportunity in hybrid products</p>

</div>
<div class="insight risk">

#### Risk Must Be Managed
<p>Smart contract risk is the biggest challenge</p>

</div>
</div>

<div class="recommendations">

### Strategic Recommendations
1. **Short-term (6-12mo):** Pilot with small allocations, build evaluation framework
2. **Medium-term (1-3yr):** Scale DeFi exposure, explore hybrid RWA products
3. **Long-term (3-5yr):** Full portfolio integration, achieve TradFi-DeFi convergence

</div>
</div>

---

## Questions & Discussion

<!--
[Study Notes - Page 21: Questions & Discussion]

Purpose of this page:
- Guide audience questions
- Present common Q&A
- Deepen understanding of key concepts
- Facilitate interactive discussion

6 common questions and detailed answers:

1. Technical Question: How is smart contract security ensured?

Background:
This is the most frequently asked question, as smart contract vulnerabilities are DeFi's biggest risk.

Standard answer:
- Multiple audits:
  * Both Strata and Pendle audited by top audit firms
  * Auditors: Certik, Trail of Bits, OpenZeppelin, etc.
  * Re-audited after each major update

- Bug Bounty programs:
  * High rewards attract white hat hackers
  * Hosted on Immunefi platform
  * Up to $1M rewards

- Timelock and multisig:
  * Critical operations have 24-48 hour timelock
  * Multisig wallets control key parameters
  * Community can monitor

- Formal verification:
  * Mathematical proofs of code correctness
  * Critical modules formally verified

Additional notes:
- Even with these measures, 100% security cannot be guaranteed
- Recommend DeFi insurance as additional protection
- Diversify, don't all-in on single protocol

---

2. Regulatory Question: Are DeFi products legal?

Background:
Regulatory uncertainty is one of investors' biggest concerns.

Standard answer:
- Current state:
  * Most countries have not enacted clear legislation
  * In regulatory gray area
  * Different jurisdictions have different attitudes

- USA:
  * SEC takes hard stance, considers some DeFi tokens securities
  * CFTC considers crypto as commodities
  * Regulatory framework in development

- EU:
  * MiCA regulation effective 2024
  * Relatively friendly and clear
  * Provides compliance path for DeFi

- Asia:
  * Singapore, Hong Kong relatively open
  * Mainland China banned
  * Japan has clear licensing system

Investment advice:
- Follow regulatory developments
- Choose compliance-conscious protocols
- Keep tax records
- Consider using VPN and decentralized frontends

---

3. Investment Question: How should regular investors start?

Background:
New investors often don't know where to begin.

Standard answer - 5-step method:

Step 1: Learn basics (1-2 weeks)
- Understand blockchain, DeFi fundamentals
- Learn wallet usage (MetaMask, etc.)
- Understand gas fees, transaction confirmations
- Recommended resources:
  * Binance Academy
  * CoinGecko Learn
  * YouTube tutorials

Step 2: Prepare tools (1 week)
- Install MetaMask wallet
- Buy small amount of ETH (for gas)
- Understand DEXs (like Uniswap)
- Learn to use block explorers

Step 3: Small-scale testing ($100-500)
- Choose 1-2 protocols
- Invest in conservative products (Senior, PT)
- Experience complete process
- Record all operations

Step 4: Risk assessment (ongoing)
- Check audit reports
- Review TVL and user count
- Follow community discussions
- Set price alerts

Step 5: Gradually expand (after 3-6 months)
- Adjust strategy based on experience
- Increase investment amounts
- Try different products
- Build portfolio

Key principles:
- Only invest in products you understand
- Only invest money you can afford to lose
- Start small
- Continuous learning

---

4. Product Question: What's the difference between Strata and Pendle?

Background:
Many people confuse the functions of these two products.

Standard answer - Core differences:

Strata: Risk Tranching Engine
- Function: Separates risk into Senior/Junior
- Analogy: Like mortgage priority/subordinated debt
- Suitable for: Investors with different risk preferences
- Yield source: Redistribution of underlying asset returns
- Key innovation: Dynamic risk adjustment

Pendle: Yield Tokenization Platform
- Function: Separates yield into PT/YT
- Analogy: Like separating bond principal and interest
- Suitable for: Investors with different yield expectations
- Yield source: Yield rate trading
- Key innovation: Yield marketplace

Can be used together:
- First use Strata for tranching
- Then use Pendle for yield separation
- Create more complex products

Memory tip:
- Strata = Separate risk (vertical layers)
- Pendle = Separate yield (present/future)

---

5. Yield Question: Why are DeFi yields so high?

Background:
Many question the sustainability of high yields.

Standard answer - Yield source analysis:

Legitimate yield sources:
1. Protocol real revenue:
   - Trading fees
   - Lending interest
   - Liquidation penalties
   - These are sustainable

2. Improved capital efficiency:
   - Remove intermediaries
   - Automation reduces costs
   - 24/7 operation
   - Global liquidity pools

3. Early growth dividends:
   - Market still growing rapidly
   - Competition not yet full
   - Many efficiency arbitrage opportunities

Unsustainable yield sources (beware):
1. Token incentives:
   - Protocol distributes governance tokens
   - Token price drops affect yields
   - Incentives may end

2. Ponzi structures:
   - New money pays old yields
   - Unsustainable
   - Need to be cautious (e.g., Terra/Luna)

Evaluation methods:
- Check protocol real revenue
- Understand yield composition
- Be cautious of excessive yields (>50% APY needs scrutiny)
- Monitor TVL trends

Reasonable expectations:
- Stablecoin products: 3-8% APY
- Risk-tranched products: 5-15% APY
- High-risk products: 15-30% APY
- Over 30% requires extra caution

---

6. Risk Question: What's the worst case scenario?

Background:
Investors need to understand maximum risk.

Standard answer - Worst case analysis:

Scenario 1: Smart contract hack
- Probability: Medium (has happened multiple times historically)
- Consequence: Total loss of funds
- Mitigation: Audits, insurance, diversification
- Historical case: Poly Network $611M

Scenario 2: Protocol shut down by regulators
- Probability: Medium
- Consequence: Cannot access, but funds may be withdrawable
- Mitigation: Monitor regulation, use decentralized frontends
- Historical case: Tornado Cash

Scenario 3: Extreme market volatility
- Probability: High (common in crypto markets)
- Consequence: Significant asset value decline, possible liquidation
- Mitigation: Avoid excessive leverage, hold long-term
- Historical case: 2022 bear market ETH -82%

Scenario 4: Liquidity exhaustion
- Probability: Medium (during panic)
- Consequence: Cannot exit or massive slippage
- Mitigation: Choose high TVL protocols
- Historical case: UST depeg event

Scenario 5: Rug pull
- Probability: Low (for established protocols)
- Consequence: Total loss of funds
- Mitigation: Choose highly decentralized protocols
- Historical case: Various small DeFi projects

Risk management recommendations:
- Invest max 20-30% of total assets in DeFi
- Single protocol max 10%
- Purchase DeFi insurance
- Maintain liquidity reserves
- Regular review and rebalancing

---

How to handle Q&A session:

1. Encourage questions:
- "Any questions?"
- "These 6 are common questions, do you have others?"
- Maintain open and friendly attitude

2. Answering techniques:
- First understand the question, repeat if needed
- Explain complex concepts in simple terms
- Use analogies and examples
- Acknowledge uncertainty (don't pretend to know)

3. Time management:
- Reserve 10-15 minutes for Q&A
- Keep each question to 2-3 minutes
- Complex questions can be discussed after

4. Guide discussion:
- If no one asks, say: "Many people ask..."
- Invite experienced audience to share views
- Facilitate exchange among audience

Key learning points:
- Prepare answers for these 6 questions
- Understand concerns behind each question
- Practice explaining in simple terms
- Stay honest, acknowledge risks and uncertainties
-->

<style scoped>
.qa-container {
  max-width: 94%;
  margin: 0.3rem auto 0 auto;
}
.qa-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.5rem;
  font-size: 0.82em;
}
.qa-card {
  background: linear-gradient(135deg, rgba(45, 91, 255, 0.15), rgba(45, 91, 255, 0.05));
  border: 2px solid;
  border-radius: 6px;
  padding: 0.5rem;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.15);
  display: flex;
  flex-direction: column;
}
.qa-card.tech {
  border-color: var(--danger-color);
  box-shadow: 0 3px 10px rgba(255, 107, 107, 0.2);
}
.qa-card.regulation {
  border-color: var(--info-color);
  box-shadow: 0 3px 10px rgba(33, 150, 243, 0.2);
}
.qa-card.sustainability {
  border-color: var(--warning-color);
  box-shadow: 0 3px 10px rgba(255, 152, 0, 0.2);
}
.qa-card.adoption {
  border-color: var(--success-color);
  box-shadow: 0 3px 10px rgba(76, 175, 80, 0.2);
}
.qa-card.competition {
  border-color: var(--purple-color);
  box-shadow: 0 3px 10px rgba(156, 39, 176, 0.2);
}
.qa-number {
  position: absolute;
  top: 0.3rem;
  right: 0.3rem;
  width: 1.8em;
  height: 1.8em;
  border-radius: 50%;
  background: rgba(0, 0, 0, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.9em;
  font-weight: 700;
  color: var(--accent-color);
  border: 2px solid var(--accent-color);
}
.qa-card {
  position: relative;
}
.qa-question {
  font-size: 1.05em;
  font-weight: 700;
  margin-bottom: 0.3rem;
}
.qa-card.tech .qa-question { color: var(--danger-color); }
.qa-card.regulation .qa-question { color: var(--info-color); }
.qa-card.sustainability .qa-question { color: var(--warning-color); }
.qa-card.adoption .qa-question { color: var(--success-color); }
.qa-card.competition .qa-question { color: var(--purple-color); }
.qa-content {
  font-size: 1em;
  line-height: 1.5;
  opacity: 0.9;
  flex: 1;
}
</style>

<div class="qa-container">
<div class="qa-grid">

<div class="qa-card tech">
<div class="qa-number">1</div>
<div class="qa-question">Technical Risk</div>
<div class="qa-content">How to assess and manage smart contract risk?</div>
</div>

<div class="qa-card regulation">
<div class="qa-number">2</div>
<div class="qa-question">Regulatory Path</div>
<div class="qa-content">What's the compliance path for DeFi structured products?</div>
</div>

<div class="qa-card sustainability">
<div class="qa-number">3</div>
<div class="qa-question">Yield Sustainability</div>
<div class="qa-content">Are current high yields sustainable?</div>
</div>

<div class="qa-card adoption">
<div class="qa-number">4</div>
<div class="qa-question">Institutional Adoption</div>
<div class="qa-content">When will traditional institutions enter at scale?</div>
</div>

<div class="qa-card competition">
<div class="qa-number">5</div>
<div class="qa-question">Competitive Landscape</div>
<div class="qa-content">Are Strata and Pendle competitors or complements?</div>
</div>

<div class="qa-card tech" style="border-color: var(--accent-color); box-shadow: 0 3px 10px rgba(241, 196, 15, 0.2);">
<div class="qa-question" style="color: var(--accent-color);">Ask Questions</div>
<div class="qa-content" style="text-align: center; font-size: 1.1em; font-weight: 600; color: var(--accent-color);">Looking forward to in-depth discussion</div>
</div>

</div>
</div>

---

<!-- _class: lead -->

<style scoped>
.contact-container {
  text-align: center;
  max-width: 90%;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 80%;
}
.contact-title {
  font-size: 2.4em;
  font-weight: 700;
  margin-bottom: 0.5rem;
  color: var(--text-primary);
  letter-spacing: -0.02em;
}
.contact-subtitle {
  font-size: 1.15em;
  margin-bottom: 1.8rem;
  color: var(--text-secondary);
  font-weight: 400;
  font-style: italic;
}
.section-title {
  color: var(--accent-color);
  font-weight: 600;
  font-size: 1.1em;
  letter-spacing: 0.05em;
  text-align: center;
  text-transform: uppercase;
  margin-bottom: 0.8rem;
}
.qrcode-image {
  width: 180px;
  height: 180px;
  border: 1px solid var(--border-default);
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
  background: white;
  padding: 10px;
}
</style>

<div class="contact-container">
<div class="contact-title">Thank You</div>
<div class="contact-subtitle">Looking forward to further discussion</div>

<div class="section-title">Scan to Connect</div>
<img src="qrcode.jpg" alt="WeChat QR Code" class="qrcode-image">
</div>

---

<!-- _class: lead -->

<!--
[Study Notes - Page 22: Thank You]

Purpose of this page:
- Conclude the presentation
- Leave lasting impression
- Provide contact information
- Encourage follow-up communication

Closing remarks key points:

1. Core message recap (30 seconds)

At closing, briefly reiterate 3 most important points:

Point 1: DeFi structured products are at the frontier of financial innovation
- Combines TradFi's mature concepts with DeFi's technical advantages
- Provides investors unprecedented flexibility and transparency
- This is a sector worth long-term attention

Point 2: Opportunity and risk coexist
- High returns come with high risks
- Smart contract risk is the biggest challenge
- Risk management more important than chasing returns

Point 3: Start small, continuous learning
- Don't rush into large investments
- Understand mechanisms first, then invest
- This field changes rapidly, requires continuous learning

---

2. Call to Action

Give audience clear next steps:

Immediate actions:
- Visit Strata and Pendle websites, read documentation
- Join Discord/Telegram communities
- Follow Twitter for latest updates
- Read audit reports

Short-term (1-2 weeks):
- Set up MetaMask wallet
- Buy small amount of ETH for testing
- Experience products on testnet
- Small investment ($100-500) to test

Medium-term (1-3 months):
- Adjust strategy based on experience
- Gradually increase investment
- Participate in community discussions
- Share learning insights

---

3. Contact and Resources

Speaker contact:
- WeChat: Scan QR code
- Email: [provide email]
- Twitter: [provide handle]
- LinkedIn: [provide link]

Recommended learning resources:

Official documentation:
- Strata Protocol: docs.strata.xyz
- Pendle Finance: docs.pendle.finance

Communities:
- Discord: [link]
- Telegram: [link]
- Twitter: @StrataProtocol, @pendle_fi

Learning platforms:
- Binance Academy
- CoinGecko Learn
- DeFi Pulse
- The Defiant

Data analytics:
- DeFi Llama (TVL data)
- Dune Analytics (on-chain data)
- Token Terminal (protocol revenue)

Audit reports:
- Certik
- Trail of Bits
- OpenZeppelin

---

4. Thank you message

Standard thank you template:

"Thank you for listening and participating!

Today we explored the exciting field of DeFi structured products together. From Strata's risk tranching, to Pendle's yield tokenization, to comparisons with traditional finance, I hope this presentation helped you:

✅ Understand core mechanisms of DeFi structured products
✅ Recognize opportunities from technological innovation
✅ Appreciate the importance of risk management
✅ Find investment strategies suited to you

Remember: This is a high-risk, high-reward emerging field. Please ensure:
- Only invest in products you understand
- Only invest money you can afford to lose
- Continuous learning, stay vigilant
- Prioritize risk management

If you have any questions, feel free to contact me via WeChat or email. I'm happy to continue discussing and exchanging ideas.

Let's witness the future of DeFi together!

Thank you!"

---

5. Q&A Transition (if time permits)

If time allows, you can say:

"Before we officially conclude, we have a few minutes left. If anyone has remaining questions, now is the last opportunity. Don't hesitate, all questions are welcome!"

Common final questions:
- "Do you personally invest in DeFi?"
  * Answer honestly, share experience
  * Emphasize this is not investment advice

- "Which protocol do you favor most?"
  * Can share views, but explain reasoning
  * Emphasize need for own research (DYOR)

- "Is now a good time to invest?"
  * Avoid giving explicit timing advice
  * Emphasize long-term perspective
  * Remind of market volatility

---

6. Post-Event Follow-up

What to do after the presentation:

Immediately (same day):
- Share presentation highlights on social media
- Thank organizers and audience
- Respond to business cards/contact requests received

Short-term (within 1 week):
- Compile Q&A questions into FAQ
- Share presentation PPT (if permitted)
- Send supplementary materials to interested attendees
- Write a summary article

Medium-term (within 1 month):
- Follow up with deep engagement attendees
- Organize small discussion groups
- Share latest industry developments
- Build long-term connections

---

7. Presentation Tips Reminder

Body language at closing:
- Maintain smile and eye contact
- Stand straight, project confidence
- Gestures should be open and friendly
- Don't rush off stage

Tone and pacing:
- Slow down speech, let audience digest
- Tone should be sincere and enthusiastic
- Final sentence should be powerful
- Pause, give audience time to applaud

Handling silence:
- If no applause, don't be awkward
- Can proactively say "Thank you everyone"
- Start packing materials, natural transition
- Stay professional and composed

---

8. Core Quote: "Innovation Never Stops, Yields Keep Growing"

Meaning:
- Innovation never stops: DeFi continuously innovates, new products emerge constantly
- Yields keep growing: Innovation brings new yield opportunities
- Double meaning: Refers to both protocol innovation and personal learning growth

Why this quote:
- Short and powerful, easy to remember
- Positive and inspiring
- Captures DeFi's core characteristics
- Leaves lasting impression

Alternative closing phrases:
- "Embrace innovation, manage risk, create the future together"
- "The future of DeFi, written by us together"
- "From understanding to practice, from small amounts to growth"
- "Technology transforms finance, learning transforms destiny"

---

Key learning points:

As a presenter:
- Prepare concise and powerful closing
- Provide clear action recommendations
- Leave contact information
- Stay open and friendly

As a learner:
- Review core points of entire presentation
- Create your own learning plan
- Start small-scale practice
- Join community, continuous learning

Most important:
- This is not the end, but the beginning
- DeFi structured products are a long-term learning and investment journey
- Maintain curiosity and vigilance
- Grow with the community

Remember:
- Only invest in what you understand
- Only invest what you can afford to lose
- Risk management first
- Continuous learning, stay humble

---

Complete Presentation Flow Review:

1. ✅ Opening (Page 1): Capture attention, build trust
2. ✅ Agenda (Page 2): Set expectations, show structure
3. ✅ Core Content (Pages 3-19): Deep dive, data support
4. ✅ Summary (Page 20): Distill key points, reinforce memory
5. ✅ Q&A (Page 21): Interactive exchange, answer questions
6. ✅ Closing (Page 22): Call to action, leave impression

Presentation success criteria:
- Audience understands core concepts of DeFi structured products
- Audience recognizes opportunities and risks
- Audience knows how to start learning and practicing
- Audience willing to continue following and engaging

Congratulations on completing the entire presentation study!

You now have mastered all 22 pages of content and presentation skills. Next steps:
1. Practice the full presentation multiple times
2. Familiarize yourself with key points of each page
3. Prepare answers for common questions
4. Stay confident and enthusiastic

Best of luck with your presentation! 🎉
-->

<style scoped>
.quote {
  font-size: 1.8em;
  font-weight: 700;
  text-align: center;
  background: linear-gradient(90deg, var(--primary-color) 0%, var(--accent-color) 50%, var(--success-color) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  padding: 2rem;
}
</style>

<div class="quote">Innovation Never Stops, Yields Keep Growing</div>
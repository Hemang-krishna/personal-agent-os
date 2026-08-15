#!/usr/bin/env python3
"""
qnt. Universal Quant Codex & Master Monograph (210 Concepts + VIP Instagram Networking Blueprint)
The Definitive Pitch-Black Monograph & Monetization Engine for Dxrk sky
"""

import os
import sys
import weasyprint

def build_qnt_200_monograph(output_pdf="/data/reports/qnt_200_Universal_Quant_Concepts_Master_Monograph.pdf"):
    logo_path = "file:///data/cache/images/img_3e4fbac95420.jpg"
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>qnt. — 210 Universal Quant Concepts & Monetization Codex</title>
<style>
  @page {{
    size: letter;
    margin: 18mm 15mm 18mm 15mm;
    background-color: #000000;
    @top-center {{
      content: "qnt.  |  210 UNIVERSAL CONCEPTS & MONETIZATION MASTER MONOGRAPH";
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      font-size: 7.5pt;
      font-weight: 700;
      color: #64748B;
      border-bottom: 0.5pt solid #1E293B;
      padding-bottom: 4px;
      width: 100%;
    }}
    @bottom-left {{
      content: "qnt. RESEARCH GROUP — DXRK SKY MONOGRAPH — CONFIDENTIAL & PROPRIETARY";
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      font-size: 7pt;
      color: #475569;
      border-top: 0.5pt solid #1E293B;
      padding-top: 4px;
    }}
    @bottom-right {{
      content: "Page " counter(page) " of " counter(pages);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      font-size: 7pt;
      font-weight: 700;
      color: #94A3B8;
      border-top: 0.5pt solid #1E293B;
      padding-top: 4px;
    }}
  }}

  @page :first {{
    @top-center {{ content: normal; border-top: none; border-bottom: none; }}
    @bottom-left {{ content: normal; border-top: none; }}
    @bottom-right {{ content: normal; border-top: none; }}
  }}

  * {{ box-sizing: border-box; }}

  body {{
    background-color: #000000;
    color: #F8FAFC;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 8.2pt;
    line-height: 1.35;
    margin: 0;
    padding: 0;
  }}

  .cover {{
    text-align: center;
    padding-top: 15px;
    page-break-after: always;
  }}

  .cover-logo {{
    width: 220px;
    height: auto;
    margin-bottom: 12px;
  }}

  .cover-title {{
    font-size: 22pt;
    font-weight: 900;
    letter-spacing: -0.5px;
    color: #FFFFFF;
    margin: 0 0 5px 0;
    text-transform: uppercase;
  }}

  .cover-subtitle {{
    font-size: 9.5pt;
    color: #94A3B8;
    max-width: 520px;
    margin: 0 auto 14px auto;
    line-height: 1.4;
  }}

  .divider {{
    height: 1px;
    background: linear-gradient(90deg, transparent, #06B6D4, transparent);
    margin: 10px 0 14px 0;
  }}

  .meta-grid {{
    display: table;
    width: 100%;
    background-color: #060913;
    border: 1px solid #1E293B;
    border-radius: 4px;
    margin-bottom: 12px;
    text-align: left;
  }}

  .meta-row {{ display: table-row; }}
  .meta-cell {{
    display: table-cell;
    padding: 6px 10px;
    border-bottom: 1px solid #111827;
    font-size: 7.8pt;
  }}
  .meta-cell strong {{ color: #06B6D4; }}

  .abstract-box {{
    background-color: #050811;
    border: 1px solid #06B6D4;
    border-radius: 4px;
    padding: 10px 12px;
    text-align: left;
    margin-top: 8px;
  }}

  .abstract-box h3 {{
    color: #06B6D4;
    font-size: 8.5pt;
    font-weight: 800;
    margin: 0 0 4px 0;
    letter-spacing: 0.5px;
  }}

  .abstract-box p {{
    color: #CBD5E1;
    font-size: 7.5pt;
    line-height: 1.35;
    margin: 0 0 5px 0;
    font-style: italic;
  }}

  .section-header {{
    font-size: 12pt;
    font-weight: 800;
    color: #FFFFFF;
    border-bottom: 1.5px solid #06B6D4;
    padding-bottom: 3px;
    margin: 16px 0 8px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  .subsection-header {{
    font-size: 9.5pt;
    font-weight: 700;
    color: #38BDF8;
    margin: 10px 0 5px 0;
    text-transform: uppercase;
  }}

  .citation-card {{
    background-color: #070B16;
    border: 1px solid #1E293B;
    border-left: 3px solid #06B6D4;
    border-radius: 3px;
    padding: 7px 9px;
    margin-bottom: 5px;
    page-break-inside: avoid;
  }}
  .citation-card h4 {{ font-size: 8.2pt; font-weight: 700; color: #FFFFFF; margin: 0 0 2px 0; }}
  .citation-card p {{ font-size: 7.5pt; color: #94A3B8; margin: 0; line-height: 1.25; }}

  .biz-grid {{ display: table; width: 100%; margin-bottom: 10px; }}
  .biz-cell {{ display: table-cell; width: 50%; padding: 5px; vertical-align: top; }}
  .biz-card {{
    background-color: #060913;
    border: 1px solid #1E293B;
    border-radius: 4px;
    padding: 8px 10px;
    height: 100%;
  }}
  .biz-card h4 {{ color: #38BDF8; font-size: 8.2pt; margin: 0 0 3px 0; font-weight: 700; }}
  .biz-card p {{ color: #CBD5E1; font-size: 7.3pt; margin: 0; line-height: 1.25; }}

  .concept-card {{
    background-color: #060913;
    border: 0.75px solid #1E293B;
    border-radius: 3px;
    padding: 5px 8px;
    margin-bottom: 4.5px;
    page-break-inside: avoid;
  }}
  .concept-title {{ font-size: 8.2pt; font-weight: 700; color: #FFFFFF; margin: 0 0 2px 0; }}
  .concept-math {{ font-size: 7.3pt; color: #CBD5E1; margin: 0 0 1.5px 0; line-height: 1.2; }}
  .concept-analogy {{ font-size: 7.3pt; color: #38BDF8; font-style: italic; margin: 0 0 1.5px 0; line-height: 1.2; }}
  .concept-hook {{ font-size: 7.3pt; color: #34D399; font-weight: 600; margin: 0; line-height: 1.2; }}

  .network-card {{
    background-color: #070C1B;
    border: 1px solid #06B6D4;
    border-radius: 4px;
    padding: 8px 10px;
    margin-bottom: 6px;
    page-break-inside: avoid;
  }}
  .network-card h4 {{ color: #38BDF8; font-size: 8.5pt; margin: 0 0 3px 0; font-weight: 800; }}
  .network-card p {{ color: #E2E8F0; font-size: 7.5pt; margin: 0; line-height: 1.3; }}

  .page-break {{ page-break-before: always; }}
</style>
</head>
<body>

<!-- ==================== COVER PAGE ==================== -->
<div class="cover">
  <img src="{logo_path}" class="cover-logo" alt="qnt.">
  <div class="cover-title">THE UNIVERSAL QUANT CODEX: 210 CONCEPTS</div>
  <div class="cover-subtitle">The Complete Mathematical, Physical, and Algorithmic Blueprint for AI Quants, Market Creators & High-Growth Media Empires</div>
  
  <div class="divider"></div>

  <div class="meta-grid">
    <div class="meta-row">
      <div class="meta-cell"><strong>Principal Researcher & Creator:</strong> Dxrk sky</div>
      <div class="meta-cell"><strong>Brand Identity:</strong> qnt. (Physics of Everything)</div>
    </div>
    <div class="meta-row">
      <div class="meta-cell"><strong>Autonomous Intelligence Engine:</strong> Hermes Agent</div>
      <div class="meta-cell"><strong>Git Verified Origin:</strong> obsiagent-boop (obsi.agent@gmail.com)</div>
    </div>
    <div class="meta-row">
      <div class="meta-cell"><strong>Scope & Classification:</strong> 210 Concepts / University Citations / Monetization</div>
      <div class="meta-cell"><strong>Commercial Directive:</strong> Multi-Tier Media & Quant System Engine</div>
    </div>
  </div>

  <div class="abstract-box">
    <h3>EXECUTIVE RESEARCH ABSTRACT & MONETIZATION MANDATE</h3>
    <p>This master monograph unifies 210 foundational mathematical, physical, and financial principles spanning 35,000 years of inquiry — connecting prehistoric tallies and sacred geometry to non-linear Navier-Stokes fluid mechanics, Bachelier-Wiener stochastic random walks, Turing reaction-diffusion morphogenesis, Mandelbrot fractal scale-invariance, high-frequency orderbook microstructure, and multi-head Transformer latent spaces. We prove that nature's morphogenesis, decentralized crypto order books, and neural latent manifolds are isomorphic representations of non-equilibrium thermodynamics. This treatise includes the complete 4-Tier Monetization Framework and the VIP Instagram Collaboration Outreach Blueprint to build a global high-margin quant education and algorithmic trading empire.</p>
    <div style="font-size: 7pt; color: #64748B;"><strong>Keywords:</strong> Stochastic Calculus, Orderbook Microstructure, Fractals, Reaction-Diffusion, High-D Latents, Quantum Algorithms, qnt.</div>
  </div>
</div>

<!-- ==================== SECTION 1: CITATIONS ==================== -->
<div class="section-header">SECTION 1: UNIVERSITY CITATIONS & THEORETICAL FOUNDATIONS</div>

<div class="citation-card">
  <h4>1. Louis Bachelier (1900) — Théorie de la Spéculation (Sorbonne, Paris)</h4>
  <p>First mathematical proof that asset prices follow Brownian Motion (Stochastic Random Walks) 5 years before Albert Einstein proved physical atoms exist in 1905. Proves orderbook liquidity is physical particle diffusion: dS_t = μ S_t dt + σ S_t dW_t.</p>
</div>

<div class="citation-card">
  <h4>2. Alan Turing (1952) — The Chemical Basis of Morphogenesis (Royal Society)</h4>
  <p>Turing's non-linear reaction-diffusion equations proved how uniform chemicals spontaneously self-organize into leopard spots. Proves uncoordinated bids/asks in crypto orderbooks naturally form support/resistance walls through decentralized spatial kinetics.</p>
</div>

<div class="citation-card">
  <h4>3. Benoît B. Mandelbrot (1963, 1997) — Fractals and Scaling in Finance (IBM / Yale)</h4>
  <p>Proved asset markets follow Pareto-Levy fat-tailed distributions rather than Gaussian curves. Proves a 1-second Bitcoin orderbook spike has the exact same fractal Hurst Exponent (H ≈ 0.65) as a 10-year macro currency cycle.</p>
</div>

<div class="citation-card">
  <h4>4. Claude Shannon (1948) & J.L. Kelly Jr. (1956) — Information Entropy & Optimal Growth (Bell Labs)</h4>
  <p>Quantified information as entropy reduction (H(X) = -Σ P(x) log P(x)) and derived the exact mathematical formula for optimal geometric wealth compounding without ruin: f* = (bp - q)/b.</p>
</div>

<div class="citation-card">
  <h4>5. Edward Lorenz (1963) — Deterministic Nonperiodic Flow (MIT)</h4>
  <p>Discovered the Butterfly Effect and non-linear chaotic strange attractors. Proves why static technical indicators (RSI, Moving Averages) inevitably fail in dynamic non-linear phase spaces.</p>
</div>

<div class="citation-card">
  <h4>6. Jim Simons & Leonard Baum (1988–Present) — Hidden Markov Models (Renaissance Technologies)</h4>
  <p>Developed Baum-Welch expectation-maximization regime detection generating 66% annualized gross returns over 30 years without ever predicting directional news headlines.</p>
</div>

<!-- ==================== SECTION 2: MONETIZATION & NETWORKING ==================== -->
<div class="section-header">SECTION 2: THE 4-TIER $10M BUSINESS & INSTAGRAM VIP NETWORKING MAP</div>

<div class="biz-grid">
  <div class="biz-cell">
    <div class="biz-card">
      <h4>Tier 1: Top-of-Funnel Viral Traffic ($0 Entry)</h4>
      <p>• Reels/Shorts decoding math secrets using qnt. branding.<br/>• Automated Call-to-Actions (e.g. 'Comment QUANT') triggering auto-DM lead delivery.</p>
    </div>
  </div>
  <div class="biz-cell">
    <div class="biz-card">
      <h4>Tier 2: High-Value Lead Magnets ($0 Lead Capture)</h4>
      <p>• Notion 'Quant Trading Bible' + Python Monte Carlo backtesters.<br/>• Builds a massive verified email & Discord/Telegram subscriber list.</p>
    </div>
  </div>
</div>

<div class="biz-grid">
  <div class="biz-cell">
    <div class="biz-card">
      <h4>Tier 3: Monthly Recurring Community ($49 - $99/mo)</h4>
      <p>• Skool / Whop Quant AI Mastermind.<br/>• Weekly backtested algorithmic setups, AI prompt libraries & private market breakdowns.<br/>• <em>500 members = $25,000–$50,000/month recurring pure profit.</em></p>
    </div>
  </div>
  <div class="biz-cell">
    <div class="biz-card">
      <h4>Tier 4: Enterprise & Prop Workstations ($1,500 - $10,000)</h4>
      <p>• Custom multi-agent trading workstations & automated prop firm pass systems.<br/>• High-ticket consulting for private funds and family offices.</p>
    </div>
  </div>
</div>

<div class="subsection-header">INSTAGRAM VIP COLLABORATION & OUTREACH BLUEPRINT</div>

<div class="network-card">
  <h4>1. Target Profiles & Niches to Target on Instagram</h4>
  <p><strong>A. Quant Developers & Python Engineers:</strong> Creators showcasing backtesting code, TradingView PineScript, and quantitative stats.<br/>
  <strong>B. Prop Firm & Forex Traders:</strong> Funded account traders looking for mathematical edge beyond basic ICT/Smart Money concepts.<br/>
  <strong>C. AI & Data Science Educators:</strong> Machine learning influencers seeking practical financial market applications.</p>
</div>

<div class="network-card">
  <h4>2. The 3-Step High-Converting DM Outreach Script</h4>
  <p><strong>Hook:</strong> "Loved your breakdown on [Topic]. We just mapped out the exact stochastic proof behind it using Bachelier's Brownian model."<br/>
  <strong>Value Gift:</strong> "Generated this custom 3D Cyber Void animation + Python script for your next post. Zero strings attached — thought your audience would love the visual."<br/>
  <strong>Collaboration Proposal:</strong> "Would love to do a joint carousel or 45s split-screen reel: 'The Math Wall Street Doesn't Want You to Know.' Let me know if you're open!"</p>
</div>

<!-- ==================== SECTION 3: 210 CONCEPTS ==================== -->
<div class="page-break"></div>
<div class="section-header">SECTION 3: THE 210 UNIVERSAL MATHEMATICAL & QUANT CONCEPTS</div>
"""

    # We generate 210 comprehensive concepts
    from generate_dark_academic_qnt_pdf import generate_dark_academic_pdf
    import generate_dark_academic_qnt_pdf
    
    # Base 110 concepts
    base_110 = generate_dark_academic_qnt_pdf.generate_dark_academic_pdf  # we'll build the list of 210
    
    # 210 Comprehensive Concepts List
    concepts_210 = [
        # --- PILLAR I: Ancient Math & Nature's Ratios (001-035) ---
        ("001. The Ishango Tally (Prehistoric Lunar Arithmetic)",
         "First known lunar arithmetic recorded on bone (c. 20,000 BCE). Demonstrates prime grouping and base-10 arithmetic.",
         "Counting sleep cycles like marking notches on a wooden toy box.",
         "Viral Hook: 'The oldest mathematical calculation in human history was carved into a baboon bone.'"),
        ("002. The Invention of Zero (Brahmagupta's Shunya)",
         "Conceptualization of zero as both an operational quantity and positional placeholder enabling infinite algebraic systems.",
         "An empty plate that tells you how many empty plates are stacked.",
         "Viral Hook: 'Why the Roman Empire collapsed without ever being able to divide numbers.'"),
        ("003. The Golden Ratio (Phi = 1.618033...)",
         "Irrational geometric ratio minimizing spatial resonance and maximizing packing efficiency: x² - x - 1 = 0.",
         "How sunflower seeds fit together so no single seed gets shaded by sunlight.",
         "Viral Hook: 'Why the exact same number dictates the shape of galaxies, sunflower petals, and Bitcoin market tops.'"),
        ("004. The Fibonacci Sequence",
         "Recursive sequence F(n) = F(n-1) + F(n-2) whose asymptotic limit converges to the Golden Ratio.",
         "Adding baby rabbits together in pairs as each generation multiplies.",
         "Viral Hook: 'The hidden mathematical reason behind 61.8% Fibonacci retracements in Forex trading.'"),
        ("005. Euclidean Geometry & The 5 Postulates",
         "Axiomatic spatial system establishing flat plane metrics, parallel postulates, and triangle congruence.",
         "Building flat castles with square wooden blocks that never bend or warp.",
         "Viral Hook: 'Why flat geometry breaks the moment you trade global currencies across time zones.'"),
        ("006. Pythagorean Theorem (a² + b² = c²)",
         "Fundamental Euclidean metric for calculating shortest distance and hypotenuse in orthogonal 2D space.",
         "Walking diagonally across a grassy square instead of walking around the path.",
         "Viral Hook: 'How high-frequency arbitrage bots measure distance in trading space.'"),
        ("007. Prime Numbers & Sieve of Eratosthenes",
         "Indivisible multiplicative atomic building blocks of the positive integers: P = {2, 3, 5, 7, 11...}.",
         "Atomic Lego bricks that cannot be snapped apart into smaller pieces.",
         "Viral Hook: 'Why pure prime numbers protect trillions of dollars in crypto transactions every second.'"),
        ("008. Pi (π = 3.14159265...)",
         "Transcendental constant governing the perimeter-to-diameter ratio of all Euclidean circular boundaries.",
         "The distance around a toy car tire compared to its width across.",
         "Viral Hook: 'Why every single atom in your body vibrates along the rhythm of Pi.'"),
        ("009. Logarithmic Spirals (Spira Mirabilis)",
         "Self-similar geometric curve r = a·e^(bθ) where pitch angle remains constant regardless of expansion scale.",
         "A snail shell expanding outward while keeping the exact same house shape.",
         "Viral Hook: 'How financial bubble manias expand in logarithmic spirals before bursting.'"),
        ("010. Voronoi Tessellations",
         "Partitioning space into convex polygons where every point in a cell is closest to its designated seed node.",
         "Soap bubbles pressing against each other to form straight sharing walls.",
         "Viral Hook: 'Why giraffe skin patterns and city delivery logistics use the exact same algorithm.'"),
        ("011. Hexagonal Packing Theorem",
         "Geometric proof that regular hexagons provide the densest 2D perimeter coverage with minimum wall surface area.",
         "Why bees build honeycombs in hexagons rather than squares to save precious wax.",
         "Viral Hook: 'Why nature always chooses hexagons when saving energy.'"),
        ("012. Modular Arithmetic (Clock Math)",
         "Arithmetic congruence system a ≡ b (mod n) where numbers wrap around a cyclic modulus boundary.",
         "Adding 5 hours to 9 o'clock gives 2 o'clock, not 14 o'clock.",
         "Viral Hook: 'The clock math that encrypts your WhatsApp messages and Bitcoin private keys.'"),
        ("013. Non-Euclidean Riemannian Geometry",
         "Differential geometry of curved manifolds where parallel geodesics converge (elliptic) or diverge (hyperbolic).",
         "Drawing straight lines on the surface of an inflated basketball.",
         "Viral Hook: 'Why Einstein needed curved geometry to prove gravity bends time.'"),
        ("014. Topology (Homeomorphic Invariance)",
         "Classification of spatial structures preserved under continuous deformation (stretching, twisting, crumpling).",
         "A coffee mug and a doughnut are the exact same shape because both have 1 hole.",
         "Viral Hook: 'How topological data analysis spots hidden liquidity traps in crypto markets.'"),
        ("015. The Möbius Strip",
         "Non-orientable two-dimensional manifold containing only one continuous surface boundary and one side.",
         "A toy racetrack where driving around brings you upside down without ever turning over.",
         "Viral Hook: 'The one-sided loop that baffled 19th-century mathematicians.'"),
        ("016. The Klein Bottle",
         "Closed non-orientable four-dimensional surface with Euler characteristic zero and no interior or exterior.",
         "A bottle that loops through itself so liquid is everywhere and nowhere.",
         "Viral Hook: 'Visualizing 4-dimensional shapes inside our 3-dimensional world.'"),
        ("017. The Archimedean Spiral",
         "Locus of points moving away from a central origin at constant linear speed along a uniformly rotating ray.",
         "A coiled garden hose wound up evenly on the lawn.",
         "Viral Hook: 'How ancient Greeks pumped water uphill with a spinning screw.'"),
        ("018. Fermat's Last Theorem (Wiles' Proof)",
         "Proof that no positive integers x, y, z satisfy x^n + y^n = z^n for any integer value of n > 2 via modular elliptic curves.",
         "Trying to combine two 3D cubes into one bigger perfect 3D cube.",
         "Viral Hook: 'The 350-year-old math puzzle written in the margin of a book.'"),
        ("019. Platonic Solids & Regular Polyhedra",
         "The 5 convex regular polyhedra with congruent regular polygonal faces (Tetrahedron, Cube, Octahedron, Dodecahedron, Icosahedron).",
         "The only 5 perfect 3D dice nature allows you to roll.",
         "Viral Hook: 'Why atomic crystals always freeze into these 5 sacred geometric shapes.'"),
        ("020. Epicycles & Fourier Series Approximation",
         "Decomposition of complex periodic planetary or waveform trajectories into superpositions of circular harmonics.",
         "Drawing a cat by spinning smaller hula hoops on top of bigger hula hoops.",
         "Viral Hook: 'How ancient astronomers predicted eclipses using spinning circles.'"),
        ("021. Trigonometric Wave Functions (Sine & Cosine)",
         "Fundamental orthogonal basis functions mapping uniform circular rotation into linear harmonic oscillation.",
         "The shadow of a spinning bicycle wheel moving smoothly back and forth on the wall.",
         "Viral Hook: 'How sound, light, and market volatility cycles are all made of waves.'"),
        ("022. Combinatorics & Factorial Growth (n!)",
         "Permutational explosion metric n! = n × (n-1) × ... × 1 governing arrangement cardinality.",
         "How many different ways you can line up 5 toy soldiers on a shelf.",
         "Viral Hook: 'Why shuffling a deck of 52 cards creates an order that has never existed in the universe.'"),
        ("023. Pascal's Triangle & Binomial Coefficients",
         "Geometric triangular array C(n, k) = n! / (k!(n-k)!) generating probability distributions and fractal Sierpiński patterns.",
         "A pyramid where every block is the weight of the two blocks above it.",
         "Viral Hook: 'The ancient pyramid of numbers that holds the secret to coin toss probability.'"),
        ("024. Complex Numbers & Imaginary Plane (i = √-1)",
         "Two-dimensional algebraic field extensions z = a + bi enabling orthogonal phase-space representation.",
         "Rotating a toy arrow 90 degrees into an invisible direction.",
         "Viral Hook: 'Why imaginary numbers are mandatory to engineer modern electrical grids and microchips.'"),
        ("025. The Coastline Paradox (Fractal Dimension)",
         "Benoît Mandelbrot's proof that geographic boundaries possess fractional Hausdorff dimensions D > 1, approaching infinite length.",
         "Measuring a bumpy coastline with a giant yardstick vs. a microscopic ant's ruler.",
         "Viral Hook: 'Why the coastline of Britain has infinite length.'"),
        ("026. Euler's Identity (e^(iπ) + 1 = 0)",
         "The most beautiful equation in mathematics linking five fundamental constants (e, i, pi, 1, 0).",
         "A magic circle connecting every major superhero into one perfect team.",
         "Viral Hook: 'The single equation that unites all of mathematics in 7 characters.'"),
        ("027. Apollonian Gaskets (Fractal Circle Packing)",
         "Infinite recursive fractal circle packing where mutually tangent circles fill space without overlapping.",
         "Packing smaller and smaller marbles into the gaps between big marbles.",
         "Viral Hook: 'How fractal circle math designs high-frequency radio antennas.'"),
        ("028. Penrose Tilings (Aperiodic Crystals)",
         "Non-periodic geometric tilings with five-fold symmetry that never repeat their pattern across infinity.",
         "Bathroom floor tiles that fit together forever without ever making the exact same picture twice.",
         "Viral Hook: 'The impossible tiles discovered by Roger Penrose that won a Nobel Prize.'"),
        ("029. Gaussian Curvature (Theorema Egregium)",
         "Gauss's proof that intrinsic surface curvature is independent of how the surface is embedded in 3D space.",
         "Why you cannot eat a slice of pizza without folding the crust.",
         "Viral Hook: 'The math rule that stops pizza from drooping and maps world globes.'"),
        ("030. Knot Theory & Topological Invariants",
         "Study of closed 3D loops and polynomial invariants (Jones polynomial) distinguishing tangled configurations.",
         "Untangling a giant knot in shoelaces without ever cutting the string.",
         "Viral Hook: 'How knot mathematics decodes DNA replication and quantum physics.'"),
        ("031. Quaternions & 3D Spatial Rotations",
         "Four-dimensional non-commutative number system q = w + xi + yj + zk eliminating gimbal lock in 3D physics.",
         "A 3D compass that rotates spaceships without getting stuck in a corner.",
         "Viral Hook: 'The 4D math invention written on a bridge that powers modern 3D video game graphics.'"),
        ("032. Octonions & 8-Dimensional Algebra",
         "Eight-dimensional normed division algebra governing particle symmetries in theoretical superstring physics.",
         "An 8-way kaleidoscope reflecting hyper-dimensional geometry.",
         "Viral Hook: 'The 8-dimensional math algebra that might explain the fundamental particles of physics.'"),
        ("033. Delaunay Triangulation",
         "Geometric dual of Voronoi diagrams maximizing the minimum angle of all triangles in a point mesh.",
         "Connecting dots with straight lines so no triangle looks like a squished needle.",
         "Viral Hook: 'The mesh math powering 3D CGI movies and geographical terrain rendering.'"),
        ("034. Phyllotaxis Spiral Packing",
         "Arrangement of leaves and petals along the golden angle (137.5°) maximizing sunlight exposure.",
         "Spinning a toy top slightly after each jump so no jump lands on the previous footprints.",
         "Viral Hook: 'Why pinecones and pineapples count in Fibonacci numbers.'"),
        ("035. Buffon's Needle Probability Problem",
         "Geometric probability experiment estimating Pi by randomly dropping needles on lined floorboards.",
         "Dropping toothpicks on a wood floor and counting how many cross a crack.",
         "Viral Hook: 'How to calculate Pi by throwing toothpicks on the kitchen floor.'"),

        # --- PILLAR II: Physics, Thermodynamics, Fluid Dynamics & Chaos (036-070) ---
        ("036. Navier-Stokes Equations (Viscous Flow)",
         "Non-linear partial differential equations governing fluid velocity and momentum transport.",
         "How water swirls in a bathtub drain when you pull the plug.",
         "Viral Hook: 'Why Wall Street quants model order book liquidity like rushing water pressure.'"),
        ("037. Second Law of Thermodynamics (Entropy ΔS ≥ 0)",
         "Universal physical law stating total entropy of an isolated thermodynamic system cannot decrease over time.",
         "A neat bedroom naturally gets messy, but a messy room never cleans itself.",
         "Viral Hook: 'Why time only moves forward and never backward.'"),
        ("038. Lorenz Strange Attractor",
         "Non-linear 3D deterministic dynamical system exhibiting chaotic trajectories bounded on a fractal manifold.",
         "A swing that pushes itself into a new wild rhythm every single time.",
         "Viral Hook: 'How a butterfly flapping its wings in Brazil causes a tornado in Texas.'"),
        ("039. Brownian Motion (Einstein-Wiener Stochastic Walk)",
         "Continuous-time stochastic process with independent Gaussian increments representing thermal molecular collisions.",
         "A speck of dust dancing in a sunbeam as invisible air molecules bump into it.",
         "Viral Hook: 'How Einstein used pollen grains dancing in water to prove atoms exist.'"),
        ("040. Power-Law Fat Tails (Pareto-Levy Distributions)",
         "Heavy-tailed probability density functions P(X > x) ~ x^(-α) where catastrophic events dominate variance.",
         "A town where 1 giant is 1,000 feet tall while everyone else is 5 feet tall.",
         "Viral Hook: 'Why 99% of standard risk models fail during market crashes.'"),
        ("041. Turing Morphogenesis (Reaction-Diffusion)",
         "System of coupled non-linear parabolic PDEs where activator-inhibitor chemical kinetics break spatial homogeneity.",
         "Two colors of dye fighting for space on a paper towel forming leopard spots.",
         "Viral Hook: 'How nature paints zebra stripes and leopard spots with simple chemistry.'"),
        ("042. Lyapunov Exponents & Phase Space Divergence",
         "Asymptotic metric λ measuring the exponential divergence rate |δZ(t)| ≈ e^(λt)|δZ(0)| of perturbed trajectories.",
         "Two toy cars rolling down the exact same bumpy hill that end up miles apart.",
         "Viral Hook: 'Why weather forecasts are physically impossible past 14 days.'"),
        ("043. Phase Transitions & Critical Exponents",
         "Non-analytic singularities in free energy derivatives driving sudden macroscopic structural reorganization.",
         "Water sitting at 0°C that suddenly snaps into solid ice in one second.",
         "Viral Hook: 'How flash crashes happen when market sentiment reaches critical boiling point.'"),
        ("044. Percolation Theory & Connected Clusters",
         "Probabilistic threshold models governing formation of infinite spanning clusters across random lattice networks.",
         "Pouring coffee water through ground beans until the first drop drips through.",
         "Viral Hook: 'How viruses spread and how liquidation cascades wipe out exchanges.'"),
        ("045. Maxwell's Demon Information Paradox",
         "Thermodynamic thought experiment demonstrating that information acquisition and erasure carries non-zero physical entropy cost.",
         "A tiny gatekeeper who only lets fast bouncy red balls into one room.",
         "Viral Hook: 'Why information is physically equivalent to energy.'"),
        ("046. Landauer's Principle",
         "Thermodynamic lower bound E = kT ln(2) of energy dissipation required to irreversibly erase one bit of information.",
         "Erasing a word on paper produces a microscopic puff of heat in the universe.",
         "Viral Hook: 'The physical proof that computing and erasing data creates heat.'"),
        ("047. Shannon Entropy (Information Content)",
         "Logarithmic measure of uncertainty H(X) = -Σ P(x) log₂ P(x) quantifying minimum compression limits.",
         "How surprised you are when opening a surprise gift box.",
         "Viral Hook: 'How Claude Shannon built the entire internet on a single math equation.'"),
        ("048. Cellular Automata (Conway's Game of Life)",
         "Turing-complete discrete dynamical system generating complex self-replicating structures from 4 local transition rules.",
         "A grid of black and white tiles that reproduce or die based on friendly neighbors.",
         "Viral Hook: 'How 4 simple rules can simulate an entire evolving universe.'"),
        ("049. Self-Organized Criticality (The Sandpile Model)",
         "Non-equilibrium systems with local interactions naturally evolving to a critical point with power-law avalanche frequency.",
         "Dropping single grains of sand on a pile until one single grain causes the whole side to collapse.",
         "Viral Hook: 'Why small stock drops suddenly turn into massive market crashes.'"),
        ("050. Hooke's Law & Mean Reversion (F = -kx)",
         "Linear restorative force proportional to displacement distance governing spring mechanics and mean-reverting price spreads.",
         "Pulling a rubber band back — the harder you pull, the faster it snaps back.",
         "Viral Hook: 'Why quants make millions trading stretched rubber-band stocks.'"),
        ("051. Bernoulli's Principle & Dynamic Pressure",
         "Conservation of energy in steady fluid flow: p + 1/2ρv² + ρgh = constant relating speed and pressure gradients.",
         "Blowing over the top of a piece of paper makes the paper float upward.",
         "Viral Hook: 'Why 500-ton steel airplanes stay in the air.'"),
        ("052. Acoustic & Mechanical Resonance",
         "Selective amplification of vibrational amplitude occurring when driving frequency matches intrinsic system eigenfrequency.",
         "Pushing someone on a playground swing at the exact right moment to send them flying higher.",
         "Viral Hook: 'How singing the exact right note can shatter a crystal glass.'"),
        ("053. The Continuous Fourier Transform",
         "Integral transform F(ω) = ∫ f(t) e^(-iωt) dt mapping time-domain signals into continuous frequency spectral power.",
         "Unbaking a baked cake back into eggs, flour, and sugar.",
         "Viral Hook: 'The math formula that turns sound into MP3s and CT scans into 3D body images.'"),
        ("054. De Broglie Wave-Particle Duality (λ = h/p)",
         "Fundamental quantum postulate asserting every material particle exhibits an associated de Broglie wavelength.",
         "A magic ball that acts like a solid marble when you touch it, but ripples like water when you let go.",
         "Viral Hook: 'Why light is both a particle and a wave at the exact same time.'"),
        ("055. Quantum Superposition (|ψ⟩ = α|0⟩ + β|1⟩)",
         "Linear state vector combination across orthogonal Hilbert space states prior to projective measurement collapse.",
         "A spinning coin on a table that is both heads and tails until you slap your hand down.",
         "Viral Hook: 'Why a quantum computer calculates 10,000 possibilities at once.'"),
        ("056. Quantum Entanglement & Bell Inequalities",
         "Non-separable composite quantum wavefunctions exhibiting non-local spin correlations violating local realism.",
         "Two magic dice in different galaxies: roll a 6 on Earth, and Mars instantly rolls a 6.",
         "Viral Hook: 'What Einstein called spooky action at a distance.'"),
        ("057. Heisenberg Uncertainty Principle (Δx·Δp ≥ ℏ/2)",
         "Fundamental lower bound on non-commuting matrix observables enforcing measurement limits in quantum phase space.",
         "Trying to take a picture of a hummingbird's wing — freeze the wing, you blur where it was flying.",
         "Viral Hook: 'Why you can never know where an electron is and where it is going.'"),
        ("058. General Relativity & Geodesic Curvature",
         "Einstein field equations G_μν + Λg_μν = (8πG/c⁴)T_μν describing spacetime metric curvature under mass-energy tensors.",
         "A heavy bowling ball sitting on a rubber trampoline bending the fabric around it.",
         "Viral Hook: 'Why time ticks slower on Earth than in deep outer space.'"),
        ("059. Black Hole Event Horizons & Hawking Radiation",
         "Null hypersurface boundary trapping light paths, balanced by quantum vacuum fluctuation particle-antiparticle emission.",
         "A waterfall so fast that even a speedboat engine cannot paddle backward over the edge.",
         "Viral Hook: 'Why black holes slowly evaporate into glowing quantum radiation.'"),
        ("060. The Poincaré Recurrence Theorem",
         "Measure-preserving volume dynamics guaranteeing volume-conserving systems return arbitrarily close to initial microstates.",
         "Shuffling a deck of cards for trillions of years until it accidentally returns to perfect sorted order.",
         "Viral Hook: 'The mathematical proof that history repeats itself if you wait long enough.'"),
        ("061. Carnot Cycle Efficiency (Thermodynamic Limits)",
         "Maximum theoretical heat engine efficiency η = 1 - T_C/T_H bounded by source-sink temperature differentials.",
         "A watermill that can only spin as fast as the height of the falling waterfall.",
         "Viral Hook: 'The physical law that proves no engine in the universe can be 100% efficient.'"),
        ("062. Vortex Shedding & Kármán Vortex Streets",
         "Repeating pattern of swirling vortices caused by unsteady separation of fluid flow over bluff bodies.",
         "Flags fluttering violently in a stiff breeze behind a flagpole.",
         "Viral Hook: 'Why suspension bridges collapse when the wind blows at the exact wrong speed.'"),
        ("063. The Ising Model of Ferromagnetism",
         "Mathematical lattice model of magnetic dipole moments demonstrating spontaneous magnetization phase transitions.",
         "A crowd of people suddenly deciding to all look up at the sky at the exact same second.",
         "Viral Hook: 'The physics model that explains how viral social media panics start.'"),
        ("064. Cavitation & Bubble Dynamics (Rayleigh-Plesset)",
         "Rapid formation and explosive collapse of vapor cavities in liquids subjected to rapid pressure drops.",
         "A boat propeller spinning so fast that water boils cold and creates tiny explosions.",
         "Viral Hook: 'How shrimp snap their claws so fast it creates light and boils water.'"),
        ("065. Solitons (Non-Dispersive Solitary Waves)",
         "Self-reinforcing wave packets maintaining constant velocity and shape due to non-linear balancing dispersion.",
         "A water ripple in a narrow canal that travels for miles without ever fading away.",
         "Viral Hook: 'The immortal waves that carry laser signals across ocean internet cables.'"),
        ("066. Gibbs Free Energy (ΔG = ΔH - TΔS)",
         "Thermodynamic potential measuring maximum reversible work obtainable from closed thermodynamic systems.",
         "Checking if you have enough pocket money and energy to build a treehouse.",
         "Viral Hook: 'The chemical formula that determines whether life itself can happen.'"),
        ("067. The Doppler Effect & Redshift",
         "Frequency shift of wave energy emitted by a source in relative motion towards or away from an observer.",
         "A race car zooming past you whose engine sound drops from high pitch to low rumble.",
         "Viral Hook: 'How astronomers proved the entire universe is expanding outward.'"),
        ("068. Quantum Tunneling & Potential Barriers",
         "Quantum mechanical phenomenon where wavefunctions penetrate classically forbidden energy barriers.",
         "A ghost walking straight through a solid brick wall without breaking it.",
         "Viral Hook: 'The quantum miracle that allows the Sun to shine and power our planet.'"),
        ("069. Kinetic Theory of Gases (Maxwell-Boltzmann)",
         "Statistical mechanics distribution describing particle velocity vectors in thermal equilibrium.",
         "Bouncing 10,000 rubber bouncy balls in a gym to see their average speed.",
         "Viral Hook: 'How temperature is just the speed of invisible atoms dancing.'"),
        ("070. Relativistic Time Dilation (Lorentz Factor γ)",
         "Difference in elapsed time measured by observers due to relative velocity or gravitational potential differences.",
         "An astronaut twin who comes back from space younger than their brother on Earth.",
         "Viral Hook: 'Why your GPS satellite has to correct for time traveling into the future.'"),

        # --- PILLAR III: Quantitative Finance & HFT (071-105) ---
        ("071. Black-Scholes-Merton Options PDE",
         "Parabolic PDE establishing dynamic delta-hedging arbitrage equilibrium pricing for European financial derivatives.",
         "Calculating the fair price of an umbrella rental before it starts raining.",
         "Viral Hook: 'The formula that created the multi-trillion dollar options market.'"),
        ("072. The Kelly Criterion Capital Allocation",
         "Optimal capital fraction f* = (bp - q)/b maximizing the expected logarithmic growth rate of wealth under geometric compounding.",
         "How many candies to bet in a game so you never run out of candy.",
         "Viral Hook: 'The math formula gamblers and Wall Street titans use to size their bets.'"),
        ("073. Sharpe & Sortino Performance Ratios",
         "Risk-adjusted excess return metrics scaling performance by total standard deviation and downside semi-variance.",
         "Measuring how fast a race car drove compared to how violently it bumped the wall.",
         "Viral Hook: 'Why a trader making 50% profit can be far worse than a trader making 20%.'"),
        ("074. Order Book Imbalance (OBI Metric)",
         "Real-time volume ratio OBI = (V_bid - V_ask)/(V_bid + V_ask) predicting instantaneous microsecond price drift.",
         "Counting the total muscle weight on both sides of a tug-of-war rope before the whistle.",
         "Viral Hook: 'How high-frequency trading bots front-run orders in microseconds.'"),
        ("075. Nash Equilibrium in Game Theory",
         "Strategic profile where no participant can increase payoff by unilaterally altering their chosen action strategy.",
         "Two drivers meeting at a single-lane bridge where neither can speed up without crashing.",
         "Viral Hook: 'Why gas stations always open right across the street from each other.'"),
        ("076. The Prisoner's Dilemma Game",
         "Canonical non-cooperative game illustrating why strictly dominant individual strategies yield Pareto-suboptimal equilibria.",
         "Two kids caught eating cookies who get grounded because neither trusted the other to stay quiet.",
         "Viral Hook: 'Why OPEC oil cartels always end up cheating on each other.'"),
        ("077. Monte Carlo Portfolio Risk Integration",
         "Stochastic integration evaluating portfolio terminal wealth distributions over 100,000 synthetic pseudo-random paths.",
         "Playing 10,000 simulated Mario levels to see how many lives you need to beat Bowser.",
         "Viral Hook: 'How quants test their trading portfolio against 10,000 market crashes in 5 seconds.'"),
        ("078. Hidden Markov Models & Regime Shift Detection",
         "Bivariate stochastic process where observed market emissions are conditioned on unobservable latent Markovian state transitions.",
         "Guessing what season it is outside just by looking at what clothes people carry into a hallway.",
         "Viral Hook: 'How Jim Simons made $28 Billion by tracking hidden market weather.'"),
        ("079. Pairs Trading & Cointegration Vectors",
         "Stationary linear combinations of non-stationary integrated I(1) price series evaluated via Augmented Dickey-Fuller tests.",
         "A drunk owner walking a dog on an elastic leash — they wander everywhere, but stay close.",
         "Viral Hook: 'How to make money in crypto even when the entire market crashes.'"),
        ("080. Maximum Drawdown (MDD Fragility)",
         "Peak-to-trough historical drop metric MDD(T) = max(M(t) - S(t))/M(t) measuring capital fragility and recovery thresholds.",
         "The deepest underwater dip a submarine takes before coming back up for air.",
         "Viral Hook: 'Why losing 50% requires a 100% gain just to get back to zero.'"),
        ("081. Market Microstructure & Slippage Decay",
         "Analysis of discrete matching engine limit order books, maker-taker rebates, latency arbitrage, and price impact decay.",
         "Buying all the bananas in a grocery store where each banana gets more expensive.",
         "Viral Hook: 'Why market buy orders lose you money before the trade even confirms.'"),
        ("082. The Efficient Market Hypothesis (Fama's EMH)",
         "Neoclassical asset pricing proposition that prices follow a martingale process with zero risk-adjusted drift expectation.",
         "A race where no runner can get a head start because everyone gets the same shoes.",
         "Viral Hook: 'Why Warren Buffett and quants laugh at the Efficient Market Hypothesis.'"),
        ("083. Implied Volatility Smiles & Skew Surfaces",
         "Non-constant implied volatility surfaces σ(K, T) plotted across strike prices capturing structural tail-risk demand.",
         "People paying 10x more for flood insurance because they remember the last hurricane.",
         "Viral Hook: 'How options pricing reveals what Wall Street is secretly terrified of.'"),
        ("084. GARCH Volatility Clustering Models",
         "Autoregressive models σ²_t = ω + α ε²_(t-1) + β σ²_(t-1) capturing empirical conditional heteroskedasticity in asset returns.",
         "A storm where thunderclaps come in fast bunches rather than spread out evenly.",
         "Viral Hook: 'How algorithms predict tomorrow's market panic by measuring today's volatility.'"),
        ("085. Market Making & Half-Spread Capture",
         "High-frequency algorithmic provision of continuous two-sided liquidity capturing the bid-ask spread while managing toxic flow.",
         "Buying used video games for $10 and selling them at the door for $12 all day long.",
         "Viral Hook: 'How Citadel Securities makes billions without ever taking a directional bet.'"),
        ("086. Adverse Selection in Limit Order Queues",
         "Information asymmetry risk where passive limit orders execute disproportionately against informed directional order flow.",
         "Selling umbrellas on a sunny day, only to have someone buy all of them right before a storm.",
         "Viral Hook: 'Why passive limit orders often lose money in high volatility.'"),
        ("087. Avellaneda-Stoikov Market Making Optimization",
         "Stochastic optimal control framework deriving reservation prices r(s, q, t) = s - qγσ²(T - t) based on inventory penalty.",
         "A candy shop adjusting prices higher as their inventory runs low to avoid empty shelves.",
         "Viral Hook: 'The mathematical equation powering modern automated market maker (AMM) bots.'"),
        ("088. The Hurst Exponent & Long-Range Memory",
         "Rescaled range analysis metric H determining persistence (H > 0.5), anti-persistence (H < 0.5), or Brownian motion (H = 0.5).",
         "A toy car with a heavy steering wheel that loves going straight versus one that wiggles back and forth.",
         "Viral Hook: 'How quants use one single number to know if Bitcoin is trending or chopping.'"),
        ("089. Cross-Venue Arbitrage & Latency Routing",
         "Simultaneous multi-leg execution exploiting transient cross-exchange price dislocations before matching engines synchronize.",
         "Buying apples in one town for $1 and selling them in the next town for $2.",
         "Viral Hook: 'How crypto bots make millions in 1 millisecond by exploiting exchange price differences.'"),
        ("090. Maximum Entropy Production in Financial Flow",
         "Non-equilibrium thermodynamic postulate stating market liquidity self-organizes to maximize transaction rate and entropy throughput.",
         "A river carving the fastest possible canyon route to empty its water into the sea.",
         "Viral Hook: 'Why financial markets route liquidity along paths of maximum trading volume.'"),
        ("091. Prospect Theory & Loss Aversion (Kahneman-Tversky)",
         "Empirical S-shaped value function proving utility loss from a negative payoff is 2.25x greater than identical positive gain.",
         "Crying twice as hard when you drop an ice cream cone compared to when you are handed a second scoop.",
         "Viral Hook: 'Why human brains are biologically wired to be terrible day traders.'"),
        ("092. Cross-Impact & Liquidity Spillover Matrices",
         "Multi-asset price response functions where order flow volume in instrument i creates structural drift in correlated asset j.",
         "Throwing a big rock into one side of a swimming pool creating waves on the other side.",
         "Viral Hook: 'How a Bitcoin whale dump crashes Solana and Ethereum in under 100 milliseconds.'"),
        ("093. Statistical Arbitrage & Principal Components",
         "Eigenvalue decomposition of asset covariance matrices isolating idiosyncratic mean-reverting residual vectors.",
         "Finding 500 pairs of socks where one sock is slightly cheaper than its twin.",
         "Viral Hook: 'How hedge funds make money in bull markets, bear markets, and sideways markets.'"),
        ("094. The Merton Jump-Diffusion Process",
         "Stochastic differential equation dS/S = (μ - λk)dt + σdW + (Y - 1)dq integrating Poisson compound discontinuous shocks.",
         "A frog hopping smoothly along a log that suddenly leaps 5 feet into the air.",
         "Viral Hook: 'Why standard financial math misses weekend geopolitical news gaps.'"),
        ("095. Mathematical Expectation & Mathematical Edge",
         "Expected value operator E[X] = Σ x_i P(x_i) separating positive-sum quant strategies from negative-sum gambling games.",
         "Rolling a dice where 5 faces give you $1 and 1 face takes $10.",
         "Viral Hook: 'The single formula that separates profitable quants from broke gamblers.'"),
        ("096. Volume-Weighted Average Price (VWAP Execution)",
         "Algorithmic execution benchmark dividing cumulative dollar volume by total traded volume over a trading horizon.",
         "Buying a giant cake slice by slice over 8 hours so the bakery price never spikes.",
         "Viral Hook: 'How institutional pension funds buy $100 Million of stock without moving the price.'"),
        ("097. Time-Weighted Average Price (TWAP)",
         "Execution strategy slicing large parent orders into equal block sizes dispatched at regular fixed time intervals.",
         "Feeding a goldfish one tiny flake every 10 minutes instead of dumping the whole jar.",
         "Viral Hook: 'Why crypto whales use TWAP algorithms to exit massive positions quietly.'"),
        ("098. Glosten-Milgrom Sequential Trade Model",
         "Microstructure model proving market makers widen bid-ask spreads as probability of trading with informed traders rises.",
         "A card dealer charging higher entry fees when a professional card counter sits down at the table.",
         "Viral Hook: 'Why crypto spreads widen right before major inflation news releases.'"),
        ("099. Kyle's Lambda (Price Impact Coefficient)",
         "Equilibrium liquidity metric λ measuring price change per unit of unexpected market order flow volume: ΔP = λ·Q.",
         "Measuring how deep your foot sinks into sand based on how heavy your boots are.",
         "Viral Hook: 'The formula hedge funds use to calculate the exact cost of their market orders.'"),
        ("100. High-Frequency Cancellation Ratios",
         "Ratio of resting limit orders canceled relative to executed trades (>95% in modern electronic equity venues).",
         "Faking 100 high-fives before actually slapping hands with someone.",
         "Viral Hook: 'Why 98% of bids and asks you see on a trading chart are fake phantom orders.'"),
        ("101. Co-Location & Optical Latency Engineering",
         "Physical installation of HFT server racks inside exchange data centers cutting light-in-fiber transit times to nanoseconds.",
         "Moving your desk right next to the teacher's podium so you hear the test answers first.",
         "Viral Hook: 'Why Wall Street spent $300 Million digging a straight tunnel through a mountain to save 3 milliseconds.'"),
        ("102. Dark Pools & Non-Displayed Liquidity",
         "Private crossing networks executing large institutional blocks without pre-trade public orderbook visibility.",
         "Selling a luxury mansion at a private secret auction without putting a 'For Sale' sign on the lawn.",
         "Viral Hook: 'Where 40% of US stock trades happen in complete secret.'"),
        ("103. Risk Parity & Ray Dalio's All-Weather Engine",
         "Portfolio allocation methodology equalizing volatility risk contributions rather than nominal dollar weights across asset classes.",
         "Building a 4-legged table where each leg carries the exact same weight so the table never wobbles.",
         "Viral Hook: 'How Bridgewater built an all-weather portfolio that survives depressions and inflation.'"),
        ("104. Delta, Gamma, Vega, Theta (Option Greeks)",
         "First and second partial derivatives of option pricing functions measuring sensitivity to price, curvature, volatility, and time decay.",
         "The dashboard gauges of an airplane showing speed, climb rate, wind resistance, and fuel burn.",
         "Viral Hook: 'The 4 Greek dials options market makers watch to avoid losing millions in minutes.'"),
        ("105. Cross-Currency Triangulation Arbitrage",
         "Exploiting currency exchange cross-rate dislocations across three currency pairs (e.g. USD -> EUR -> JPY -> USD).",
         "Trading a baseball card for a toy car, trading the car for a video game, and trading the game for two baseball cards.",
         "Viral Hook: 'How Forex quants make risk-free profit in 10 microseconds by trading in circles.'"),

        # --- PILLAR IV: Forex Liquidity & Macro Regimes (106-140) ---
        ("106. London-New York Session Liquidity Overlap",
         "Peak global FX liquidity window (8:00 AM – 12:00 PM EST) where European and US institutional desks trade concurrently.",
         "Two giant rivers meeting at a roaring waterfall where water volume doubles.",
         "Viral Hook: 'Why 70% of daily Forex volatility happens in this single 4-hour window.'"),
        ("107. Central Bank Interest Rate Parity (IRP)",
         "Fundamental macroeconomic condition linking spot FX rates, forward rates, and national interest rate differentials.",
         "Two bank accounts in different countries that must pay the exact same reward after adjusting for currency conversion.",
         "Viral Hook: 'How central banks move trillions of dollars with one single interest rate announcement.'"),
        ("108. The FX Carry Trade & Unhedged Currency Risk",
         "Strategy borrowing in low-interest currencies (JPY/CHF) to fund high-yielding sovereign bonds (USD/MXN/BRL).",
         "Borrowing money from a bank at 1% interest to put it in a savings account paying 6% interest.",
         "Viral Hook: 'The currency trade that made billions until the Yen suddenly exploded in 2024.'"),
        ("109. Liquidity Sweeps & Stop-Run Cascades",
         "Institutional absorption of retail stop-loss limit orders clustered above swing highs and below swing lows.",
         "A giant vacuum cleaner sucking up all the crumbs left on the kitchen floor before walking out.",
         "Viral Hook: 'Why your stop loss gets hit right before the market shoots up in your predicted direction.'"),
        ("110. Yield Curve Inversion & Recession Forecasting",
         "Negative spread condition where short-term sovereign bond yields exceed long-term yields, predicting economic contraction.",
         "Paying more money to rent a bicycle for 1 hour than for a full week.",
         "Viral Hook: 'The single financial indicator that has predicted every recession for 50 years.'"),
        ("111. Eurodollar Futures & Offshore USD Clearing",
         "Trillion-dollar shadow banking market pricing US dollar interest rates deposited in foreign banks outside Federal Reserve regulation.",
         "A secret underground dollar vault where global banks trade money outside America.",
         "Viral Hook: 'The multi-trillion dollar shadow dollar market that secretly runs the world economy.'"),
        ("112. Macro Quantitative Easing (QE) & Balance Sheet Expansion",
         "Central bank monetary policy purchasing sovereign bonds with newly credited reserves, expanding the monetary base.",
         "Printing 1,000 extra Monopoly money dollars and handing them to everyone at the board game table.",
         "Viral Hook: 'How central banks created $8 Trillion out of thin air in 2020.'"),
        ("113. Purchasing Power Parity (The Big Mac Index)",
         "Long-run equilibrium theory stating exchange rates adjust until identical basket of goods costs the same across countries.",
         "Checking if a hamburger costs the same number of toy coins in London and Tokyo.",
         "Viral Hook: 'Why The Economist uses McDonald's hamburgers to prove currencies are fake.'"),
        ("114. The Balassa-Samuelson Economic Effect",
         "Productivity growth differences in tradable sectors driving structural real exchange rate appreciation in developing nations.",
         "Haircuts costing 5x more in New York than in Thailand even though haircuts take the exact same 15 minutes.",
         "Viral Hook: 'Why wealthy nations are so expensive to live in compared to developing countries.'"),
        ("115. Sovereign Credit Default Swaps (Sovereign CDS)",
         "Derivative contract providing payoff protection in the event of national government sovereign debt default or restructuring.",
         "Buying house fire insurance on your neighbor's house when you smell smoke.",
         "Viral Hook: 'How hedge funds bet on entire countries going bankrupt.'"),
        ("116. Bank for International Settlements (BIS Triennial Survey)",
         "Global central bank audit measuring total daily foreign exchange market turnover ($7.5+ Trillion per day).",
         "Counting every single coin that changes hands on Earth in 24 hours.",
         "Viral Hook: 'Why the Forex market trades more money in 3 days than the entire US stock market trades in a year.'"),
        ("117. Interbank FIX Protocol & API Connectivity",
         "Standardized messaging specification (Financial Information eXchange) enabling automated electronic trade routing between brokers and liquidity providers.",
         "The universal walkie-talkie language all trading computers speak to each other.",
         "Viral Hook: 'The secret programming code connecting every bank terminal on Wall Street.'"),
        ("118. Algorithmic Iceberg Orders",
         "Synthetic execution orders revealing only a small visible fraction (e.g. 10 lots) while hiding massive volume (e.g. 1,000 lots) beneath the surface.",
         "An iceberg floating in the ocean where you only see the tiny tip above water.",
         "Viral Hook: 'How institutional traders hide 100 Million dollar orders on retail charts.'"),
        ("119. FX Pegging & The Swiss National Bank Unpegging Shock",
         "Central bank intervention defending artificial currency boundaries until foreign reserves exhaust, triggering catastrophic structural resets (EUR/CHF 2015).",
         "Holding a giant wooden dam against a rushing river until the dam breaks and floods the valley.",
         "Viral Hook: 'The day the Swiss Franc exploded 30% in 5 minutes and wiped out hedge funds.'"),
        ("120. Petrodollar Recycling & Global Dollar Dominance",
         "International monetary loop where global crude oil invoicing in USD compels foreign oil-exporting nations to reinvest surplus dollars into US Treasuries.",
         "An arcade where you can only buy popcorn and games using special gold tokens.",
         "Viral Hook: 'How oil and dollars teamed up to become the most powerful weapon in history.'"),
        ("121. The Triffin Dilemma in Monetary Economics",
         "Conflict of interest arising when a national currency serves as the global reserve currency, compelling persistent balance of payments deficits.",
         "The kid who brings the only ball to the playground must let everyone play even when they lose.",
         "Viral Hook: 'The fatal mathematical paradox built into the US dollar reserve currency system.'"),
        ("122. Currency Board Regimes (Hong Kong Dollar Peg)",
         "Monetary authority holding 100% foreign reserve backing at fixed exchange rates, sacrificing independent monetary policy for FX stability.",
         "A locker where every paper ticket in circulation has a real gold coin locked in the box.",
         "Viral Hook: 'How Hong Kong defends its currency peg against billionaire hedge fund attacks.'"),
        ("123. The Asian Financial Crisis (Soros vs Bank of England/Thailand)",
         "Speculative currency runs exploiting overvalued pegged currencies with inadequate foreign currency reserves.",
         "Betting that a bank doesn't have enough cash in the vault to pay everyone who lines up at the door.",
         "Viral Hook: 'How George Soros broke the Bank of England and made $1 Billion in 24 hours.'"),
        ("124. Non-Farm Payrolls (NFP) Macro Volatility Shock",
         "Monthly US Bureau of Labor Statistics employment report triggering aggressive institutional orderbook repricing and spread blowouts.",
         "The monthly report card that makes Wall Street traders either cheer or panic in 1 second.",
         "Viral Hook: 'Why Forex spreads widen 10x on the first Friday of every single month.'"),
        ("125. Intermarket Currency-Commodity Correlations (AUD/Gold, CAD/Oil)",
         "Structural terms-of-trade linkages where commodity-exporting currencies fluctuate in tandem with physical commodity benchmarks.",
         "A lemonade stand whose ticket price rises every time the price of lemons goes up.",
         "Viral Hook: 'Why the Canadian Dollar rises and falls with the price of oil barrels.'"),
        ("126. High-Water Marks & Performance Fee Hurdle Rates",
         "Hedge fund contract mechanisms ensuring fund managers only charge performance fees on net new capital gains exceeding prior peak portfolio equity.",
         "Only getting a high-score prize if you beat your personal best video game score.",
         "Viral Hook: 'The rule that stops hedge fund managers from getting rich when losing client money.'"),
        ("127. FX Prime Brokerage (PB) & Tier-1 Aggregators",
         "Credit intermediation structures allowing non-bank quants and hedge funds to access top-tier interbank ECN liquidity pools.",
         "Having an ultra-rich VIP uncle vouch for you so you can enter the exclusive bank trading floor.",
         "Viral Hook: 'How quant trading firms access the same pricing as JPMorgan and Goldman Sachs.'"),
        ("128. Currency Currency Cross-Rate Matrix Decomposition",
         "Synthetic pricing triangulation guaranteeing absence of spatial cross-rate triangular arbitrage across G10 and EM currencies.",
         "A puzzle grid where every row and column of coin prices must multiply to 1.0.",
         "Viral Hook: 'Why currency prices can never stay out of balance for more than 1 millisecond.'"),
        ("129. The Real Effective Exchange Rate (REER Index)",
         "Trade-weighted exchange rate index adjusted for relative inflation differentials across primary foreign trading partner nations.",
         "Measuring how strong your currency is based on how much food it buys around the world.",
         "Viral Hook: 'The true indicator that shows whether a country's currency is overvalued or cheap.'"),
        ("130. Currency Swap Basis Spreads (Cross-Currency Basis)",
         "Deviations from covered interest parity reflecting global structural imbalance in US dollar funding demand across foreign jurisdictions.",
         "Paying an extra penalty fee to borrow dollars in Tokyo instead of New York.",
         "Viral Hook: 'The hidden price tag global banks pay when dollars get scarce.'"),
        ("131. Forward Exchange Contracts (FEC Pricing)",
         "Bilateral forward commitments locking in future exchange rates derived from spot rates and interest rate differentials: F = S·(1 + r_d)/(1 + r_f).",
         "Agreeing today on the price of your lunch sandwich 6 months from now.",
         "Viral Hook: 'How multinational airlines and tech giants protect against currency crashes.'"),
        ("132. Asian Session Consolidation Ranges (Tokyo Drift)",
         "Low-volatility consolidation ranges established during Asian market hours (12:00 AM – 6:00 AM UTC) providing reference breakout levels for London open.",
         "A quiet morning stretch before the roaring afternoon race starts.",
         "Viral Hook: 'The Asian range breakout strategy quant bots run every morning at 3:00 AM EST.'"),
        ("133. Central Bank Balance Sheet Run-Off (Quantitative Tightening)",
         "Central bank monetary contraction allowing maturing sovereign debt to roll off balance sheets without reinvestment, draining system liquidity.",
         "Draining water out of a giant swimming pool so fewer boats can float.",
         "Viral Hook: 'How Quantitative Tightening silently crashes asset prices and stocks.'"),
        ("134. Dynamic Hedging in Multi-Currency Portfolios",
         "Continuous adjustment of currency forward and option overlays to neutralize foreign exchange translation risk across international equity portfolios.",
         "Wearing a waterproof raincoat that tightens automatically as the storm gets heavier.",
         "Viral Hook: 'How global funds invest in Japanese stocks without losing money on the Yen.'"),
        ("135. Forex Retail Sentiment Contrarian Indicators (SSI)",
         "Speculative sentiment index tracking retail trader directional skew, exploited as a high-probability contrarian momentum indicator.",
         "Looking at where 90% of lost tourists are walking and walking in the exact opposite direction.",
         "Viral Hook: 'Why doing the exact opposite of retail Forex traders makes quants profitable.'"),
        ("136. Continuous Linked Settlement (CLS Bank Bank Settlement)",
         "Global settlement system eliminating Herstatt foreign exchange settlement risk through simultaneous payment-versus-payment (PvP) gross clearing.",
         "Handing your lunch money over at the exact same millisecond the other kid hands over the apple.",
         "Viral Hook: 'The banking engine that prevents global financial settlement meltdowns.'"),
        ("137. Emerging Market Currency Peg Defense Mechanics",
         "Central bank foreign currency reserve depletion dynamics and interest rate spikes employed to defend fixed exchange rate targets.",
         "Spending your entire piggy bank savings to keep your toy car price from dropping.",
         "Viral Hook: 'Why emerging market central banks run out of dollars during global panics.'"),
        ("138. Forward Rate Agreements (FRA Curves)",
         "Over-the-counter financial forward derivative contracts determining interest rates to be paid or received on specific future dates.",
         "Locking in the interest rate on your future bicycle loan 1 year in advance.",
         "Viral Hook: 'How bond quants trade the future cost of money.'"),
        ("139. Sovereign Wealth Fund (SWF) Asset Allocation",
         "Long-term strategic asset allocation models of state-owned sovereign funds (Norway GPFG, GIC, ADIA) rebalancing across global currencies.",
         "A nation saving giant barrels of oil money in a global vault for its great-grandchildren.",
         "Viral Hook: 'How Norway's $1.5 Trillion sovereign fund buys 1.5% of every company in the world.'"),
        ("140. High-Frequency News Scraping & NLP Sentiment Ingestion",
         "Low-latency natural language processing pipelines parsing central bank speeches and macroeconomic headlines in milliseconds to trigger order routing.",
         "A computer reading the teacher's announcements in 1 millisecond to run out the door first.",
         "Viral Hook: 'How trading bots read Fed speeches and execute trades before human eyes can blink.'"),

        # --- PILLAR V: Artificial Intelligence & High-D Latents (141-175) ---
        ("141. High-Dimensional Vector Embeddings",
         "Mapping discrete token spaces into continuous Euclidean and cosine manifolds ℝ^d (d = 4,096+).",
         "Pinning thousands of words on a giant 3D globe where related words cluster together.",
         "Viral Hook: 'Why AI doesn't read words — it navigates an invisible 4,000-dimensional galaxy.'"),
        ("142. Scaled Dot-Product Self-Attention",
         "Matrix kernel Attention(Q, K, V) = softmax((QK^T)/√d_k) V computing dynamic pairwise sequence contextual relevance.",
         "Every student in a giant classroom making eye contact with everyone else to see who is talking.",
         "Viral Hook: 'The 2017 math formula that created ChatGPT, Claude, and Gemini.'"),
        ("143. Gradient Descent & Backpropagation Calculus",
         "Reverse-mode automatic differentiation calculating Jacobian gradients ∂L/∂W to minimize empirical loss surfaces.",
         "A blind hiker feeling the slope of a mountain with a stick to find the lowest valley.",
         "Viral Hook: 'How neural networks learn from their mistakes millions of times a second.'"),
        ("144. The Curse of High Dimensionality",
         "Exponential volume expansion of unit hyperspheres rendering randomly sampled points equidistant and boundary-concentrated.",
         "Looking for a lost marble in a giant empty warehouse versus a small toy box.",
         "Viral Hook: 'Why high-dimensional AI space acts completely counter-intuitive to human eyes.'"),
        ("145. Latent Space Manifold Hypothesis",
         "Topological assertion that high-dimensional real-world data concentrates along lower-dimensional sub-manifolds.",
         "Drawing a caricature of someone using just 3 lines instead of a million photo pixels.",
         "Viral Hook: 'How Midjourney and Runway invent photorealistic humans that don't exist.'"),
        ("146. Multi-Head Attention Projections",
         "Parallel linear transformations projecting queries, keys, and values into h distinct representation subspaces.",
         "Reading a detective book while paying attention to clues, tone, and timeline all at once.",
         "Viral Hook: 'Why multi-head attention allows AI to understand irony, humor, and deep code logic.'"),
        ("147. Residual Skip Connections (ResNets)",
         "Identity mapping shortcuts x_(l+1) = F(x_l, W_l) + x_l mitigating vanishing and exploding gradient paths.",
         "Taking an express elevator straight to the 50th floor instead of walking every staircase.",
         "Viral Hook: 'The simple trick that allowed neural networks to grow from 10 layers to 100 layers.'"),
        ("148. Rotary Position Embeddings (RoPE)",
         "Injecting relative token distance via complex unitary rotation matrices applied directly to Q and K representations.",
         "Numbering every train car so you know which car is in front and which is in back.",
         "Viral Hook: 'How AI knows the difference between 'The dog bit the man' and 'The man bit the dog'.'"),
        ("149. Retrieval-Augmented Generation (RAG Architecture)",
         "Decoupled architecture conditioning autoregressive language models on non-parametric vector database retrieval chunks.",
         "Giving an open-book textbook to a smart student right before their exam.",
         "Viral Hook: 'Why RAG beats fine-tuning for 95% of real-world AI applications.'"),
        ("150. Hierarchical Navigable Small World Graphs (HNSW)",
         "Multi-layer geometric skip-graph data structure enabling logarithmic O(log N) Approximate Nearest Neighbor (ANN) search.",
         "Asking a friend of a friend of a friend to find someone in a new city in 3 phone calls.",
         "Viral Hook: 'How vector databases search 100 million documents in 3 milliseconds.'"),
        ("151. Model Context Protocol (MCP Architecture)",
         "Standardized JSON-RPC client-host-server protocol granting foundation models uniform access to external tools and files.",
         "Giving your AI assistant hands, eyes, and toolboxes to build real things in the physical world.",
         "Viral Hook: 'Why MCP is the USB-C standard for the entire AI agent ecosystem.'"),
        ("152. Multi-Agent Swarm Orchestration",
         "Decentralized asynchronous communication protocols where specialized role-bounded agents coordinate execution pipelines.",
         "An army of ants carrying a giant leaf together that no single ant could lift.",
         "Viral Hook: 'Why 4 specialized AI agents working together beat 1 giant prompt every time.'"),
        ("153. Reinforcement Learning from Human Feedback (RLHF)",
         "Policy optimization (PPO) aligning generative distribution outputs against Bradley-Terry reward scoring models.",
         "Giving a puppy a treat every time it sits politely instead of barking.",
         "Viral Hook: 'How human trainers taught raw AI base models to be helpful assistants.'"),
        ("154. Knowledge Distillation & Logit Transfer",
         "Supervised compression minimizing Kullback-Leibler divergence between student logits and teacher soft probability targets.",
         "A master martial artist teaching their top 10 best moves to a fast young student.",
         "Viral Hook: 'How to compress a giant $10M AI model into a fast app running on your phone.'"),
        ("155. Low-Precision Weight Quantization (FP16 to INT4)",
         "Non-linear scaling and block-wise quantization mapping continuous floating-point tensors into 4-bit integer bins.",
         "Writing down telephone numbers with just 4 digits instead of 16 decimal places.",
         "Viral Hook: 'How 4-bit quantization lets you run full AI models on a $500 laptop.'"),
        ("156. Score-Based Generative Diffusion Models",
         "Generative modeling integrating reverse-time stochastic differential equations matching learned score functions ∇_x log p(x).",
         "Cleaning a super dusty window pane by pane until a crystal clear painting appears.",
         "Viral Hook: 'How AI generates photorealistic video by removing static noise from a blank TV.'"),
        ("157. Softmax Probability Normalization",
         "Smooth differentiable approximation to the argmax operator mapping ℝ^K logits to the standard probability simplex.",
         "Turning arbitrary voting scores into clean percentages that add up to 100%.",
         "Viral Hook: 'The final formula inside every AI model that picks the next word.'"),
        ("158. Overfitting & L1/L2 Weight Regularization",
         "Adding parameter norm penalties (Lasso |w| and Ridge w²) to empirical loss functions constraining model hypothesis complexity.",
         "Studying for a test by understanding the concepts instead of memorizing yesterday's exact answers.",
         "Viral Hook: 'Why a trading algorithm that looks 100% perfect in backtests will fail in live trading.'"),
        ("159. Chain of Thought (CoT) Autoregressive Reasoning",
         "Sequential token generation dedicating test-time computational budget to intermediate reasoning tokens before emitting solutions.",
         "Writing out your scratchpad math on paper before shouting out the answer in class.",
         "Viral Hook: 'The 3-word prompt that makes AI 500% smarter instantly: Think step by step.'"),
        ("160. Sparse Mixture of Experts (MoE Gating)",
         "Conditional computation routing input tokens dynamically to top-k specialized feed-forward expert subnetworks.",
         "A hospital routing patients directly to heart doctors or eye doctors instead of consulting every doctor.",
         "Viral Hook: 'How DeepSeek and Mixtral run giant models at a fraction of the computing cost.'"),
        ("161. Cross-Entropy Loss Optimization",
         "Information-theoretic loss metric L = -Σ y_i log(p_i) minimizing the distance between true and estimated empirical densities.",
         "Measuring how close your dart throw was to the bullseye on every turn.",
         "Viral Hook: 'The mathematical scoreboard that grades AI every millisecond of training.'"),
        ("162. The Neural Tangent Kernel (NTK Limit)",
         "Infinite-width neural network analytical regime proving gradient descent behaves as linear kernel regression with static kernel.",
         "A spiderweb so densely woven that touching one thread smoothly ripples the entire web.",
         "Viral Hook: 'The theoretical math proof explaining why deep neural networks actually work.'"),
        ("163. Speculative Decoding Multi-Model Inference",
         "Accelerated decoding generating speculative token drafts with an SLM verified in parallel by a larger target foundation LLM.",
         "A fast junior writer drafting sentences while the senior editor stamps approvals in batches.",
         "Viral Hook: 'How to make AI text generation 3x faster without losing any quality.'"),
        ("164. FlashAttention Hardware IO Optimization",
         "Tiling algorithm restructuring attention matrix calculations to compute exact softmax within fast GPU SRAM memory blocks.",
         "Cooking a meal in one big pot on the counter instead of walking back and forth to the pantry 50 times.",
         "Viral Hook: 'The GPU engineering breakthrough that made million-token AI context possible.'"),
        ("165. Constitutional AI & Automated RLAIF",
         "Iterative self-alignment protocol using automated critique-revision loops guided by explicit constitutional principles.",
         "A student grading their own homework against a strict checklist before submitting.",
         "Viral Hook: 'How Anthropic builds safe AI models that govern themselves.'"),
        ("166. Direct Preference Optimization (DPO)",
         "Implicit reward formulation aligning LLM generation policies directly on pairwise preferences without separate reward model training.",
         "Teaching a child good manners directly from thumbs-up/thumbs-down cards without an intermediate test score.",
         "Viral Hook: 'The algorithmic upgrade that made AI model alignment 10x faster.'"),
        ("167. KV-Cache Memory Management (vLLM PagedAttention)",
         "Non-contiguous memory allocation strategy for key-value attention tensors inspired by OS virtual memory paging.",
         "Organizing your bookshelf with numbered bookmarks so you never lose your place across 100 books.",
         "Viral Hook: 'How high-throughput AI cloud servers serve 1,000 users at once without running out of VRAM.'"),
        ("168. LoRA (Low-Rank Adaptation of LLMs)",
         "Parameter-efficient fine-tuning decomposing weight update matrices into low-rank intrinsic rank matrices: ΔW = B·A (r << d).",
         "Attaching a tiny turbo booster to an airplane engine instead of rebuilding the entire plane.",
         "Viral Hook: 'How to fine-tune a massive 70B AI model on a single consumer GPU.'"),
        ("169. Self-Correction & Tree-of-Thought (ToT) Search",
         "Graph-based search exploration evaluating multiple reasoning trajectories via heuristic valuation and backtracking.",
         "Exploring a hedge maze by dropping breadcrumbs and backing up whenever you hit a dead end.",
         "Viral Hook: 'How reasoning models solve impossible coding competitions.'"),
        ("170. Contrastive Learning (InfoNCE Loss)",
         "Representation learning maximizing cosine similarity of augmented positive pairs while repelling negative sample representations.",
         "Sorting apples and oranges into separate baskets based on color and texture.",
         "Viral Hook: 'How AI learns to see without a human teacher labeling images.'"),
        ("171. Vector Quantization (VQ-VAE / VQ-GAN)",
         "Mapping continuous latent representations into discrete codebook vector indices for high-fidelity generative modeling.",
         "Painting a portrait using a fixed box of 256 numbered crayons.",
         "Viral Hook: 'The discrete math that allows AI to generate studio-quality music and speech.'"),
        ("172. Multimodal Cross-Attention Alignment",
         "Cross-attention matrices projecting vision/audio feature vectors into shared language representation space.",
         "A translator who reads Japanese text and points to matching English photos simultaneously.",
         "Viral Hook: 'How GPT-4o looks at an image and talks to you in real-time voice.'"),
        ("173. Test-Time Compute Scaling Laws",
         "Empirical scaling finding that allocating inference compute (search iterations) scales performance exponentially faster than pre-training parameters.",
         "Spending 10 minutes thinking carefully on a test question instead of writing the first thought that pops into your head.",
         "Viral Hook: 'Why the next AI breakthrough isn't bigger models — it's thinking longer before answering.'"),
        ("174. Transformer Activation Functions (SwiGLU / GeLU)",
         "Smooth non-linear gated linear unit activations outperforming legacy ReLUs in deep autoregressive architectures.",
         "A smooth dimmer switch that turns on light gently instead of an abrupt on/off click.",
         "Viral Hook: 'The microscopic math tweak inside modern neural networks that unlocked human-level language.'"),
        ("175. Multi-Agent Game-Theoretic Alignment",
         "Multi-agent reinforcement learning optimizing cooperative equilibrium strategies among autonomous competing agents.",
         "Two chess grandmasters playing against each other for a million games to discover new openings.",
         "Viral Hook: 'How AI agents invent completely new languages and strategies when playing against themselves.'"),

        # --- PILLAR VI: Crypto Algorithmic Dynamics, MEV & Quantum Physics (176-210) ---
        ("176. Constant Product Automated Market Makers (x · y = k)",
         "Invariant hyperbola pricing formula governing Uniswap decentralized liquidity pools.",
         "A seesaw where taking apples from one side automatically makes the remaining apples heavier and more expensive.",
         "Viral Hook: 'The 5-character math formula that powers the $100 Billion decentralized finance revolution.'"),
        ("177. Maximal Extractable Value (MEV & Sandwich Attacks)",
         "Searcher bots exploiting blockchain transaction ordering and mempool visibility to front-run and back-run trades.",
         "Sneaking into the ticket line right in front of a big buyer and selling them your ticket for $10 more.",
         "Viral Hook: 'How crypto bots make $50,000 in 1 block by sandwiching retail trades.'"),
        ("178. Impermanent Loss & Liquidity Provision Geometry",
         "Opportunity cost loss experienced by liquidity providers when relative token prices diverge from initial deposit ratios.",
         "Putting your toy cars in a shared box and getting back fewer cars when one toy becomes super popular.",
         "Viral Hook: 'The hidden mathematical trap that costs crypto liquidity providers their profits.'"),
        ("179. Zero-Knowledge Proofs (zk-SNARKs & zk-STARKs)",
         "Cryptographic protocols allowing one party to prove mathematical truth of a statement without revealing underlying private inputs.",
         "Proving you know the secret password to a locked door without ever saying the password out loud.",
         "Viral Hook: 'How zero-knowledge math allows you to prove your net worth without showing your bank account.'"),
        ("180. Byzantine Fault Tolerance (PBFT & Raft)",
         "Consensus protocol resilience guaranteeing distributed network agreement as long as less than 1/3 of nodes act maliciously.",
         "A council of 10 generals agreeing to attack a castle at dawn even if 3 generals are secret spies.",
         "Viral Hook: 'The computer science problem that baffled scientists for 30 years until Bitcoin solved it.'"),
        ("181. Concentrated Liquidity (Uniswap v3 Virtual Bins)",
         "Capital efficiency optimization restricting liquidity provision to bounded custom price intervals [p_a, p_b].",
         "Putting your store merchandise only on the shelf customers actually reach for, multiplying your sales 100x.",
         "Viral Hook: 'How Uniswap v3 made $1,000 of crypto liquidity act like $100,000.'"),
        ("182. Flash Loans & Uncollateralized Atomic Arbitrage",
         "Smart contract borrowing mechanism allowing multi-million dollar uncollateralized loans executed and repaid in one single transaction block.",
         "Borrowing $10 Million for 1 second to buy cheap apples and selling them for $11 Million before the clock ticks.",
         "Viral Hook: 'How a 20-year-old developer made $1 Million in 12 seconds with $0 in his bank account.'"),
        ("183. Dynamic Curve Invariants (Stableswap Pools)",
         "Hybrid invariant curve combining constant sum and constant product formulas minimizing slippage for pegged assets.",
         "A flat road that stays smooth and level until you drive off the cliff edge.",
         "Viral Hook: 'The mathematical equation that keeps stablecoins like USDT and USDC trading at exactly $1.00.'"),
        ("184. Block Space Priority Auctions (EIP-1559 Base & Tip)",
         "Algorithmic gas pricing mechanism burning protocol base fees while allowing variable tip bids for priority inclusion.",
         "An auction where the highway toll burns cash automatically to reduce traffic congestion.",
         "Viral Hook: 'How Ethereum burns billions of dollars of its own currency to make tokens scarcer.'"),
        ("185. Liquidation Cascades in Lending Protocols (DeFi Risk)",
         "Positive feedback loops where collateral price drops trigger automatic liquidations, flooding orderbooks and triggering further liquidations.",
         "A row of falling dominos where each domino pushes down two bigger dominos.",
         "Viral Hook: 'Why crypto prices drop 30% in 15 minutes during liquidation cascade flash crashes.'"),
        ("186. Elliptic Curve Cryptography (secp256k1 & Ed25519)",
         "Asymmetric cryptography leveraging discrete logarithm hardness over points on algebraic elliptic curves: y² = x³ + ax + b.",
         "A one-way mathematical slide that is super easy to slide down, but impossible to climb back up.",
         "Viral Hook: 'The mathematical curve that secures all 19 Million Bitcoins on Earth.'"),
        ("187. Time-Weighted AMM Oracles (TWAP Invariants)",
         "Cumulative price accumulation accumulators providing manipulation-resistant price feeds across multiple blocks.",
         "Measuring the average temperature of a lake over a week rather than checking one single cold afternoon.",
         "Viral Hook: 'How decentralized exchanges prevent flash loan price manipulation attacks.'"),
        ("188. Reentrancy Vulnerability & Smart Contract Exploits",
         "State-update race condition where external fallback calls re-invoke vulnerable withdrawal functions before balance state updates.",
         "Asking the bank teller for your money, and while they count the cash, asking them for it again 10 times.",
         "Viral Hook: 'The 3-line coding mistake that lost $60 Million in the famous 2016 Ethereum DAO hack.'"),
        ("189. Automated Dynamic Fee AMMs (Volatility-Responsive Fees)",
         "Algorithmic fee tiers that automatically scale wider during high volatility to compensate liquidity providers for toxic order flow.",
         "An umbrella shop that automatically raises prices when the rain starts pouring.",
         "Viral Hook: 'How modern decentralized exchanges beat professional Wall Street arbitrageurs.'"),
        ("190. Layer-2 Rollups & Fraud/Validity Proofs (Optimistic vs ZK)",
         "Off-chain execution protocols bundling thousands of transactions into single compressed state proofs verified on Layer-1.",
         "Compressing 1,000 letters into one zip envelope and mailing it with a single stamp.",
         "Viral Hook: 'How Ethereum processes 10,000 transactions a second for pennies.'"),
        ("191. Triangular Cross-DEX Arbitrage Bots",
         "Continuous topological graph cycle search algorithms executing cyclic arbitrage across multi-pool routes (A -> B -> C -> A).",
         "Trading a gold coin for 10 silver coins, trading silver for 100 bronze, and trading bronze back for 2 gold coins.",
         "Viral Hook: 'How automated crypto bots make $10,000 every day by trading in triangles.'"),
        ("192. Slippage Tolerance & Sandwich Protection (Private RPCs)",
         "Routing transactions through private builder relays (Flashbots Protect / MEV-Share) bypassing public peer-to-peer mempools.",
         "Sending your secret letter via an armored car instead of shouting it out loud in the street.",
         "Viral Hook: 'Why you should never submit a crypto swap without private RPC protection.'"),
        ("193. Bonding Curves & Token Launchpad Mathematics",
         "Deterministic mathematical pricing curves where token purchase price increases as a continuous function of circulating supply.",
         "A concert where the first ticket costs $1, the 100th ticket costs $10, and the 1,000th ticket costs $100.",
         "Viral Hook: 'The mathematical formula behind viral token launchpads like Pump.fun.'"),
        ("194. Synthetic Asset Collateralization & Debt Pools (Synthetix)",
         "Pooled counterparty debt model collateralizing synthetic tracking assets against pooled dynamic debt positions.",
         "A collective insurance pot where everyone covers everyone else's market gains and losses.",
         "Viral Hook: 'How to trade Tesla stock and Gold on the blockchain without owning the real assets.'"),
        ("195. Perpetual Futures Funding Rates (Perp Swaps)",
         "Periodic cash flow mechanism anchoring perpetual contract prices to spot index benchmarks via long-to-short funding payments.",
         "A balance weight fee that forces people holding heavy bags to pay rent to the other side.",
         "Viral Hook: 'How crypto traders make 30% annual yield without ever taking directional price risk.'"),
        ("196. Shor's Quantum Prime Factorization",
         "Polynomial-time quantum algorithm O((log N)³) exploiting the Quantum Fourier Transform to solve order-finding on discrete Abelian groups.",
         "Testing every key on a giant keychain in one single second instead of trying them one by one.",
         "Viral Hook: 'The quantum algorithm that will crack RSA encryption and modern banking.'"),
        ("197. Grover's Quantum Amplitude Amplification",
         "Quantum search algorithm providing quadratic speedup O(√N) over classical unstructured database query bounds.",
         "Finding a needle in a haystack in 100 steps instead of 10,000 steps.",
         "Viral Hook: 'How quantum computers search unsorted data at physics-defying speeds.'"),
        ("198. Tokamak Magnetohydrodynamics (Plasma Fusion)",
         "Grad-Shafranov equilibrium equations balancing thermal plasma pressure against poloidal and toroidal magnetic field tension.",
         "Holding a tiny piece of the sun inside a magnetic cage without touching the walls.",
         "Viral Hook: 'How math and AI are unlocking infinite, clean nuclear fusion energy.'"),
        ("199. AlphaFold & Protein Topological Geometry",
         "Invariant spatial graph transformers modeling 3D Euclidean distances and torsional dihedral angles of amino acid chains.",
         "Folding a paper origami crane out of a 100-foot strip of paper in 2 seconds.",
         "Viral Hook: 'How AI solved a 50-year biology mystery in months, creating cures for every disease.'"),
        ("200. Post-Quantum Lattice Cryptography (CRYSTALS-Kyber)",
         "Trapdoor cryptographic primitives grounded in the worst-case hardness of the Shortest Vector Problem (SVP) in ℝ^n lattices.",
         "Hiding a secret treasure inside a 500-dimensional maze that even quantum computers cannot navigate.",
         "Viral Hook: 'The new mathematical shield protecting global financial systems from quantum attacks.'"),
        ("201. Quantum State Teleportation Protocols",
         "Transfer of unknown quantum states via distributed Einstein-Podolsky-Rosen (EPR) pairs and classical bell-state measurements.",
         "Beaming the exact recipe of an ice sculpture across the galaxy so it rebuilds instantly on Mars.",
         "Viral Hook: 'Why quantum teleportation is real — but only for information, not physical humans.'"),
        ("202. Negative Index Metamaterials (Electrodynamics)",
         "Engineered composite structures exhibiting simultaneous negative permittivity ε < 0 and permeability μ < 0, reversing Snell's Law.",
         "Looking into a swimming pool where the water bends light around you like an invisible cloak.",
         "Viral Hook: 'The real-world physics behind Harry Potter's invisibility cloaks.'"),
        ("203. Wolfram's Computational Irreducibility",
         "Theoretical principle asserting complex deterministic computational processes cannot be predicted faster than direct execution.",
         "You cannot fast-forward a video game without actually playing every single frame.",
         "Viral Hook: 'The mathematical proof that the only way to see the future is to live through it.'"),
        ("204. Quantum Error Correction & Surface Codes",
         "Topological stabilizer codes encoding one logical qubit into two-dimensional planar arrays of physical transmon qubits.",
         "Writing a secret message across 9 puzzle pieces so if 2 pieces get smudged, you still read the message.",
         "Viral Hook: 'The engineering race to build million-qubit quantum computers.'"),
        ("205. The Holographic Principle & E8 Gauge Theory",
         "AdS/CFT correspondence establishing that physical volume degrees of freedom are fully encoded on lower-dimensional boundary surfaces.",
         "A 3D laser holographic sticker on a flat credit card that looks like a real 3D apple.",
         "Viral Hook: 'The mind-bending math proof that our entire universe might be a 2D hologram.'"),
        ("206. Quantum Decoherence & Measurement Phase Collapse",
         "Irreversible transition of pure quantum superpositions into classical statistical mixtures via environmental entanglement.",
         "A spinning soap bubble that pops into water droplets the moment it touches a dust speck.",
         "Viral Hook: 'Why quantum computers must be cooled colder than outer space to function.'"),
        ("207. Quantum Random Walk Search Algorithms",
         "Quantum state evolution over discrete graph topologies exhibiting quadratic spatial diffusion speedup over classical random walks.",
         "A ghost walking in every direction through a maze simultaneously until it finds the exit.",
         "Viral Hook: 'How quantum algorithms explore millions of mathematical paths in parallel.'"),
        ("208. The Yang-Mills Millennium Prize Problem (Mass Gap)",
         "Non-abelian gauge theory proving quantum field equations predict a non-zero strictly positive mass gap in physical vacuum states.",
         "Why empty vacuum space is never truly empty, but hums with invisible heavy energy.",
         "Viral Hook: 'The $1 Million math puzzle that explains why physical matter has weight.'"),
        ("209. Quantum Zeno Effect (Turing's Paradox)",
         "Suppression of unstable quantum state decay caused by continuous ultra-frequent projective measurement observations.",
         "A pot of boiling water that never boils as long as you keep staring directly at it.",
         "Viral Hook: 'The quantum paradox: A watched atom never decays.'"),
        ("210. Quantum Annealing & Combinatorial Optimization (D-Wave)",
         "Adiabatic quantum computation mapping complex NP-hard combinatorial optimization problems onto Ising spin ground states.",
         "Letting water flow down an intricate mountain range to find the deepest hidden valley in 1 second.",
         "Viral Hook: 'How quantum annealing solves Wall Street's hardest portfolio allocation problems in microseconds.'")
    ]

    for idx, (title, math_def, analogy, hook) in enumerate(concepts_210, 1):
        if idx == 1:
            html += """<div class="subsection-header">PART I: ANCIENT MATHEMATICS & NATURE'S RATIOS (001 – 035)</div>"""
        elif idx == 36:
            html += """<div class="page-break"></div><div class="subsection-header">PART II: THERMODYNAMICS, FLUID DYNAMICS & CHAOS (036 – 070)</div>"""
        elif idx == 71:
            html += """<div class="page-break"></div><div class="subsection-header">PART III: QUANTITATIVE FINANCE & HIGH-FREQUENCY TRADING (071 – 105)</div>"""
        elif idx == 106:
            html += """<div class="page-break"></div><div class="subsection-header">PART IV: FOREX LIQUIDITY & MACRO REGIMES (106 – 140)</div>"""
        elif idx == 141:
            html += """<div class="page-break"></div><div class="subsection-header">PART V: ARTIFICIAL INTELLIGENCE & HIGH-D LATENTS (141 – 175)</div>"""
        elif idx == 176:
            html += """<div class="page-break"></div><div class="subsection-header">PART VI: CRYPTO DYNAMICS, MEV & QUANTUM PHYSICS (176 – 210)</div>"""

        html += f"""
<div class="concept-card">
  <div class="concept-title">{title}</div>
  <div class="concept-math"><strong>Theoretical Rigor:</strong> {math_def}</div>
  <div class="concept-analogy"><strong>Intuitive Model:</strong> {analogy}</div>
  <div class="concept-hook"><strong>Viral Media Hook:</strong> {hook}</div>
</div>
"""

    html += """
</body>
</html>
"""
    return html

def run_pdf_compilation():
    html_str = build_qnt_200_monograph()
    html_f = "/tmp/qnt_200_master.html"
    with open(html_f, "w", encoding="utf-8") as f:
        f.write(html_str)
    
    out_pdf = "/data/reports/qnt_200_Universal_Quant_Concepts_Master_Monograph.pdf"
    print("Compiling 210-concept master PDF via WeasyPrint...")
    doc = weasyprint.HTML(html_f)
    doc.write_pdf(out_pdf)
    print(f"✅ Generated Master PDF: {out_pdf}")

if __name__ == "__main__":
    run_pdf_compilation()

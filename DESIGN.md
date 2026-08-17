---
version: alpha
name: qnt-cream-black
description: Luxury Cream & Ivory academic design system with pitch-black typography and obsidian line architecture for qnt. master research monographs.
colors:
  primary: "#000000"
  secondary: "#0F172A"
  canvas: "#FAF8F5"
  surface: "#FFFFFF"
  surface-card: "#F4EFEA"
  surface-highlight: "#EFE9E1"
  border: "#000000"
  border-subtle: "#CBD5E1"
  accent-emerald: "#047857"
  text-primary: "#000000"
  text-secondary: "#1E293B"
  text-muted: "#475569"

typography:
  font-family: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
  font-src: "file:///data/fonts/InterVariable.ttf"
  font-weights:
    regular: 400
    medium: 500
    semibold: 600
    bold: 700
    extrabold: 800
    black: 900
  leading:
    dense: 1.25
    body: 1.30
    header: 1.15

page-architecture:
  size: "letter"
  margin: "10mm 10mm 10mm 10mm"
  flow: "continuous-dense"
  rules:
    - "Strictly eliminate page-break-after: always"
    - "Apply break-inside: avoid ONLY to individual cards, tables, and access boxes"
    - "Apply break-after: avoid to volume and module headers"
    - "100% canvas utilization from top to bottom with zero empty voids"

branding:
  name: "qnt."
  logo-asset: "file:///data/project_qnt/assets/qnt_logo.jpg"
  attribution: "qnt. Quantitative Wealth Systems"
  intelligence-shield: "Zero external social handles (@...); institutional statutory citations only"

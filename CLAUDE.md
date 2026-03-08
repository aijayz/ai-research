# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a research and documentation repository focused on:
- AI Agent concepts and architecture
- DeFi structured products research (bilingual: English and Chinese)
- MCP (Model Context Protocol) setup guides

## Project Structure

```
/
├── AI_Agent_Guide.md           # AI Agent concepts, architecture, and use cases
├── Augment/
│   └── augment-mcp-setup-guide.md  # MCP server configuration for Augment
└── structured product/
    ├── defi-structured-products-en.md   # English research document
    ├── defi-structured-products-zh.md   # Chinese research document
    ├── *.html, *.pptx, *.svg           # Generated presentations and visualizations
```

## Document Types

- **Markdown (.md)**: Primary source documents
- **HTML (.html)**: Web-rendered versions of research documents
- **PowerPoint (.pptx)**: Presentation versions for sharing
- **SVG (.svg)**: Visualizations (risk matrices, tech radars)

## Bilingual Content

The "structured product" directory contains parallel English (en) and Chinese (zh) versions of the same research. When updating one, consider whether the translation needs updating as well.

## No Build System

This repository contains static documentation. There are no build, test, or lint commands. The venv directory is empty (no project Python scripts).

## GitHub Safety

Per the global CLAUDE.md, always ask for confirmation before any destructive GitHub operations (deleting repos/branches, force pushing, closing issues/PRs).
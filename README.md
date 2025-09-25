# Synaptics Astra SR SDK User Guide

This repository contains the Sphinx documentation for the Synaptics Astra SR SDK User Guide, hosted on GitHub Pages with automated CI/CD deployment.

## 🚀 Quick Start

### Automated Deployment (Recommended)

The repository includes a **GitHub Actions workflow** that automatically builds and deploys documentation:

- **Triggers**: Push to `main` branch, pull requests, or manual trigger
- **Build**: Uses Docker with Synaptics Sphinx theme builder
- **Deploy**: Automatically deploys to GitHub Pages

Simply push your changes and the documentation will be built and deployed automatically!

### Manual Build Commands

| Command | Description |
|---------|-------------|
| `./build.sh` | **Docker build** (matches CI/CD) |
| `make html` | Build to `_build/html/` (traditional Sphinx) |
| `make github` | Build to `docs/` folder (for GitHub Pages /docs config) |
| `make root` | Build directly to root directory (for GitHub Pages root config) |
| `make deploy` | Clean root + build to root (one-step deployment) |
| `make clean-root` | Clean HTML files from root directory |
| `make clean` | Clean `_build/` directory |

### Development Workflow

**Automated (Recommended):**
```bash
# Edit your .rst/.md files
git add .
git commit -m "Update documentation"
git push origin main
# GitHub Actions will build and deploy automatically
```

**Manual deployment:**
```bash
./build.sh  # Docker build
git add .
git commit -m "Update documentation"
git push origin main
```

**Local development:**
```bash
make html
cd _build/html && python3 -m http.server 8000
```

## 📁 Repository Structure

```
├── .github/workflows/       # GitHub Actions CI/CD
│   └── build-and-deploy.yml # Auto-build and deploy workflow
├── build.sh                 # Docker-based build script
├── conf.py                  # Sphinx configuration
├── Makefile                 # Build commands
├── index.rst                # Main documentation index
├── *.rst, *.md              # Documentation source files
├── _static/                 # Static assets (images, PDFs)
├── _templates/              # Custom Sphinx templates
├── _build/                  # Traditional Sphinx build output
├── docs/                    # GitHub Pages build output (/docs config)
└── *.html                   # Root directory build output (root config)
```

## 🐳 Docker Build

The repository uses a custom Docker container for building:

- **Image**: `ghcr.io/syna-astra-dev/synaptics-sphinx-theme/builder:latest`
- **Purpose**: Builds Sphinx documentation with custom Synaptics theme
- **Usage**: `./build.sh`

## 🌐 GitHub Pages Configuration

This repository supports automatic deployment to GitHub Pages:

1. **GitHub Actions**: Builds and deploys automatically on push
2. **Pages Source**: Deploy from GitHub Actions (recommended)
3. **Alternative**: Manual deployment to root directory or `/docs` folder

## 📝 Adding Content

1. **Create/Edit** `.rst` or `.md` files
2. **Add to index.rst** if needed for navigation
3. **Commit and push** - GitHub Actions will build and deploy automatically

## 🔧 PDF Integration

PDFs are automatically included via `html_extra_path` in `conf.py`. Place PDF files in the root directory and reference them in your documentation as `_static/filename.pdf`.

## 🎨 Theme

Uses a custom Synaptics Sphinx theme via Docker container for consistent branding and styling.

## 🔄 CI/CD Pipeline

The GitHub Actions workflow:

1. **Triggers** on push to main branch
2. **Builds** documentation using Docker
3. **Verifies** build output
4. **Deploys** to GitHub Pages automatically
5. **Provides** build status and deployment URL

---

**Live Site**: https://rajdeep-syna.github.io/

**Documentation Sections**:
- OpenOCD Debug Guide for xSPI Flash Driver
- OV5647 DataSheet
- RGB IR Sensor Guide

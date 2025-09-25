# GitHub Actions Workflows

## Build and Deploy Documentation

This workflow (`build-and-deploy.yml`) automatically builds and deploys the Sphinx documentation to GitHub Pages.

### How it works:

1. **Triggers**: 
   - Automatically on push to `main` or `master` branch
   - On pull requests to `main` or `master`
   - Manually via GitHub Actions UI

2. **Build Process**:
   - Uses the existing `build.sh` script with Docker
   - Runs the Synaptics Sphinx theme builder container
   - Generates HTML files in the repository root

3. **Deployment**:
   - Uploads the entire repository root as a GitHub Pages artifact
   - Deploys to GitHub Pages automatically

### Docker Container:
- **Image**: `ghcr.io/syna-astra-dev/synaptics-sphinx-theme/builder:latest`
- **Purpose**: Builds Sphinx documentation with custom Synaptics theme
- **Environment**: Passes `GITHUB_REF` and `GITHUB_REPOSITORY` variables

### Manual Deployment:
You can also trigger the workflow manually:
1. Go to Actions tab in GitHub
2. Select "Build and Deploy Documentation"
3. Click "Run workflow"

### Local Testing:
To test the build locally:
```bash
chmod +x build.sh
./build.sh
```

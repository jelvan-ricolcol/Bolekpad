# Bolek Desk Deployment Guide

This guide provides clear, step-by-step instructions for downloading your workspace files, creating a GitHub repository, and deploying your application to **Cloudflare Pages** (and optionally Cloudflare Workers for full-stack API capabilities).

Because we have implemented a **robust, zero-dependency offline sandbox fallback**, your application will run **100% flawlessly** as a purely static Single-Page Application (SPA) on Cloudflare Pages without needing any backend server configured!

---

## 1. How to Download Your Project Files

You can download your entire project from AI Studio as a ready-to-run ZIP archive:
1. Click the **Settings** menu (gear icon) in the top right or bottom left of your AI Studio workspace.
2. Select **Export as ZIP** or **Export to GitHub**.
3. If you download the ZIP, extract it to a local folder on your computer.

---

## 2. Pushing Your Code to GitHub

1. Open your terminal (macOS/Linux) or Command Prompt/Git Bash (Windows) and navigate to your project directory:
   ```bash
   cd /path/to/extracted/bolek-desk
   ```
2. Initialize a local Git repository:
   ```bash
   git init
   ```
3. Add all files to stage:
   ```bash
   git add .
   ```
4. Commit your files:
   ```bash
   git commit -m "Initial commit: Bolek Desk complete workspace"
   ```
5. Create a new repository on [GitHub](https://github.com/new). Do **not** initialize it with a README, `.gitignore`, or License (as they are already provided in this project).
6. Link your local repository to GitHub and push your code:
   ```bash
   git branch -M main
   git remote add origin https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git
   git push -u origin main
   ```

---

## 3. Deploying to Cloudflare Pages (Recommended - Free & Fast)

Cloudflare Pages is the best place to host high-performance React SPAs. It is free, globally distributed, and hooks up directly to your GitHub repository for automatic CD/CD (builds every time you push).

### Step 3.1: Connect Your GitHub Repository
1. Log in to your [Cloudflare Dashboard](https://dash.cloudflare.com/).
2. In the left navigation, click **Workers & Pages**.
3. Click **Create** and select the **Pages** tab.
4. Click **Connect to Git** and authorize Cloudflare to access your GitHub account.
5. Select your newly created `bolek-desk` repository and click **Begin setup**.

### Step 3.2: Configure Build & Deployment Settings
On the configuration screen, apply the following build settings:
- **Project Name:** `bolek-desk` (or your preferred name)
- **Production Branch:** `main`
- **Framework Preset:** `Vite` (if listed) or select **None**
- **Build Command:** `npm run build`
- **Build Output Directory:** `dist`

Click **Save and Deploy**. Cloudflare will download your dependencies, build the React SPA, and provide you with a secure, live production URL (e.g., `https://bolek-desk.pages.dev`).

---

## 4. Full-Stack / Express Backend (Optional)

If you explicitly want the server-side `/api/boleksend/send` backend (which prints dispatch logs in the terminal console) to run under Cloudflare, you can migrate the `server.ts` Express route to a lightweight serverless function using **Cloudflare Pages Functions**.

### How to use Pages Functions:
1. In your project, create a directory called `functions` at the root:
   ```bash
   mkdir functions
   ```
2. Inside `functions`, create an api handler file `functions/api/boleksend/send.ts` to handle the serverless API requests:
   ```typescript
   export async function onRequestPost({ request }) {
     try {
       const { to, subject, message } = await request.json();
       
       if (!to || !subject || !message) {
         return new Response(JSON.stringify({ error: "Missing required fields" }), {
           status: 400,
           headers: { "Content-Type": "application/json" }
         });
       }

       // Simulated dispatch logging
       console.log(`Boleksend Serverless Dispatch to: ${to}`);

       return new Response(JSON.stringify({ success: true, message: "Dispatched via Cloudflare Pages Function." }), {
         headers: { "Content-Type": "application/json" }
       });
     } catch (err) {
       return new Response(JSON.stringify({ error: "Invalid payload" }), {
         status: 400,
         headers: { "Content-Type": "application/json" }
       });
     }
   }
   ```
3. Commit and push this change to GitHub. Cloudflare Pages will automatically detect the `functions/` folder and host your API endpoints serverlessly!

---

## 5. Local Development Mode

To run and test the application with its native full-stack Express server locally:
1. Install dependencies:
   ```bash
   npm install
   ```
2. Run the development command:
   ```bash
   npm run dev
   ```
3. Open `http://localhost:3000` in your web browser.

---

## 6. Google OAuth Configuration

To support Google Signup and Login in your production or development environments, make sure to:
1. Open the [Google Cloud Console Credentials page](https://console.cloud.google.com/apis/credentials).
2. Create an **OAuth 2.0 Client ID** (Web application).
3. Set your **Authorized JavaScript origins** to your app URL (e.g., `https://your-app.run.app`).
4. Set your **Authorized redirect URIs** to your callback URL (e.g., `https://your-app.run.app/auth/callback`).
5. Set the following environment secrets in your hosting dashboard (e.g. AI Studio, Cloudflare, or local `.env`):
   - `GOOGLE_CLIENT_ID`: Your Google OAuth client ID.
   - `GOOGLE_CLIENT_SECRET`: Your Google OAuth client secret.

---

## 7. Passkeys (WebAuthn) Authentication

The application features a modern hybrid Passkeys (WebAuthn) authentication flow:
- **Production Standard**: If accessed over a secure context (`https://` or `localhost`) and WebAuthn is supported by the browser, the application utilizes the native `navigator.credentials` WebAuthn standard API to create and authenticate platform credentials (using Windows Hello, Apple Touch ID / Face ID, or security keys).
- **Environment Fallback**: For contexts where the application is executed within iframe sandboxes or non-HTTPS preview frames (e.g., standard staging/review containers), a highly polished, interactive visual biometric verification simulator is automatically used. This allows testing the full biometric experience seamlessly.
- **Instant Test Feature**: When clicking the **Passkey** button on the Login screen, if no passkeys are yet registered in the local browser cache, the user is offered a prompt to generate a secure virtual demonstration credential instantly to test the complete passwordless biometric login.
- **Passkeys Settings**: Users can register and revoke multiple passkeys on-the-fly under the **Security tab** inside their **Profile Settings** interface.

---

## 8. Mobile Responsiveness & Swipeable Horizontal Board

To achieve high-end mobile usability on small screens, the application features a custom swipeable horizontal layout system:
- **Horizontal Swiping (Kanban Board)**: On screens below `768px`, the multi-column board is rendered as a fluid horizontal pager using native, high-performance CSS Scroll Snap (`snap-x snap-mandatory`). Users can swipe left and right natively to browse columns seamlessly.
- **Bi-directional Tab Synchronization**: Swiping automatically triggers a scroll event listener that updates the highlighted active column pill in the top navigation tab bar in real-time. Conversely, tapping any column tab smoothly scrolls the swipe container directly to that column's index.
- **Ultra-Compact Login Page**: The glassmorphic login card features custom `@media` scaling rules on mobile viewports that reduce margins, input paddings, and font sizes to prevent vertical scrolling and deliver an elegant, comfortable, fit-to-screen appearance on small screens.
- **Responsive Logo Selector**: Dynamically uses a high-definition pixel-perfect PNG logo asset on mobile screens to prevent SVG pixelation and scaling distortion, ensuring flawless branding representation on all displays.


🔐 Secure Authentication System using GitHub OAuth Apps
========================================================

A secure and efficient authentication system built using GitHub OAuth Applications, designed to facilitate user login through GitHub accounts while maintaining security and ease of use.

🧠 Features
-----------
- OAuth 2.0 Authorization Code Flow.
- Secure storage and handling of tokens.
- Error handling during authentication.
- Redirect handling after successful login.
- Clean and minimal frontend integration.

🚀 Getting Started
------------------

🔧 Prerequisites:
- Node.js installed.
- GitHub account with a registered OAuth App.

📥 Installation:
1. Clone the repository:

```bash
git clone https://github.com/other3li/Secure-Authentication-System-using-GitHub-OAuth-Apps.git
cd Secure-Authentication-System-using-GitHub-OAuth-Apps
```

2. Install the dependencies:

```bash
npm install
```

3. Create a `.env` file and add your GitHub OAuth credentials:

```
CLIENT_ID=your_github_client_id
CLIENT_SECRET=your_github_client_secret
REDIRECT_URI=http://localhost:3000/callback
```

4. Run the application:

```bash
npm start
```

5. Open your browser and navigate to:

```
http://localhost:3000/
```

🛠️ How Authentication Works
-----------------------------
1. User clicks "Login with GitHub".
2. User is redirected to GitHub OAuth authorization page.
3. After successful authentication, GitHub redirects back with a temporary code.
4. Server exchanges the code for an access token.
5. User is authenticated and redirected to a protected resource.

🔍 Technologies Used
---------------------
- Backend: Node.js, Express.js
- Authentication: GitHub OAuth Apps
- Frontend: HTML/CSS (basic)
- Environment Management: dotenv

📁 Project Structure
---------------------
```
/secure-auth-system/
├── app.js
├── package.json
├── .env
├── views/
│   ├── home.html
│   └── callback.html
├── public/
│   └── styles.css
└── README.md
```

📚 References
-------------
- [GitHub OAuth Apps Documentation](https://docs.github.com/en/apps/oauth-apps)  
- [Node.js Express Framework](https://expressjs.com/)  
- [Dotenv for Environment Variables](https://www.npmjs.com/package/dotenv)  
- [Official GitHub REST API Reference](https://docs.github.com/en/rest)

⚠️ Important Notes
-------------------
- Ensure your OAuth App is registered correctly: [GitHub Developer Settings](https://github.com/settings/developers)
- Never expose your `CLIENT_SECRET` in public repositories.

🧑‍💻 Creator
------------
Designed and developed by **Ali Mohamed Oqab**

📄 License
----------
This project is open-source and distributed under the MIT License. See the LICENSE file for more information.

🔗 Sources Used
---------------
- [GitHub Docs: About READMEs](https://docs.github.com/en/repositories/working-with-files/using-files/about-readmes)
- [GitHub OAuth Apps Overview](https://docs.github.com/en/apps/oauth-apps/creating-oauth-apps/about-oauth-apps)
- [Best Practices for GitHub OAuth Security](https://docs.github.com/en/developers/apps/securing-oauth-apps)


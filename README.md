Secure Authentication System using GitHub OAuth Apps
A secure and efficient authentication system built using GitHub OAuth Applications, designed to facilitate user login through GitHub accounts while maintaining security and ease of use.

⭐designed and developed by ALI MOHAMED OQAB⭐

Project Description
This project implements OAuth 2.0 authentication flow with GitHub, allowing users to sign into a system securely using their GitHub credentials. It focuses on maintaining best security practices during the OAuth handshake and token management.

Features
OAuth 2.0 Authorization Code Flow.

Secure storage and handling of tokens.

Error handling during authentication.

Redirect handling after successful login.

Clean and minimal frontend integration.

Technologies Used
Backend: Node.js, Express

Authentication: GitHub OAuth Apps

Frontend: HTML/CSS (basic)

Environment Management: dotenv (.env files)

Project Structure
/secure-auth-system/
├── app.js
├── package.json
├── .env
├── views/
│ ├── home.html
│ └── callback.html
├── public/
│ └── styles.css
└── README.md

Installation & Setup
1.Clone the Repository :
git clone https://github.com/other3li/Secure-Authentication-System-using-GitHub-OAuth-Apps.git
cd Secure-Authentication-System-using-GitHub-OAuth-Apps


2.Install Dependencies :
npm install


3.Create a .env File Add your GitHub OAuth credentials :
CLIENT_ID=your_github_client_id
CLIENT_SECRET=your_github_client_secret
REDIRECT_URI=http://localhost:3000/callback


4.Run the Application :
npm start


5.Access the App Open your browser and navigate to:
http://localhost:3000/
How Authentication Works
User clicks "Login with GitHub".

Redirects to GitHub OAuth authorization page.

Upon successful authentication, GitHub redirects back to the application with a temporary code.

The server exchanges the code for an access token.

User is authenticated and redirected to a protected resource.

References
GitHub OAuth Apps Documentation: https://docs.github.com/en/apps/oauth-apps

Node.js Express Framework: https://expressjs.com/

Dotenv for Environment Variables: https://www.npmjs.com/package/dotenv

Official GitHub REST API Reference: https://docs.github.com/en/rest

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
Distributed under the MIT License. See LICENSE file for more information.

Notes
Make sure you registered your OAuth App correctly on GitHub Developer Settings: https://github.com/settings/developers

Always keep your CLIENT_SECRET secure. Never expose it in public repositories.

Sources Used
GitHub Docs: About READMEs: https://docs.github.com/en/repositories/working-with-files/using-files/about-readmes

GitHub OAuth Apps Overview: https://docs.github.com/en/apps/oauth-apps/creating-oauth-apps/about-oauth-apps

Best Practices for GitHub OAuth Security: https://docs.github.com/en/developers/apps/securing-oauth-apps




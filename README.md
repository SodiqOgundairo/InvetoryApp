# InvetoryApp

Built with Django, &amp; Bootstrap

## Hosting on Heroku from GitHub

1.  **Create a Heroku account:** If you don't already have one, sign up for a free account at [heroku.com](https://www.heroku.com/).
2.  **Install the Heroku CLI:** Follow the instructions for your operating system at [devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli).
3.  **Log in to Heroku:** Open your terminal and run the following command:
    ```
    heroku login
    ```
4.  **Create a new Heroku app:**
    ```
    heroku create <your-app-name>
    ```
5.  **Add a `Procfile`:** Create a new file named `Procfile` in the root of your project with the following content:
    ```
    web: gunicorn InvApp.wsgi
    ```
6.  **Configure environment variables:** In the Heroku dashboard for your app, navigate to the "Settings" tab and click "Reveal Config Vars." Add a new variable with the key `SECRET_KEY` and a unique, randomly generated value.
7.  **Connect to GitHub:** In the Heroku dashboard, navigate to the "Deploy" tab and connect your GitHub account.
8.  **Enable automatic deploys:** Select the repository for your app and enable automatic deploys from the `main` branch.
9.  **Deploy your app:** Click the "Deploy Branch" button to deploy your app for the first time.

# Telegram bot

## Running
To run the application in development mode run:
  ```docker-compose up```
PS. 
You need to create a `serviceAccount.json` file at the root folder with a service account from google cloud to configure Firebase.
Also, you need to create a `config.json` file in the root folder with two keys:
- telegram_token: `the telegram api token`
- google_application_credentials: `serviceAccount.json`
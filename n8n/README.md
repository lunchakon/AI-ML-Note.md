# n8n Google Sheets YouTube Telegram Integration

This project integrates Google Sheets, YouTube, and Telegram using n8n to automate the process of reading data from Google Sheets, fetching articles or videos from YouTube, summarizing key points, and posting the summaries to Telegram.

## Project Structure

```
n8n-google-sheets-youtube-telegram
├── workflows
│   ├── google-sheets-to-youtube.json
│   └── youtube-summary-to-telegram.json
├── docs
│   └── integration-setup.md
├── .env.example
├── docker-compose.yml
└── README.md
```

## Features

- **Google Sheets Integration**: Read data from Google Sheets to fetch links.
- **YouTube Integration**: Retrieve articles or videos from YouTube using the links obtained from Google Sheets.
- **Summarization**: Summarize key points from the fetched content.
- **Telegram Integration**: Post the summaries to a specified Telegram channel.

## Setup Instructions

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd n8n-google-sheets-youtube-telegram
   ```

2. **Environment Variables**: 
   - Copy the `.env.example` to `.env` and fill in the required API keys and configuration settings.

3. **Docker Setup**: 
   - Ensure Docker is installed and running.
   - Start the n8n application using Docker Compose:
     ```bash
     docker-compose up -d
     ```

4. **Access n8n**: 
   - Open your browser and navigate to `http://localhost:5678`.

5. **Import Workflows**: 
   - Import the workflows from the `workflows` directory into n8n.

6. **Follow Documentation**: 
   - Refer to `docs/integration-setup.md` for detailed setup instructions on integrating Google Sheets, YouTube, and Telegram.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes. 

## License

This project is licensed under the MIT License.


------------
# Integration Setup for Google Sheets, YouTube, and Telegram

This document provides step-by-step instructions on how to set up the integration between Google Sheets, YouTube, and Telegram using n8n.

## Prerequisites

1. **n8n Installed**: Ensure that you have n8n installed and running. You can use Docker to set it up as described in the `docker-compose.yml` file.
2. **Google Sheets API**: You need to enable the Google Sheets API and obtain the necessary credentials (API key or OAuth 2.0 client ID).
3. **YouTube Data API**: Enable the YouTube Data API and obtain the API key.
4. **Telegram Bot**: Create a Telegram bot using BotFather and obtain the bot token.

## Step 1: Configure Environment Variables

1. Copy the `.env.example` file to `.env` and fill in the required API keys and tokens:
   ```
   GOOGLE_SHEETS_API_KEY=your_google_sheets_api_key
   YOUTUBE_API_KEY=your_youtube_api_key
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_telegram_chat_id
   ```

## Step 2: Set Up Google Sheets Workflow

1. Open the `workflows/google-sheets-to-youtube.json` file in n8n.
2. Configure the Google Sheets node:
   - Set the credentials using the API key.
   - Specify the spreadsheet ID and range from which to read data.
3. Add any necessary nodes to process the data and extract links.

## Step 3: Set Up YouTube Summary Workflow

1. Open the `workflows/youtube-summary-to-telegram.json` file in n8n.
2. Configure the YouTube node:
   - Use the links obtained from the Google Sheets workflow.
   - Set up the parameters to fetch video details or articles.
3. Add a summarization node to process the fetched content.
4. Configure the Telegram node to send the summary to your chat.

## Step 4: Running the Workflows

1. Start the n8n application using Docker:
   ```
   docker-compose up
   ```
2. Access the n8n editor at `http://localhost:5678`.
3. Activate both workflows and monitor their execution.

## Conclusion

You have successfully set up the integration between Google Sheets, YouTube, and Telegram using n8n. You can now automate the process of reading data, fetching content, summarizing it, and posting to Telegram.
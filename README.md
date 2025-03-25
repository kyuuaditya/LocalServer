# LocalServer

A simple Python-based local server that allows you to serve files and retrieve your system's IP address, sending it to a Telegram bot for easy access.

## Features
- Runs a basic HTTP server to serve files from your machine.
- Retrieves the local IPv4 address of your computer.
- Sends the IP address to a Telegram bot for remote access.
- Automatically starts on boot.

## Installation
### Prerequisites
- Python 3.x installed
- `requests` module (for Telegram API requests)

To install `requests`, run:
```sh
pip install requests
```

## Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/kyuuaditya/LocalServer.git
   cd LocalServer
   ```

2. **Set Up Your Credentials**
   - Create a file named `credentials.py` in the same directory.
   - Add the following details:
     ```python
     BOT_TOKEN = "your_telegram_bot_token"
     CHAT_ID = "your_telegram_chat_id"
     ```
   - Replace `your_telegram_bot_token` and `your_telegram_chat_id` with your actual Telegram bot credentials.

3. **Run the Server**
   - Open `start_server.bat`, 
   The server will start, and your local IP address will be sent to your Telegram bot.

## Automating Server Startup on Boot
### Windows (Using Task Scheduler)
1. Open **Task Scheduler** (`Win + R`, type `taskschd.msc`, and press Enter).
2. Click **Create Basic Task** in the right panel.
3. Give the task a name (e.g., `LocalServer`) and click **Next**.
4. Choose **When I log on** as the trigger and click **Next**.
5. Choose **Start a Program** as the action and click **Next**.
6. Click **Browse** and select navigate to the folder and select `start_server.bat`.
   ```
   "C:\path\to\LocalServer\start_server.bat"
   ```
8. Click **Finish** to save the task.

Now, the server will start automatically when you log into Windows.

## Contributing
Feel free to submit issues or pull requests to improve this project!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


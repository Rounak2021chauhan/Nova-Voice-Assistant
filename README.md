# Nova - Voice Assistant 🚀

Nova is a Python-based voice assistant capable of performing various tasks like telling jokes, fetching news, searching YouTube, browsing the web, and providing weather updates — all through voice commands!

![Nova](Nova.jpg)

---

## 🗂 Project Structure
Assistant.py : Main file to run the voice assistant  
jokes.py : Tells random jokes  
news.py : Fetches latest news using an API  
selenium_web.py : Automates web browsing via Selenium  
selenium_yt.py : Searches and plays YouTube videos  
ss.py : Stores API keys securely  
weather.py : Provides weather information  
Nova.jpg : Project image/logo 

## ⚙️ Requirements

**Python version:** 3.8 or higher

### Install Dependencies

Run this command to install the required libraries:

```bash
pip install -r requirements.txt
```
  If you don’t have a requirements.txt file yet, create one with the following content:  

requests  
pyttsx3  
speechrecognition  
pyaudio  
selenium  
python-dotenv  
Make sure you have Google Chrome installed and download the matching ChromeDriver version for Selenium:  
https://sites.google.com/chromium.org/driver/  

## ▶️ How to Run the Project
Open your terminal, navigate to the project directory, and run:

```bash
python Assistant.py
```
Ensure your microphone and speakers are connected properly for voice input/output.  

## 🔐 API Keys
Create a file named ss.py in the project folder and add your keys like this:

weather_api_key = "YOUR_OPENWEATHERMAP_API_KEY"  
news_api_key = "YOUR_NEWS_API_KEY"  
⚠️ Keep your API keys secure and do not share them publicly.  

## 💡 Features
🎤 Voice interaction (speech recognition + TTS)  
🌦 Real-time weather updates  
📰 Fetch current news headlines  
😂 Random jokes  
🔍 Web browsing using Selenium  
🎬 YouTube search and play via voice commands  
📝 Notes  
 
If PyAudio fails to install, use these commands:

```bash
pip install pipwin
pipwin install pyaudio
```
Make sure chromedriver.exe is added to your system PATH or placed in the project directory.


## 📬 Contact
Feel free to fork the repo, contribute, or reach out for collaboration.

### Let me know if you want me to auto-generate the `requirements.txt` file or help with a GitHub setup.

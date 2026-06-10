# Site has been closed

# 🔍 YGG Torrent Scrapper

## ⚠️ LEGAL DISCLAIMER

**WARNING: This project is developed for purely educational and research purposes only.**

- ❌ **Web scraping may violate the terms of service of targeted websites**
- ❌ **Using this code to access copyrighted content is illegal**
- ❌ **The developers of this project are not responsible for misuse of this code**
- ❌ **Using this scrapper may violate copyright laws in your country**

**🚨 USE THIS CODE AT YOUR OWN RISK AND RESPONSIBILITY**

This project is intended for:
- ✅ Understanding web scraping techniques
- ✅ Learning automation with Selenium/Botasaurus
- ✅ Studying website protection mechanisms
- ✅ Academic and educational research

## 🚀 Project Integration & Real-World Usage

This scrapper serves as a **foundational template** that can be integrated into larger projects:

### 🏗️ Integration Examples

- **Media Management Systems**: Integrate torrent metadata into personal media libraries
- **Research Platforms**: Collect data for academic studies on P2P networks
- **Monitoring Tools**: Track availability and popularity of specific content
- **API Development**: Build REST APIs that expose torrent search functionality
- **Data Analytics**: Analyze trends in torrent categories and user behavior

### 🔧 Extensibility Features

The modular architecture allows easy customization:
- **Custom Search Filters**: Extend search functionality with size, date, quality filters
- **Database Integration**: Store scraped data in PostgreSQL, MongoDB, or SQLite
- **API Wrapper**: Transform into a microservice with FastAPI or Flask
- **Notification System**: Add alerts for new torrents matching criteria
- **Batch Processing**: Scale to handle multiple concurrent search operations

## 📋 Project Description

This automated scrapper extracts torrent information from YGG Torrent using:

- **Botasaurus**: Advanced web scraping framework
- **Selenium WebDriver**: Browser automation
- **Python 3.12**: Programming language
- **Dev Container**: Containerized development environment

### 🎯 Features

- 🔐 Automatic login with credentials
- 🔍 Torrent search by term
- 📊 Metadata extraction (name, size, seeders, leechers, etc.)
- 📸 Screenshot capture for debugging
- 🏷️ Automatic torrent categorization
- 🛡️ Cloudflare protection bypass

## 🚀 Installation and Usage with Dev Container

### Prerequisites

- **Docker** installed on your system
- **Visual Studio Code** with "Dev Containers" extension
- **Git** to clone the repository

### Step 1: Clone the repository

```bash
git clone <REPO_URL>
cd TrustScrapper
```

### Step 2: Configure credentials

Create a `.env` file at the project root:

```bash
# .env file
USERNAME=your_ygg_username
PASSWORD=your_ygg_password
```

⚠️ **Important**: Add `.env` to your `.gitignore` to avoid exposing your credentials!

### Step 3: Open with Dev Container

1. Open the project in VS Code
2. A notification will appear: "Reopen in Container" → Click it
3. Or use `Ctrl+Shift+P` → "Dev Containers: Reopen in Container"

The container will automatically:
- 🐍 Install Python 3.12
- 🌐 Install Chromium and Xvfb
- 📦 Install Python dependencies
- ⚙️ Configure the development environment

### Step 4: Using the scrapper

```python
from src.scraper import extract_torrents_data
from src.login import login_to_ygg
from src.search import search_torrents
from botasaurus.browser import Driver

# Initialize driver
driver = Driver()

try:
    # Login to YGG
    login_url, login_title = login_to_ygg(driver)
    print(f"Connected: {login_title}")
    
    # Search torrents
    search_url, search_title = search_torrents(driver)
    print(f"Search performed: {search_title}")
    
    # Extract data
    torrents = extract_torrents_data(driver)
    
    # Display results
    for torrent in torrents:
        print(f"📁 {torrent['name']}")
        print(f"   Type: {torrent['type']}")
        print(f"   Size: {torrent['size']}")
        print(f"   Seeders: {torrent['seed']}")
        print(f"   Leechers: {torrent['leech']}")
        print("---")
        
finally:
    driver.quit()
```

## 📁 Project Structure

```
TrustScrapper/
├── .devcontainer/
│   └── devcontainer.json     # Dev container configuration
├── src/
│   ├── __init__.py          # Python package
│   ├── config.py            # Configuration and URLs
│   ├── login.py             # Login management
│   ├── search.py            # Search functions
│   ├── scraper.py           # Data extraction
│   ├── screenshots.py       # Screenshot capture
│   └── static.py            # Torrent categories
├── requirements.txt         # Python dependencies
├── .env                     # Credentials (to create)
└── README.md               # This documentation
```

## ⚙️ Configuration

### Modify search term

In `src/config.py`:

```python
SEARCH_TERM = "Your search term"
```

### Add categories

In `src/static.py`:

```python
CATEGORIES = {
    "2157": "Emulator",
    "2148": "Music", 
    "2151": "Audio",
    "2189": "Adult Film",
    "2183": "Film",
    # Add your categories here
}
```

## 🛠️ Development

### Debugging

The project includes screenshot functions:

```python
from src.screenshots import take_screenshots

# Take a screenshot at any time
screenshot_path = take_screenshots(driver, "debug_step")
print(f"Screenshot saved: {screenshot_path}")
```

### Logs and monitoring

Botasaurus provides detailed logs automatically. Monitor the console for:
- ✅ Successful connections
- ❌ Navigation errors
- 🔄 Scraping steps
- ⏱️ Execution time

## 🚨 Legal and Ethical Considerations

### Respect robots.txt

Always check the site's `robots.txt` file:
```
https://ygg.re/robots.txt
```

### Limit request frequency

- Add delays between requests (`time.sleep()`)
- Don't overload servers
- Respect rate limits

### Responsible use

- 🚫 Don't use this code for illegal activities
- 🚫 Don't redistribute copyrighted content
- 🚫 Don't maliciously bypass security measures
- ✅ Use only for learning and research

## 📚 Educational Resources

- [Botasaurus Documentation](https://botasaurus.com/)
- [Selenium Python Guide](https://selenium-python.readthedocs.io/)
- [Web Scraping Legality](https://blog.apify.com/is-web-scraping-legal/)

## 🤝 Contribution

Educational contributions are welcome:
- 📖 Documentation improvements
- 🧪 Unit test additions
- 🛡️ Error handling improvements
- 🎨 Code optimization

## 📄 License

This project is distributed under MIT license for educational purposes only.

---

**⚠️ FINAL REMINDER: This project is strictly intended for education and research. Using it to illegally access protected content is prohibited and is your sole responsibility.**

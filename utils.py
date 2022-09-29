import urllib

def create_options(options, headless):
    if headless:
        options.add_argument("--headless")
    
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-crash-reporter")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-in-process-stack-traces")
    options.add_argument("--disable-logging")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--log-level=3")
    options.add_argument("--output=/dev/null")
    options.add_argument("user-data-dir=C:/Users/jonat/AppData/Local/Google/Chrome/User Data/Selenium")
    
    return options

def parse_greeting(greeting):
    return urllib.parse.quote(f"Olá!")
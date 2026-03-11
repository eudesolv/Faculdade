import pandas as pd
import time
from playwright.sync_api import sync_playwright

def main():
    tweets = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://x.com/login")
        
        print("Faça o login e pressione ENTER...")
        input()
        
        page.goto("https://x.com/FalleNCS")
        time.sleep(10)
        
        for _ in range(25):
            for tweet in page.query_selector_all('article[data-testid="tweet"]'):
                try:
                    tweets.append({
                        "autor": tweet.query_selector('[data-testid="User-Name"]').inner_text(),
                        "descricao": tweet.query_selector('[data-testid="tweetText"]').inner_text(),
                        "data": tweet.query_selector('time').get_attribute('datetime')
                    })
                except:
                    pass
            page.keyboard.press("End")
            time.sleep(3)

    pd.DataFrame(tweets).drop_duplicates().to_csv("tweets_sza.csv", index=False)
    print(f"{len(tweets)} tweets salvos!")

if __name__ == "__main__":
    main()
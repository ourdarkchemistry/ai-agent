from playwright.sync_api import sync_playwright

class Browser:
    def __init__(self):
        self.pw = sync_playwright().start()
        self.browser = self.pw.chromium.launch(headless=False, slow_mo=300)
        self.page = self.browser.new_page()

    def goto(self, url: str):
        self.page.goto(url)

    def click(self, selector: str):
        self.page.click(selector)

    def type(self, selector: str, text: str):
        self.page.fill(selector, text)

    def content(self):
        return self.page.content()

    def screenshot(self, path="screen.png"):
        self.page.screenshot(path=path)

    def close(self):
        self.browser.close()
        self.pw.stop()

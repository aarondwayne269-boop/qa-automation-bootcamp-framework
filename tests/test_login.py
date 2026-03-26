from selenium import webdriver

def test_open_page():
    driver = webdriver.Chrome()
    driver.get("https://example.com")

    assert "Example" in driver.title

    driver.quit()

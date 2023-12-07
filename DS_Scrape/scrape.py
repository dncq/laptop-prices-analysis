from selenium import webdriver
import json
import os

def scrape_and_save_data(page_number):
    # Define Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')

    # Initialize the WebDriver with the defined options
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the website
        url = f'https://www.newegg.com/p/pl?N=100017489&PageSize=96&page={page_number}'  # Replace with the URL of the website you want to scrape
        driver.get(url)

        # Use JavaScript to extract the window.__initialState__ content
        script = "return JSON.stringify(window.__initialState__);"
        json_data = driver.execute_script(script)

        # Parse the JSON data
        try:
            window_initial_state = json.loads(json_data)
            save_directory = "assets/new_egg/scraped_json"

            # Create the directory if it doesn't exist
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)

            # Construct the filename based on the page number
            filename = f"{save_directory}/page{page_number}_data.json"

            with open(filename, 'w') as file:
                json.dump(window_initial_state, file)

            print(f"Data for page {page_number} saved successfully.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    finally:
        driver.quit()

    return window_initial_state

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python your_script_name.py <page_number>")
        sys.exit(1)

    try:
        page_number_to_scrape = int(sys.argv[1])
    except ValueError:
        print("Invalid page number. Please enter a valid integer.")
        sys.exit(1)

    scraped_data = scrape_and_save_data(page_number_to_scrape)

    # Access the loaded data as needed
    product_dict = scraped_data["Products"]
    print(len(product_dict))
    print(product_dict[95]['ItemCell']['Description']['WebDescription'])


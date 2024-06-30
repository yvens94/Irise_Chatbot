from bs4 import BeautifulSoup
import requests
import os
import json

#Urls to scrape dictionary
URLs={
    "about Interfaithrise, contact and resources": "https://interfaithrise.org/",

    "Our partners & Community collaborators":"https://interfaithrise.org/coalition-members/",

    "Jobs":"https://interfaithrise.org/employment-opportunities/",

    "client services":" https://interfaithrise.org/client-services/",

    "Other Agencies info": "https://interfaithrise.org/client-services/",

    "Case management":"https://interfaithrise.org/case-management-2/",

    "employment, job search and other job readiness services":"https://interfaithrise.org/employment-services/",

    "English Classes and carreer training":"https://interfaithrise.org/employment-services/",

    "Who do we help and how can we help":"https://interfaithrise.org/preferred-communities/",

    "Cash assistance": "https://interfaithrise.org/refugee-cash-assistance/",

    "School":"https://interfaithrise.org/refugee-school-impact/",

    "Career development": "https://interfaithrise.org/career-pathways/"
                        
                            }




#browsers user agents dict
user_agents = {
    "chrome": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "firefox": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "safari": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "edge": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.864.64 Safari/537.36 Edg/91.0.864.64",
    "android": "Mozilla/5.0 (Linux; Android 11; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
}
#use user agent with the headers accordinly
def get_user_agent(browser):
    if browser.lower() in user_agents:
        return user_agents[browser.lower()]
    else:
        # If the browser is not found in the user_agents dictionary, default to Chrome
        return user_agents["chrome"]


def print_text_with_links(url, headers):
    # Send a GET request to the specified URL
    response = requests.get(url=url, headers=headers)
     # Initialize a variable to hold all scraped text
    text_body = ""
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose()
        
        # Print the text content of the webpage
        for element in soup.find_all(['p', 'a']):
            if element.name == 'a' and 'href' in element.attrs:
                text_body += (f'{element.get_text()} ,({element["href"]})\n')
            else:
                text_body +=(f'{element.get_text()},\n')

        return text_body
    
            
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return "Failed to retrieve the"

#choose the broswe
browser ="edge"

#call the get user agent function
user_agent = get_user_agent(browser)

# Set the headers with the selected user agent
headers = {
    "User-Agent": user_agent
}

#Creating the folder to save the files folder we would maybe later upload to a database
curr_dir =os.getcwd()
data_dir = os.path.join(curr_dir, 'data','Raw_data')
path_json_dir= os.path.join(data_dir,'json_scraped')
os.makedirs(path_json_dir, exist_ok=True)

# puting everythin together and creating the Json files
for title, url in URLs.items():
    filepath=os.path.join(path_json_dir, f'{title}.json')
    print(f"\nScraping:{title}\n{'-'*40}")
    textscraped ={

        "title":title,
        "url":url,
        "body": print_text_with_links(url =url, headers=headers)
        
        }

    with open(filepath, 'w', encoding='utf-8') as json_file:
        json.dump(textscraped, json_file,ensure_ascii=False, indent=4)





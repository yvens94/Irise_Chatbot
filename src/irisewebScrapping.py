from bs4 import BeautifulSoup
import requests
import re

#url= "https://interfaithrise.org/employment-opportunities/"
# #fetch web page


# #chek if request was successful
# if response.status_code ==200:
#     #parse the content of the beautifulsoup
#     soup = BeautifulSoup(response.content, 'html.parser')
# else:
#     print("failed to retrieve the web page code:" ,response.status_code )

#print(soup.title.string)



# #print(soup.prettify())
# for link in soup.find_all('a'):
#     print (link.get('href'), "this the link for", link.text)


# print(soup.text)


# def print_text_with_links(soup):
#     for element in soup.descendants:
#         if isinstance(element, str):
#             print(element, end=' ')
#         elif element.name == 'a' and 'href' in element.attrs:
#             print(f"{element.get_text()} ({element['href']})", end=' ')

# print_text_with_links(soup)

URLs={
    "main page, about Interfaithrise, Contact,farm, donations and ressources links": "https://interfaithrise.org/",

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




url = "https://interfaithrise.org/employment-opportunities/"




user_agents = {
    "chrome": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "firefox": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "safari": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "edge": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.864.64 Safari/537.36 Edg/91.0.864.64",
    "android": "Mozilla/5.0 (Linux; Android 11; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
}

for browser, user_agent in user_agents.items():
    headers = {
        "User-Agent": user_agent}


def print_text_with_links(url):
    # Send a GET request to the specified URL
    response = requests.get(url, headers=headers)
    
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
                print(f'{element.get_text()} ({element["href"]})')
            else:
                print(element.get_text())
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Example usage
print_text_with_links(url)

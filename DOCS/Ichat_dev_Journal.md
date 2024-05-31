# Journal of the development of this project

## Part 1: Getting the data
### Download important pdfs, or get them from the documentations
### The Web scraper with BeautifulSoup to get the data on the Irise website on important information 

#### 5/29/2024
  - Started the webscraper
  - Define what urls we will scraped based on the information they have
  - Set all urls in one dictionary to scrape them all at once in the same format
  - Run into Headers issue to acces subsequent pages: solved it using the Microsoft edge headers
  - Set headers for Mozzilla, chrome, safari, edge and android so the scapper works with all of them using their respective user agent.
  - Got rid of the scripts and css styles to get only the texts
  code:    
        ```
          #Remove script and style elements

                for script_or_style in soup(['script', 'style']):
                    script_or_style.decompose()
        ```
  - Get the text element along with their links so the chatbot can always provide links in support of the answers that the user can go to.

#### 5/30/2024

- I got some of the pdfs and got the webscrapper to work, Next I will save the documents as json files
  they have the title but should we

#### 5/31/2024

- Finally getting the Json file to be assemble, 

- Issues:
  1-choosing the browser iterating over the browsers dict.
    - I set it up so we have a function that choose the user agent base on the broswer we specify and the code, would be probably good to just establish, chrome or edge


  2- saving the text after each element to just add the next itereration to it


  3- iterating over each url in URLs


- LESSONS LEARNED
  - webscraping with beautiful soup
  - Navigate HTML trees: tags, elements, descendants, scripts and styles etc..
  - Headers and user agents
  - generate json files
  - 
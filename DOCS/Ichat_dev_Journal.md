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
  - Use github better
  - create a dev journal
  - work better with path and files management


  6/2/2024
  Creating a folder for the pdfs
  and starting to work on the master json

    - first it will be necessary to change the pdf files into json
    -and then consolidate all the files into one json
  

  Learning to work with pydf

  6/4/2024
  Learned about embeddings and how the embeddigs models are created
  from one hot encoding to Hierachical Softmax


  6/5/2024

  Pull request using GIT PULL 
  
    too long names in github can't pull

    conflict in github
    After resolving the conflicts, use git add <resolved-file> to stage the changes, and then commit to complete the merge1.

    Instead of a regular git pull, consider using git pull --rebase. This option fetches the latest changes from the remote branch and applies your local changes on top of them.
    The advantage is that it avoids creating a merge commit, keeping your changes linear. However, you’ll still need to resolve any merge conflicts that arise.
    To set this as your default behavior for git pull, run: git config --global pull.rebase true1.

    clean repository tree
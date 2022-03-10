# Mission to Mars – Web Scraping with HTML/CSS  

## Overview of the project

The purpose of this project is to help Robin, a data scientist with an interest in outer space, to extract Mars data and images from various websites, store this data, and then use it to build a webpage. The webpage will contain a button that will run the scraping program when clicked, and automatically update the page with the newly scraped content.  

Below is a summary of the tools and the process used to accomplish this task:
- Chrome Developer Tools: Identify HTML components for content that’s of interest for our webpage
- Splinter: Automated web browser used to navigate pages to facilitate scraping process
- Beautiful Soup: Extract and parse website data using insight gained via Chrome Developer Tools
- MongoDB: NoSQL database used to store scraped Mars data
- Flask: Create a webpage to display our stored data
- Bootstrap: Customize and prettify our webpage

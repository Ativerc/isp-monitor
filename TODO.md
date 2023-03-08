# TODO

## Core
* Scraper
  - [ ] Scraper
  - [ ] Crawler + Scraper
  - [ ] Dynamic Website Handler   
- [ ] Logging In
- [ ] Data Processor
- [ ] Supported ISPs List


## ISP
- [ ] ISP Constants File:
    * Scraping Type [Scrape, Crawl-Scrape, Dynamic]
    * ISP Login Type
    * Login URL
    * Base URL
- [ ] Data Metadata yml File with: 
    * Each data in these profile info pages of ISPs are usually in the form of `Tag: Value`. For example: `Email: youremailid@email.com`. Both the tag and value are important.
    * So the yml file to target and scrape the data:
    ```yml
    Username:
      tag: 
        visible_tag: "Username" # Create
        invisible_tag_value: "" # I don't know why this is here?? Will try to find later.
        selector: "#user_widget > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(1) " # XPath to data's Tag
        type: string # type of the value in data's Tag
      value:
        type: string # type of the value
        visible_value: ""
        selector: "#user_widget > div:nth-child(2) > div > div:nth-child(1) > div > div:nth-child(1) > a"  # Xpath to value
      property: # Some metadata about the data
        private: False # Is the data personally identifiable info. This is used by Data Processor to hide the data when outputting the data in some cases.
        core-data: True # Some isp-specific metadata.
    ```

## API
* Which ISP are supported?
* Get data for isp-credentials combo. _How do I secure this though?_
* 
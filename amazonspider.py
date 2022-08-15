import scrapy
import pandas as pd

class AmazonspiderSpider(scrapy.Spider):
    name = 'amazonspider'
    allowed_domains = ['amazon.nl']
    
    def start_requests(self):
        df = pd.read_csv(r'C:\Users\Gebruiker\Desktop\merchants2 clean.csv')

        urls = df['href']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response): 
        reviews = response.css('#feedback-table div.feedback-row')

        for review in reviews:
            
            yield {
                'URL': response.url,
                'Rating': review.css('.feedback-stars > span::text').get(),
                'Review Text': review.css('#-expanded, #-text::text').get(),
                'Author & Date': review.css('.feedback-rater::text').get(),
                'Company Name': response.css('#page-section-detail-seller-info > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > span:nth-child(2)::text').get(),
                'Type of Company': response.css('#page-section-detail-seller-info > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > span:nth-child(2)::text').get(),
                'BTW Number': response.css('#page-section-detail-seller-info > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(6) > span:nth-child(2)::text').get(),
                }




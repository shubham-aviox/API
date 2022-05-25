import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/gameofthrones/']
    start_urls = ['http://www.reddit.com/r/gameofthrones/']

    def parse(self, response):
        print("procesing:"+response.url, 'fdggggggggd')
        titles = response.css('._eYtD2XCVieq6emjKBH3m::text').extract()
        votes = response.css('._3a2ZHWaih05DgAOtvu6cIo::text').extract()
        times = response.css('._3jOxDPIQ0KaOWpzvSQo-1s::text').extract()
        comments = response.css('.FHCV02u6Cp2zYL0fhQPsO::text').extract()

        for item in zip(titles,votes,times,comments):
            print(item, 'dgsfgdjsgkdjgsdk=======>>>>>>>>>>')
            scraped_info = {
                'url': response.url,
                'title': item[0],
                'vote': item[1],
                'time': item[2],
                'comment': item[3],
            }

            yield scraped_info
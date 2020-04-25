# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonreviewsItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'

    start_urls = ['https://www.amazon.in/Test-Exclusive-TST_Exclusive1043-3GB-Storage/product-reviews/B07S6BW832']

    def parse(self, response):
        items = AmazonreviewsItem()

        all_data = response.css("#filter-info-section")
        for data in all_data:
            reviews = data.xpath('//*[@id="filter-info-section"]/span/text()').extract()

            items['Total_Reviews'] = reviews
            yield items

import scrapy

class TezSpider(scrapy.Spider):
    name = "teztour.by"
    allowed_domains = ["www.teztour.by"]
    start_urls = ["https://tourist.tez-tour.com/toursearch/fcc12b3288efc612f9cfdc8620c549bb/tourType/1/cityId/786/before/01.07.2023/after/11.06.2023/countryId/7067149/minNights/7/maxNights/14/adults/2/flexdate/0/flexnight/0/hotels/196507/hotels/641065/hotels/445053/hotels/196513/hotels/420458/hotels/210576/hotelTypeId/269506/mealTypeId/15350/rAndBBetter/yes/isTableView/0/lview/cls/noTicketsTo/no/noTicketsFrom/no/hotelInStop/no/recommendedFlag/no/onlineConfirmFlag/no/tourMaxPrice/30000000/categoryGreatThan/yes/currencyId/533067/dtype/period.ru.html"]
    current_page = 1

    def parse(self, response, **kwargs):
        for product in response.css(".items-container .hotel_point"):
            image_div = product.css(".image_row")
            image_name = f"https://www.teztour.by/{image_div.css('a::attr(href)').get()}"
            data = {
                "external_id": int(product.attrib.get("data-hid")),
                "name": product.css("h5").get().strip(),
                "price": product.css(".gray-old-price").get().strip(),
                "category": product.css(".clipped-text").get().strip(),
                "image_name": image_name,
                "link": f"{self.allowed_domains[0]}{product.css('a.area-link::attr(href)').get()}",
            }
            yield data

        next_page = response.css(".page-nav_box .btn__page-nav:last-child::attr(href)").get()
        if next_page is not None:
            self.current_page += 1
            if self.current_page == 2:
                return
            yield response.follow(next_page, callback=self.parse)
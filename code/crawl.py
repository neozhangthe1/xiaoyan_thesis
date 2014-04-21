import time
from scrapy.item import Item, Field
from selenium import webdriver
from scrapy.spider import BaseSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector


class kjhmItem(Item):
    link = Field()

class kjhmSpider(BaseSpider):
    name = "kjhm"
    allowed_domains = ["kjhm.org.cn"]
    start_urls = ["http://www.kjhm.org.cn/app/Cresult.aspx?id=%s" % i for i in range(1635)]

	def __init__(self):
	    self.driver = webdriver.Firefox()

	def set_code(code):
		script = """
		$("hfTCode").value = "%s";
		""" % code
		return script

	def search():
		script = """
		$('ibSearch').click();
		"""
		return script

	def get_id(href):
		_id = href[href.find("id")+3:]
		return _id

	def parse_code(category):
		driver.get(response.url)
		tab = driver.find_element_by_id("I%s00" % category)
		tab.click()
		import codecs
		f_out = codecs.open("D:\\code_%s.txt" % category, "w", encoding="utf8")
		elems = driver.find_elements_by_css_selector("a[id^='T%s']" % category)
		for ele in elems:
			text = ele.text
			_id = ele.get_attribute("id")
			f_out.write("%s %s\n" % (_id, text))
			print _id, text

	def crawl_category(code):
		driver.get(response.url)
		import codecs
		page = 1
		f_out = codecs.open("D:\\%s.txt" % code, "w", encoding="utf8")
		driver.execute_script(set_code(code))
		driver.execute_script(search())
		items = []
		url_base = "http://www.kjhm.org.cn/app/%s"
		while True:
			links = driver.find_elements_by_xpath("//ul[@id='newslist']/li/span/a")
			for l in links:
				href = l.get_attribute("href")
				_id = href[href.find("id")+3:]
				f_out.write("%s\t%s\t%s\n" % (_id, l.text, href))
			page += 1
			try:
				next = driver.find_element_by_link_text(str(page))
				next.click()
			except:
				break

	def parse_list(file):
		import codecs
		f_in = codecs.open(file, "r", encoding="utf8")
		for line in f_in:
			x = line.strip().split(" ")[0]
			if x[3] != "0":
				crawl_category(x[1:])


	def parse(self, response):
		import codecs
		f_out = codecs.open()
		hxs.select("")



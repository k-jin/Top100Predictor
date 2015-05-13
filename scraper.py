from lxml import html
import requests


statelist =['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New_Hampshire', 'New_Jersey', 'New_Mexico', 'New_York', 'North_Carolina', 'North_Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode_Island', 'South_Carolina', 'South_Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']


page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.text)

#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

print 'Buyers: ', buyers
print 'Prices: ', prices


#for i in range(50):
#	webstring='http://en.wikipedia.org/wiki/'+statelist[i]
#	page3= requests.get(webstring)
#	tree3 = html.fromstring(page3.text)
#	title=tree3.xpath('//*[@id="firstHeading"]/text()')
#	firstpara=tree3.xpath('//*[@id="mw-content-text"]/p[1]/text()')
#	capital =tree3.xpath('//*[@id="mw-content-text"]/table[1]/tbody/tr[8]/td/a/text()')
#	print 'State: ', title
#	print 'Capital: ',capital
#	print 'A little bit about it: ',firstpara

page5 = requests.get('http://www.billboard.com/charts/year-end/2014/hot-100-songs')
tree5 = html.fromstring(page5.text)

#test1='//*[@id="row-9"]/div/div[4]/h3/a/test()'
#t1=tree5.xpath(test1)
#print 'test: ',t1

for ii in range(100):
	#This will create a list of buyers:
	str1='//*[@id="row-'+repr(ii+1)+'"]/div/div[4]/h2/text()'
	str2='//*[@id="row-'+repr(ii+1)+'"]/div/div[4]/h3/a/text()'
	song = tree5.xpath(str1)
	artist=tree5.xpath(str2)
	#This will create a list of prices
	name=song[0]

	#print 'artist[0] is : ', artist[0]

	artistname=artist[0]
	nicename=''
	niceart=''

	for j in range(len(name)):
		if(name[j]!='\t' and name[j]!='\n'):
			nicename=nicename+name[j]

	for k in range(len(artistname)):
		if(artistname[k]!='\t' and artistname[k]!='\n'):
			niceart=niceart+artistname[k]


	print 'Track',repr(ii+1),': ', nicename, ' Artist: ', niceart






#page2= requests.get('http://en.wikipedia.org/wiki/Wisconsin')
#page2= requests.get('http://en.wikipedia.org/wiki/Illinois')


#tree2 = html.fromstring(page2.text)

#title=tree2.xpath('//*[@id="firstHeading"]/text()')
#firstpara=tree2.xpath('//*[@id="mw-content-text"]/p[1]/text()')

#print 'State: ', title
#print 'A little bit about it: ',firstpara

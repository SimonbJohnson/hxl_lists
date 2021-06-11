import requests
import json
import urllib
import time

def getData(link):
	print 'calling proxy'
	encodedLink = urllib.quote_plus(link)
	proxyLink = hxlProxyURL + '/data.json?dest=data_edit&filter01=cut&cut-include-tags01=%23org-id-type&url=' + encodedLink
	print proxyLink
	try:
		response = urllib.urlopen(proxyLink)
		print 'HXL proxy response'
		data = json.loads(response.read())

	except:
		time.sleep(5)
		return False

	if 'status' in data:
		return False
	else:
		print 'HXL data found'
		getOrgs(data)
		time.sleep(2)
		return True

def getOrgs(data):
	currentOrgs = []
	rowIndex = 0
	for row in data:
		if rowIndex>1:
			for cell in row:
				print(cell)
				currentOrgs.append(cell)

		rowIndex = rowIndex + 1
	orgs.append(currentOrgs)


def processPackages(packages):
	count = 1
	for package in packages:
		print(count)
		if count>startPlace:
			for resource in package['resources']:
				link = resource['link']
				getData(link)
			if(count % 10==0):
				with open('data/orgs_'+str(count)+'.json', 'w') as f:
					json.dump(orgs, f)
		count = count+1
		

packageFile = 'hdxDataScrape.json'
hxlProxyURL = 'https://proxy.hxlstandard.org'
startPlace = -1
orgs = []

print 'Loading file'
with open(packageFile) as json_file:
	packages = json.load(json_file)
	print 'Processing Packages'
	processPackages(packages)


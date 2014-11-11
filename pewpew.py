# -*- coding: utf-8 -*-
from show.show import draw_xkcd
import pymongo
import time

def get_data_single(word, collection):
	r = collection.find({"data.words" : word}, {"data.occurrences.$":1, "date":1})
	retval = {}
	for doc in r:
		#print doc
		cdate = doc['date'].date()
		occ = doc['data']['occurrences'][0]
		if (cdate in retval):
			retval[cdate] = retval[cdate] + int(occ)
		else:
			retval[cdate] = int(occ)
	return retval

def get_data(words):
	"""
		receives list of words, for which occurrences should be extracted
		returns map, where key - word, value - pair of lists for (dates, occurrences)
	"""
	retval = {}
	try:
		client = pymongo.MongoClient('mongodb://flipflop.systems:27017/')
		authed = client['mmwocdb'].authenticate('public', 'public')
		for word in words:
			t = get_data_single(word, client['mmwocdb'].graph)
			retval[word] = t
	except pymongo.errors.PyMongoError as e:
		print e
	return retval

def pass_to_show(data, ext):
	for key in data:
		xs = sorted(data[key].keys())
		ys = map(lambda x : data[key][x], xs)
		draw_xkcd(xs, ys, unicode('время', 'UTF-8'), unicode('частота', 'UTF-8'), unicode(key, 'UTF-8'), ext)

pass_to_show(get_data([
						'украина'
						, 'россия'
						, 'рубль'
						, 'доллар'
						, 'сша'
						, 'ополченец'
						, 'днр'
						, 'война'
						, 'мир'
						, 'путин'
						, 'крым'
						, 'газ'
						, 'хунта'
						, 'санкция'
						, 'фашист'
				   ]), '.svg')
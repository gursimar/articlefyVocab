from nytimesarticle import articleAPI
import urllib2
import json

key = 'e6cc8415ae478443a170e6755fd35759:4:69754109'

api = articleAPI(key)
articles = api.search( q = 'Obama', fq = {'headline':'Obama', 'source':['Reuters','AP', 'The New York Times']}, begin_date = 20111231, facet_field = ['source','day_of_week'], facet_filter = True )




import feedparser
from datetime import datetime
import calendar

app_contries = {
    'China':'cn',
    'United States':'us'
}

app_sortby = {
    'Most Recent':'mostRecent',
    'Most Helpful':'mostHelpful',
    # 'Most Favorable':'mostFavorable',
    # 'Most Critical':'mostCritical'
}

def mk_appfeed(app_id, country_code, sortby=app_sortby['Most Recent']):
    return 'https://itunes.apple.com/%s/rss/customerreviews/id=%s/sortBy=%s/xml' %\
        (country_code,app_id, sortby)

def parse_feed(url):
    review_map = {}
    feed = feedparser.parse(url)
    review_map.setdefault('title', feed.feed['title'])
    review_map.setdefault('updated',
                          calendar.timegm(feed.feed['updated_parsed']))

    if not feed.entries:
        print 'Get nothing from ' + url
        return None
    review_map.setdefault('apptitle', feed.entries[0]['title'])
    review_map.setdefault('applink', feed.entries[0]['id'])

    reviews = []
    for entry in feed.entries[1:]:
        reviews.append({'title': entry['title'],
                        'content': entry['content'][0]['value'],
                        'author': entry['author'],
                        'rating': entry['im_rating'],
                        'updated': calendar.timegm(entry['updated_parsed'])
                    })
    review_map.setdefault('reviews', reviews)
    return review_map

def print_reviews(review_map):
    if not review_map:
        print 'Input None'
        return

    print 'Title:    %s' % review_map['title']
    print 'Updated:  %s' % datetime.fromtimestamp(review_map['updated'])
    print 'App Name: %s' % review_map['apptitle']
    print 'Link:     %s' % review_map['applink']

    index = 0
    for entry in review_map['reviews']:
        index+=1
        print '*** %d ***' % index
        print 'Title:    %s' % entry['title']
        print 'Content:  %s' % entry['content']
        print 'Author:   %s' % entry['author']
        print 'Rating:   %s' % entry['rating']
        print 'Updated   %s' % datetime.fromtimestamp(entry['updated'])

def get_app_reviews(app_id, country_name, sortby='Most Recent'):
    print_reviews(parse_feed(mk_appfeed(app_id, app_contries[country_name],
                                        app_sortby[sortby])))

import feedparser
from datetime import datetime
import calendar

app_contries = {
    'China':'cn',
    'United States':'us'
}

app_ranklists = {
    'Top Free':'topfreeapplications',
    'Top Paid':'toppaidapplications',
    'Top Grossing':'topgrossingapplications',
    'Top Free iPad':'topfreeipadapplications',
    'Top Paid iPad':'toppaidipadapplications',
    'Top Grossing iPad':'topgrossingipadapplications',
    'Top Mac Apps':'topmacapps'
}

app_genres = {
    'None':None,
    'Books':'6018',
    'Business':'6000',
    'Catalogs':'6022',
    'Education':'6017',
    'Entertainment':'6016',
    'Finance':'6015',
    'Food & Drink':'6023',
    'Games':'6014',
    'Health & Fitness':'6013',
    'Lifestyle':'6012',
    'Medical':'6020',
    'Music':'6011',
    'Navigation':'6010',
    'News':'6009',
    'Newsstand':'6021',
    'Photo & Video':'6008',
    'Productivity':'6007',
    'Reference':'6006',
    'Social Networking':'6005',
    'Sports':'6004',
    'Travel':'6003',
    'Utility':'6002',
    'Weather':'6001'
}

def mk_rssfeed(country_code, rank_list, genre_code=None, limit=300):
    """
    country_code short name of country, eg, cn, us
    rank_list rank list name, eg, topfreeapplications
    genre_code app category code, eg, Sports=
    """
    rss_feed_parts = []
    rss_feed_parts.append('https://itunes.apple.com')
    rss_feed_parts.append(country_code)
    rss_feed_parts.append('rss')
    rss_feed_parts.append(rank_list)
    rss_feed_parts.append('limit=%d' % limit)
    if genre_code != None:
        rss_feed_parts.append('genre=' + genre_code)
    rss_feed_parts.append('xml')
    return ('/').join(rss_feed_parts)


def get_app_rank(app_id_list, country_code, rank_list, app_genre_code=None):
    rank_map = {}
    app_id_set = set(app_id_list)
    feed_url = mk_rssfeed(country_code, rank_list, app_genre_code)
    rank_map.setdefault('rank_feedurl', feed_url)
    feed_title, rank_list = parse_feed(feed_url)
    rank_map.setdefault('rank_title', feed_title)

    id_item = {}
    for item in rank_list:
        if item['id'] in app_id_set:
            id_item.setdefault(item['id'], item)
        if len(id_item.keys()) == len(app_id_set):
            break
    rank_map.setdefault('ranks', id_item)
    return rank_map

def print_rank_map(rank_map):
    print 'Rank List:    %s' % rank_map['rank_title']
    print 'From:         %s' % rank_map['rank_feedurl']
    for key, item in rank_map['ranks'].iteritems():
        print '\n'
        print 'App ID:       %s' % key
        print 'Rank:         %d' % item['rank']
        print 'App Title:    %s' % item['title']
        print 'App Link:     %s' % item['link']
        print 'Updated At:   %s' % datetime.fromtimestamp(item['timestamp'])

def get_ranks(app_ids, contry_name, rank_list_name, app_genre_name=None):
    '''
    Get App Ranks by specified ids, country names, list names and genres
    '''
    import getpass
    username = getpass.getuser()
    print 'Working ... Be patient, Master %s!' % username

    if contry_name in app_contries:
        contry_id = app_contries[contry_name]
    else:
        print 'Invalid country name'
        return
    if rank_list_name in app_ranklists:
        rank_list = app_ranklists[rank_list_name]
    else:
        print 'Invalid rank list name'
        return

    if not app_genre_name:
        app_genre_code = None
    elif app_genre_name in app_genres:
        app_genre_code = app_genres[app_genre_name]
    else:
        print 'Invalid app genre name'
        return

    rank_map = get_app_rank(app_ids, contry_id, rank_list, app_genre_code)
    if not rank_map['ranks'].keys():
        print 'Nothing was found, Don\'t be sad, Master %s!' % username
    else:
        print_rank_map(rank_map)

def parse_feed(url):
    feed = feedparser.parse(url)
    rank_list = []
    rank = 0
    for item in feed.entries:
        rank += 1
        link = item['id']
        rank_list.append({'rank':rank,
                          'id':link[link.find('/id')+3:link.find('?mt')],
                          'title':item['title'],
                          'link':link,
                          'timestamp':calendar.timegm(item['updated_parsed'])})
    return feed.feed.title, rank_list

if __name__ == '__main__':
    pass

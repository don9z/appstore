Tools for AppStore
==================

## Rank ##
Print app rank information by multiple app ids (Rank below 300 will not be shown)

    import rank
    rank.get_ranks(['506627515', '580765736'], 'United States', 'Top Grossing', 'Games')

    Working ... Be patient, Master chris!
    Rank List:    iTunes Store: Top Grossing
    From:         https://itunes.apple.com/us/rss/topgrossingapplications/limit=300/genre=6014/xml


    App ID:       580765736
    Rank:         11
    App Title:    Megapolis - Social Quantum
    App Link:     https://itunes.apple.com/us/app/megapolis/id580765736?mt=8&uo=2
    Updated At:   2013-04-18 15:08:49


    App ID:       506627515
    Rank:         4
    App Title:    Hay Day - Supercell
    App Link:     https://itunes.apple.com/us/app/hay-day/id506627515?mt=8&uo=2
    Updated At:   2013-04-18 15:08:49

## Reviews ##
Print app reviews by app id (At most 50 reviews will be printed)

    import review
    review.get_app_reviews('506627515', 'United States')

    Title:    iTunes Store: Customer Reviews
    Updated:  2013-04-18 15:35:08
    App Name: Hay Day - Supercell
    Link:     https://itunes.apple.com/us/app/hay-day/id506627515?mt=8&uo=2
    *** 1 ***
    Title:    Great game
    Content:  Good game
    Author:   Guido830
    Rating:   5
    Updated   2013-04-18 10:35:00
    *** 2 ***
    Title:    Fix!
    Content:  Agree with evry1.... When u open the newspaper it crashes automatically and I have even turned off my iphone and still doesn't wrk. Plz fix! Also there really should be a confirm button wen using gems...
    Author:   Kqnsnowhdn
    Rating:   3
    Updated   2013-04-18 10:35:00
    *** 3 ***
    Title:    Crashes
    Content:  Please fix the crashes. Before the update, I had never encountered those crashes but now I am so upset. I love the game so much. Please do something.
    Author:   Aanda6
    Rating:   4
    Updated   2013-04-18 10:34:00
    *** 4 ***
    Title:    So addicting
    Content:  Get it and be addicted lol.
    Author:   Theappsgamer
    Rating:   5
    Updated   2013-04-18 10:34:00
    *** 5 ***
    Title:    Addicting
    Content:  So much fun but can be addicting and you'll spend hours on this lol
    Author:   Lindsay4566779996478
    Rating:   5
    Updated   2013-04-18 10:29:00

    ...

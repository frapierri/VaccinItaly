import time
import pandas as pd
from urllib.parse import urlparse
import datetime
import requests

### Custom function adapted from https://pypi.org/project/PyCrowdTangle/
def ct_get_search_posts(count=100, start_date=None, end_date=None, include_history=None,
                 sort_by="date", types=None, search_term=None, account_types=None,
                 min_interactions=0, offset=0, api_token=None, platforms="facebook,instagram"):
    """Retrieve a set of posts for the given parameters get post from crowdtangle
    Args:
        count (int, optional): The number of posts to return. Defaults to 10. options [1-100]
        start_date (str, optional): The earliest date at which a post could be posted. Time zone is UTC.
                                    Format is “yyyy-mm-ddThh:mm:ss” or “yyyy-mm-dd”
                                    (defaults to time 00:00:00).
        end_date (str, optional): The latest date at which a post could be posted.
                                  Time zone is UTC. Format is “yyyy-mm-ddThh:mm:ss”
                                  or “yyyy-mm-dd” (defaults to time 00:00:00).
                                  defaults to "now".
        include_history (str, optional): Includes timestep data for growth of each post returned.
                                         Defaults to null (not included). options: 'true'
        sort_by (str, optional): The method by which to filter and order posts.
                                options: 'date', 'interaction_rate', 'overperforming',
                                'total_interactions', 'underperforming'.
                                defaults 'overperforming'
        min_interactions (int, optional): If set, will exclude posts with total interactions
                                          below this threshold. options int > 0, default 0
        offset (int, optional): The number of posts to offset (generally used for pagination).
                                Pagination links will also be provided in the response.
        types (str, optional):  The types of post to include. These can be separated by commas
                                to include multiple types. If you want all live videos
                                (whether currently or formerly live), be sure to include both
                                live_video and live_video_complete. The "video" type does not
                                mean all videos, it refers to videos that aren't native_video,
                                youtube or vine (e.g. a video on Vimeo).
                                options: "episode", "extra_clip", "link", "live_video",
                                "live_video_complete", "live_video_scheduled", "native_video",
                                "photo", "status", "trailer","video", "vine", "youtube"
                                default all
        search_term (str, optional): Returns only posts that match this search term.
                                     Terms AND automatically. Separate with commas for OR,
                                     use quotes for phrases. E.g. CrowdTangle API -> AND.
                                     CrowdTangle, API -> OR. "CrowdTangle API" -> AND in that
                                     exact order. You can also use traditional Boolean search
                                     with this parameter. default null
        api_token (str, optional): you can locate your API token via your crowdtangle dashboard
                                   under Settings > API Access.
    Returns:
        [dict]: The Response contains both a status code and a result. The status will always
                be 200 if there is no error. The result contains an array of post objects and
                a pagination object with URLs for both the next and previous page, if they exist
    Example:
        ct_get_posts(include_history = 'true', api_token="AKJHXDFYTGEBKRJ6535")
    """

    # api-endpoint
    URL_BASE = "https://api.crowdtangle.com/posts/search"
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'count': count, 'sortBy': sort_by, 'token': api_token,
              'minInteractions': min_interactions, 'offset': offset}

    # add params parameters
    if start_date:
        PARAMS['startDate'] = start_date
    if end_date:
        PARAMS['endDate'] = end_date
    if include_history == 'true':
        PARAMS['includeHistory'] = include_history
    if types:
        PARAMS['types'] = types
    if account_types:
        PARAMS['accountTypes'] = account_types
    if search_term:
        PARAMS['searchTerm'] = search_term
    if platforms:
        PARAMS["platforms"] = platforms

        # sending get request and saving the response as response object
    r = requests.get(url=URL_BASE, params=PARAMS)
    # if r.status_code != 200:
    #     out = r.json()
    #     print(f"status: {out['status']}")
    #     print(f"Code error: {out['code']}")
    #     print(f"Message: {out['message']}")
    return r.json()

api_token = "************" ## put your Crowdtangle key here

track = ["vaccini", "vaccino", "vaccinazioni", "vaccinazione", "vaccinarsi",
         "vaccinare", "vacciniamoci", "vaccinerò", "vaccinerete"]

track = ','.join(track)

start = datetime.datetime.today() - datetime.timedelta(days=7)
start = start.strftime("%Y-%m-%d")
end = datetime.datetime.today().strftime('%Y-%m-%d')
while 1:
    try:
        results = ct_get_search_posts(api_token=api_token, include_history="true",
                                      count=10000, start_date=start, end_date=end,
                                      search_term=track, sort_by="date")
        results = results["result"]["posts"]
        count = 0
        for post in results:
            ### do something with it ###
            ############################
        L = results.__len__()
        last_date = results[L - 1]["date"]
        print(str(last_date) + " - " + str(end) + ": " + str(count))
        ## get last post date to continue the search forward (you get a duplicated post, but that is the only way)
        if L == 10000:
            L = results.__len__()
            last_date = results[L - 1]["date"]
            end = last_date
            continue
        else:
            break
    except Exception as e:  # 6 calls/minute limit
        print(e)
        time.sleep(60)
        continue

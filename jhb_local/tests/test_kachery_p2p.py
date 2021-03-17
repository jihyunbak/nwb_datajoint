import kachery_p2p as kp
#from kachery_p2p._core import _api_port, _api_host, _http_post_json
#from kachery_p2p._feeds import _load_feed, _get_feed_id
from kachery_p2p._daemon_connection import _api_port, _api_host
from kachery_p2p._misc import _http_post_json
from kachery_p2p._feeds import _load_feed, _get_feed_id

_feed_name = 'beans20190718_jhbak_000000'
# _feed_name = 'beans20190718_jhbak2_000000.nwb'

def test_kachery_p2p_check():
    ''' check if the kachery-p2p daemon is running in the background '''
    # this works
    kp_channel = kp.get_channels()

def test_get_feed_id():
    ''' adapted from kp.get_feed_id(_feed_name) '''
    port = _api_port()
    host = _api_host()
    url = f'http://{host}:{port}/feed/getFeedId'
    x = _http_post_json(url, dict(
        feedName=_feed_name
    ))
    assert x['success'], ('feedID: {}'.format(x['feedId']))

def test_load_feed_create_false():
    ''' try load_feed '''
    # my error: from kachery_p2p._feeds._get_feed_id(),
    # "Exception: Unable to load feed with name: beans20190718_jhbak_000000"
    # perhaps this simply means that this feed is not yet created?
    _ = _load_feed(feed_name_or_uri=_feed_name, timeout_sec=None, create=False)

def test_load_feed_create_true():
    ''' try load_feed, and create_feed if not loaded '''
    # my error: from kachery_p2p._feeds._create_feed(),
    # "Exception: Unable to create feed: beans20190718_jhbak_000000"
    _ = _load_feed(feed_name_or_uri=_feed_name, timeout_sec=None, create=True)

def test_kachery_p2p_create_feed():
    port = _api_port() # this is 20431
    host = _api_host() # this is 'localhost
    url = f'http://{host}:{port}/feed/createFeed'
    req_data = {'feedName': _feed_name}
    x = _http_post_json(url, req_data)
    # failure case:
    # x = {'success': False,
    #  'error': 'Error posting json: 500 SQLITE_READONLY: attempt to write a readonly database'}
    assert x['success'], (x['error'] + f'. url = {url}')

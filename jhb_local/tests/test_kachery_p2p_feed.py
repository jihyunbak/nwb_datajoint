import kachery_p2p as kp
from kachery_p2p._daemon_connection import _api_port, _api_host
from kachery_p2p._misc import _http_post_json
from kachery_p2p._feeds import _load_feed, _get_feed_id

#_feed_name = 'beans20190718_jhbak_000000'
_feed_name = 'test_feed_jhbak'

def test_kachery_p2p_check():
    ''' check if the kachery-p2p daemon is running in the background '''
    kp_channel = kp.get_channels()

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

def test_get_feed_id():
    ''' adapted from kp.get_feed_id(_feed_name) '''
    port = _api_port()
    host = _api_host()
    url = f'http://{host}:{port}/feed/getFeedId'
    x = _http_post_json(url, dict(
        feedName=_feed_name
    ))
    assert x['success'], ('feedID: {}'.format(x['feedId']))


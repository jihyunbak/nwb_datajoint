import kachery_p2p as kp
#from kachery_p2p._daemon_connection import _api_port, _api_host, _api_url, _probe_result
#from kachery_p2p._misc import _http_post_json, _http_get_json
#from kachery_p2p._feeds import _load_feed, _get_feed_id


def test_kachery_p2p_check():
    ''' check if the kachery-p2p daemon is running in the background '''
    # this fails
    kp_channel = kp.get_channels()

#def test_probe_daemon():
#    api_url = _api_url()
#    url = f'{api_url}/probe'
#    x = _http_get_json(url)
#    try:
#        x = _http_get_json(url)
#    except:
#        return None
#    #res = _probe_result(x) if x is not None else None
#    #print(res)
#    print(x)


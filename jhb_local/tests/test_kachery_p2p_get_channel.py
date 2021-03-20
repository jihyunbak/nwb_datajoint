import kachery_p2p as kp

def test_kachery_p2p_check():
    ''' check if the kachery-p2p daemon is running in the background '''
    kp_channel = kp.get_channels()


#!/bin/bash

now=$(date +"%Y%m%d_%H%M")
logfile="kachery_p2p_daemon_${now}.log"

#nohup kachery-p2p-start-daemon --label franklab --static-config franklab_kachery-p2p_config.yaml > "$logfile" 2>&1 &
#nohup kachery-p2p-start-daemon --label franklab >> "$logfile" 2>&1 &
nohup kachery-p2p-start-daemon --label jihyun >> "$logfile" 2>&1 &


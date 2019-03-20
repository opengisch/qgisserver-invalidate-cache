#! /usr/bin/env python3

# QGIS project dir
DIR = "/geodata/qgis_projects/"

# this must be the same as the interval of the cron executing the script
INTERVAL = 60  # sec - min 60

# URL of the INVALIDATECACHE service the port is the docker *internal* one
SERVERS = [
    "http://localhost:80/local/",
]
URLPARAMS = {"service": "INVALIDATECACHE", "map": None}

# file where the status is stored
PICKLE_FILE = "touched.pkl"

##################################
########## END CONFIG ############
##################################


import glob
import os
import pickle
import requests
import sys
from datetime import datetime
from time import time


# we do this to allow some slack in case a process runs slightly later
interval = INTERVAL * 1.5


def invalidate_cache_by_url(filepath, now):
    URLPARAMS["map"] = filepath
    responses = []
    for server in SERVERS:
        response = requests.get(server, URLPARAMS)
        responses.append("%s - %s " % (response, response.text))
    
    print("invalidated cache for %s %s: %s" % (filepath, datetime.fromtimestamp(now).isoformat(), responses))

    return responses


def invalidate_cache_by_touch(filepath, time):
    # update access and modified time
    # doing only os.utime does not seem to generate
    # enough inotify events (only ATTRIB)
    try:
        with open(filepath, "a") as f:
            # this generates an inotify ATTRIB
            os.utime(filepath)
            # this would also generate an inotify MODIFY
            # f.write(" ")
        return True
    except:
        return False


def invalidate_cache(filepath, now):
    return invalidate_cache_by_url(filepath, now)


def scan():
    for filepath in glob.iglob(DIR + "/**", recursive=True):
        if os.path.isfile(filepath) and (
            filepath.endswith(".qgs") or filepath.endswith(".qgz")
        ):
            now = time()
            modif_time = os.path.getmtime(filepath)
            diff = now - modif_time

            # we look at all files that where changed in the last 1.5 INTERVAL
            if diff < interval:
                if filepath in TOUCHED and TOUCHED[filepath] >= modif_time:
                    # the file was last touched by this tool
                    pass
                else:
                    # file was changed after last touch or never touched
                    TOUCHED[filepath] = now
                    invalidate_cache(filepath, now)
                    
    # create new dict with elements that
    # were touched only within the las two cycles
    # we do this to keep the pickled object small
    cutoff_time = time() - 2 * interval
    cleaned_touched = {k: v for k, v in TOUCHED.items() if v > cutoff_time}

    with open(PICKLE_FILE, "wb") as f:
        pickle.dump(cleaned_touched, f)


if __name__ == "__main__":
    try:
        with open(PICKLE_FILE, "rb") as f:
            TOUCHED = pickle.load(f)
    except FileNotFoundError:
        TOUCHED = {}
    try: 
        print ("Invalidating single file cache: %s - %s " % (sys.argv[1], time()))
        invalidate_cache(sys.argv[1], time())
    except IndexError:
        scan()


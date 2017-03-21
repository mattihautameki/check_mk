#!/usr/bin/env python2.7
import requests
import urllib2
import json
import argparse
import sys

"""
This Script uses the WATO Web-API https://mathias-kettner.de/checkmk_wato_webapi.html
to edit, add and delete hosts in WATO
"""

SRV = "https://YOUR-DOMAIN-OR-HOSTNAME"
URL = "/YOUR-CHECK_MK-SITE/check_mk/webapi.py"
USER = "YOUR-AUTOMATION-USER"
PW = 'YOUR-AUTOMATION-SECRET'


def listAllHosts(folder='/'):
    hosts = {}
    params = [('action', 'get_all_hosts'),
              ('_username', USER),
              ('_secret', PW)]
    data = "request = {{'attributes':{{'folder': {0}}}}}".format(folder)
    r = requests.get(SRV + URL, 
                     params = params,
		     data = data)
    r.close()
    if r.status_code == requests.codes.ok:
        hosts = r.json().get('result').keys()

    return hosts


def getHostAttr(hostname=""):
    HOST = SRV + URL + "?action=get_host&_username={}&_secret={}& effective_attributes=1".format(USER, PW)
    req = urllib2.Request(HOST, data = 'request={{"hostname":"{0}"}}'.format(hostname))
    return json.load(urllib2.urlopen(req))


def setAttributes(hostname, key, param, unset=""):
    HOST = SRV + URL + "?action=edit_host&_username={}&_secret={}".format(USER, PW)
    if unset:
        req = urllib2.Request(HOST, data = 'request={{"hostname":"{0}","unset_attributes": ["{3}"] }}'.format(hostname, key, param, unset))
    else:
        req = urllib2.Request(HOST, data = 'request={{"hostname":"{0}", "attributes":{{ "{1}": "{2}" }}}}'.format(hostname, key, param, unset))
    return json.load(urllib2.urlopen(req))


def addHost(hostname):
    configured_hosts = listAllHosts()
    if hostname in configured_hosts:
        return {"result": "Host already configured", 'return_code': 0}
    HOST = SRV + URL + "?action=add_host&_username={}&_secret={}".format(USER, PW)
    req = urllib2.Request(HOST, data = 'request={{"hostname": "{0}","folder": "/"}}'.format(hostname))
    return json.load(urllib2.urlopen(req))


def delHost(hostname):
    HOST = SRV + URL + "?action=delete_host&_username={}&_secret={}".format(USER, PW)
    req = urllib2.Request(HOST, data = 'request={{"hostname":"{0}"}}'.format(hostname))
    return json.load(urllib2.urlopen(req))

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script adds, deletes and modifies hosts in WATO')
    parser.add_argument('-a', dest='action', metavar='action', type=str, required=True,
                       choices=['edit', 'add', 'del'],
                       help='Which action shall be perfomed - choices are ["edit", "del", "add"]')
    parser.add_argument('-H', dest='hostname', metavar='hostname', type=str,
                       help='Hostname')
    parser.add_argument('-t', dest='tagname', metavar='tagname', type=str,
                       help='Tagname to modify (tag must exists in WATO)')
    parser.add_argument('-u', dest='delete', metavar='delete', type=str,
                       help='Tagname which shall be unset')
    parser.add_argument('-p', dest='param', metavar='param', type=str,
                       help='Value of the tag specified with "-t"')
    args = parser.parse_args()
    if args.action == 'edit':
        f = setAttributes(args.hostname, args.tagname, args.param, args.delete)
        print args.hostname, f
    elif args.action == 'add':
        f = addHost(args.hostname)
        print args.hostname, f
    elif args.action == 'del':
        f = delHost(args.hostname)
        if f.get('result_code') != 0 and f.get('result') == 'No such host':
            f = {u'result': u'Host not in Monitoring', u'result_code': 1}
            print args.hostname, f.get('result_code')
        else:
            print args.hostname, f.get('result_code')
    else:
        pass
        # we dont run into here because of argparse

    sys.exit(f.get('result_code'))

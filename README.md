# check_mk Plugins

Here are some selfwritten check_mk plugins.

More can be found at http://git.anglmaier.at

## watoapi
The Script ```watoapi.py``` is designed to add, edit and delete hosts in WATO.

Examples
```bash
./watoapi.py -h
usage: watoapi.py [-h] -a action [-H hostname] [-t tagname] [-u delete]
                  [-p param]

Script adds, deletes and modifies hosts in WATO

optional arguments:
  -h, --help   show this help message and exit
  -a action    Which action shall be perfomed - choices are ["edit", "del",
               "add"]
  -H hostname  Hostname
  -t tagname   Tagname to modify (tag must exists in WATO)
  -u delete    Tagname which shall be unset
  -p param     Value of the tag specified with "-t"
```

Add Hosts 
```
./watoapi.py -a add -H newhost
newhost {u'result': None, u'result_code': 0}

./watoapi.py -a add -H newhost
newhost {'result': 'Host already configured', 'return_code': 0}
```


Edit Tags - tagnames have to be prefixed with "tag_"
```
./watoai.py -a edit -H newhost -t tag_OS -p Appliance
newhost {u'result': None, u'result_code': 0}

./watoai.py -a edit -H newhost -u tag_OS
newhost {u'result': None, u'result_code': 0}
```


Delete Host
```
./watoai.py -a del -H newhost
newhost 0
./watoai.py -a del -H newhost
newhost 1
```     


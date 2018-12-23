Where have I been, globally?
============================
*You can download your data from FB and Google. In the midst of JSON files,
there is a history of your coordinations with computer-friendly timestamps.
What does it look like on the map? Let's find out.*

Tools
=====
We use the `ELK` stack to store and visualize our data. There are two main
parts:
1. A [`script`][0] to extract the coordinate and timestamp from JSON to STDOUT > file
2. `logstash` will ingest the output file to ElasticSearch for posterity
3. `http` to `PUT` a json setting for `geo_point` data type

Work Flow
=========
*Create a python virtualenv if you want*
```
$ ./utils/fb2json.py /path/to/history_location.json > ingest/my_locs.json
$ docker-compose up -d
$ cat geo_point.json | http localhost:9200/_template/global_trek
```

TODO: * How do I set the index template permanent for elasticsearch?

__author__: *tuan t. pham*

References
==========
* Setting `geo_point` for all indices template from [`stackoverflow`][1]


[0]: ./utils/fb2json.py
[1]: https://stackoverflow.com/questions/37792826/geo-point-for-all-indexs-template-mappings

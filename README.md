# ggetjson
Uses grequests to pull JSON en masse. 

## Usage

    from ggetjson import ggetjson
    data = ggetjson(urls=['http://api.microprediction.org/lagged/traffic_absolute_speed.json','http://api.microprediction.org/lagged/die.json], failover_urls=None)

## Warning

A bit dangerous due to the monkey patching. Use with care. If you don't really need lots of requests, the getjson package is simpler. 

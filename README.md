# ggetjson
Uses grequests to pull JSON. A bit dangerous due to the monkey patching. Use with care. 

## Usage

    from ggetjson import ggetjson
    data = ggetjson(urls=['http://api.microprediction.org/lagged/traffic_absolute_speed.json','http://api.microprediction.org/lagged/die.json], failover_urls=None)

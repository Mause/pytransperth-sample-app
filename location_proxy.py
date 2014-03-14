import logging

from transperth.jp.location import (
    determine_location as _determine_location_raw
)

_location_cache = {}


def determine_location(from_loco, to_loco):
    """
    Wraps transperth's determine_location function, providing
    a caching functionality
    """

    cache_from = _location_cache.get(from_loco)
    cache_to = _location_cache.get(to_loco)

    if cache_from and cache_to:
        logging.info('Cache hit')

        return {
            'to': cache_to,
            'from': cache_from
        }

    logging.info('Cache miss')

    locations = _determine_location_raw(from_loco, to_loco)

    _location_cache[to_loco] = locations['to']
    _location_cache[from_loco] = locations['from']

    return locations

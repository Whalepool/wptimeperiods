
from pprint import pprint
from datetime import datetime

from wptimeperiods import tp


print('\nGet all timeperiods')
pprint(tp.get_timeperiods())


now = datetime.now()

print('\nGet current 1m')
pprint(tp.get_timeperiods( now, '1T' ))

print('\nGet current 4H')
pprint(tp.get_timeperiods( now, '4H' ))

print('\nGet Previous 4H')
pprint( tp.increment_timeperiods( tp.get_timeperiods( now, '4H' ), -1, '4H' ) )

print('\nGet timeframe 15m')
pprint( tp.get_tfs( '15T' ) )

print('\nGet timeframe 15m, 30m')
pprint( tp.get_tfs( ['15T', '30T'] ) )

print('\nGet timeframe >= 1D')
pprint( tp.get_tfs( '>=1D' ) )

print('\nGet timeframe > 1D')
pprint( tp.get_tfs( '>1D' ) )

print('\nGet timeframe <= 1H')
pprint( tp.get_tfs( '<=1H' ) )

print('\nGet timeframe < 1H')
pprint( tp.get_tfs( '<1H' ) )

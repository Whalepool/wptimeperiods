# Whalepool Timeperiods
Tested on python 3.8.2

#### Usage
```python
from wptimeperiods import tp 
```

### See it in action
```bash
python examples.py
```

### Get all timeperiods 
```python
pprint(tp.get_timeperiods())
# OrderedDict([('1T', datetime.datetime(2020, 12, 10, 8, 11)),
#              ('5T', datetime.datetime(2020, 12, 10, 8, 10)),
#              ('15T', datetime.datetime(2020, 12, 10, 8, 0)),
#              ('30T', datetime.datetime(2020, 12, 10, 8, 0)),
#              ('1H', datetime.datetime(2020, 12, 10, 8, 0)),
#              ('2H', datetime.datetime(2020, 12, 10, 8, 0)),
#              ('3H', datetime.datetime(2020, 12, 10, 6, 0)),
#              ('4H', datetime.datetime(2020, 12, 10, 8, 0)),
#              ('6H', datetime.datetime(2020, 12, 10, 6, 0)),
#              ('8H', datetime.datetime(2020, 12, 10, 8, 0)),
#              ('12H', datetime.datetime(2020, 12, 10, 0, 0)),
#              ('1D', datetime.datetime(2020, 12, 10, 0, 0)),
#              ('2D', datetime.datetime(2020, 12, 10, 0, 0)),
#              ('3D', datetime.datetime(2020, 12, 10, 0, 0)),
#              ('4D', datetime.datetime(2020, 12, 8, 0, 0)),
#              ('5D', datetime.datetime(2020, 12, 9, 0, 0)),
#              ('6D', datetime.datetime(2020, 12, 10, 0, 0)),
#              ('7D', datetime.datetime(2020, 12, 10, 0, 0)),
#              ('8D', datetime.datetime(2020, 12, 4, 0, 0)),
#              ('9D', datetime.datetime(2020, 12, 7, 0, 0)),
#              ('10D', datetime.datetime(2020, 12, 4, 0, 0)),
```

```python
now = datetime.now()
```

### Get current 1m
```python
tp.get_timeperiods( now, '1T' )
# datetime.datetime(2020, 12, 10, 8, 11)
```

### Get current 4H
```python
tp.get_timeperiods( now, '4H' )
# datetime.datetime(2020, 12, 10, 8, 0)
```

### Get previous 4H
```python
tp.increment_timeperiods( tp.get_timeperiods( now, '4H' ), -1, '4H' ) 
# datetime.datetime(2020, 12, 10, 4, 0)
```

### Get timeframe 15m
```python
tp.get_tfs( ['15T', '30T'] ) 
# ['15T', '30T']
```

### Get timeframe >= 1D
```python
tp.get_tfs( '>=1D' ) 
# ['1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D']
```

### Get timeframe > 1D
```python
tp.get_tfs( '>1D' ) 
# ['2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D']
```

### Get timeframe <= 1H
```python
tp.get_tfs( '<=1H' ) 
# ['1T', '5T', '15T', '30T', '1H']
```

### Get timeframe < 1H
```python
tp.get_tfs( '<1H' ) 
# ['1T', '5T', '15T', '30T']
```

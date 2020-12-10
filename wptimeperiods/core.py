from pprint import pprint 
from datetime import datetime, timedelta as datetime_timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd 
from collections import OrderedDict 
import sys



class wptimeperiods:


	timeframes_list = ['1T','5T','15T','30T','1H','2H','3H','4H','6H','8H','12H','1D','2D','3D','4D','5D','6D','7D','8D','9D','10D']
	timeframe_key_order = dict(zip(timeframes_list, range(len(timeframes_list))))
	resample_list = [
		['1T', ['5T','15T','30T'] ],
		['1H', ['2H','3H','4H','6H','8H','12H'] ],
		['1D', ['2D','3D','4D','5D','6D','7D','8D','9D','10D'] ]
	]
	timeframes = OrderedDict({
		'1T'   : {                    
			'seconds': 60, 
		},
		'5T'   : { 
			'upcycle': '1T',   
			'seconds':5*60,
			'group_intervals': [0,5,10,15,20,25,30,35,40,45,50,55]
		}, 
		'15T'  : { 
			'upcycle': '5T',   
			'seconds':15*60,
			'group_intervals': [0,15,30,45]
		}, 
		'30T'  : { 
			'upcycle': '15T',  
			'seconds':30*60,
			'group_intervals': [0,30]
		}, 
		'1H'   : { 
			'upcycle': '30T',  
			'seconds':60*60,
			'group_intervals': [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
		}, 
		'2H'   : { 
			'upcycle': '1H',   
			'seconds':2*(60*60),
			'group_intervals': [0,2,4,6,8,10,12,14,16,18,20,22]
		}, 
		'3H'   : { 
			'upcycle': '1H',   
			'seconds':3*(60*60),
			'group_intervals': [0,3,6,9,12,18,21]
		}, 
		'4H'   : { 
			'upcycle': '2H',   
			'seconds':4*(60*60),
			'group_intervals': [0,4,8,12,16,20]
		}, 
		'6H'   : {
			'upcycle': '3H',   
			'seconds':6*(60*60),
			'group_intervals': [0,6,12,18]
		}, 
		'8H'   : { 
			'upcycle': '4H',   
			'seconds':8*(60*60),
			'group_intervals': [0,8,16] 
		}, 
		'12H'  : { 
			'upcycle': '6H',   
			'seconds':12*(60*60),
			'group_intervals': [0,12]
		}, 
		'1D'   : { 
			'upcycle': '12H',  
			'seconds':24*(60*60) 
		}, 
		'2D'   : { 
			'upcycle': '2D',  
			'seconds':(24*(60*60))*2
		}, 
		'3D'   : { 
			'upcycle': '3D',  
			'seconds':(24*(60*60))*3
		}, 
		'4D'   : { 
			'upcycle': '4D',  
			'seconds':(24*(60*60))*4
		}, 
		'5D'   : { 
			'upcycle': '5D',  
			'seconds':(24*(60*60))*5
		}, 
		'6D'   : { 
			'upcycle': '6D',  
			'seconds':(24*(60*60))*6
		}, 
		'7D'   : { 
			'upcycle': '7D',  
			'seconds':(24*(60*60))*7
		}, 
		'8D'   : { 
			'upcycle': '8D',  
			'seconds':(24*(60*60))*8
		}, 
		'9D'   : { 
			'upcycle': '9D',  
			'seconds':(24*(60*60))*9
		}, 
		'10D'   : { 
			'upcycle': '10D',  
			'seconds':(24*(60*60))*10
		}
	})

	def __init__(self):
		pass 

	def get_tfs(self, tf):
		if tf in self.timeframes_list:
			return tf

		if type(tf) == list:
			return sorted( tf, key=lambda x: self.timeframe_key_order[x])

		if '>=' in tf: 
			return self.timeframes_list[ self.timeframes_list.index( tf[2:] ) : ]

		elif '<=' in tf:
			return self.timeframes_list[ : self.timeframes_list.index( tf[2:] )+1 ]

		elif '>' in tf:
			return self.timeframes_list[ self.timeframes_list.index( tf[1:] )+1 : ]
		
		elif '<' in tf:
			return self.timeframes_list[ : self.timeframes_list.index( tf[1:] ) ]

		else:
			return tf 


	def increment_timeperiods(self, orig_timestamp, num=1, resolution=None):

		if resolution == None:
			resolution = '1T'

		if resolution == 'MS': 
			output =  orig_timestamp + relativedelta(months=num)
			return output
		else:
			output = orig_timestamp + relativedelta(seconds=(self.timeframes[resolution]['seconds']*num))
			return output 


	def now(self):
		return datetime.utcnow().replace(second=0, microsecond=0)

	def get_timeperiods(self, now=None, resolution=None):

		periods = OrderedDict({})

		if now == None:
			now = datetime.utcnow().replace(second=0, microsecond=0)

		year   = now.year
		month  = now.month
		day    = now.day
		hour   = now.hour
		minute = now.minute

		if (resolution == None) or (resolution in ['1T']):
			periods['1T'] = now.replace(second=0, microsecond=0)


		# 5T, 15T, 30T 
		bins = ['5T','15T','30T']
		if (resolution == None) or (resolution in bins):
			for timeperiod in bins: 

				p = str(year)+"-"+str(month).zfill(2)+"-"+str(day).zfill(2)+" "+str(hour).zfill(2)+":00"

				for i in self.timeframes[ timeperiod ]['group_intervals']:
					if i <= minute:
						p = str(year)+"-"+str(month).zfill(2)+"-"+str(day).zfill(2)+" "+str(hour).zfill(2)+":"+str(i).zfill(2)
				
				periods[timeperiod] = datetime.strptime(p, '%Y-%m-%d %H:%M')


		# 1H 
		if (resolution == None) or (resolution in ['1H','2H','3H','4H','6H','8H','12H']):

			p = str(year)+"-"+str(month).zfill(2)+"-"+str(day).zfill(2)+" "+str(hour).zfill(2)+":00"
			p = datetime.strptime(p, '%Y-%m-%d %H:%M')
			periods['1H'] = p


		# 2H, 3H, 4H, 6H, 8H, 12H
		bins = ['2H','3H','4H','6H','8H','12H']
		if (resolution == None) or (resolution in bins):
			for timeperiod in bins: 

				p = str(year)+"-"+str(month).zfill(2)+"-"+str(day).zfill(2)+" 00:00"
				for i in self.timeframes[ timeperiod ]['group_intervals']:
					if i <= hour:
						p = str(year)+"-"+str(month).zfill(2)+"-"+str(day).zfill(2)+" "+str(i).zfill(2)+":00"
				
				periods[timeperiod] = datetime.strptime(p, '%Y-%m-%d %H:%M')


		# 1D 
		if (resolution == None) or (resolution in ['1D','2D','3D','4D','5D','6D','7D','8D','9D','10D']):
			p = str(year)+"-"+str(month).zfill(2)+"-"+str(day).zfill(2)
			p = datetime.strptime(p, '%Y-%m-%d').replace(hour=0, minute=0)
			periods['1D'] = p


		# 2d, 3d, 4d, 5d, 6d, 7d, 8d, 9d, 10d
		if (resolution == None) or (resolution in ['2D','3D','4D','5D','6D','7D','8D','9D','10D']):	
			first_day = datetime.utcnow().replace(year=2013,month=1, day=1, minute=0, second=0, microsecond=0)
			days_since = (datetime.utcnow() - first_day).days+1
			dr = pd.date_range( first_day, periods= days_since, freq='D' )
			s = pd.Series( range(len(dr)), index=dr )


			bins = ['2D','3D','4D','5D','6D','7D','8D','9D','10D']
			for timeperiod in bins:
				rsmpl = s.resample(timeperiod, origin='epoch').sum()
				rsmpl = rsmpl.index.to_pydatetime()

				# pprint('\n'+timeperiod)
				# pprint(rsmpl[-4:])

				periods[timeperiod] = rsmpl[-1]



		# W-MON
		if (resolution == None) or (resolution in ['W-MON']):	
			to_beggining_of_week = datetime_timedelta(days=now.weekday())
			p = (now - to_beggining_of_week).replace(hour=0, minute=0, second=0, microsecond=0)
			periods['W-MON'] = p

		# M
		if (resolution == None) or (resolution in ['MS']):
			p = datetime.strptime(str(year)+"-"+str(month).zfill(2)+"-01", '%Y-%m-%d')
			#next_month = p.replace(day=28) + datetime_timedelta(days=4)
			#p = next_month - datetime_timedelta(days=next_month.day)
			periods['MS'] = p


		if resolution != None:
			return periods[resolution]

		else:
			return periods


	def datetime_to_miliseconds(self, inputdate=None):
		if inputdate == None:
			inputdate = datetime.utcnow()
		return (inputdate - datetime.utcfromtimestamp(0)).total_seconds() * 1000 

	def miliseconds_to_datetime(self, ms):
		return datetime.utcfromtimestamp(ms/1000.0)

	def string_to_datetime(self, string):
		return datetime.strptime(string,'%Y-%m-%d %H:%M:%S')
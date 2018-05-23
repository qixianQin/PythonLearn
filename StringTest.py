# -*- conding:utf-8 -*- 

span = ''' <span>


那是我上中学放暑假的时候、偶然帮我妈洗了一次衣服，发现兜里有钱，从此我就踏上了帮我妈洗衣服的不归路、当时还纳闷、怎么经常能洗到钱、结婚后我妈才把真相告诉我，她都是故意放的，就为了让我帮她洗衣服！

</span>'''

ss = ''' <span class="stats-vote"><i class="number">2100</i> 好笑</span>'''

if ss.startswith(' <span>'):
	print('yyyyyy')
else:
	print('nnnnn')
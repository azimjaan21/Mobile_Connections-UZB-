#Distribution of mobile connections in Uzbekistan from 2020 to 2025, by technology
#Mobile connections share in Uzbekistan 2020-2025, by technology
#Published by Statista Research Department, Oct 4, 2023
#3G connections, which were the most common in Uzbekistan in 2020, 
#would decrease their share in the mobile technology mix in favor or 4G and 5G 
#in the following years until 2025. The 5G technology was expected to occupy a 10 percent share in 2025.

import pygal

chart_mb = pygal.Bar()
chart_mb.title = 'Distribution of mobile connections in Uzbekistan from 2020 to 2025, by technology \n*by percentage(%)'
chart_mb.y_labels = ['0%','25%', '50%','75%','100%','125%']
chart_mb.x_labels = ['2020', '2025*']
chart_mb.add('2G',[24, 4])
chart_mb.add('3G',[50, 36])
chart_mb.add('4G',[26, 51])
chart_mb.add('5G',[0, 10])




chart_mb.render_in_browser()
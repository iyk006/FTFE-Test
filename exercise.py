import os
import pandas as pd 
import matplotlib.pyplot as plt
from pyulog import *


# command line scripts, used to generate csv file for the actuator_controls_0 topic
#os.system('cmd /k "ulog_info test.ulg"')
#os.system('cmd /k "ulog2csv -m actuator_controls_0 test.ulg"')

test_ac = pd.read_csv('test_actuator_controls_0_0.csv')
topics =  test_ac.loc[:,"control[0]":"control[7]"]
time_axis = test_ac.loc[:,"timestamp"]
topic_labels = list(topics.columns)

plt.plot(time_axis, topics, linewidth=0.75)
plt.legend(topic_labels)
plt.show()
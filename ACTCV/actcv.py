# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:22:41 2019

@author: Sebastian Blum
"""
import actr
import pandas as pd
from tqdm.auto import tqdm

class ActCV():

    def __init__(self, data, head, indexinput = 0):
        self.header =  []
        self.statelist = []
        self.state_start = []
        self.time_offset = 0
        self.header = head
        self.index = indexinput
        try:
	        self.data = data
        except:
            print(f"Not able to load {data}")
        actr.add_command("commit-to-visicon", self.commit_to_visicon, "load the current line in the visicon")
       # actr.add_command("initialize-visicon", initialize_visicon, "run initialize the visicon")

    def commit_to_visicon(self, indices, statelist):
        state_current = statelist[indices]
        actr.delete_all_visicon_features()        
        for index, headname in enumerate(self.header):
            value = state_current[index]
            actr.add_visicon_features(['isa', 'visual-location', 
                                       'value', value,
                                       'color', headname,
                                       'screen-x', 0, 
                                       'screen-y', 0, 
                                       'width', 50, 
                                       'height', 15])

		
    def set_states(timecolumnname):
        # set start time
	    time_start = self.data[timecolumnname][0]
        time_last_current = time_start

        # set states
        self.state_start = self.data.iloc[0] # the iloc seems critical
        state_previous = self.state_start
        self.statelist.append(state_previous.values.tolist())

        for itertuple in data.itertuple():
            #print(state_iter)
            time_current = itertuple.timecolumnname # das geht wahrscheinlich nicht, weil es ein string ist
            self.time_offset = time_current - starttime
            self.time_offset = self.time_offset + starttime
            time_difference = time_current - time_last_current

            if time_difference > timebreak:          
                time_last_current = time_current
                state_current = itertuple
                previous_value = state_previous[alarmnumbercolumn]
                current_value = state_current[alarmnumbercolumn]
                alarm_active = state_current[alarmactivecolumn]
                # use tuples and save time offset, index and self statelist. 
        		# Then convert it to list and call the function for each entry
                self.statelist.append(state_current.values.tolist()) # does it make sense to create a dictionary here?
                self.index += 1
                if previous_value != current_value and previous_value == 0.0 and alarm_active == 1.0:
                    #inser into tone list
            state_previous = state_current


    def schedule_Visicon(self, alarmactivecolumn, alarmnumbercolumn, timecolumnname, freq, duration, starttime = 0, timebreak = 0.01):            
        pass

    def load_vision():
        # loop through list
        # actr.schedule_event(self.time_offset, "commit-to-visicon", params = [self.index, self.statelist], maintenance = True )     
        # loop through list
        # actr.new_tone_sound(freq, duration, self.time_offset) # input these variables
        # print(f" Tone scheduled at {self.time_offset}")     
        pass

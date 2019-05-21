import time as t
import pandas as pd
import numpy as np
import datetime as dt

while True:
        pd.set_option('display.max_columns',500)
        CITY_DATA = { 'chicago': 'chicago.csv',
                    'new york': 'new_york_city.csv',
                    'washington': 'washington.csv' }

        print('\nHello! Let\'s explore some US bikeshare data!\n\nAvailable Cities:\n\n1.Chicago \n2.New York \n3.Washington')
        #function to select the city
        def select_city():
            '''Asks the user for a city and returns the filename for that city's bike share data.
            Args:
                none.
            Returns:
                (str) Filename for a city's bikeshare data.
            '''
            city=''
            while city.lower() not in ['chicago','new york','washington','ny']:    
                city = input('\nEnter the name of selected city from the list above: ').lower()
            if city.lower() =='chicago':
                return CITY_DATA[city.lower()]
            elif city.lower()=='new york' or city.lower()=='new york city' or city.lower()=='ny':
                return CITY_DATA['new york']
            elif city.lower()=='washington':
                return CITY_DATA[city.lower()]
            
        

        months_dict = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4,
                        'may': 5, 'jun': 6}

        #function to select the month
        def select_month():
            '''Asks the user for the month and returns the specified month.
            Args:
                none.
            Returns:
                (int) month for the bikeshare data.
            '''
            month_input = ''
            while month_input.lower() not in months_dict.keys():
                month_input = input('\nAvailable months (kindly use the format of the options below):\n\n1.Jan\n2.Feb\n3.Mar\n4.Apr'
                                    ' \n5.May\n6.Jun\n\n').lower()
                if month_input.lower() not in months_dict.keys():
                    print('Sorry, I do not understand your input. Please type in a '
                        'month between January and June. ')
                else:
                    return months_dict[month_input]

       

        weekday_dict = {'mon': 0, 'tue': 1, 'wed': 2, 'thur': 3,
                        'fri': 4, 'sat': 5,'sun':6}


        def select_weekday():
            '''Asks the user for the weekday required
            Args:
                none.
            Returns:
                (int) weekday number to be used with the dt.dayoftheweek method'''
            weekday_input=''
            while weekday_input.lower() not in weekday_dict.keys():
                weekday_input = input('\nSelect day of the week (kindly use the format of the options below):\n\n1.Mon\n2.Tue\n3.Wed\n4.Thur'
                                    ' \n5.Fri\n6.Sat \n7.Sun\n\n').lower()
                if weekday_input.lower() not in weekday_dict.keys():
                    print('Sorry, I do not understand your input. Please type in a '
                        'weekday between Mon and Sun\n\n')
                else:
                    return weekday_dict[weekday_input]

        

        #statistics for times of travel
            #most popular month
        def pop_month():
            '''Does the calculation for the popular month data
            Args:
                none.
            Returns:
                (str) most popular month results based on user inputs'''
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            index = int(df['start_month'].mode())
            num_trips = int(df['start_month'].value_counts()[index-1])
            most_pop_month = months[index -1]
            if QuesFil_month =='n':
                Current_month_nt = int(df_filtered_m.shape[0])
            elif QuesFil_month =='y':
                Current_month_nt = int(df_filtered_m['start_month'].value_counts()[month])
                Sel_month = months[month-1]
            if QuesFil_month =='n':
                print('\nThe most popular month to travel is in {}.There have been over {} trips made during that month!!'.format(most_pop_month,num_trips))
            elif QuesFil_month =='y':
                print('\nThe most popular month to travel is in {}.There have been over {} trips made during that month!!\nthe selected month of {} has {} trips'.format(most_pop_month,num_trips,Sel_month,Current_month_nt))

            #Most popular day of the week
        def pop_weekday():
            '''Does the calculation for the popular weekday data
            Args:
                none.
            Returns:
                (str) most popular weekday results based on user inputs'''
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            weekdays=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
            index_wd =int(df['weekday'].mode())
            num_trips_wd = int(df['weekday'].value_counts()[index_wd-1])
            most_pop_weekday = weekdays[index_wd -1]
            if QuesFil_day =='n':
                Current_popday = int(df_filtered_m['weekday'].mode())#most popular day for the selected month,if all months are selected it would show all months
                most_pop_weekday_sl= weekdays[Current_popday-1]
                Current_popday_nt = int(df_filtered_m['weekday'].value_counts()[Current_popday-1])#number of trips made on during popular days that month,,if all months are selected it would show all months
            elif QuesFil_day =='y':
                Sel_month = months[month-1]
                Current_popday_nt = int(df_filtered_m['weekday'].value_counts()[day])#number of trips for the selected day
                Current_popday_nt_tp = int(df['weekday'].value_counts()[day])
                most_pop_weekday_ch =  weekdays[day]  
            if  QuesFil_month =='n':
                print('\nThe most popular day to travel is on a {}.There have been over {} trips made on that day so far!!'.format(most_pop_weekday,num_trips_wd))
            elif QuesFil_month =='y' and QuesFil_day =='y':
                print('\nThe most popular day to travel is on a {}.There have been over {} trips made on that day so far!!, \n{}\'s in the month of {} and have {} trips and have {} trips in the year so far.'.format(most_pop_weekday,num_trips_wd,most_pop_weekday_ch,Sel_month,Current_popday_nt,Current_popday_nt_tp))
            elif QuesFil_day =='n'and QuesFil_month =='y':
                Sel_month = months[month-1]
                print('\nThe most popular day to travel is on a {}.There have been over {} trips made on that day so far!!\nThe most popular day in the month of {} is {} and it has over {} trips'.format(most_pop_weekday,num_trips_wd,Sel_month,most_pop_weekday_sl,Current_popday_nt))

            #Most hour time to travel        
        def pop_hour():
            '''Does the calculation for the popular hour data
            Args:
                none.
            Returns:
                (str) most popular hour results based on user inputs'''
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            weekdays=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
            if  QuesFil_month =='n':
                most_pop_hour1 = int(df['hour'].mode())
                print('\nThe most popular hour to travel this year seems to be at around the {} hour of the day'.format(most_pop_hour1))
            elif QuesFil_month =='y' and QuesFil_day =='y':
                most_pop_hour2 = int(df_filtered['hour'].mode())
                Sel_month = months[month-1]
                most_pop_weekday_ch =  weekdays[day]
                print('\nThe most popular hour to travel during the month of {} seems to be at around the {} hour of the day on {}\'s.'.format(Sel_month,most_pop_hour2,most_pop_weekday_ch))
            elif QuesFil_day =='n'and QuesFil_month =='y':
                most_pop_hour3 = int(df_filtered_m['hour'].mode())
                Sel_month = months[month-1]
                print('\nThe most popular hour to travel during the month of {} seems to be at around the {} hour of the day.'.format(Sel_month,most_pop_hour3))

        #statistics for stations and trips
            #Most common start station
        def pop_start_stn():
            '''Does the calculation for the popular start station data
            Args:
                none.
            Returns:
                (str) most popular Station results based on user inputs'''
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            weekdays=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
            if  QuesFil_month =='n':
                most_pop_stn1 = str(df['Start Station'].mode().to_string(index = False))
                print('\nThe most popular station to travel from this year seems to be at :\n{}.'.format(most_pop_stn1))
            elif QuesFil_month =='y' and QuesFil_day =='y':
                most_pop_stn2 = str(df_filtered['Start Station'].mode().to_string(index = False))
                Sel_month = months[month-1]
                most_pop_weekday_ch =  weekdays[day]
                print('\nThe most popular station to travel from during the month of {} on {}\'s seems to be at :\n{}.'.format(Sel_month,most_pop_weekday_ch,most_pop_stn2))
            elif QuesFil_day =='n'and QuesFil_month =='y':
                most_pop_stn3 = str(df_filtered_m['Start Station'].mode().to_string(index = False))
                Sel_month = months[month-1]
                print('\nThe most popular station to travel from during the month of {},seems to be at :\n{}.'.format(Sel_month,most_pop_stn3))
            #Most popular end station
        def pop_end_stn():
            '''Does the calculation for the popular end station data
            Args:
                none.
            Returns:
                (str) most popular Station results based on user inputs'''
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            weekdays=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
            if  QuesFil_month =='n':
                most_pop_stn1 = str(df['End Station'].mode().to_string(index = False))
                print('\nThe most popular station to travel to this year seems to be at :\n{}.'.format(most_pop_stn1))
            elif QuesFil_month =='y' and QuesFil_day =='y':
                most_pop_stn2 = str(df_filtered['End Station'].mode().to_string(index = False))
                Sel_month = months[month-1]
                most_pop_weekday_ch =  weekdays[day]
                print('\nThe most popular station to travel to during the month of {} on {}\'s seems to be at :\n{}.'.format(Sel_month,most_pop_weekday_ch,most_pop_stn2))
            elif QuesFil_day =='n'and QuesFil_month =='y':
                most_pop_stn3 = str(df_filtered_m['End Station'].mode().to_string(index = False))
                Sel_month = months[month-1]
                print('\nThe most popular station to travel to during the month of {},seems to be at :\n{}.'.format(Sel_month,most_pop_stn3))        
            #Most popular Trip
        def pop_trip():
            '''Does the calculation for the popular trip data
            Args:
                none.
            Returns:
                (str) most popular trip results based on user inputs'''
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            weekdays=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
            if  QuesFil_month =='n':
                most_pop_stn1 = str(df['trip'].mode().to_string(index = False))
                print('\nThe most popular trip(s) to travel on this year seems to be :\n{}.'.format(most_pop_stn1))
            elif QuesFil_month =='y' and QuesFil_day =='y':
                most_pop_stn2 = str(df_filtered['trip'].mode().to_string(index = False))
                Sel_month = months[month-1]
                most_pop_weekday_ch =  weekdays[day]
                print('\nThe most popular trip(s) to travel on during the month of {} on {}\'s seems to be :\n{}.'.format(Sel_month,most_pop_weekday_ch,most_pop_stn2))
            elif QuesFil_day =='n'and QuesFil_month =='y':
                most_pop_stn3 = str(df_filtered_m['trip'].mode().to_string(index = False))
                Sel_month = months[month-1]
                print('\nThe most popular trip(s) to travel on during the month of {},seems to be :\n{}.'.format(Sel_month,most_pop_stn3))        

        #statistics for Trip Duration
            #Total travel time
        def tt_traveltime():
            '''Does the calculation for the travel time data
            Args:
                none.
            Returns:
                (str) travel time results based on user inputs'''
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            weekdays=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
            if  QuesFil_month =='n':
                total_duration_1 = df['Trip Duration'].sum()
                minute, second = divmod(total_duration_1, 60)
                hour, minute = divmod(minute, 60)
                print('\nPeople have spent over {} hours, {} minutes and {} seconds in transit during the year'.format(hour, minute, round(second,2)))
            elif QuesFil_month =='y' and QuesFil_day =='y':
                total_duration_2 = df_filtered['Trip Duration'].sum()
                minute, second = divmod(total_duration_2, 60)
                hour, minute = divmod(minute, 60)
                Sel_month = months[month-1]
                most_pop_weekday_ch =  weekdays[day]
                print('\nDuring the month of {} on {}\'s People have spent over {} hours, {} minutes and {} seconds in transit.'.format(Sel_month,most_pop_weekday_ch,hour, minute, round(second,2)))
            elif QuesFil_day =='n'and QuesFil_month =='y':
                total_duration_3 = df_filtered_m['Trip Duration'].sum()
                minute, second = divmod(total_duration_3, 60)
                hour, minute = divmod(minute, 60)
                Sel_month = months[month-1]
                print('\nDuring the month of {}.People have spent over {} hours, {} minutes and {} seconds in transit'.format(Sel_month,hour, minute, round(second,2)))

            #Average travel time
        def avg_traveltime():
            '''Does the calculation for the average travel time data
            Args:
                none.
            Returns:
                (str) average travel time results based on user inputs'''
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            weekdays=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
            if  QuesFil_month =='n':
                total_duration_1 = df['Trip Duration'].mean()
                minute, second = divmod(total_duration_1, 60)
                hour, minute = divmod(minute, 60)
                print('\nPeople have had an average travel time of {} hours, {} minutes and {} seconds during the year'.format(hour, minute, round(second,2)))
            elif QuesFil_month =='y' and QuesFil_day =='y':
                total_duration_2 = df_filtered['Trip Duration'].mean()
                minute, second = divmod(total_duration_2, 60)
                hour, minute = divmod(minute, 60)
                Sel_month = months[month-1]
                most_pop_weekday_ch =  weekdays[day]
                print('\nDuring the month of {} on {}\'s People had an average travel time of {} hours, {} minutes and {} seconds.'.format(Sel_month,most_pop_weekday_ch,hour, minute, round(second,2)))
            elif QuesFil_day =='n'and QuesFil_month =='y':
                total_duration_3 = df_filtered_m['Trip Duration'].mean()
                minute, second = divmod(total_duration_3, 60)
                hour, minute = divmod(minute, 60)
                Sel_month = months[month-1]
                print('\nDuring the month of {}.People have had an average travel time of {} hours, {} minutes and {} seconds.'.format(Sel_month,hour, minute,round(second,2)))

        #statistics for User Information
            #User Type information
        def user_type_count():
            '''Does the calculation for the user type data
            Args:
                none.
            Returns:
                (str) user type results based on user inputs'''
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            weekdays=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
            if  QuesFil_month =='n':
                cofuser_sub1= df['User Type'].value_counts()['Subscriber']
                cofuser_cus1= df['User Type'].value_counts()['Customer']
                try:
                    cofuser_dep1= df['User Type'].value_counts()['Dependent']
                except KeyError:
                    cofuser_dep1 = 0
                print('\nThe count of User types for the period are as follows:\nCustomers  :{}\nSubcribers :{}\nDependents :{}'.format(cofuser_sub1,cofuser_cus1,cofuser_dep1))
            elif QuesFil_month =='y' and QuesFil_day =='y':
                cofuser_sub2= df_filtered['User Type'].value_counts()['Subscriber']
                cofuser_cus2= df_filtered['User Type'].value_counts()['Customer']
                try:
                    cofuser_dep2= df_filtered['User Type'].value_counts()['Dependent']
                except KeyError:
                    cofuser_dep2 =0
                Sel_month = months[month-1]
                most_pop_weekday_ch =  weekdays[day]
                print('\nThe count of User types for the month of {} on {}\'s are as follows:\nCustomers  :{}\nSubcribers :{}\nDependents :{}'.format(Sel_month,most_pop_weekday_ch,cofuser_sub2,cofuser_cus2,cofuser_dep2))
            elif QuesFil_day =='n'and QuesFil_month =='y':
                cofuser_sub3= df_filtered_m['User Type'].value_counts()['Subscriber']
                cofuser_cus3= df_filtered_m['User Type'].value_counts()['Customer']
                try:
                    cofuser_dep3= df_filtered_m['User Type'].value_counts()['Dependent']
                except KeyError:
                    cofuser_dep3 =0
                Sel_month = months[month-1]
                print('\nThe count of User types for the month of {} are as follows:\nCustomers  :{}\nSubcribers :{}\nDependents :{}'.format(Sel_month,cofuser_sub3,cofuser_cus3,cofuser_dep3))
            
            #User gender information
        def user_gen():
            '''Does the calculation for the user gender data
            Args:
                none.
            Returns:
                (str) user gender results based on user inputs'''
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            weekdays=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
            if  QuesFil_month =='n':
                try:
                    cofuser_m1= df['Gender'].value_counts()['Male']
                    cofuser_fm1= df['Gender'].value_counts()['Female']
                    print('\nDuring the year the number of Male and Female travelers were as follows:\nMale  :{}\nFemale :{}'.format(cofuser_m1,cofuser_fm1))
                except KeyError:
                    print('\nNo gender data available')
            elif QuesFil_month =='y' and QuesFil_day =='y':
                try:
                    cofuser_m2= df_filtered['Gender'].value_counts()['Male']
                    cofuser_fm2= df_filtered['Gender'].value_counts()['Female']
                    Sel_month = months[month-1]
                    most_pop_weekday_ch =  weekdays[day]
                    print('\nDuring the month of {} on {}\'s the number of Male and Female travelers were as follows:\nMale  :{}\nFemale :{}'.format(Sel_month,most_pop_weekday_ch,cofuser_m2,cofuser_fm2))
                except KeyError:
                    print('\nNo gender data available')
            elif QuesFil_day =='n'and QuesFil_month =='y':
                try:
                    cofuser_m3= df_filtered_m['User Type'].value_counts()['Subscriber']
                    cofuser_fm3= df_filtered_m['User Type'].value_counts()['Customer']
                    Sel_month = months[month-1]
                    print('\nDuring the month of {} the number of Male and Female travelers were as follows:\nMale  :{}\nFemale :{}'.format(Sel_month,cofuser_m3,cofuser_fm3))
                except KeyError:
                    print('\nNo gender data available')
            
            #User age information
        def user_birthyr():
            '''Does the calculation for the Birth year data
            Args:
                none.
            Returns:
                (str) Birth year results based on user inputs'''
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            weekdays=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
            if  QuesFil_month =='n':
                try:
                    oldest1 = int(df['Birth Year'].min())
                    youngest1 = int(df['Birth Year'].max())
                    mode1 = int(df['Birth Year'].mode())
                    print('\nThe infomation for the year suggests that :\nThe oldest user was born in {}.\nThe youngest user was born in {}.\nMost users on the system are born in {}.'.format(oldest1,youngest1,mode1))
                except KeyError:
                     print('No Birthyear data available')
            elif QuesFil_month =='y' and QuesFil_day =='y':
                try:
                    oldest2 = int(df_filtered['Birth Year'].min())
                    youngest2 = int(df_filtered['Birth Year'].max())
                    mode2 = int(df_filtered['Birth Year'].mode())
                    Sel_month = months[month-1]
                    most_pop_weekday_ch =  weekdays[day]
                    print('\nThe infomation for the year suggests that during the month of {} on {}\'s :\nThe oldest user was born in  {}.\nThe youngest user was born in {}.\nMost users on the system are born in {}.'.format(Sel_month,most_pop_weekday_ch,oldest2,youngest2,mode2))
                except KeyError:
                     print('No Birthyear data available')
            elif QuesFil_day =='n'and QuesFil_month =='y':
                try:
                    oldest3 = int(df_filtered_m['Birth Year'].min())
                    youngest3 = int(df_filtered_m['Birth Year'].max())
                    mode3 = int(df_filtered_m['Birth Year'].mode())
                    Sel_month = months[month-1]
                    print('\nThe infomation for the year suggests that during the month of {} :\nThe oldest user was born in  {}.\nThe youngest user was born in {}.\nMost users on the system are born in {}.'.format(Sel_month,oldest3,youngest3,mode3))
                except KeyError:
                     print('No Birthdyear data available')
                
        def display_extr():
            '''shows the data extract for the first five rows of data
            Args:
                none.
            Returns:
                (str) shows the data extract for the first five rows of data'''
            Disp_data=''
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            weekdays=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
            rows = 5
            q1=''
            while Disp_data.lower() not in ['y','n']:
                Disp_data = input('\n\nWould you like to see a 5 row extract of the user data? [y/n] ').lower()
            if  QuesFil_month =='n' and Disp_data=='y' :
                print('\n',df.iloc[0:rows])
                while q1.lower() not in ['n','y']:
                    q1=input('\n\nWould you like to see another 5 of the user data? [y/n] ').lower()
                    if q1=='y':
                        while q1=='y':
                            rows=rows+5
                            print('\n',df.iloc[0:rows])
                            q1=input('\n\nWould you like to see another 5 of the user data? [y/n] ').lower()
                    if q1=='n':
                        print('\nYou have requested not to view anymore of the data extract')
            elif QuesFil_month =='n' and Disp_data=='n':
                print('You have requested not to view the data extract')
            
            if  QuesFil_month =='y' and QuesFil_day =='y' and Disp_data=='y':
                Sel_month = months[month-1]
                most_pop_weekday_ch =  weekdays[day]
                print('\nThis is the data for the month of {} for all {}\'s\n'.format(Sel_month,most_pop_weekday_ch))
                print('\n',df_filtered.iloc[0:rows])
                while q1.lower() not in ['n','y']:
                    q1=input('\n\nWould you like to see another 5 of the user data? [y/n] ').lower()
                    if q1=='y':
                        while q1=='y':
                            rows=rows+5
                            print('\n',df_filtered.iloc[0:rows])
                            q1=input('\n\nWould you like to see another 5 of the user data? [y/n] ').lower()
                    if q1=='n':
                        print('\nYou have requested not to view anymore of the data extract')
            elif QuesFil_month =='y' and QuesFil_day =='y' and Disp_data=='n':
                print('You have requested not to view the data extract')
            if QuesFil_day =='n'and QuesFil_month =='y' and Disp_data=='y':
                Sel_month = months[month-1]
                print('\nThis is the data for the month of {}\n'.format(Sel_month))
                print('\n',df_filtered_m.iloc[0:rows])
                while q1.lower() not in ['n','y']:
                    q1=input('\n\nWould you like to see another 5 of the user data? [y/n] ').lower()
                    if q1=='y':
                        while q1=='y':
                            rows=rows+5
                            print('\n',df_filtered_m.iloc[0:rows])
                            q1=input('\n\nWould you like to see another 5 of the user data? [y/n] ').lower()
                    if q1=='n':
                        print('\nYou have requested not to view anymore of the data extract')
            elif QuesFil_day =='n'and QuesFil_month =='y' and Disp_data=='n':
                print('You have requested not to view the data extract')


        #code to collect the user inputs
        QuesFil_month = ''
        QuesFil_day =''


        city = select_city()
        while QuesFil_month.lower() not in ['y','n']:
            QuesFil_month = input('\n\nWould you like to filter by month? [y/n]\nNote: Select (n) to autodisplay all statistics ').lower()
            if QuesFil_month =='y':
                month = select_month()
                while QuesFil_day.lower() not in ['y','n']:
                    QuesFil_day = input('\n\nWould you like to filter by day? [y/n] ').lower()
                    if QuesFil_day =='y':
                        day = select_weekday()
                    elif QuesFil_day =='n':
                        print('\n\nFilter by month coming up!')
            elif QuesFil_month =='n':
                print('\n\nIll be back with your stats!')

        #Filters the data based on the inputs from the user

        df = pd.read_csv(city)
        #creating the additional columns required
        df['start_month'] = pd.to_datetime(df['Start Time']).dt.month
        df['weekday']= pd.to_datetime(df['Start Time']).dt.weekday#pd.DatetimeIndex
        df['hour'] =pd.to_datetime(df['Start Time']).dt.hour
        df['trip']= df['Start Station'].str.cat(df['End Station'], sep=' (to) ')


        #applying the necessary filters based on user inputs
        month_filter =''
        if QuesFil_month =='y' and QuesFil_day =='n':
            month_filter = df['start_month'] == month
            df_filtered = df[month_filter]
            df_filtered_m = df[month_filter]
        elif QuesFil_month =='y' and QuesFil_day =='y':
            month_filter = df['start_month'] == month
            day_filter = df['weekday'] == day  
            combined_filter = month_filter & day_filter 
            df_filtered = df[combined_filter]
            df_filtered_m = df[month_filter]
        elif QuesFil_month =='n':
            df_filtered = df
            df_filtered_m =df


        print('\n___________________________________________________________________')
        print('\nSTATISTICS FOR TIMES OF TRAVEL!\n')
        print('1.MONTH STATISTICS')
        pop_month()
        print('\n2.WEEKDAY STATISTICS')
        pop_weekday()
        print('\n3.HOUR STATISTICS','\n(Hours are shown in 24hr format) ')
        pop_hour()
        print('\n____________________________________________________________________')
        print('\nSTATISTICS FOR STATIONS AND TRIPS!\n')
        print('1.START STATION STATISTICS')
        pop_start_stn()
        print('\n2.END STATION STATISTICS')
        pop_end_stn()
        print('\n3.END STATION STATISTICS')
        pop_trip()
        print('\n____________________________________________________________________')
        print('\nSTATISTICS ON TRIP DURATION!\n')
        print('1.STATISTICS ON TOTAL TRAVEL TIME')
        tt_traveltime()
        print('\n2.STATISTICS ON AVERAGE TRAVEL TIME')
        avg_traveltime()
        print('\n____________________________________________________________________')
        print('\nSTATISTICS ON USER INFORMATION!\n')
        print('1.STATISTICS ON USER TYPE')
        user_type_count()
        print('\n2.USER GENDER STATISTICS')
        user_gen()
        print('\n3.USER AGE STATISTICS\n')
        user_birthyr()
        print('\n____________________________________________________________________')
        print('\nDATA EXTRACT\n')
        display_extr()
        #code to restart the program at the request of the user
        answer = input('\nWould you like to look at data for another city? [y/n]: ').lower()
        while answer.lower() not in ['y','n']:
            answer = input('\nwould you like to look at another city? [y/n]: ').lower()
        if answer == 'y':
            print('Lets try some other options!')
            continue
        else:
            print('Thankyou. Hope you have a great day!....or night!')
        break




import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def check_input(input_str,input_type):
    while True:
        input_read=input(input_str)
        try:
            if input_read.lower() in ['chicago','new york city','washington'] and input_type == 1:
                break
            elif input_read.lower() in ['january', 'february', 'march', 'april', 'may', 'june','all'] and input_type == 2:
                break
            elif input_read.lower() in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all'] and input_type == 3:
                break
            else:
                if input_type == 1:
                    print("Sorry, your input should be: chicago new york city or washington")
                if input_type == 2:
                    print("Sorry, your input should be: january, february, march, april, may, june or all")
                if input_type == 3:
                    print("Sorry, your input should be: sunday, ... friday, saturday or all")
        except ValueError:
            print("Sorry, your input is wrong")
    return input_read


def get_filters():
          
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #Asks user to specify a city, month, and day to analyze.
    city= check_input(' Please choose which city to process  : Chicago, New York city ; or Washington ?',1)
    month = check_input('Please choose which month (or all)?',2)
    day = check_input('which day or (all)?',3)
    print ("_"*80) 
    return city.lower(),month.lower(),day.lower()
#Returns:
 #       (str) city - name of the city to analyze
  #      (str) month - name of the month to filter by, or "all" to apply no month filter
   #     (str) day - name of the day of week to filter by, or "all" to apply no day filter
 

    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get userinput for day of week (all, monday, tuesday, ... sunday)
   
def dispaly_raw_data(df):
    print('\n Raw data are available to check..\n')
    print(df.head())
    
    counter=0
    index = df.index
    no_of_rows = len(index)
    while True:
        
        print('\nyou have seen {} rows out of {}'.format(counter+5,no_of_rows))
        display_raw = input('\nWould you like to have a look at some more rows: Type Yes or No : ')
        if display_raw.lower() != 'yes':
            return
        counter +=5
        print(df.iloc[counter:counter+5])
   
    

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (hour) hour - 
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week,hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    print('Most common month is :')
    print (df['month'].mode()[0])
    # TO DO: display the most common day of week
    print('Most common day is :')
    print (df['day_of_week'].mode()[0])
    # TO DO: display the most common start hour
    print('Most common start hour is :')
    print (df['hour'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

  

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    #TO DO: display most commonly used start station
    print ('Most commonly used Start Station is:')
    print (df['Start Station'].mode()[0])
    # TO DO: display most commonly used end station
    print ('\nMost commonly used End Station is:')
    print (df['End Station'].mode()[0])
    # TO DO: display most frequent combination of start station and end station trip
    combined_field = df.groupby(['Start Station','End Station'])
    print('\nMost frequent comination of Start Station and End Station is:')
    print(combined_field.size().sort_values(ascending=False).head(1))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

def trip_duration_stats(df):
    #Displays statistics on the total and average trip duration.
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    print ('Total Travel Time is :')
    print(df['Trip Duration'].sum())
    # TO DO: display mean travel time
    print('Average travel time is : ')
    print(df['Trip Duration'].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

def user_stats(df,city):
    #Displays statistics on bikeshare users.
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    print('count of user grouped by type (Subscriber/customer) is : ')
    print(df['User Type'].value_counts())
    # TO DO: Display counts of gender
    if city != 'washington':
        print('\nCount of users grouped by gender is :')
        print(df['Gender'].value_counts())
        
        # TO DO: Display earliest, most recent, and most common year of birth
        print('\n Most earliest year of birth is:')
        print(df['Birth Year'].min())
        
        print('\n Most recent year of birth is:')
        print(df['Birth Year'].max())
        
        print('\nThe most common year of birth is :')
        print(df['Birth Year'].mode()[0])
    else:
        print('\n Note: Washington city has no data for gender or birth year')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        dispaly_raw_data(df)
        restart = input('\nWould you like to restart and choose another parameters? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()




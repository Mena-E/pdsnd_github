import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #while True:
    while True:
        city = input("\nWhich city would you like to explore today? \nType chicago, new york city, washington: ")
        if city.lower() not in ('chicago', 'new york city', 'washington'):
            print("\nThat's not a valid entry! Please try again: ")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month_list = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
        month = input("\nWhich month would you like to explore today? Make your selection as follows: \nTo explore all months: type all \nOr type in any of the following months: \njanuary, february, march, april, may, or june: ")
        if month.lower() not in month_list:
            print("\nThat's not a valid month entry! Please try again: ")
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_list = ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
        day = input("\nWhich day of the week would you like to explore today? \nMake your selection as follows: \nTo explore all days of the week: type all \nOr type in any of the following days: \nsunday, monday, tuesday, wednesday, thursday, friday, or saturday: ")
        if day not in day_list:
            print("\nThat's not a valid day entry! Please try again: ")
            continue
        else:
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    elif day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def rows_display(d_frame):
    first_row = 0
    num_rows = 5
    while True:
        raw_data = input("\nWould you like to see some raw data? \nType 'y' for yes and 'n' for no: ")
        if raw_data.lower() not in ('y', 'yes','n', 'no'):
            print("\nThat's not a answer! Please try again: ")
            continue
        elif raw_data.lower() == 'y':
            print(d_frame[0:][first_row:num_rows])
            first_row += 5
            num_rows += 5
            continue
        else:
            break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    pop_month = df['month'].mode()[0]
    print("Most common month is: {}".format(pop_month))

    # TO DO: display the most common day of week
    pop_day = df['day_of_week'].mode()[0]
    print("Most common day of week is: {}".format(pop_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    pop_hour = df['hour'].mode()[0]
    print("Most common start hour is: {}".format(pop_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start = df['Start Station'].mode()[0]
    print("Most commonly used start station is: {}".format(pop_start))

    # TO DO: display most commonly used end station
    pop_end = df['End Station'].mode()[0]
    print("Most commonly used end station is: {}".format(pop_end))

    # TO DO: display most frequent combination of start station and end station trip
    df_combo = df['Start Station'] + ' to ' + df['End Station']
    pop_combo = df_combo.mode()[0]
    print("Most frequent combination of start and end station trip is: {}".format(pop_combo))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = sum(df['Trip Duration'])
    print("The total trip duration is: {}".format(total_time))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The mean travel time is: {}".format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Count of user type is: {}".format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print("\nCount of each gender is: {}".format(gender_count))
    else:
        print("There is no gender data available for your selected city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        print("\nThe earliest birth year is: {} \nThe most recent birth year is: {} \nThe most common birth year is: {}".format(earliest_year, most_recent_year, most_common_year))
    else:
        print("There is no birth year data available for your selected city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rows_display(df)
        
        restart = input('\nWould you like to restart? Enter yes or no: ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

#########################
#Adjustments compared to v1
# - Concantenated the record breaking highs and lows in 2015
# - Combined the dataset for 2015 for scatterplotting to one for 2015
# - As a result of above changes, one label was reduced in legend
##########################



# Add a dummy year 1900 in Date for plotting the datetime on x-axis
# Convert data in Date column from object type to datetime type for plotting
def addyear(row):
    row['Date']='1900'+'-'+row['MM_DD']
    return row

rec_hi = rec_hi.apply(addyear, axis='columns')
rec_lo = rec_lo.apply(addyear, axis='columns')

dates = pd.to_datetime(rec_hi['Date'])

##################################
# 2 Plot the data for 2005-2014
##################################

# Adjust the dpi for better resolution
# Then plot the two lines representing the record highs and lows for 2005-2014
# Set the lines on the bottom layer
plt.figure(dpi=300)
plt.plot(dates, rec_hi['Data_Value'], color='r', label = '2005-2014 TMAX', zorder=0)
plt.plot(dates, rec_lo['Data_Value'], color='b', label = '2005-2014 TMIN', zorder=0)

# Convert the dates to a NumPy array of datetime64s
# Then shade the difference between the two lines
d = dates.values
plt.gca().fill_between(d,
                      rec_hi['Data_Value'], rec_lo['Data_Value'],
                      facecolor='b',
                      alpha=0.15)

plt.ylabel('Temperatures in tenths of degrees C')
plt.title('Temperatures recorded from 2005 through 2014 \nfor Ann Arbor, Michigan, US')

# Remove the frame of the plot
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# Add the major grid for y-axis for better reading the temperatures
# Set the format in which x-axis lables are displayed
    # (effectively hiding dummy year 1990)
plt.grid(which='major', axis='y')
plt.gca().xaxis.set_major_formatter(DateFormatter('%m-%d'))


#############################
# 3 Prepare the data for 2015
#############################

# Extract and process data for year 2015
# Change the year to 1900 to use the same x-axis as for 2005-2014
y_2015 = df[df['Date'] > '2015']

max2015 = y_2015.groupby('Date').agg({'Data_Value': np.max})
min2015 = y_2015.groupby('Date').agg({'Data_Value': np.min})
max2015 = max2015.reset_index()
min2015 = min2015.reset_index()

def changeYear(row):
    row['Date'] = row['Date'].replace('2015', '1900')
    return row

max2015 = max2015.apply(changeYear, axis='columns')
min2015 = min2015.apply(changeYear, axis='columns')

# Merge the records for 2015 with that for 2005-2014
# Get two tables, one of data in 2015 lower than the lowest in 2005-2014
    # the other of data in 2015 higher tan the highest in 2005-214
omax = max2015.merge(rec_hi, left_on='Date', right_on='Date')
omax = omax[omax['Data_Value_x'] > omax['Data_Value_y']]
omin = min2015.merge(rec_lo, left_on='Date', right_on='Date')
omin = omin[omin['Data_Value_x'] < omin['Data_Value_y']]
orec = pd.concat([omax, omin])

orec['Date'] = pd.to_datetime(orec['Date'])
# omin['Date'] = pd.to_datetime(omin['Date'])


#############################
# 4 Plot the data for 2015
#############################

# Plot the all-time (2005-2015) highs and lows recorded in 2015 as dots
# Set their layer so they appear above the lines for 2005-2015
plt.scatter(orec['Date'].values, orec['Data_Value_x'],
            s=1, c='black', label='Record breaking temperatures in 2015 ', zorder=5)
# plt.scatter(omin['Date'].values, omin['Data_Value_x'],
#            s=1, c='black', alpha=0.8, label='Record breaking 2015 TMIN', zorder=5)
plt.legend(loc=4, prop={'size': 6})
# plt.savefig('temp2005-2015.png')
plt.show()

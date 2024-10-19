import pandas as pd
import sidetable

flights = pd.read_csv("C:/Users/nickd/OneDrive/Desktop/MSIS5193_Datasets/flights.csv")

#below prints the first 5 rows
print(flights.head())

#below prints the number of rows and columsn
print(flights.shape)

#below prints the type of each variable
print(flights.dtypes)

#how many carriers exist?
#what is the size of the carrier in terms of number of flights
print(flights[['flight', 'carrier']])
carrier = flights.stb.freq(["carrier"])
print(carrier)
#double check results with aggregate functions
num_carrier = flights.groupby('carrier')["carrier"].count()
print(num_carrier)
#same results found


#what if we needed number of flights by carrier and flight number
num_flights_by_carrier = flights.groupby(['carrier','flight'])["carrier"].count()
print(num_flights_by_carrier)

#calculate the mean dep_delay and arr_delay for each flight (defined as carrier and flight)
flight_agg = flights.groupby(['carrier','flight'],as_index=False).agg(avg_dep_delay = ("dep_delay","mean"), avg_arr_delay = ("arr_delay", "mean")).sort_values(by=["avg_dep_delay","avg_arr_delay"],ascending=False)
print(flight_agg)
print(flight_agg[['avg_dep_delay','avg_arr_delay']].mean())
#another way to check the flight_agg results
del_arr_avg = flights.groupby(['carrier','flight'])[["dep_delay","arr_delay"]].mean().sort_values(by=["dep_delay","arr_delay"],ascending=False)
print(del_arr_avg)

#compare the average arr_delay in January (month=1) and February (month=2) vs in June (month=6) and July (month=7)
months = flights.stb.freq(["month"])
print(months)
arr_months = flights.groupby('month')['arr_delay'].mean()
print(arr_months)


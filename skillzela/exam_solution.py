# Take no of Bus Route
sample_input = int(input())

# Calsulate and Store route cost in ans
ans = []
while(sample_input >= 1):
    no_of_bus = int(input())
    bus_rate = str(input())

    # Convert route cost string to int list
    bus_rate_list = []
    for data in bus_rate.split():
        bus_rate_list.append(int(data))

    # Sort route cost in descending order
    bus_rate_list.sort(reverse=True)
    sample_input = sample_input - 1

    # Calculate trip cost
    count = 1
    trip_cost = 0
    for value in bus_rate_list:
        trip_cost = trip_cost + (value * count)
        if count < (no_of_bus-1):
            count = count + 1

    # Add final and to ans list
    ans.append(trip_cost)

for trip_price in ans:
    print(trip_price)


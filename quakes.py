# Project 5
#
# Name: Parker Mitchell
# Instructor: Hatalsky
# Section: 11

from quakeFuncs import *
from math import *

def main():


    quakes = read_quakes_from_file('quakes.txt')

    display_data(quakes)

    choice = 'z'  # to start the while loop

    while choice.lower() != 'q':  # while they have't quit
        choice = print_options()

        if choice.lower() == 'f':  # filter earthquakes by either magnitude or place
            filter = input("Filter by (m)agnitude or (p)lace? ")

            if filter.lower() == 'm':
                lower = float(input("Lower bound: "))
                upper = float(input("Upper bound: "))

                print()
                filtered_mag = filter_by_mag(quakes, lower, upper)  # ask if they are out of order??? print and compare
                display_data(filtered_mag)
            elif filter.lower() == 'p':
                string = input("Search for what string? ")

                print()
                filtered_place = filter_by_place(quakes, string)
                display_data(filtered_place)

        if choice.lower() == 's':  # sort earthquakes my mag, tim, long, or lat
            sort = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? ")
            print()

            if sort.lower() == 'm':
                quakes.sort(key = attrgetter('mag'), reverse = True)
                display_data(quakes)
            elif sort.lower() == 't':
                quakes.sort(key = attrgetter('time'), reverse = True)
                display_data(quakes)
            elif sort.lower() == 'l':
                quakes.sort(key = attrgetter('longitude'))
                display_data(quakes)
            elif sort.lower() == 'a':
                quakes.sort(key = attrgetter('latitude'))
                display_data(quakes)

        if choice.lower() == 'n':
            eq_dict = get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')

            features = eq_dict["features"]
            json_quakes = []
            new_quakes = []

            for f in features:
                json_quakes.append(quake_from_feature(f))

            for quake in json_quakes:
                if quake not in quakes:
                    new_quakes.append(quake)
                    quakes.append(quake)

            print()
            display_data(new_quakes)



    write_out(quakes)






if __name__ == "__main__":
    main()
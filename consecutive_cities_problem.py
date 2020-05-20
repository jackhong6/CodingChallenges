# Jack Hong
# May 19, 2020
#
# Solutions to interview coding problem:
# Problem description:
#   You decide to go for a very long drive on a very straight road. Along this road are five cities. As you travel, you
#   record the distance between each pair of consecutive cities. You would like to calculate a distance table that
#   indicates the distance between any two of the cities you have encountered.
#
# Input:
#   Four positive integers less than 1000, each representing the distances between consecutive pairs of consecutive
#   cities: specifically, the ith integer represents the distance between city i and city i+1
#   SAMPLE INPUT: 3, 10, 12, 5
#
# Output:
#   Five lines, with the ith line (1 <= i <= 5) containing the distance from city i to cities 1,2,...,5 in order,
#   separated by one space.
#   SAMPLE OUTPUT (for sample input):
#       0 3 13 25 30
#       3 0 10 22 27
#       13 10 0 12 17
#       25 22 12 0 5
#       30 27 17 5 0


def calculate_dist_table_1(d1, d2, d3, d4):
    """A simple first solution that hard codes the formula for each distance.
    This is efficient as it only requires performing a few additions.
    However, it is not generic and cannot easily be used to solve similar problems, such as when more cities are added.
    """
    return [[0, d1, d1 + d2, d1 + d2 + d3, d1 + d2 + d3 + d4],
            [d1, 0, d2, d2 + d3, d2 + d3 + d4],
            [d1 + d2, d2, 0, d3, d3 + d4],
            [d1 + d2 + d3, d2 + d3, d3, 0, d4],
            [d1 + d2 + d3 + d4, d2 + d3 + d4, d3 + d4, d4, 0]]


def calculate_dist_table_2(*args):
    """A second solution using loops inspired by the patterns and symmetry observed in the first solution.
    This is more generic than the first solution because it allows for a variable number of cities.
    """
    table_size = len(args) + 1
    dist_table = [table_size * [0] for _ in range(table_size)]  # create a matrix of zeros

    # loop through every pair of cities and update dist_table
    for i in range(table_size):
        for j in range(i+1, table_size):
            dist_table[i][j] = dist_table[j][i] = sum(args[i:j])
    return dist_table


def calculate_dist_table_3(*args):
    """A third solution that is as general and efficient as solution 2. This approach uses the idea that as we move to
    the ith city, the distances to the cities before the ith city increases by args[i] and the distances to the rest
    of the cities decreases by args[i].
    """
    dist_table = [[sum(args[:i]) for i in range(len(args)+1)]]  # calculate the first row of dist_table

    for i in range(len(args)):
        # for each subsequent row, the distances to each city before the ith city increases by args[i] while
        # the distances to each city after the ith city decreases by args[i]
        dist_table.append([elem + args[i] for elem in dist_table[i][:i+1]]
                          + [elem - args[i] for elem in dist_table[i][i+1:]])

    return dist_table


def calculate_dist_table_4(*args):
    """A fourth solution similar to solutions 2 and 3. This uses the idea that the distance between city-i and city-j is
    the distance from city-0 to city-j minus the distance from city-0 to city-i.
    """
    table_size = len(args) + 1
    dist_from_start = [sum(args[:i]) for i in range(0, len(args)+1)]
    dist_table = []

    # loop through every pair of cities and update dist_table
    for i in range(table_size):
        dist_table.append([abs(d - dist_from_start[i]) for d in dist_from_start])
    return dist_table


def print_distance_table(dist_table):
    for lst in dist_table:
        row = ""
        for dist in lst:
            row += str(dist) + " "
        print(row)


def main():
    print_distance_table(calculate_dist_table_2(3, 10, 12, 5))


if __name__ == "__main__":
    main()

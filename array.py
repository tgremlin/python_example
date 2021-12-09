numbers = [[1,2,-3,-4], [5,-6,7,-8],[9,10,-11,-12],[-13,14,-15]]

def negativeNumbers(array):
    count = 0

    for row in array:
        for element in row:
            if element < 0:
                count += 1
    
    print(f"There are {count} negative numbers in this array")

negativeNumbers(numbers)
def canReach(x1, y1, x2, y2):
    # Write your code here
    if x2 == 0 or y2 == 0:
        if (x1,y1) == (x2, y2):
            return "Yes"
        else:
            return "No"

    while x2 != x1 or y2 != y1:
        if y1 > y2 or x1 > x2:
            return "No"
        elif x2 == y2:
            return ((0, y2)==(x1, y1) or (x2, 0)==(x1, y1))

        if y2 > x2:
            if x2 == x1:
                if (y2-y1) % x1 == 0:
                    return "Yes"
                else:
                    return "No"
        else:
            if y2 == y1:
                if (x2-x1) % y1 == 0:
                    return "Yes"
                else:
                    return "No"


        return "Yes"
            
print(canReach(1,1,5,2))

    
    

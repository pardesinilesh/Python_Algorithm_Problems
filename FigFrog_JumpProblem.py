


# Python wih X starting point Y end Point and D as fix Jump distance.

def solution(X, Y, D):

    # Use Case 1: Jump Distance 0
    # Through exeption
    if Y < X or D <= 0:
        raise Exception("Invalid arguments")
    # Use case 2: Y in multiplication of D
    # Use case 3: Y in Not in multiplecaiton of D
    if (Y- X) % D == 0:
        return (Y- X) // D
    else:
        return ((Y- X) // D) + 1
    # Code COntributed by Nilesh
    # To Test Try X=10, Y=85 D=30

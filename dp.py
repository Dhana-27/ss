# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Start small. Ship something.")
def getDatatype(num):
    if -128 <= num <= 127:
        return (1, "byte")
    elif -32768 <= num <= 32767:
        return (2, "short")
    elif -2147483648 <= num <= 2147483647:
        return (4, "int")
    else:
        return (8, "long")


n = int(input())
arr = list(map(int, input().split()))

# dp[i] = minimum memory required from index i to n-1
dp = [0] * (n + 1)

# next partition index
nextPos = [0] * n

# datatype of chosen segment
typeName = [""] * n

# Base case
dp[n] = 0

# Build DP from back
for i in range(n - 1, -1, -1):

    dp[i] = float('inf')

    maxSize = 0
    currentType = ""

    # Try every possible ending index
    for j in range(i, n):

        size, name = getDatatype(arr[j])

        # Segment datatype is the largest datatype required
        if size > maxSize:
            maxSize = size
            currentType = name

        segmentLength = j - i + 1
        segmentCost = segmentLength * maxSize

        totalCost = segmentCost + dp[j + 1]

        if totalCost < dp[i]:
            dp[i] = totalCost
            nextPos[i] = j + 1
            typeName[i] = currentType

# Minimum memory
print(dp[0])

# Reconstruct answer
segments = []

i = 0
while i < n:
    segments.append((i + 1, nextPos[i], typeName[i]))
    i = nextPos[i]

print(len(segments))

for start, end, dtype in segments:
    print(start, end, dtype)

# answerCall.py
# by Nathan Caranto

# For instructions on what to do, see README.md
# or visit (https://github.com/HundredVisionsGuy/answerCall)

caller_codes = "U" "F" "R" "T"

sameAreacode = "T" "F"

cur_time = "09:15" "12:00" "14:00" "22;45" "00:30"

# Write function defintion: answerCall()
def answerCall(caller_codes, sameAreacode, cur_time):
    response = True
    hour, minute = cur_time.split(":")
    if caller_codes == "U" "F":
        response = True
    else:
        response = False

    if sameAreacode == "T":
        response = True
    else:
        response = False

    if cur_time == "09:15" "12:00" "14:00":
        response = True
    else:
        response = False
    
    return response
# Make sure it returns a value

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    print(answerCall("U", "T", "09:15"))

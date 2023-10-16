# answerCall.py
# by Nathan Caranto

# For instructions on what to do, see README.md
# or visit (https://github.com/HundredVisionsGuy/answerCall)

# Write function defintion: answerCall()
def answerCall(caller_codes, sameAreacode, cur_time):
    response = True
    hour, minute = cur_time.split(":")
    if hour >= "22" or hour < "07":
        response = False
    
    elif caller_codes == "R" or caller_codes == "F":
        response = True  
    else:
        response = False
        
        if caller_codes == "U" and sameAreacode:
            response = True
        else:
            response = False
    return response
# Make sure it returns a value

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    answerCall("U", True, "09:15")
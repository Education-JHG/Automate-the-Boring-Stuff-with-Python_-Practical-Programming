import time, sys

indent = 0 # How many spaces to indent after it iteration
indentIncreasing = True
try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second

        if indentIncreasing:
            # Increase the number of spaces:
            indent += 1
            if indent == 20:
                # When indent reachs 20 spaces (to the right), switch directions as to come back
                indentIncreasing = False

        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()

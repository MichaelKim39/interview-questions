"""
You are given the following commands:

Sound <TIME> - play sound for time length

Wait <TIME> - wait for time length

IF AFTER <TIME> <COMMAND> - if statement where command is run after a time

IF STOP <COMMAND> - if statement where the command is run after the stop button is pressed

:label - you may label your commands (or group of command)

Goto <label> - you may jump to a label

You start at midday. Your job is to create an alarm clock which sounds at 8AM everyday. The alarm then keeps playing until the stop button is pressed. 
It then plays the alarm again the next day.
"""

Sound 17: 00
Wait 17: 00
: ifafter
IF AFTER 17: 00 < cmd >
IF STOP < cmd >
Goto ifafter

# With time slices

: start
Wait 08: 00
: soundAlarm
Sound 0.0001s
IF STOP Goto start
Goto soundAlarm

# With time durations
: waitUntilDayEnd
IF AFTER 24: 00 Goto: start
Goto: waitUntilDayEnd

: start
IF AFTER 08: 00 goto: soundAlarm
Goto: start

: soundAlarm
IF STOP Goto: waitUntilDayEnd
Sound 0.0000001s
Goto: soundAlarm

"""
Compare current time with 12:00 (First day start)
If after - not the first day (goto soundAlarm)
If
"""

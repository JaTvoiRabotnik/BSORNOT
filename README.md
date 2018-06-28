# BSORNOT
A robot for detecting BS statements

Currently this works as a Twitter bot. Mention **@BSORNOT1** in order to get an
assessment of whether the statement is bullshit or not.

Next developments:

- add a REST API to allow other services to ask questions to
the robot.
- add a streamer to Telegram
- add a way to receive feedback from authorised users
- add a way to measure confidence level of assessment
- add a way to improve the model with increased feedback

In order to test the system use:

```
python -m unittest discover -v
```

To run the Twitter streamer use:

```
python -u bsornot/bot.py
```

Note that the source code does not include the file *secrets.py*, for obvious reasons. That means you will need to mock it in order to run it locally. There's no reason for you to want to test the streamer though (well, not yet anyway... we are nowhere near close to have to worry about scalability).

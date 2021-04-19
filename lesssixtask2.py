def countdown(func):
    import time
    time.sleep(3)
    func()

def vremya():
    @countdown
    def current_time():
        import time
        import datetime
        datetime.datetime.now()
        print(time.strftime("%H:%M"))

vremya()

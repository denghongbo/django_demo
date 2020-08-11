class Sample:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("CallExit")

    def do_something(self):
        print("I'm done.")


with Sample() as sample:
    sample.do_something()
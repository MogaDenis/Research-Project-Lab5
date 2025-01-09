class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Testing Singleton
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output should be True as both are the same instance

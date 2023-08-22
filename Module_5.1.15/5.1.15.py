class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:                       # при первом вызове создаем объект
            cls._instance = object.__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.program_name = "GenerationPy"
        self.environment = "release"
        self.loglevel = "verbose"
        self.version = "1.0.0"




config = Config()

print(config.program_name)
print(config.environment)
print(config.loglevel)
print(config.version)

# TEST_2:
config1 = Config()
config2 = Config()
config3 = Config()

print(config1 is config2)
print(config1 is config3)

# TEST_3:
config1 = Config()
config2 = Config()

print(config1.program_name is config2.program_name)
print(config1.environment is config2.environment)
print(config1.loglevel is config2.loglevel)
print(config1.version is config2.version)

# TEST_4:
config = Config()
configs = [Config() for _ in range(1000)]
print(all(item is config for item in configs))

# TEST_5:
config = Config()
print('program_name' in config.__dict__)
print('environment' in config.__dict__)
print('loglevel' in config.__dict__)
print('version' in config.__dict__)
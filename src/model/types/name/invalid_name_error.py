class InvalidNameError(ValueError):
    def __init__(self, message: str = 'name.invalid'):
        super().__init__(message)
        self.message = message

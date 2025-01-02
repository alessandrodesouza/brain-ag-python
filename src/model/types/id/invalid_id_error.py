class InvalidIdError(ValueError):
    def __init__(self, message: str = 'id.invalid'):
        super().__init__(message)
        self.message = message

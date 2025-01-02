class FarmerCreateError(ValueError):
    def __init__(self, message = '', messages = []):
        super().__init__(message)
        self.message = message
        self.messages = messages

class InvalidDocumentError(ValueError):
    def __init__(self, message: str = 'document.invalid'):
        super().__init__(message)
        self.message = message



class ExtractionError(Exception):
    """Base exception for extraction errors."""


class InvalidInputError(ExtractionError):
    """Raised when input text is invalid."""


class ToolExecutionError(ExtractionError):
    """Raised when tool execution fails."""


class AIServiceError(ExtractionError):
    """Raised when AI service fails."""

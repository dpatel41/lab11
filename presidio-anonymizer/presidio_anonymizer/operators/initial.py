from .operator import Operator, OperatorType


class Initial(Operator):
    """Minimal Initial operator placeholder."""

    def operator_name(self) -> str:
        return "initial"

    def operate(self, text: str, params=None) -> str:
        # Minimal behavior for now; will change in later tasks
        return text

    def validate(self, params: dict | None = None) -> None:
        """No special parameters needed for Initial yet, so nothing to validate."""
        # Other operators use this to validate 'params'. We don't need it yet.
        return

    def operator_type(self) -> OperatorType:
        """This is an anonymization operator (not a deanonymizer)."""
        return OperatorType.Anonymize

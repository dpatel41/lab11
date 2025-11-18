from .operator import Operator, OperatorType


class Initial(Operator):
    """Operator which converts words to initials, e.g. 'John Smith' -> 'J. S.'"""

    def operator_name(self) -> str:
        return "initial"

    def operate(self, text: str, params=None) -> str:
        if text is None:
            return ""

        # Remove leading/trailing whitespace
        stripped = text.strip()
        if not stripped:
            return ""

        # Split on any whitespace – this collapses multiple spaces into single tokens
        tokens = stripped.split()

        # Convert each token into its initial form
        initials_tokens = [self._token_to_initial(token) for token in tokens]

        # Filter out any empty tokens, then join with a single space
        initials_tokens = [t for t in initials_tokens if t]
        return " ".join(initials_tokens)

    @staticmethod
    def _token_to_initial(token: str) -> str:
        if not token:
            return ""

        # Keep any leading non-alphanumeric characters (prefix)
        prefix_chars = []
        i = 0
        while i < len(token) and not token[i].isalnum():
            prefix_chars.append(token[i])
            i += 1

        rest = token[i:]

        if not rest:
            # Token has no alphanumeric characters at all
            return "".join(prefix_chars)

        # Find the first alphanumeric character in the remaining part
        initial_char = None
        for ch in rest:
            if ch.isalnum():
                initial_char = ch.upper()
                break

        if initial_char is None:
            # Just return prefix if no alphanumeric found
            return "".join(prefix_chars)

        # e.g. prefix "@", initial "A" → "@A."
        return "".join(prefix_chars) + initial_char + "."

    def validate(self, params=None) -> None:
        """No special parameters needed for Initial yet, so nothing to validate."""
        return

    def operator_type(self) -> OperatorType:
        """This is an anonymization operator (not a deanonymizer)."""
        return OperatorType.Anonymize

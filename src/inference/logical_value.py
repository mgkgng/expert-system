class LogicalValue:
    def __init__(self, value):
        if value not in [True, False, None]:
            raise ValueError("LogicalValue must be True, False, or None (undefined).")
        self.value = value

    def _and(self, other):
        if self.value is False or other.value is False:
            return LogicalValue(False)
        elif self.value is True and other.value is True:
            return LogicalValue(True)
        else:
            return LogicalValue(None)

    def _or(self, other):
        if self.value is True or other.value is True:
            return LogicalValue(True)
        elif self.value is False and other.value is False:
            return LogicalValue(False)
        else:
            return LogicalValue(None)

    def _xor(self, other):
        if self.value is None or other.value is None:
            return LogicalValue(None)
        else:
            return LogicalValue(self.value != other.value)

    def _not(self):
        if self.value is None:
            return LogicalValue(None)
        else:
            return LogicalValue(not self.value)
        
    def __eq__(self, other):
        if isinstance(other, bool):
            return self.value == other
        if other is None:
            return self.value is None
        return self.value == other.value

    def __repr__(self):
        return "Undetermined" if self.value is None else f"{self.value}"

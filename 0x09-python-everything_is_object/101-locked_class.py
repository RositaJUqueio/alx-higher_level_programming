#!/usr/bin/python3
# Rosita J Uqueio
"""class prevents user from creating new instance attributes"""


class LockedClass:
    """except if the new instance attribute is called first_name."""
    __slots__ = ('first_name',)

    def __setattr__(self, name, value):
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError(f"Cannot create new attribute '{name}'")
        super().__setattr__(name, value)

"""
    Contains class with PetStatus categories
"""
from enum import Enum


class PetStatus(Enum):
    """
        Enum class, which contains possible statuses of Pet
    """
    AVAILABLE = 'available'
    PENDING = 'pending'
    SOLD = 'sold'

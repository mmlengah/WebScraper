import sqlite3
from abc import ABC, abstractmethod

class AbstractSQLiteTable(ABC):
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = self._connect()

    def __del__(self):
        self._close()

    @abstractmethod
    def create(self, data):
        """Create a new record in the table."""
        pass

    @abstractmethod
    def read(self, criteria):
        """Read records from the table based on given criteria."""
        pass

    @abstractmethod
    def update(self, criteria, update_data):
        """Update records in the table based on given criteria."""
        pass

    @abstractmethod
    def delete(self, criteria):
        """Delete records from the table based on given criteria."""
        pass

    def _connect(self):
        """Internal method to connect to the SQLite database."""
        return sqlite3.connect(self.db_path)

    def _close(self):
        """Internal method to close the SQLite database connection."""
        if self.connection:
            self.connection.close()
from user_entry import UserEntry
from entry_processor import EntryProcessor

if __name__ == "__main__":
    entry = UserEntry()
    processor = EntryProcessor()
    processor.entry_processing(entry.get_entry())

class Database(object):
    '''
    Database class for vector model

    A Vector database is a key store that maps coordinates (a key) to a value
    The key is a 3D coordinate
    '''
    def __init__(self) -> None:
        # In memory database
        # TODO: connect to a real database
        self.db = dict()


    def get(self, key: str) -> str:
        '''
        Get the value of the key
        '''
        pass

    def set(self, key: str, value: str) -> None:
        '''
        Set the value of the key
        '''
        pass

    def delete(self, key: str) -> None:
        '''
        Delete the key
        '''
        pass

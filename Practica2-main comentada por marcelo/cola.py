# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
class Cola():
    '''
    Attributes
    ----------
    Data: Planes in the queue
    Size: Number of planes in that are in queue

    Methods
    -------
    update_size: Checks what is the length of the queue and updates the size with that value.
    enqueue: adds a plane to the queue and updates its size.
    dequeue: erases a plane from teh queue and updates its size.
    first: returns the first plane of the queue.
    is_empty: checks if the queue is empty or not.
    '''
    
    def __init__(self):
        '''
        Initializes the self attributes.

        Attributes
        ----------
        self.data: list
            Used to store the different planes simulating a queue
        self.size: int
            Number of planes in the data list.

        Returns
        -----------
        None
    
        '''
        self.data = []
        self.size = 0
    
    def update_size(self):

        '''
        Updates the data list length
        Attributes:
        -----------

        None


        Return:
        -----------
        None

        '''
        
        self.size = len(self.data)
    
    def enqueue(self, e):
        '''
        Attributes:
        ----------
        e: avion
            This is the plane that will be put in the queue.
        Return:
        ----------
        None
        '''
        self.data += [e]
        self.update_size()
        
    def dequeue(self):
        '''
         Attributes:
        ----------
        e: avion
            This is the plane that will be deleted from the the queue.
        Return:
        e: avion
            The deleted plane.
        ----------
        None
        '''
        if self.is_empty() is False:
            e = self.first()
            self.data = self.data[1:]
            self.update_size()
            return e
        else:
            return None
    
    def first(self):
        '''
         Attributes:
        ----------
        None
        Return:
        ----------
        self.data[0]: avion
            This is the first plane of the queue
        '''
        return self.data[0]

    def is_empty(self):
        '''
         Attributes:
        ----------
        None
        Returns:
        ----------
        Returns true or false depending if the list is empty or not.
        '''
        return self.size == 0
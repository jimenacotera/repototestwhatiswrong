
from unittest import TestCase, skip 

import API.endpoints as ep


class EndpointTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello(self):
        hello = ep.HelloWorld(Resource)
        get = hello.get()
        self.assertIsInstance(ret, dict)
        self.assertIn(ep.HELLO, ret)

    def test_create_room(self):
        """
        See if we can successfully create a new room.
        Post-condition: room is in DB.
        """
        cr = ep.CreateRoom(Resource)
        new_room = new_entity_name("room")
        ret = cr.post(new_room)
        rooms = db.get_rooms()
        self.assertIn(new_room, rooms)

    def test_list_rooms1(self):
    """
    Post-condition 1: return is a dictionary.
    """
        lr = ep.ListRooms(Resource)
        ret = lr.get()
        self.assertIsInstance(ret, dict)

    def test_list_rooms2(self):
    """
    Post-condition 2: keys to the dict are strings
    """
        lr = ep.ListRooms(Resource)
        ret = lr.get()
        for key in ret:
        self.assertIsInstance(key, str)

    def test_list_rooms3(self):
    """
    Post-condition 3: the values in the dict are themselves dicts
    """
        lr = ep.ListRooms(Resource)
        ret = lr.get()
        for val in ret.values():
        self.assertIsInstance(val, dict)

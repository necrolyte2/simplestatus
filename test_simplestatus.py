import socket
from io import StringIO

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import mock

import simplestatus

@mock.patch.object(simplestatus, 'socket')
class TestCheckHost(unittest.TestCase):
    def setUp(self):
        self.sock = mock.MagicMock()

    def test_raises_unknown_exception(self, msocket):
        msocket.socket.return_value = self.sock
        self.sock.connect.side_effect = OSError('foo')

        r = simplestatus.check_host('foo.bar', 80)
        self.assertFalse(r[0])
        self.assertEqual('foo', r[1])

    def test_raises_error(self, msocket):
        msocket.socket.return_value = self.sock
        msocket.error = socket.error
        self.sock.connect.side_effect = socket.error('foo')
    
        r = simplestatus.check_host('foo.bar', 80)
        self.assertFalse(r[0])
        self.assertEqual('foo', r[1])

    def test_raises_error_oserror(self, msocket):
        msocket.socket.return_value = self.sock
        msocket.error = socket.error
        self.sock.connect.side_effect = socket.error((1, 'foo'))
    
        r = simplestatus.check_host('foo.bar', 80)
        self.assertFalse(r[0])
        self.assertEqual("(1, 'foo')", r[1])

    def test_raises_herror(self, msocket):
        msocket.socket.return_value = self.sock
        msocket.herror = socket.herror
        self.sock.connect.side_effect = socket.herror(1, 'foo')

        r = simplestatus.check_host('foo.bar', 80)
        self.assertFalse(r[0])
        self.assertEqual('[Errno 1] foo', r[1])

    def test_raises_gaierror(self, msocket):
        msocket.socket.return_value = self.sock
        msocket.gaierror = socket.gaierror
        self.sock.connect.side_effect = socket.gaierror(1, 'foo')

        r = simplestatus.check_host('foo.bar', 80)
        self.assertFalse(r[0])
        self.assertEqual('[Errno 1] foo', r[1])

    def test_raises_timout(self, msocket):
        msocket.socket.return_value = self.sock
        msocket.timeout = socket.timeout
        self.sock.connect.side_effect = socket.timeout('timed out')

        r = simplestatus.check_host('foo.bar', 80)
        self.assertFalse(r[0])
        self.assertEqual('timed out', r[1])

    def test_returns_up(self, msocket):
        msocket.socket.return_value = self.sock
        self.sock.connect.return_value = None

        r = simplestatus.check_host('foo.bar', 80)
        self.assertTrue(r[0])
        self.assertEqual('', r[1])


@mock.patch.object(simplestatus, 'sys')
@mock.patch.object(simplestatus, 'socket')
class TestCheckAll(unittest.TestCase):
    def setUp(self):
        self.sock = mock.MagicMock()
        self.sout = StringIO()
        self.serr = StringIO()

    def test_writes_correct_errors_up(self, msocket, msys):
        msocket.socket.return_value = self.sock
        msocket.error = socket.error
        msys.stdout = self.sout
        msys.stderr = self.serr

        hosts = [
            ('foo.bar', 80, 'Foo Bar'),
            ('foo.bar.bar', 80, 'Foo Bar Bar'),
            ('bar.foo', 80, 'Bar Foo')
        ]

        self.sock.connect.side_effect = [None, socket.error('error'), None]
        simplestatus.check_all(hosts)

        sout = msys.stdout.getvalue().splitlines()
        self.assertEqual('Foo Bar - UP', sout[0])
        self.assertEqual('Foo Bar Bar - DOWN', sout[1])
        self.assertEqual('\tfoo.bar.bar on port 80 seems down: error', sout[2])
        self.assertEqual('Bar Foo - UP', sout[3])

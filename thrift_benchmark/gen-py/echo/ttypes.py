#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys

from thrift.transport import TTransport


class Packet(object):
    """
    Attributes:
     - ride_id
     - workout_id
     - seconds_since_pedaling_start
     - total_work
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'ride_id', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'workout_id', 'UTF8', None, ),  # 2
        (3, TType.I16, 'seconds_since_pedaling_start', None, None, ),  # 3
        (4, TType.DOUBLE, 'total_work', None, None, ),  # 4
    )

    def __init__(self, ride_id=None, workout_id=None, seconds_since_pedaling_start=None, total_work=None,):
        self.ride_id = ride_id
        self.workout_id = workout_id
        self.seconds_since_pedaling_start = seconds_since_pedaling_start
        self.total_work = total_work

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.ride_id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.workout_id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I16:
                    self.seconds_since_pedaling_start = iprot.readI16()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.DOUBLE:
                    self.total_work = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Packet')
        if self.ride_id is not None:
            oprot.writeFieldBegin('ride_id', TType.STRING, 1)
            oprot.writeString(self.ride_id.encode('utf-8') if sys.version_info[0] == 2 else self.ride_id)
            oprot.writeFieldEnd()
        if self.workout_id is not None:
            oprot.writeFieldBegin('workout_id', TType.STRING, 2)
            oprot.writeString(self.workout_id.encode('utf-8') if sys.version_info[0] == 2 else self.workout_id)
            oprot.writeFieldEnd()
        if self.seconds_since_pedaling_start is not None:
            oprot.writeFieldBegin('seconds_since_pedaling_start', TType.I16, 3)
            oprot.writeI16(self.seconds_since_pedaling_start)
            oprot.writeFieldEnd()
        if self.total_work is not None:
            oprot.writeFieldBegin('total_work', TType.DOUBLE, 4)
            oprot.writeDouble(self.total_work)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.ride_id is None:
            raise TProtocolException(message='Required field ride_id is unset!')
        if self.workout_id is None:
            raise TProtocolException(message='Required field workout_id is unset!')
        if self.seconds_since_pedaling_start is None:
            raise TProtocolException(message='Required field seconds_since_pedaling_start is unset!')
        if self.total_work is None:
            raise TProtocolException(message='Required field total_work is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
